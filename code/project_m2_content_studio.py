import time
from langchain.chat_models import init_chat_model
# Why: Keep model settings and memory limits in one place.
config = {
    "precise_model": "ollama:gemma3:1b ",
    "creative_model": "ollama:gemma3:1b ",
    "max_messages": 8,
}

facts = {
    "name": "Sweet Crumbs",
    "business": "Bakery",
    "city": "Lahore",
    "hours": "9 am to 10 pm",
    "delivery": "200 PKR, free for orders from 3,000 PKR",
    "prices": {
        "Chocolate Cake": 1500,
        "Cupcake": 250,
        "Brownie": 300,
        "Mango Tart": 0,
    },
}

tones = {
    "fun": "Playful, cheerful, and catchy",
    "premium": "Elegant and calm, focused on quality",
    "urgent": "Exciting and persuasive, encouraging customers to order soon",
}
precise = init_chat_model(
    config["precise_model"],
    temperature=0.2,
)

creative = init_chat_model(
    config["creative_model"],
    temperature=0.8,
)

system_message = f"""
You are the AI assistant for {facts['name']}, a {facts['business']}
in {facts['city']}.

Business facts:
- Name: {facts['name']}
- Business: {facts['business']}
- City: {facts['city']}
- Hours: {facts['hours']}
- Delivery: {facts['delivery']}
- Prices: {facts['prices']}

Only use these facts when answering business questions.
Never invent products, prices, policies, or business details.
If you do not know a fact, clearly say that you do not know.
A price of 0 means that the product is coming soon.
Keep answers short and helpful.
"""

messages = [
    {"role": "system", "content": system_message}
]
stats = {
    "chat_answers": 0,
    "menu_descriptions": 0,
    "posts": 0,
    "price_answers": 0,
    "total_tokens": 0,
    "total_seconds": 0.0,
}
def record_usage(response, elapsed_seconds):
    """Add token usage and elapsed time for a completed AI call."""
    usage = getattr(response, "usage_metadata", None) or {}

    stats["total_tokens"] += (
        usage.get("total_tokens")
        or usage.get("input_tokens", 0) + usage.get("output_tokens", 0)
    )
    stats["total_seconds"] += elapsed_seconds
print("=" * 50)
print("   Sweet Crumbs AI Content Studio")
print("=" * 50)
print("Commands: /menu, /post fun|premium|urgent, "
      "/price <item>, /reset, bye")

while True:
    user_input = input("You: ").strip()

    # Why: Ignore empty input so it does not waste a model call.
    if not user_input:
        print("Studio: Please enter a question or command.")
        continue

    command_parts = user_input.split(maxsplit=1)
    command = command_parts[0].lower()
    argument = command_parts[1].strip() if len(command_parts) > 1 else ""

    if command == "bye" and not argument:
        print("Studio: Goodbye!")
        break

    elif command == "/reset" and not argument:
        messages = [{"role": "system", "content": system_message}]
        print("Studio: Chat memory cleared.")

    elif command == "/price":
        stats["price_answers"] += 1
        item_name = argument.casefold()

        matched_item = next(
            (
                (name, price)
                for name, price in facts["prices"].items()
                if name.casefold() == item_name
            ),
            None,
        )

        # Why: Prices are fixed business facts, so no AI call is needed.
        if matched_item is None:
            print("Studio: That item is not on our menu.")
        else:
            name, price = matched_item
            if price == 0:
                print(f"Studio: {name} is coming soon.")
            else:
                print(f"Studio: {name} costs {price:,} PKR.")

    elif command == "/menu" and not argument:
        menu_items = []

        for item_name, price in facts["prices"].items():
            # Why: Skip unavailable products before calling the AI.
            if price == 0:
                print(f"Studio: Skipping {item_name.casefold()} "
                      "(coming soon)")
                continue

            prompt = [
                {
                    "role": "system",
                    "content": (
                        f"You write product descriptions for {facts['name']}. "
                        "Use only the supplied facts. Write exactly one "
                        "appealing sentence and invent no details."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Product: {item_name}. "
                        f"Price: {price:,} PKR. "
                        "Write a one-sentence product description."
                    ),
                },
            ]

            start_time = time.perf_counter()
            response = creative.invoke(prompt)
            elapsed_seconds = time.perf_counter() - start_time

            record_usage(response, elapsed_seconds)

            menu_items.append({
                "name": item_name,
                "price": price,
                "description": response.text,
            })
            stats["menu_descriptions"] += 1

        print("-" * 50)

        for number, item in enumerate(menu_items, start=1):
            print(f"{number}. {item['name']} ({item['price']:,} PKR)")
            print(f"   {item['description']}")

        print("-" * 50)

    elif command == "/post":
        tone_name = argument.casefold()
        tone_description = tones.get(
            tone_name,
            "Friendly, clear, and engaging",
        )

        prompt = [
            {
                "role": "system",
                "content": (
                    f"You create social media posts for {facts['name']}. "
                    f"Tone: {tone_description}. "
                    f"Business facts: {facts}. "
                    "Use only these facts. Never invent offers or products. "
                    "Write a short, ready-to-publish post."
                ),
            },
            {
                "role": "user",
                "content": "Write a social media post for our bakery.",
            },
        ]

        print(f"Studio ({tone_description}):")

        start_time = time.perf_counter()
        final_chunk = None

        for chunk in creative.stream(prompt):
            if chunk.content:
                if isinstance(chunk.content, str):
                    print(chunk.content, end="", flush=True)
                else:
                    for block in chunk.content:
                        if isinstance(block, dict) and block.get("text"):
                            print(block["text"], end="", flush=True)

            # Keep the latest usage metadata exposed by the model.
            if getattr(chunk, "usage_metadata", None):
                final_chunk = chunk

        elapsed_seconds = time.perf_counter() - start_time
        print()

        if final_chunk is not None:
            record_usage(final_chunk, elapsed_seconds)
        else:
            stats["total_seconds"] += elapsed_seconds

        stats["posts"] += 1

    else:
        # All other input is treated as a chat question.
        messages.append({"role": "user", "content": user_input})

        # Keep the system message and the most recent conversation messages.
        messages = [
            messages[0]
        ] + messages[1:][-config["max_messages"]:]

        start_time = time.perf_counter()
        response = precise.invoke(messages)
        elapsed_seconds = time.perf_counter() - start_time

        record_usage(response, elapsed_seconds)

        messages.append({
            "role": "assistant",
            "content": response.text,
        })

        stats["chat_answers"] += 1

        usage = response.usage_metadata or {}
        tokens_sent = (
            usage.get("input_tokens")
            if usage.get("input_tokens") is not None
            else "N/A"
        )

        print(f"Studio: {response.text}")
        print(
            f"        (memory: {len(messages) - 1} messages, "
            f"{tokens_sent} tokens sent)"
        )

print("=" * 50)
print("Session report")
print(
    f"Chat answers: {stats['chat_answers']} | "
    f"Menu descriptions: {stats['menu_descriptions']} | "
    f"Posts: {stats['posts']} | "
    f"Price answers: {stats['price_answers']}"
)
print(
    f"AI usage: {stats['total_tokens']:,} tokens in "
    f"{stats['total_seconds']:.1f} seconds"
)
print("=" * 50)
