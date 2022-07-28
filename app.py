import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv(
    "OPENAI_API_KEY")


@app.route("/korean/", methods=("GET", "POST"))
def ko():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"Translate this into 1. Korean:\n\n{animal}\n\n1. ",
            temperature=0.3,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return redirect(url_for("ko", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


@app.route("/english/", methods=("GET", "POST"))
def en():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"Translate this into 1. english:\n\n{animal}\n\n1. ",
            temperature=0.3,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return redirect(url_for("en", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index_2.html", result=result)


@app.route("/sentiment/", methods=("GET", "POST"))
def sentiment():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"Decide whether a Tweet's sentiment is positive, neutral, or negative.\n\nTweet: \"{animal}\"\nSentiment:",
            temperature=0,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return redirect(url_for("sentiment", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index_3.html", result=result)


@app.route("/movie/", methods=("GET", "POST"))
def movie():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"Convert movie titles into emoji.\n\nBack to the Future: 👨👴🚗🕒 \nBatman: 🤵🦇 \nTransformers: 🚗🤖 \n{animal}:",
            temperature=0.8,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\n"]
        )
        return redirect(url_for("movie", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index_4.html", result=result)


@app.route("/chat/", methods=("GET", "POST"))
def chat():
    if request.method == "POST":
        animal = request.form["animal"]

        response_1 = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"Translate this into 1. english:\n\n{animal}\n\n1. ",
            temperature=0.3,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        result_1 = response_1.choices[0].text

        response_2 = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"Marv is a chatbot that reluctantly answers questions with sarcastic responses:\n\nYou: How many pounds are in a kilogram?\nMarv: This again? There are 2.2 pounds in a kilogram. Please make a note of this.\nYou: What does HTML stand for?\nMarv: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.\nYou: When did the first airplane fly?\nMarv: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.\nYou: What is the meaning of life?\nMarv: I’m not sure. I’ll ask my friend Google.\n{result_1}\nMarv:",
            temperature=0.5,
            max_tokens=1000,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=0.0
        )
        result_2 = response_2.choices[0].text

        response_3 = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"Translate this into 1. Korean:\n\n{result_2}\n\n1. ",
            temperature=0.3,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        return redirect(url_for("chat", result=response_3.choices[0].text))

    result = request.args.get("result")
    return render_template("index_5.html", result=result)

# def generate_prompt(animal):
#     return """Suggest three names for an animal that is a superhero.

# Animal: Cat
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
# Animal: {}
# Names:""".format(
#         animal.capitalize()
#     )
