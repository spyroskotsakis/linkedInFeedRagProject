# langchain_community.tools.azure_cognitive_services.utils — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/azure_cognitive_services/utils.html
**Word Count:** 17
**Links Count:** 14
**Scraped:** 2025-07-21 09:16:48
**Status:** completed

---

# Source code for langchain\_community.tools.azure\_cognitive\_services.utils               import os     import tempfile     from urllib.parse import urlparse          import requests                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.azure_cognitive_services.utils.detect_file_src_type.html#langchain_community.tools.azure_cognitive_services.utils.detect_file_src_type)     def detect_file_src_type(file_path: str) -> str:         """Detect if the file is local or remote."""         if os.path.isfile(file_path):             return "local"              parsed_url = urlparse(file_path)         if parsed_url.scheme and parsed_url.netloc:             return "remote"              return "invalid"                                             [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.azure_cognitive_services.utils.download_audio_from_url.html#langchain_community.tools.azure_cognitive_services.utils.download_audio_from_url)     def download_audio_from_url(audio_url: str) -> str:         """Download audio from url to local."""         ext = audio_url.split(".")[-1]         response = requests.get(audio_url, stream=True)         response.raise_for_status()         with tempfile.NamedTemporaryFile(mode="wb", suffix=f".{ext}", delete=False) as f:             for chunk in response.iter_content(chunk_size=8192):                 f.write(chunk)              return f.name