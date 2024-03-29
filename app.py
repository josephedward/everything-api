from openai import OpenAI
import os
from flask import Flask

# load environment variables
from dotenv import load_dotenv

load_dotenv()

# Load OpenAI API key from environment variable

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = """Generate an html document that matches  the following URL path: `{{URL_PATH}}`
add href links to related topics
"""

html_snippet = """
<!doctype html>
<html>
<head><title>Everything Site</title></head>
<body>
"""
app = Flask(__name__)


@app.route("/")
@app.route("/<path:path>")
def catch_all(path=""):
    response = client.completions.create(
        # engine="text-davinci-003",
        model="text-davinci-003",
        prompt=prompt.replace("{{URL_PATH}}", path),
        max_tokens=512,
        n=1,
        temperature=0.7,
    )

    return html_snippet + response.choices[0].text
