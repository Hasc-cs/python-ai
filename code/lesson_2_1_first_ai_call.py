from langchain.chat_models import init_chat_model
import time

topic = input("Enter a topic: ")
level = input("Enter your learning level (beginner/intermediate/advanced): ")

llm = init_chat_model(
    "ollama:gemma4:31b-cloud",
    temperature=0.2
)

messages = [
    {
        "role": "system",
        "content": (
            "You are a friendly AI tutor. "
            "Explain concepts clearly with examples "
            "according to the student's learning level."
        ),
    },
    {
        "role": "user",
        "content": f"Teach me about {topic} at a {level} level.",
    },
]

start_time = time.perf_counter()

response = llm.invoke(messages)

end_time = time.perf_counter()

print("\n" + "=" * 40)
print("           AI TUTOR")
print("=" * 40)
print(response.text)

print("\n" + "=" * 40)
print("           CALL DETAILS")
print("=" * 40)

usage = response.usage_metadata or {}

print(f"Input tokens: {usage.get('input_tokens', 'N/A')}")
print(f"Output tokens: {usage.get('output_tokens', 'N/A')}")
print(f"Total tokens: {usage.get('total_tokens', 'N/A')}")
print(f"Response time: {end_time - start_time:.2f} seconds")
