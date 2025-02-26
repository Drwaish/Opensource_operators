from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import asyncio
from dotenv import load_dotenv
import os


load_dotenv()
# from llm_init import ChatOpenRouter


from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContextConfig
browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path= '/usr/bin/google-chrome',  # Linux path
        # '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # macOS path
        # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        # For Linux, typically: '/usr/bin/google-chrome'
    )
            
        )

# llm = ChatOpenRouter(model_name="qwen/qwen2.5-vl-72b-instruct:free")
llm = ChatGoogleGenerativeAI(api_key=os.getenv("Google_API_KEY"), model="gemini-2.0-flash")
async def main():
    agent = Agent(
        task="Open a linkedin and find all new Genrative mid or intermmeiate level AI Job postings  globally specially US or Europe of expereince 1 to 2 years, apply from linkedin resume ",
        llm=llm,
        browser=browser  # Uncomment to use your own Chrome browser
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
exit()