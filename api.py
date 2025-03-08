import os
import logging
import asyncio
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException,Form
from fastapi.responses import JSONResponse

from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContextConfig

from llm_init import get_llm


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
load_dotenv()


browser = Browser(
    config=BrowserConfig(
        headless=True,  # Set to True to disable the browser GUI
        # Specify the path to your Chrome executable
        # chrome_instance_path= '/usr/bin/google-chrome',  # Linux path
        # '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # macOS path
        # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        # For Linux, typically: '/usr/bin/google-chrome'
    )
            
        )
llm = get_llm()
app = FastAPI()

@app.post("/query")
async def main(query: str = Form(...)):
    try:
        agent = Agent(
            task=query,
            llm=llm,
            browser=browser  # Uncomment to use your own Chrome browser
        )
        result = await agent.run()
        logger.info(f"Result---------: {type(result)}---{result.to_dict()}")
        return result

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# asyncio.run(main("Check my new emails."))
# exit()
