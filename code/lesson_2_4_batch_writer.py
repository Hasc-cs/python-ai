from langchain.chat_models import init_chat_model
import time

business_name = "AI Prompt Kit"

products = [
    {
        "name": "Basic Prompt Pack",
        "price": "PKR 500",
        "details": "10 ready-to-use AI prompts for beginners",
    },
    {
        "name": "Business Prompt Pack",
        "price": "PKR 1,000",
        "details": "Custom prompts for marketing and customer service",
    },
    {
        "name": "Premium Prompt Pack",
        "price": None,
        "details": "Advanced prompts for business automation",
    },
]

llm = init_chat_model(
    "ollama:llama3.2",
    temperature=0.2,
)

total_input_tokens = 0
total_output_tokens = 0
total_tokens = 0
processed_products = 0
skipped_products = 0

start_time = time.perf_counter()

for product in products:
    # Skip products that do not have a price.
    if not product["price"]:
        print(f"\nSkipping {product['name']}: price is missing.")
        skipped_products += 1
        continue

    messages = [
        {
            "role": "system",
            "content": (
                f"You are a product copywriter for {business_name}. "
                "Write an attractive, clear product description. "
                "Use only the supplied product facts. "
                "Do not invent features or promises."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Product name: {product['name']}\n"
                f"Price: {product['price']}\n"
                f"Details: {product['details']}\n\n"
                "Write a short product description for customers."
            ),
        },
    ]

    response = llm.invoke(messages)

    print("\n" + "=" * 40)
    print(f"Product: {product['name']}")
    print(f"Price: {product['price']}")
    print(f"Description:\n{response.text}")

    usage = response.usage_metadata or {}

    input_tokens = usage.get("input_tokens", 0) or 0
    output_tokens = usage.get("output_tokens", 0) or 0
    tokens = usage.get("total_tokens", input_tokens + output_tokens) or 0

    total_input_tokens += input_tokens
    total_output_tokens += output_tokens
    total_tokens += tokens
    processed_products += 1

end_time = time.perf_counter()

print("\n" + "=" * 40)
print("BATCH SUMMARY")
print("=" * 40)
print(f"Products processed: {processed_products}")
print(f"Products skipped: {skipped_products}")
print(f"Input tokens: {total_input_tokens}")
print(f"Output tokens: {total_output_tokens}")
print(f"Total tokens: {total_tokens}")
print(f"Total time: {end_time - start_time:.2f} seconds")
