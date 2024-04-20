"""Module for performing sentiment analysis using an external API.

This module provides functionality to send text to an external sentiment analysis service
and retrieve a sentiment label and score.
"""

import json
# Standard imports should be placed before third-party imports according to PEP8
import requests


def sentiment_analyzer(text_to_analyse):
    """
    Analyze the sentiment of a given text using a predefined external API.

    Parameters:
        text_to_analyse (str): Text to analyze.

    Returns:
        dict: A dictionary containing the sentiment label and score.
    """
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }

    # Adding a timeout to requests.post to avoid indefinite hanging
    response = requests.post(url, json=myobj, headers=header, timeout=10)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None

    return {'label': label, 'score': score}
