# GitLabAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.gitlab.GitLabAPIWrapper.html
**Word Count:** 574
**Links Count:** 308
**Scraped:** 2025-07-21 08:18:47
**Status:** completed

---

# GitLabAPIWrapper\#

_class _langchain\_community.utilities.gitlab.GitLabAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/gitlab.html#GitLabAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for GitLab API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _gitlab\_base\_branch _: str | None_ _ = None_\#     

The base branch in the GitLab repository, used for comparisons. Usually ‘main’ or ‘master’. Defaults to ‘main’.

_param _gitlab\_branch _: str | None_ _ = None_\#     

The specific branch in the GitLab repository where the bot will make its commits. Defaults to ‘main’.

_param _gitlab\_personal\_access\_token _: str | None_ _ = None_\#     

Personal access token for the GitLab service, used for authentication.

_param _gitlab\_repository _: str | None_ _ = None_\#     

The name of the GitLab repository, in the form \{username\}/\{repo-name\}.

_param _gitlab\_url _: str | None_ _ = None_\#     

The url of the GitLab instance.

comment\_on\_issue\(_comment\_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/gitlab.html#GitLabAPIWrapper.comment_on_issue)\#     

> Adds a comment to a gitlab issue Parameters: >
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

    _proposed\_branch\_name : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/gitlab.html#GitLabAPIWrapper.create_branch)\#     

Create a new branch in the repository and set it as the active branch

Parameters:     

**proposed\_branch\_name** \(_str_\) – The name of the new branch to be created

Returns:     

A success or failure message

Return type:     

str

create\_file\(_file\_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/gitlab.html#GitLabAPIWrapper.create_file)\#     

> Creates a new file on the gitlab repo Parameters: >
>> file\_query\(str\): a string which contains the file path and the file contents. The file path is the first line in the string, and the contents are the rest of the string. For example, “hello\_world.md

\# Hello World\!”     

Returns:     

str: A success or failure message

Parameters:     

**file\_query** \(_str_\)

Return type:     

str

create\_pull\_request\(_pr\_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/gitlab.html#GitLabAPIWrapper.create_pull_request)\#     

> Makes a pull request from the bot’s branch to the base branch Parameters: >
>> pr\_query\(str\): a string which contains the PR title and the PR body. The title is the first line in the string, and the body are the rest of the string. For example, “Updated README

made changes to add info”     

Returns:     

str: A success or failure message

Parameters:     

**pr\_query** \(_str_\)

Return type:     

str

delete\_file\(_file\_path : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/gitlab.html#GitLabAPIWrapper.delete_file)\#     

Deletes a file from the repo :param file\_path: Where the file is :type file\_path: str

Returns:     

Success or failure message

Return type:     

str

Parameters:     

**file\_path** \(_str_\)

get\_issue\(

    _issue\_number : int_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/gitlab.html#GitLabAPIWrapper.get_issue)\#     

Fetches a specific issue and its first 10 comments :param issue\_number: The number for the gitlab issue :type issue\_number: int

Returns:     

A dictionary containing the issue’s title, body, and comments as a string

Return type:     

dict

Parameters:     

**issue\_number** \(_int_\)

get\_issues\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/gitlab.html#GitLabAPIWrapper.get_issues)\#     

Fetches all open issues from the repo

Returns:     

A plaintext report containing the number of issues and each issue’s title and number.

Return type:     

str

list\_branches\_in\_repo\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/gitlab.html#GitLabAPIWrapper.list_branches_in_repo)\#     

Get the list of branches in the repository

Returns:     

A plaintext report containing the number of branches and each branch name

Return type:     

str

list\_files\_from\_directory\(_path : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/gitlab.html#GitLabAPIWrapper.list_files_from_directory)\#     

Get the list of files in the active branch of the repository from a specific directory

Returns:     

A plaintext report containing the list of files in the repository in the active branch from the specified directory

Return type:     

str

Parameters:     

**path** \(_str_\)

list\_files\_in\_bot\_branch\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/gitlab.html#GitLabAPIWrapper.list_files_in_bot_branch)\#     

Get the list of files in the active branch of the repository

Returns:     

A plaintext report containing the list of files in the repository in the active branch

Return type:     

str

list\_files\_in\_main\_branch\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/gitlab.html#GitLabAPIWrapper.list_files_in_main_branch)\#     

Get the list of files in the main branch of the repository

Returns:     

A plaintext report containing the list of files in the repository in the main branch

Return type:     

str

parse\_issues\(

    _issues : List\[Issue\]_, \) → List\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/gitlab.html#GitLabAPIWrapper.parse_issues)\#     

Extracts title and number from each Issue and puts them in a dictionary :param issues: A list of gitlab Issue objects :type issues: List\[Issue\]

Returns:     

A dictionary of issue titles and numbers

Return type:     

List\[dict\]

Parameters:     

**issues** \(_List_ _\[__Issue_ _\]_\)

read\_file\(_file\_path : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/gitlab.html#GitLabAPIWrapper.read_file)\#     

Reads a file from the gitlab repo :param file\_path: the file path :type file\_path: str

Returns:     

The file decoded as a string

Return type:     

str

Parameters:     

**file\_path** \(_str_\)

run\(_mode : str_, _query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/gitlab.html#GitLabAPIWrapper.run)\#     

Parameters:     

  * **mode** \(_str_\)

  * **query** \(_str_\)

Return type:     

str

set\_active\_branch\(_branch\_name : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/gitlab.html#GitLabAPIWrapper.set_active_branch)\#     

Equivalent to git checkout branch\_name for this Agent. Clones formatting from Gitlab.

Returns an Error \(as a string\) if branch doesn’t exist.

Parameters:     

**branch\_name** \(_str_\)

Return type:     

str

update\_file\(_file\_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/gitlab.html#GitLabAPIWrapper.update_file)\#     

Updates a file with new content. :param file\_query: Contains the file path and the file contents.

> The old file contents is wrapped in OLD <<<< and >>>> OLD The new file contents is wrapped in NEW <<<< and >>>> NEW For example: test/hello.txt OLD <<<< Hello Earth\! >>>> OLD NEW <<<< Hello Mars\! >>>> NEW

Returns:     

A success or failure message

Parameters:     

**file\_query** \(_str_\)

Return type:     

str

Examples using GitLabAPIWrapper

  * [Gitlab Toolkit](https://python.langchain.com/docs/integrations/tools/gitlab/)

__On this page