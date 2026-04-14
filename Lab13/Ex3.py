from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def get_meme():
    url = "https://meme-api.com/gimme/wholesomememes"
    
    response = requests.request("GET", url)
    meme_data = response.json()

    meme_url = meme_data["url"]
    meme_title = meme_data["title"]
    meme_subreddit = meme_data["subreddit"]

    return render_template(
        "index.html",
        meme_url=meme_url,
        meme_title=meme_title,
        meme_subreddit=meme_subreddit
    )

if __name__ == "__main__":
    app.run(debug=True)