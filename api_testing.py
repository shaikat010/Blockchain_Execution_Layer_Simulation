# This script is for testing the apis that have been built
import requests

# The API endpoint
url = "http://127.0.0.1:8000/get_public_key"

# A GET request to the API
response = requests.get(url)

print(response.content)

print(str(response))

