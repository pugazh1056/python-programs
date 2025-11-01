import os, time, json, glob
import openai

CHUNK_DIR = os.getenv("CHUNK_DIR", "./out/chunks")
SUM_DIR = os.getenv("SUMMARY_DIR", "./out/summaries")
os.makedirs(SUM_DIR, exist_ok=True)

openai.api_key = os.getenv("OPENAI_API_KEY")

PROMPT = """Summarize this news in 2-3 lines and give 2-3 tags:
{text}"""

def summarize(text):
    resp = openai.ChatCompletion.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=[{"role":"user","content":PROMPT.format(text=text)}],
        max_tokens=150,
        temperature=0.2
    )
    return resp['choices'][0]['message']['content'].strip()

def processed(f): return os.path.exists(os.path.join(SUM_DIR, os.path.basename(f)))

if __name__ == "__main__":
    print("Summarizer running...")
    while True:
        files = glob.glob(os.path.join(CHUNK_DIR, "*.json"))
        for f in files:
            if processed(f): continue
            with open(f, "r", encoding="utf-8") as fh:
                obj = json.load(fh)
            text = obj.get("text","")
            summary = summarize(text)
            out = {"title": obj.get("title"), "link": obj.get("link"),
                   "source": obj.get("source"), "published": obj.get("published"),
                   "summary": summary}
            out_file = os.path.join(SUM_DIR, os.path.basename(f))
            with open(out_file, "w", encoding="utf-8") as of:
                json.dump(out, of, ensure_ascii=False)
            print("Summarized:", obj.get("title"))
        time.sleep(5)
