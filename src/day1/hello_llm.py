
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

# Get API key
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai!")

# Initialize Groq client
client = Groq(api_key=my_api_key)

# Select model
model = "openai/gpt-oss-120b"

# User prompt
role = "user"
prompt = "What is an API? Explain with a real-life example."

# System message
message_system = {
    "role": "system",
    "content": "You are a funny teacher. Explain everything using simple Hinglish and funny examples."
}

# User message
message = {
    "role": role,
    "content": prompt
}

# Combine messages
messages = [message_system, message]

# Generate response
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0
)

# Extract AI response
answer = response.choices[0].message.content

# Print output
print("#######################################")
print(answer)


# Combine messages
messages = [message_system, message]

# Generate response
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0
)

# Extract and print answer
answer = response.choices[0].message.content

print("#######################################")
print(answer)
