# AI AUTO Browser
Automate yiur browser base task, execute the task from python script.

# Setup
Open the terminal and enter

**Step 1**
Clone the repo:
```bash
git clone https://github.com/Drwaish/Opensource_operators.git
```
**Step 2**
```bash
cd Opersource_operators
```

**Step 3**
Install the requirements:
```bash
pip install -r requireemnts.txt
```

**Step 4**
Now execute the  file:

```bash
python main.py
```
## OR
### If you want to run as an api
```bash
uvicorn api:app --port 8001 --host 0.0.0.0 
```
You can access the swagger file:
```bash
http://127.0.0.1/docs
```

Coming Soon
Docker file.

# Settings
If you want to utilize your own browser go to file make **False** and set path according to your OS.
```bash
browser = Browser(
    config=BrowserConfig(
        headless=True,  # Set to True to disable the browser GUI
        # Specify the path to your Chrome executable
        # chrome_instance_path= '/usr/bin/google-chrome',  # Linux path
        # '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # macOS path
        # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        # For Linux, typically: '/usr/bin/google-chrome'
    )
       
``` 
# .ENV File structure
```bash
Google_API_KEY="<GOOGLE KEY>"
GOOGLE_MODEL= "gemini-2.0-flash"
```

You can create your key from Google AI Studio : https://aistudio.google.com/ 

