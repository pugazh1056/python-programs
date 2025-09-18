import requests, json, time, threading
import pathway as pw
from pathway.xpacks.llm import embedders, vectorstores, llms

# -----------------------------
# STEP 1 & 2: Fetch live news and save into JSONL file
# -----------------------------
API_KEY = "90e30d40f7be4b71ab39ae373ff49cdc"   # get from https://newsapi.org
URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
NEWS_FILE = "live_news.jsonl"

def fetch_news():
    """Continuously fetches news and appends to live_news.jsonl"""
    while True:
        try:
            resp = requests.get(URL).json()
            with open(NEWS_FILE, "a") as f:
                for article in resp.get("articles", []):
                    record = {
                        "title": article["title"],
                        "content": article["description"],
                        "publishedAt": article["publishedAt"]
                    }
                    f.write(json.dumps(record) + "\n")
            time.sleep(60)  # fetch every 1 minute
        except Exception as e:
            print("Error fetching news:", e)
            time.sleep(60)

# Run fetching in background thread
threading.Thread(target=fetch_news, daemon=True).start()

# -----------------------------
# STEP 3: Stream news with Pathway
# -----------------------------
news_stream = pw.io.jsonlines.read(NEWS_FILE, mode="streaming")

articles = news_stream.select(
    title = pw.this["title"],
    content = pw.this["content"],
    published = pw.this["publishedAt"]
)

# -----------------------------
# STEP 4: Embed articles in vector store
# -----------------------------
embedder = embedders.OpenAIEmbedder()  # requires OpenAI API key in env
vs = vectorstores.InMemoryVectorStore(articles.content, embedder=embedder)

# -----------------------------
# STEP 5: Connect LLM for answering
# -----------------------------
llm = llms.OpenAIChat()  # also needs OpenAI API key

def answer_question(query):
    context = vs.query(query, k=3)  # get top 3 related articles
    return llm(
        f"You are a helpful news assistant.\n"
        f"Here is the latest news: {context}\n"
        f"Answer this question: {query}\n"
        f"Always include the article titles and timestamps if possible."
    )

# -----------------------------
# STEP 6: Chat loop
# -----------------------------
print("✅ News chatbot is ready! Type your questions below.")
while True:
    q = input("\nAsk about the news (or type 'quit'): ")
    if q.lower() in ["quit", "exit"]:
        break
    print("\n📰 Answer:", answer_question(q))
