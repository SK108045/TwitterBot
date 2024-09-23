# TwitterBot
![Sample Tweet from Tony Will](https://simkafire.com/img/TonyWill2.png)

This Twitter bot uses AI to generate witty, humorous, and engaging tweets automatically. Powered by Google Vertex AI and Tweepy, this bot not only crafts unique tweet content but also finds and posts relevant images, making your Twitter account lively and interactive.

Key Features:

1. 🤖 AI-Generated Tweets: Uses advanced AI models to generate fresh and funny tweets that stand out.

2. 📷 Auto Image Search and Post: Enhances tweets with relevant images using Google Custom Search.

3. 🎯 Customizable Prompts: Includes a variety of prompts to keep the content dynamic and entertaining.

4. 🔥 Easy Setup and Configuration: Quickly set up with your API keys and credentials.

5. 🚀 Automated Posting: Uses a cron job to post directly to your Twitter account at scheduled times, so you don't have to lift a finger


Built With:

- Python: Core language for the bot.
- Tweepy: Handles Twitter API interactions.
- Google Vertex AI: Generates the tweet content.
- Requests: Manages API requests to fetch images.

Perfect For:

- Content creators wanting to automate tweet generation.
- Developers interested in AI-driven content creation.

## Requirements

Before you install and run the bot, ensure you have the following prerequisites:

1. **Python 3.x**: Make sure Python is installed on your system.
2. **Twitter Developer Account**: You’ll need API keys to interact with Twitter’s API.
3. **Google Cloud Account**: For accessing Google Vertex AI and Custom Search API.
4. **Tweepy**: To interact with Twitter's API.
5. **Google Custom Search API**: For searching and posting images.
6. **Cron (Linux) or Task Scheduler (Windows)**: To automate the tweet posting process.

## Installation

To get started with this bot, follow these steps:

```bash
# Clone the repository
git clone https://github.com/SK108045/TwitterBot.git

# Navigate to the project directory
cd TwitterBot

# Install required dependencies
pip install -r requirements.txt
```
## Automating with Cron (for Linux)
If you're running the bot on a Linux server, you can automate the tweet posting process using Cron jobs.

Open the Cron configuration file by running:
```bash
crontab -e
```

Add the following line to schedule the bot to post tweets every day at 7AM, 10AM, 1PM, 3PM and 5PM:

```bash
0 7,10,13,15,17 * * * /usr/bin/python3 /path/to/your/bot.py
```
This will execute the bot script everyday at the specified time. Make sure to replace /path/to/your/bot.py with the actual path to your bot script.
### For Windows

Use Task Scheduler to run the bot script at specific intervals.


## About Tony Will

Tony Will, the Twitter bot, was able to gain over 300 followers within a month of being on the platform.

![AI Tweet Bot Logo](https://simkafire.com/img/TonyWill.png)

### Sample Tweet

Here's an example of the kind of engaging content Tony Will produces:

![Sample Tweet from Tony Will](https://simkafire.com/img/TonyWill2.png)

