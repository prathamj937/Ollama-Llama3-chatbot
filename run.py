from ollama import chat

def stream_response(prompt):
    print("\nAI: ", end="", flush=True)
    stream = chat(model='llama3', messages=[{"role": "user", "content": prompt}], stream=True)
    for chunk in stream:
        content = chunk['message']['content']
        print(content, end="", flush=True)
    print()

def main():
    print("Welcome to your CLI AI Chatbot! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        stream_response(user_input)
 
if __name__ == "__main__":
    main()  