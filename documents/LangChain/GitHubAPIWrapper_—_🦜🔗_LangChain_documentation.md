# GitHubAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.github.GitHubAPIWrapper.html
**Word Count:** 775
**Links Count:** 338
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# GitHubAPIWrapper\#

_class _langchain\_community.utilities.github.GitHubAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for GitHub API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _active\_branch _: str | None_ _ = None_\#     

_param _github\_app\_id _: str | None_ _ = None_\#     

_param _github\_app\_private\_key _: str | None_ _ = None_\#     

_param _github\_base\_branch _: str | None_ _ = None_\#     

_param _github\_repository _: str | None_ _ = None_\#     

comment\_on\_issue\(_comment\_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.comment_on_issue)\#     

> Adds a comment to a github issue Parameters: >
>> comment\_query\(str\): a string which contains the issue number, two newlines, and the comment. for example: “1

Working on it now”     

> adds the comment “working on it now” to issue 1

Returns:     

str: A success or failure message

Parameters:     

**comment\_query** \(_str_\)

Return type:     

str

create\_branch\(

    _proposed\_branch\_name : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.create_branch)\#     

Create a new branch, and set it as the active bot branch. Equivalent to git switch -c proposed\_branch\_name If the proposed branch already exists, we append \_v1 then \_v2… until a unique name is found.

Returns:     

A plaintext success message.

Return type:     

str

Parameters:     

**proposed\_branch\_name** \(_str_\)

create\_file\(_file\_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.create_file)\#     

> Creates a new file on the Github repo Parameters: >
>> file\_query\(str\): a string which contains the file path and the file contents. The file path is the first line in the string, and the contents are the rest of the string. For example, “hello\_world.md

\# Hello World\!”     

Returns:     

str: A success or failure message

Parameters:     

**file\_query** \(_str_\)

Return type:     

str

create\_pull\_request\(_pr\_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.create_pull_request)\#     

> Makes a pull request from the bot’s branch to the base branch Parameters: >
>> pr\_query\(str\): a string which contains the PR title and the PR body. The title is the first line in the string, and the body are the rest of the string. For example, “Updated README

made changes to add info”     

Returns:     

str: A success or failure message

Parameters:     

**pr\_query** \(_str_\)

Return type:     

str

create\_review\_request\(

    _reviewer\_username : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.create_review_request)\#     

Creates a review request on _THE_ open pull request that matches the current active\_branch.

Parameters:     

**reviewer\_username** \(_str_\) – The username of the person who is being requested

Returns:     

A message confirming the creation of the review request

Return type:     

str

delete\_file\(_file\_path : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.delete_file)\#     

Deletes a file from the repo :param file\_path: Where the file is :type file\_path: str

Returns:     

Success or failure message

Return type:     

str

Parameters:     

**file\_path** \(_str_\)

get\_files\_from\_directory\(

    _directory\_path : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.get_files_from_directory)\#     

Recursively fetches files from a directory in the repo.

Parameters:     

**directory\_path** \(_str_\) – Path to the directory

Returns:     

List of file paths, or an error message.

Return type:     

str

get\_issue\(

    _issue\_number : int_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.get_issue)\#     

Fetches a specific issue and its first 10 comments :param issue\_number: The number for the github issue :type issue\_number: int

Returns:     

A dictionary containing the issue’s title, body, comments as a string, and the username of the user who opened the issue

Return type:     

dict

Parameters:     

**issue\_number** \(_int_\)

get\_issues\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.get_issues)\#     

Fetches all open issues from the repo excluding pull requests

Returns:     

A plaintext report containing the number of issues and each issue’s title and number.

Return type:     

str

get\_latest\_release\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.get_latest_release)\#     

Fetches the latest release of the repository.

Returns:     

The latest release

Return type:     

str

get\_pull\_request\(

    _pr\_number : int_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.get_pull_request)\#     

Fetches a specific pull request and its first 10 comments, limited by max\_tokens.

Parameters:     

  * **pr\_number** \(_int_\) – The number for the Github pull

  * **max\_tokens** \(_int_\) – The maximum number of tokens in the response

Returns:     

A dictionary containing the pull’s title, body, and comments as a string

Return type:     

dict

get\_release\(_tag\_name : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.get_release)\#     

Fetches a specific release of the repository.

Parameters:     

**tag\_name** \(_str_\) – The tag name of the release

Returns:     

The release

Return type:     

str

get\_releases\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.get_releases)\#     

Fetches all releases of the repository.

Returns:     

The releases

Return type:     

str

list\_branches\_in\_repo\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.list_branches_in_repo)\#     

Fetches a list of all branches in the repository.

Returns:     

A plaintext report containing the names of the branches.

Return type:     

str

list\_files\_in\_bot\_branch\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.list_files_in_bot_branch)\#     

Fetches all files in the active branch of the repo, the branch the bot uses to make changes.

Returns:     

A plaintext list containing the filepaths in the branch.

Return type:     

str

list\_files\_in\_main\_branch\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.list_files_in_main_branch)\#     

Fetches all files in the main branch of the repo.

Returns:     

A plaintext report containing the paths and names of the files.

Return type:     

str

list\_open\_pull\_requests\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.list_open_pull_requests)\#     

Fetches all open PRs from the repo

Returns:     

A plaintext report containing the number of PRs and each PR’s title and number.

Return type:     

str

list\_pull\_request\_files\(

    _pr\_number : int_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.list_pull_request_files)\#     

Fetches the full text of all files in a PR. Truncates after first 3k tokens. \# TODO: Enhancement to summarize files with ctags if they’re getting long.

Parameters:     

**pr\_number** \(_int_\) – The number of the pull request on Github

Returns:     

A dictionary containing the issue’s title, body, and comments as a string

Return type:     

dict

parse\_issues\(

    _issues : List\[Issue\]_, \) → List\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.parse_issues)\#     

Extracts title and number from each Issue and puts them in a dictionary :param issues: A list of Github Issue objects :type issues: List\[Issue\]

Returns:     

A dictionary of issue titles and numbers

Return type:     

List\[dict\]

Parameters:     

**issues** \(_List_ _\[__Issue_ _\]_\)

parse\_pull\_requests\(

    _pull\_requests : List\[PullRequest\]_, \) → List\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.parse_pull_requests)\#     

Extracts title and number from each Issue and puts them in a dictionary :param issues: A list of Github Issue objects :type issues: List\[Issue\]

Returns:     

A dictionary of issue titles and numbers

Return type:     

List\[dict\]

Parameters:     

**pull\_requests** \(_List_ _\[__PullRequest_ _\]_\)

read\_file\(_file\_path : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.read_file)\#     

Read a file from this agent’s branch, defined by self.active\_branch, which supports PR branches. :param file\_path: the file path :type file\_path: str

Returns:     

The file decoded as a string, or an error message if not found

Return type:     

str

Parameters:     

**file\_path** \(_str_\)

run\(_mode : str_, _query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.run)\#     

Parameters:     

  * **mode** \(_str_\)

  * **query** \(_str_\)

Return type:     

str

search\_code\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.search_code)\#     

Searches code in the repository. \# Todo: limit total tokens returned…

Parameters:     

**query** \(_str_\) – The search query

Returns:     

A string containing, at most, the top 5 search results

Return type:     

str

search\_issues\_and\_prs\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.search_issues_and_prs)\#     

Searches issues and pull requests in the repository.

Parameters:     

**query** \(_str_\) – The search query

Returns:     

A string containing the first 5 issues and pull requests

Return type:     

str

set\_active\_branch\(_branch\_name : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.set_active_branch)\#     

Equivalent to git checkout branch\_name for this Agent. Clones formatting from Github.

Returns an Error \(as a string\) if branch doesn’t exist.

Parameters:     

**branch\_name** \(_str_\)

Return type:     

str

update\_file\(_file\_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/github.html#GitHubAPIWrapper.update_file)\#     

Updates a file with new content. :param file\_query: Contains the file path and the file contents.

> The old file contents is wrapped in OLD <<<< and >>>> OLD The new file contents is wrapped in NEW <<<< and >>>> NEW For example: /test/hello.txt OLD <<<< Hello Earth\! >>>> OLD NEW <<<< Hello Mars\! >>>> NEW

Returns:     

A success or failure message

Parameters:     

**file\_query** \(_str_\)

Return type:     

str

Examples using GitHubAPIWrapper

  * [Github Toolkit](https://python.langchain.com/docs/integrations/tools/github/)

__On this page