import requests

api_key = "53f26b27c0364102b8577f661c513708"
url = ("https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=53f26b27c0364102b8577f661c513708")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])