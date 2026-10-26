from langchain.chat_models import init_chat_model

llm = init_chat_model("ollama:llama3.2",
                       temperature=0.2)

messages = [
    {
        "role": "system",
        "content": (
            "You are a friendly personal tutor. "
            "Remember what the student says during the conversation. "
            "Give short, clear answers with simple examples."
        ),
    }
]

print("Tutor: Ask me anything. Commands: /reset, /count, bye")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "bye":
        print("Tutor: Goodbye!")
        break

    if user_input == "/reset":
        messages = [messages[0]]
        print("Tutor: Memory cleared.")
        continue

    if user_input == "/count":
        print(f"Tutor: {len(messages)} messages in memory.")
        continue

    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})

    response = llm.invoke(messages)

    messages.append({"role": "assistant", "content": response.text})

    print(f"Tutor: {response.text}")

    usage = response.usage_metadata or {}
    tokens_sent = usage.get("input_tokens", "N/A")
    print(f"(tokens sent: {tokens_sent})")
    messages = [messages[0]] + messages[1:][-8:]
