# langchain_community.tools.ainetwork.transfer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/ainetwork/transfer.html
**Word Count:** 24
**Links Count:** 14
**Scraped:** 2025-07-21 09:13:22
**Status:** completed

---

# Source code for langchain\_community.tools.ainetwork.transfer               import json     from typing import Optional, Type          from langchain_core.callbacks import AsyncCallbackManagerForToolRun     from pydantic import BaseModel, Field          from langchain_community.tools.ainetwork.base import AINBaseTool                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.ainetwork.transfer.TransferSchema.html#langchain_community.tools.ainetwork.transfer.TransferSchema)     class TransferSchema(BaseModel):         """Schema for transfer operations."""              address: str = Field(..., description="Address to transfer AIN to")         amount: int = Field(..., description="Amount of AIN to transfer")                                             [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.ainetwork.transfer.AINTransfer.html#langchain_community.tools.ainetwork.transfer.AINTransfer)     class AINTransfer(AINBaseTool):         """Tool for transfer operations."""              name: str = "AINtransfer"         description: str = "Transfers AIN to a specified address"         args_schema: Type[TransferSchema] = TransferSchema              async def _arun(             self,             address: str,             amount: int,             run_manager: Optional[AsyncCallbackManagerForToolRun] = None,         ) -> str:             try:                 res = await self.interface.wallet.transfer(address, amount, nonce=-1)                 return json.dumps(res, ensure_ascii=False)             except Exception as e:                 return f"{type(e).__name__}: {str(e)}"