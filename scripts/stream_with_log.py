#!/usr/bin/env python3
"""
OpenAI Streaming Chat with Logging

This script provides a simple interface to interact with OpenAI's chat models:
- Prompts for user input
- Streams the response in real time
- Saves the full conversation to a timestamped file

Requirements:
    pip install openai

Usage:
    python stream_with_log.py
"""

import openai
import datetime
import os

openai.api_key = "your-api-key-here"

LOG_DIR = "responses"

def ensure_log_dir():
    """Create the responses directory if it doesn't exist"""
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

def save_response_to_file(prompt, response_text):
    """Save the prompt and response to a timestamped file"""
    ensure_log_dir()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{LOG_DIR}/response_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("PROMPT:\n")
        f.write(prompt + "\n\n")
        f.write("RESPONSE:\n")
        f.write(response_text)
    print(f"\n\nSaved full response to: {filename}")

def stream_response(prompt: str):
    """Stream a response from OpenAI and save it to a file"""
    print("\nStreaming response...\n")

    response_stream = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    full_response = ""
    for chunk in response_stream:
        if chunk.choices[0].delta.get("content"):
            content = chunk.choices[0].delta["content"]
            print(content, end="", flush=True)
            full_response += content

    print("\n\nStreaming complete!")
    save_response_to_file(prompt, full_response)

if __name__ == "__main__":
    user_prompt = input("What would you like to ask the model?\n> ")
    stream_response(user_prompt)
