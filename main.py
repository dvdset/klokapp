import requests
import time
import random

# Klok API URL
API_URL = "https://api1-pp.klokapp.ai/v1/chat"

# Your session token (update with your actual token)
SESSION_TOKEN = "........."  # Replace with actual token

# Chat ID (from the request body)
CHAT_ID = "..............."  # Replace with actual chat ID

# Load questions from ask.txt
try:
    with open("ask.txt", "r", encoding="utf-8") as file:
        questions = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    print("❌ Error: 'ask.txt' not found.")
    exit()

# Select 10 random questions
random_questions = random.sample(questions, min(10, len(questions)))

# Headers for the request
headers = {
    "x-session-token": SESSION_TOKEN,
    "Content-Type": "application/json"
}

# Function to wait for bot response
def wait_for_response():
    max_wait = 60  # Max wait time (seconds)
    interval = 5  # Check every 5 seconds
    waited = 0

    print("⏳ Waiting for bot response...")
    while waited < max_wait:
        time.sleep(interval)
        waited += interval
        # Add logic here to check if the bot responded (if API provides a way)
        print(f"⌛ {waited}/{max_wait} seconds passed...")
        
        # If we had an API to check response status, we could exit early
        # Example: if check_bot_response(): break  

# Send each question
for question in random_questions:
    payload = {
        "id": CHAT_ID,  # Chat room ID
        "title": "Blockchain Security",  # Chat title
        "language": "english",
        "messages": [{"role": "user", "content": question}],
        "model": "gpt-4o-mini",  # Updated model
        "sources": []
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, stream=False)

        # Print response details
        print(f"📤 Sent: {question}")
        print(f"✅ Status Code: {response.status_code}")

        # Handle response
        if response.headers.get("Content-Type") == "application/json":
            print("📩 Response JSON:", response.json())
        else:
            print("📩 Response Text:", response.text)

    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")

    # Wait for the bot to respond before sending the next question
    wait_for_response()

print("🎯 Done! 10 random questions sent.")
