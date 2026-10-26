from langchain.chat_models import init_chat_model

facts = {
    "business_name": "AI Prompt Kit",
    "service": "Custom AI prompts for business tasks",
    "price": "PKR 1,000 per prompt pack",
    "delivery": "Within 2 working days",
    "contact": "your-email@example.com",
}

personas = {
    "friendly": "You are a friendly and helpful business assistant. Use warm, simple language.",
    "professional": "You are a professional business consultant. Be clear, polite, and concise.",
    "fun": "You are a cheerful and playful business assistant. Keep replies light and engaging.",
}

current_persona = "friendly"

llm = init_chat_model(
    "ollama:llama3.2",
    temperature=0.2,
)


def make_system_message():
    return (
        f"You are the assistant for {facts['business_name']}.\n"
        f"Business facts: {facts}\n\n"
        f"Your persona: {personas[current_persona]}\n\n"
        "Rules:\n"
        "- Answer business questions using only the provided facts.\n"
        "- Never invent prices, services, or contact details.\n"
        "- If a fact is missing, say you don't have that information.\n"
        "- Keep answers short and helpful."
    )


messages = [
    {"role": "system", "content": make_system_message()}
]

print(f"Welcome to {facts['business_name']}!")
print("Commands: /persona, /price, /reset, /count, bye")
print("Available personas: friendly, professional, fun")

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    if user_input == "/persona":
        print("Choose: friendly, professional, fun")
        pass

    if user_input.startswith("/persona "):
        selected = user_input.split(maxsplit=1)[1].lower()

        if selected in personas:
            current_persona = selected
            messages = [
                {"role": "system", "content": make_system_message()}
            ]
            print(f"Bot: Persona changed to {current_persona}.")
        else:
            print("Bot: Invalid persona. Choose friendly, professional, or fun.")
        continue

    # Answer the price directly from Python, without an AI call.
    if user_input == "/price":
        print(f"Bot: {facts['business_name']} costs {facts['price']}.")
        continue

    if user_input == "/reset":
        messages = [
            {"role": "system", "content": make_system_message()}
        ]
        print("Bot: Conversation reset.")
        continue

    if user_input == "/count":
        print(f"Bot: {len(messages) - 1} messages in conversation history.")
        continue

    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})

    response = llm.invoke(messages)

    print(f"Bot ({current_persona}): {response.text}")

    messages.append(
        {"role": "assistant", "content": response.text}
    )

    messages = [messages[0]] + messages[1:][-8:]
