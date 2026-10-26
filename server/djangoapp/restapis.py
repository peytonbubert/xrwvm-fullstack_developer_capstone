# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


# def get_request(endpoint, **kwargs):
# Add code for get requests to back end
def get_request(endpoint, **kwargs):
    params = ""
    if (kwargs):
        for key, value in kwargs.items():
            params = params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as error:
        # If any error occurs
        print("Network exception occurred: ", error)


# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments
def analyze_review_sentiments(review):
    sentiment_url = os.getenv("sentiment_analyzer_url", "").strip().rstrip("/")

    if not sentiment_url:
        return {"sentiment": "unknown"}

    try:
        encoded_review = quote(str(review), safe="")
        response = requests.get(
            f"{sentiment_url}/analyze/{encoded_review}",
            timeout=30
        )

        response.raise_for_status()
        result = response.json()

        if isinstance(result, dict) and "sentiment" in result:
            return result

        print("Unexpected sentiment response:", result)
        return {"sentiment": "unknown"}

    except Exception as error:
        print("Sentiment analyzer error:", error)
        return {"sentiment": "unknown"}


# def post_review(data_dict):
# Add code for posting review
def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as error:
        print("Network exception occurred: ", error)
