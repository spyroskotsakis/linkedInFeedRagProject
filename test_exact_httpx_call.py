#!/usr/bin/env python3
"""
Test the exact httpx call that's failing
"""

import asyncio
import httpx
import json

async def test_exact_call():
    """Test the exact httpx call that's failing."""
    base_url = "http://host.docker.internal:11434"
    
    # This is the exact payload that the RAG system is sending
    payload = {
        "model": "mistral-nemo:12b",
        "prompt": """Context: Document 1 (by Awa K. Penn): How to build an AI agent using n8n

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

Document 2 (by Fortune): Aravind Srinivas wanted a simple answer. If Google had given him one, things might have turned out differently—for Srinivas and for Google.

It was the fall of 2022, weeks before OpenAI would debut its viral AI chatbot, ChatGPT. Srinivas, then 28, was an ambitious AI researcher with a PhD from UC Berkeley and prestigious internships at OpenAI and Google's AI labs under his belt, plus a year working full-time for OpenAI after earning his doctorate. Now he'd left that plum job to launch a startup with three cofounders, all AI experts.

Weeks later, ChatGPT launched. Seven days after that, Srinivas and his cofounders debuted their San Francisco–based company and its breakthrough product. They called both—borrowing a machine-learning term for how well an AI model makes predictions. Even amid the buzz around ChatGPT, Perplexity gained traction among Silicon Valley's elite and, through word of mouth, among consultants, analysts, and journalists.

Read the full story here:

Question: what do you know about n8n?

Please provide a helpful answer based on the context provided. If the context doesn't contain relevant information, say so.""",
        "stream": False,
        "options": {
            "temperature": 0.1,
            "num_predict": 2048
        }
    }
    
    print(f"Testing exact call to: {base_url}/api/generate")
    print(f"Payload size: {len(json.dumps(payload))} characters")
    
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            print("Sending POST request...")
            response = await client.post(
                f"{base_url}/api/generate",
                json=payload
            )
            
            print(f"Response status: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                response_text = result.get("response", "No response generated")
                print(f"✅ Success! Response: {response_text[:100]}...")
                return True
            else:
                print(f"❌ Error response: {response.text}")
                return False
                
    except Exception as e:
        print(f"❌ Exception: {e}")
        print(f"Exception type: {type(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_exact_call())
    print(f"Overall success: {success}") 