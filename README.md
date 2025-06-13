# 🦙 Ollama LLaMA3 Chatbot

This is a simple Python chatbot interface that streams responses using the ollama library with the LLaMA3 model.

📦 Features

Streamed responses using Ollama's local language models

Simple terminal-based chat interface

Easy to customize and extend

🛠 Requirements
Python 3.8+
Ollama installed on your system: https://ollama.com
LLaMA3 model pulled locally using ollama pull llama3

🚀 Setup Instructions

1. Clone this repo

git clone https://github.com/yourusername/ollama-chatbot.git
cd ollama-chatbot

2. Create a virtual environment

python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On Mac/Linux

3. Install dependencies

pip install ollama

4. Pull the model

ollama pull llama3

You can verify the model is downloaded:

ollama list

▶️ Run the chatbot

python run.py

Enter your prompts in the terminal and see LLaMA3 respond in real-time.



📂 Project Structure

ollama-chatbot/
├── run.py          # Main script to run the chatbot
├── README.md       # You are here
└── venv/           # Virtual environment (optional)

🧠 Example

You: Who are you?
AI: I am a language model powered by LLaMA3 from Ollama!

🧩 Troubleshooting

❌ model "llama3" not found: → Make sure you've run ollama pull llama3.
❌ Unable to create process...: → Try reinstalling pip or use a clean virtual environment.
