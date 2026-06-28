# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests>=2.31.0",
# ]
# ///

import requests

response = requests.get("https://example.com")
print(f"Status: {response.status_code}")
