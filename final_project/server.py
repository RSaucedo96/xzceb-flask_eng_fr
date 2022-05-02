import json
from machinetranslation import translator
from translator import english_to_french
from translator import french_to_english
from flask import Flask, render_template, request


app = Flask("Web Translator")

@app.route("/english_to_french")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translatedText = english_to_french(textToTranslate)
    return translatedText

@app.route("/french_to_english")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translatedText = french_to_english(textToTranslate)
    return translatedText

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)