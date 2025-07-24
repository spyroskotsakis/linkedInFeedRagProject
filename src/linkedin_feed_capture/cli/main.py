"""
Main CLI application for LinkedIn feed capture.

Provides a command-line interface with rich output formatting, progress tracking,
and comprehensive configuration options for scraping LinkedIn feeds.
"""

import json
import os
import sys
from pathlib import Path
from typing import Optional, List

import typer
from rich.console import Console
from rich.progress import Progress, TaskID, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import print as rprint
from dotenv import load_dotenv

from linkedin_feed_capture.auth.authenticator import LinkedInAuthenticator, AuthConfig
from linkedin_feed_capture.browser.driver import create_default_driver, DriverConfig, DriverFactory
from linkedin_feed_capture.scraper.extractor import FeedExtractor, ExtractionConfig
from linkedin_feed_capture.scraper.scroll import ScrollConfig
from linkedin_feed_capture.scraper.parser import ParsingConfig
from linkedin_feed_capture.models.post import Post
from linkedin_feed_capture.utils.logger import setup_logging, get_logger

# Initialize console and app
console = Console()
app = typer.Typer(
    name="linkedin-capture",
    help="Production-ready LinkedIn feed scraper for RAG applications",
    add_completion=False,
)

# Global logger
logger = get_logger(__name__)


class ProgressCallback:
    """Progress callback for extraction tracking."""
    
    def __init__(self, progress: Progress, task_id: TaskID):
        self.progress = progress
        self.task_id = task_id
        
    def __call__(self, post: Post, current: int, total: int):
        """Update progress bar."""
        self.progress.update(
            self.task_id,
            completed=current,
            description=f"Extracting posts ({current}/{total}) - Latest: {post.author[:30]}..."
        )


@app.callback()
def main(
    env_file: Optional[str] = typer.Option(
        None,
        "--env-file",
        "-e",
        help="Path to .env file with configuration"
    ),
    log_level: str = typer.Option(
        "INFO",
        "--log-level",
        "-l",
        help="Logging level (DEBUG, INFO, WARNING, ERROR)"
    ),
    log_file: Optional[str] = typer.Option(
        None,
        "--log-file",
        help="Path to log file (optional)"
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Enable verbose output"
    ),
) -> None:
    """LinkedIn Feed Capture - Extract posts for RAG applications."""
    
    # Load environment variables
    if env_file:
        load_dotenv(env_file)
    else:
        # Try to load from default locations
        for env_path in [".env", ".env.local"]:
            if Path(env_path).exists():
                load_dotenv(env_path)
                break
    
    # Setup logging
    setup_logging(
        log_level=log_level.upper(),
        log_format="console" if verbose else "json",
        log_file_path=log_file,
        enable_console=True,
    )
    
    if verbose:
        console.print("[bold green]LinkedIn Feed Capture[/bold green]")
        console.print("Production-ready scraper for RAG applications\n")


@app.command()
def capture(
    target_posts: int = typer.Option(
        50,
        "--posts",
        "-n",
        help="Number of posts to capture"
    ),
    email: Optional[str] = typer.Option(
        None,
        "--email",
        help="LinkedIn email (or set LINKEDIN_EMAIL env var)"
    ),
    password: Optional[str] = typer.Option(
        None,
        "--password",
        help="LinkedIn password (or set LINKEDIN_PASSWORD env var)"
    ),
    cookie_path: Optional[str] = typer.Option(
        None,
        "--cookie-path",
        help="Path to cookie file (or set COOKIE_PATH env var)"
    ),
    output_file: Optional[str] = typer.Option(
        None,
        "--output",
        "-o",
        help="Output file for JSON posts (default: stdout)"
    ),
    headless: bool = typer.Option(
        True,
        "--headless/--no-headless",
        help="Run browser in headless mode"
    ),
    stealth: bool = typer.Option(
        True,
        "--stealth/--no-stealth",
        help="Enable stealth mode to avoid detection"
    ),
    pretty_print: bool = typer.Option(
        False,
        "--pretty",
        "-p",
        help="Pretty print JSON output"
    ),
    streaming: bool = typer.Option(
        False,
        "--streaming",
        "-s",
        help="Stream posts as they are extracted"
    ),
    max_scroll_attempts: int = typer.Option(
        100,
        "--max-scrolls",
        help="Maximum scroll attempts"
    ),
    scroll_delay: float = typer.Option(
        2.0,
        "--scroll-delay",
        help="Base scroll delay in seconds"
    ),
    extraction_timeout: int = typer.Option(
        300,
        "--timeout",
        help="Extraction timeout in seconds"
    ),
    include_sponsored: bool = typer.Option(
        False,
        "--include-sponsored",
        help="Include sponsored/promoted posts"
    ),
    extract_media: bool = typer.Option(
        True,
        "--extract-media/--no-media",
        help="Extract media URLs from posts"
    ),
    validate_posts: bool = typer.Option(
        True,
        "--validate/--no-validate",
        help="Validate extracted posts"
    ),
) -> None:
    """Capture LinkedIn feed posts and output as JSON."""
    
    # Get configuration from environment or parameters
    linkedin_email = email or os.getenv("LINKEDIN_EMAIL")
    linkedin_password = password or os.getenv("LINKEDIN_PASSWORD")
    cookie_file_path = cookie_path or os.getenv("COOKIE_PATH", "./data/cookies.pkl")
    
    if not linkedin_email or not linkedin_password:
        console.print("[red]Error: LinkedIn email and password are required[/red]")
        console.print("Set them via --email/--password or LINKEDIN_EMAIL/LINKEDIN_PASSWORD environment variables")
        raise typer.Exit(1)
    
    # Show configuration
    with console.status("Initializing..."):
        config_table = Table(title="Capture Configuration", show_header=True)
        config_table.add_column("Setting", style="cyan")
        config_table.add_column("Value", style="magenta")
        
        config_table.add_row("Target Posts", str(target_posts))
        config_table.add_row("Email", linkedin_email)
        config_table.add_row("Headless Mode", str(headless))
        config_table.add_row("Stealth Mode", str(stealth))
        config_table.add_row("Cookie Path", cookie_file_path)
        config_table.add_row("Output File", output_file or "stdout")
        config_table.add_row("Streaming", str(streaming))
        config_table.add_row("Max Scrolls", str(max_scroll_attempts))
        config_table.add_row("Scroll Delay", f"{scroll_delay}s")
        config_table.add_row("Timeout", f"{extraction_timeout}s")
    
    console.print(config_table)
    console.print()
    
    # Initialize components
    try:
        with console.status("Creating browser driver..."):
            driver = create_default_driver(
                headless=headless,
                enable_stealth=stealth,
            )
        
        console.print("[green]✓[/green] Browser driver created")
        
        # Setup authentication
        with console.status("Setting up authentication..."):
            auth_config = AuthConfig(
                email=linkedin_email,
                password=linkedin_password,
                cookie_path=cookie_file_path,
                encryption_key=os.getenv("COOKIE_ENCRYPTION_KEY"),
            )
            authenticator = LinkedInAuthenticator(auth_config)
        
        # Authenticate
        with console.status("Authenticating with LinkedIn..."):
            authenticated = authenticator.authenticate(driver)
            
        if not authenticated:
            console.print("[red]✗[/red] Authentication failed")
            raise typer.Exit(1)
        
        console.print("[green]✓[/green] Authentication successful")
        
        # Setup extraction configuration
        extraction_config = ExtractionConfig(
            target_posts=target_posts,
            extraction_timeout=extraction_timeout,
            include_sponsored=include_sponsored,
            scroll_config=ScrollConfig(
                base_delay=scroll_delay,
                max_scroll_attempts=max_scroll_attempts,
            ),
            parsing_config=ParsingConfig(
                extract_media=extract_media,
            ),
        )
        
        # Create extractor
        extractor = FeedExtractor(extraction_config)
        
        # Start extraction
        extracted_posts: List[Post] = []
        
        if streaming:
            # Streaming extraction
            console.print(f"[blue]Starting streaming extraction of {target_posts} posts...[/blue]")
            
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                TimeElapsedColumn(),
                console=console
            ) as progress:
                task = progress.add_task("Extracting posts...", total=target_posts)
                
                # Setup progress callback
                progress_callback = ProgressCallback(progress, task)
                extraction_config.progress_callback = progress_callback
                
                for post in extractor.extract_feed_streaming(driver, target_posts):
                    extracted_posts.append(post)
                    
                    # Output post immediately if streaming to stdout
                    if not output_file:
                        _output_post(post, pretty_print)
        else:
            # Batch extraction
            console.print(f"[blue]Starting batch extraction of {target_posts} posts...[/blue]")
            
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                TimeElapsedColumn(),
                console=console
            ) as progress:
                task = progress.add_task("Extracting posts...", total=target_posts)
                
                # Setup progress callback
                progress_callback = ProgressCallback(progress, task)
                extraction_config.progress_callback = progress_callback
                
                extracted_posts = extractor.extract_feed(driver, target_posts)
        
        # Get extraction statistics
        stats = extractor.get_extraction_stats()
        
        # Display results
        _display_extraction_results(extracted_posts, stats)
        
        # Output posts to file if specified
        if output_file and not streaming:
            _output_posts_to_file(extracted_posts, output_file, pretty_print)
            console.print(f"[green]✓[/green] Posts saved to {output_file}")
        elif not output_file and not streaming:
            # Output all posts to stdout
            for post in extracted_posts:
                _output_post(post, pretty_print)
        
        # Validation
        if validate_posts:
            _validate_extracted_posts(extracted_posts)
    
    except KeyboardInterrupt:
        console.print("\n[yellow]Extraction interrupted by user[/yellow]")
        raise typer.Exit(0)
    except Exception as e:
        console.print(f"\n[red]Error during extraction: {e}[/red]")
        logger.error("Extraction failed", error=str(e), error_type=type(e).__name__)
        raise typer.Exit(1)
    finally:
        # Cleanup
        try:
            if 'driver' in locals():
                driver.quit()
        except:
            pass


@app.command()
def auth_info(
    cookie_path: Optional[str] = typer.Option(
        None,
        "--cookie-path",
        help="Path to cookie file (or set COOKIE_PATH env var)"
    ),
) -> None:
    """Display authentication information and cookie status."""
    
    cookie_file_path = cookie_path or os.getenv("COOKIE_PATH", "./data/cookies.pkl")
    
    from linkedin_feed_capture.auth.cookies import CookieManager
    
    cookie_manager = CookieManager(
        storage_path=cookie_file_path,
        encryption_key=os.getenv("COOKIE_ENCRYPTION_KEY"),
    )
    
    cookie_info = cookie_manager.get_cookie_info()
    
    # Create info table
    info_table = Table(title="Authentication Information", show_header=True)
    info_table.add_column("Property", style="cyan")
    info_table.add_column("Value", style="magenta")
    
    info_table.add_row("Cookie File", cookie_file_path)
    info_table.add_row("File Exists", "✓" if cookie_info.get("exists", False) else "✗")
    
    if cookie_info.get("exists"):
        info_table.add_row("Total Cookies", str(cookie_info.get("total_cookies", 0)))
        info_table.add_row("LinkedIn Cookies", str(cookie_info.get("linkedin_cookies", 0)))
        info_table.add_row("Created At", cookie_info.get("created_at", "Unknown"))
        info_table.add_row("Last Used", cookie_info.get("last_used", "Unknown"))
        info_table.add_row("Age (days)", f"{cookie_info.get('age_days', 0):.1f}")
        info_table.add_row("Valid Session", "✓" if cookie_info.get("has_valid_session", False) else "✗")
        
        if cookie_info.get("error"):
            info_table.add_row("Error", cookie_info["error"])
    
    console.print(info_table)


@app.command()
def test_connection(
    email: Optional[str] = typer.Option(
        None,
        "--email",
        help="LinkedIn email (or set LINKEDIN_EMAIL env var)"
    ),
    password: Optional[str] = typer.Option(
        None,
        "--password", 
        help="LinkedIn password (or set LINKEDIN_PASSWORD env var)"
    ),
    headless: bool = typer.Option(
        True,
        "--headless/--no-headless",
        help="Run browser in headless mode"
    ),
) -> None:
    """Test LinkedIn connection and authentication."""
    
    linkedin_email = email or os.getenv("LINKEDIN_EMAIL")
    linkedin_password = password or os.getenv("LINKEDIN_PASSWORD")
    
    if not linkedin_email or not linkedin_password:
        console.print("[red]Error: LinkedIn email and password are required[/red]")
        raise typer.Exit(1)
    
    console.print("[blue]Testing LinkedIn connection...[/blue]")
    
    try:
        with console.status("Creating browser..."):
            driver = create_default_driver(headless=headless, enable_stealth=True)
        
        console.print("[green]✓[/green] Browser created")
        
        with console.status("Authenticating..."):
            auth_config = AuthConfig(
                email=linkedin_email,
                password=linkedin_password,
                cookie_path="./test_cookies.pkl",
            )
            authenticator = LinkedInAuthenticator(auth_config)
            authenticated = authenticator.authenticate(driver)
        
        if authenticated:
            console.print("[green]✓[/green] Authentication successful")
            
            with console.status("Testing feed access..."):
                driver.get("https://www.linkedin.com/feed/")
                # Simple check for feed elements
                import time
                time.sleep(3)
                
                from selenium.webdriver.common.by import By
                posts = driver.find_elements(By.CSS_SELECTOR, '[data-id^="urn:li:activity"]')
                
            console.print(f"[green]✓[/green] Feed access successful - found {len(posts)} posts")
            
        else:
            console.print("[red]✗[/red] Authentication failed")
            
    except Exception as e:
        console.print(f"[red]✗[/red] Connection test failed: {e}")
        raise typer.Exit(1)
    finally:
        try:
            if 'driver' in locals():
                driver.quit()
        except:
            pass


def _output_post(post: Post, pretty_print: bool = False) -> None:
    """Output a single post as JSON."""
    post_json = post.to_json_dict()
    
    if pretty_print:
        print(json.dumps(post_json, indent=2, ensure_ascii=False))
    else:
        print(json.dumps(post_json, ensure_ascii=False))


def _output_posts_to_file(posts: List[Post], file_path: str, pretty_print: bool = False) -> None:
    """Output posts to a file."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, 'w', encoding='utf-8') as f:
        if file_path.endswith('.jsonl'):
            # JSONL format - one post per line
            for post in posts:
                f.write(json.dumps(post.to_json_dict(), ensure_ascii=False) + '\n')
        else:
            # Regular JSON array
            posts_json = [post.to_json_dict() for post in posts]
            if pretty_print:
                json.dump(posts_json, f, indent=2, ensure_ascii=False)
            else:
                json.dump(posts_json, f, ensure_ascii=False)


def _display_extraction_results(posts: List[Post], stats: dict) -> None:
    """Display extraction results summary."""
    
    # Results summary
    results_table = Table(title="Extraction Results", show_header=True)
    results_table.add_column("Metric", style="cyan")
    results_table.add_column("Value", style="magenta")
    
    results_table.add_row("Posts Extracted", str(len(posts)))
    results_table.add_row("Posts Discovered", str(stats.get("posts_discovered", 0)))
    results_table.add_row("Posts Failed", str(stats.get("posts_failed", 0)))
    results_table.add_row("Duration", f"{stats.get('duration_seconds', 0):.1f}s")
    results_table.add_row("Success Rate", f"{stats.get('success_rate', 0):.1f}%")
    results_table.add_row("Posts/Second", f"{stats.get('posts_per_second', 0):.2f}")
    results_table.add_row("Scroll Attempts", str(stats.get("scroll_attempts", 0)))
    results_table.add_row("Detection Events", str(stats.get("detection_events", 0)))
    
    console.print(results_table)
    
    if posts:
        # Sample posts preview
        console.print("\n[bold blue]Sample Posts:[/bold blue]")
        
        sample_table = Table(show_header=True)
        sample_table.add_column("Author", style="green", max_width=20)
        sample_table.add_column("Content Preview", style="white", max_width=50)
        sample_table.add_column("Likes", style="yellow", justify="right")
        sample_table.add_column("Type", style="cyan")
        
        for post in posts[:5]:  # Show first 5 posts
            content_preview = post.content[:100] + "..." if len(post.content) > 100 else post.content
            sample_table.add_row(
                post.author,
                content_preview,
                str(post.metrics.likes),
                post.post_type
            )
        
        console.print(sample_table)


def _validate_extracted_posts(posts: List[Post]) -> None:
    """Validate extracted posts and show validation results."""
    
    if not posts:
        console.print("[yellow]⚠[/yellow] No posts to validate")
        return
    
    validation_issues = []
    
    # Check for basic validation issues
    for i, post in enumerate(posts):
        if not post.author:
            validation_issues.append(f"Post {i+1}: Missing author")
        if not post.content:
            validation_issues.append(f"Post {i+1}: Missing content")
        if not post.urn:
            validation_issues.append(f"Post {i+1}: Missing URN")
        if len(post.content) < 10:
            validation_issues.append(f"Post {i+1}: Content too short")
    
    # Check for duplicates
    urns = [post.urn for post in posts]
    if len(urns) != len(set(urns)):
        validation_issues.append("Duplicate posts found")
    
    if validation_issues:
        console.print(f"[yellow]⚠[/yellow] Validation issues found ({len(validation_issues)}):")
        for issue in validation_issues[:10]:  # Show first 10 issues
            console.print(f"  • {issue}")
    else:
        console.print("[green]✓[/green] All posts passed validation")


if __name__ == "__main__":
    app() 