#!/usr/bin/env python3
"""
Test exact RAG context that's failing
"""

import asyncio
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, '/app')

from rag.components.llm_manager import LLMManager

async def test_exact_rag_context():
    """Test the exact context that RAG system sends."""
    print("Testing exact RAG context...")
    
    # Create LLM manager with same config
    llm_config = {
        'provider': 'ollama',
        'model': 'mistral-nemo:12b',
        'base_url': 'http://host.docker.internal:11434',
        'temperature': 0.1,
        'max_tokens': 2048
    }
    
    try:
        llm_manager = LLMManager(llm_config)
        await llm_manager.initialize()
        
        # This is the exact context from the RAG system logs
        exact_context = """Document 1:
Author: Awa K. Penn
Content: How to build an AI agent using n8n

With n8n, you can automate news updates,
Summarize them with AI,
And send them anywhere

Here's how to do it:

1. Start with n8n
- Create a new workflow.
- This becomes your automation hub.

2. Decide when it runs
- Schedule it daily
- Or trigger it manually when needed.

3. Pull fresh headlines
- Use an HTTP request,
- To fetch trending news from News API.

4. Summarize like a pro
- Add OpenAI.
-Give it a clear prompt.
- Let it handle the heavy lifting.

5. Make it look good
- Use bullet points,
- Insert clean links,
- and format for easy reading.

6. Send it anywhere
- Email. Discord. Notion.
- Anywhere your audience lives.

With just 3 free tools and under 30 minutes,
You'll have an AI agent running on autopilot.

--------------------------
If you want more tips and insights about AI, join my newsletter that teaches you how to leverage AI 👇

🔄 REPOST to help others know this.

👉 Follow me, for more.

Likes: 405
Comments: 0
Shares: 0
Timestamp: 
URL: https://www.linkedin.com/feed/update/urn:li:activity:7354514881645035521/

Document 2:
Author: Fortune
Content: Aravind Srinivas wanted a simple answer. If Google had given him one, things might have turned out differently—for Srinivas and for Google.

It was the fall of 2022, weeks before OpenAI would debut its viral AI chatbot, ChatGPT. Srinivas, then 28, was an ambitious AI researcher with a PhD from UC Berkeley and prestigious internships at OpenAI and Google's AI labs under his belt, plus a year working full-time for OpenAI after earning his doctorate. Now he'd left that plum job to launch a startup with three cofounders, all AI experts.

Weeks later, ChatGPT launched. Seven days after that, Srinivas and his cofounders debuted their San Francisco–based company and its breakthrough product. They called both—borrowing a machine-learning term for how well an AI model makes predictions. Even amid the buzz around ChatGPT, Perplexity gained traction among Silicon Valley's elite and, through word of mouth, among consultants, analysts, and journalists.

Read the full story here:

Likes: 425
Comments: 0
Shares: 0
Timestamp: 
URL: https://www.linkedin.com/feed/update/urn:li:activity:7354570946017419264/"""

        exact_prompt = "Based on the following documents, please answer this question: What do you know about n8n?"
        
        print(f"Context length: {len(exact_context)} characters")
        print(f"Prompt length: {len(exact_prompt)} characters")
        print(f"Total length: {len(exact_context) + len(exact_prompt)} characters")
        
        print("Calling LLM with exact RAG context...")
        response = await llm_manager.generate_response(exact_prompt, exact_context)
        print(f"✅ Success! Response: {response[:200]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_exact_rag_context())
    print(f"Overall success: {success}")
    sys.exit(0 if success else 1) 