import requests

data = {
    "storage_needed": 10000,
    "storage_type": "E-commerce",
    "number_of_regions": 2
}

response = requests.post("https://splendid-cat-2aebeb.netlify.app/.netlify/functions/process_call", json=data)
print(response.json())