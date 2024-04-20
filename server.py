"""Flask application for sentiment analysis.

This module defines a Flask web application that provides sentiment analysis for given text.
It uses the sentiment_analysis module to analyze the sentiment of text provided via a web interface.
"""

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """
    Analyze the sentiment of the provided text and
    return a string describing the sentiment and its score.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']

    if label is None:
        return "Invalid input! Try again."

    # Adjusted to reduce the line length
    response_message = f"The given text has been identified as {
        label.split('_')[1]} with a score of {score}."
    return response_message


@app.route("/")
def render_index_page():
    """
    Render the index HTML page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
