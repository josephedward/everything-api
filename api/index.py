import openai
import os
from flask import Flask


# load environment variables
from dotenv import load_dotenv
load_dotenv()

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

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


@app.route('/')
@app.route('/<path:path>')
def catch_all(path=""):

    response = openai.Completion.create(

        engine="text-davinci-003",
        prompt=prompt.replace("{{URL_PATH}}", path),
        max_tokens=100,
        n=1,
        #   stop=None,
        temperature=0.7,
    )

    return response.choices[0].text
    # return html_snippet+response.choices[0].text
    # f"<p>{path}</p>"
