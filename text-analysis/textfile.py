import requests

url = "https://www.gutenberg.org/files/1342/1342-0.txt"  # Pride and Prejudice
response = requests.get(url)

with open("test.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Saved test.txt")