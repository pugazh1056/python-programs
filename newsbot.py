import os
import time
import feedparser
import pathway as pw
from fastapi import FastAPI
import uvicorn
import openai
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# RSS feeds
FEEDS = [
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "https://feeds.bbci.co.uk/news/world/rss.xml"
]

# Pathway connector: fetch live news
class NewsStream(pw.io.python.ConnectorSubject):
    def run(self):
        while True:
            for url in FEEDS:
                feed = feedparser.parse(url)
                for entry in feed.entries[:3]:
                    self.emit({"title": entry.title, "link": entry.link})
            time.sleep(60)  # every 1 minute

# Summarizer
def summarize(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Summarize this news: {text}"}]
    )
    return response["choices"][0]["message"]["content"]

# Pathway pipeline
stream = NewsStream()
table = pw.io.python.read(stream)

summaries = table.select(
    title=table["title"],
    summary=table["title"].map(summarize)
)

pw.io.jsonlines.write(summaries, "summaries.jsonl")

# FastAPI server
app = FastAPI()

@app.get("/summaries")
def get_summaries():
    if not os.path.exists("summaries.jsonl"):
        return {"news": []}
    with open("summaries.jsonl", "r", encoding="utf-8") as f:
        lines = f.readlines()
    return {"news": [line.strip() for line in lines]}

if __name__ == "__main__":
    # Run Pathway + API server
    pw.run()
    uvicorn.run(app, host="0.0.0.0", port=8000)
