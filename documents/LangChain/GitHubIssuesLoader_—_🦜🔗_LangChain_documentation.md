# GitHubIssuesLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.github.GitHubIssuesLoader.html
**Word Count:** 287
**Links Count:** 451
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# GitHubIssuesLoader\#

_class _langchain\_community.document\_loaders.github.GitHubIssuesLoader[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/github.html#GitHubIssuesLoader)\#     

Bases: [`BaseGitHubLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.github.BaseGitHubLoader.html#langchain_community.document_loaders.github.BaseGitHubLoader "langchain_community.document_loaders.github.BaseGitHubLoader")

Load issues of a GitHub repository.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _access\_token _: str_ _\[Required\]_\#     

Personal access token - see [settings/tokens](https://github.com/settings/tokens?type=beta)

_param _assignee _: str | None_ _ = None_\#     

Filter on assigned user. Pass ‘none’ for no user and ‘\*’ for any user.

_param _creator _: str | None_ _ = None_\#     

Filter on the user that created the issue.

_param _direction _: Literal\['asc', 'desc'\] | None_ _ = None_\#     

The direction to sort the results by. Can be one of: ‘asc’, ‘desc’.

_param _github\_api\_url _: str_ _ = 'https://api.github.com'_\#     

URL of GitHub API

_param _include\_prs _: bool_ _ = True_\#     

If True include Pull Requests in results, otherwise ignore them.

_param _labels _: List\[str\] | None_ _ = None_\#     

Label names to filter one. Example: bug,ui,@high.

_param _mentioned _: str | None_ _ = None_\#     

Filter on a user that’s mentioned in the issue.

_param _milestone _: int | Literal\['\*', 'none'\] | None_ _ = None_\#     

If integer is passed, it should be a milestone’s number field. If the string ‘\*’ is passed, issues with any milestone are accepted. If the string ‘none’ is passed, issues without milestones are returned.

_param _page _: int | None_ _ = None_\#     

The page number for paginated results. Defaults to 1 in the GitHub API.

_param _per\_page _: int | None_ _ = None_\#     

Number of items per page. Defaults to 30 in the GitHub API.

_param _repo _: str_ _\[Required\]_\#     

Name of repository

_param _since _: str | None_ _ = None_\#     

Only show notifications updated after the given time. This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.

_param _sort _: Literal\['created', 'updated', 'comments'\] | None_ _ = None_\#     

What to sort results by. Can be one of: ‘created’, ‘updated’, ‘comments’. Default is ‘created’.

_param _state _: Literal\['open', 'closed', 'all'\] | None_ _ = None_\#     

Filter on issue state. Can be one of: ‘open’, ‘closed’, ‘all’.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/github.html#GitHubIssuesLoader.lazy_load)\#     

Get issues of a GitHub repository.

Returns:     

  * page\_content

  * metadata          * url

    * title

    * creator

    * created\_at

    * last\_update\_time

    * closed\_time

    * number of comments

    * state

    * labels

    * assignee

    * assignees

    * milestone

    * locked

    * number

    * is\_pull\_request

Return type:     

A list of Documents with attributes

load\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\_and\_split\(

    _text\_splitter : [TextSplitter](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") | None = None_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load Documents and split into chunks. Chunks are returned as Documents.

Do not override this method. It should be considered to be deprecated\!

Parameters:     

**text\_splitter** \(_Optional_ _\[_[_TextSplitter_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") _\]_\) – TextSplitter instance to use for splitting documents. Defaults to RecursiveCharacterTextSplitter.

Returns:     

List of Documents.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

parse\_issue\(

    _issue : dict_, \) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/github.html#GitHubIssuesLoader.parse_issue)\#     

Create Document objects from a list of GitHub issues.

Parameters:     

**issue** \(_dict_\)

Return type:     

[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")

_property _headers _: Dict\[str, str\]_\#     

_property _query\_params _: str_\#     

Create query parameters for GitHub API.

_property _url _: str_\#     

Create URL for GitHub API.

Examples using GitHubIssuesLoader

  * [GitHub](https://python.langchain.com/docs/integrations/document_loaders/github/)

__On this page