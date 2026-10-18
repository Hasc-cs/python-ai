task = input("Task (code / private / chat): ").strip().lower()
tokens = int(input("Estimated tokens: "))

# Private data must never leave the laptop, so check it first
if task== "private":
    model= "llama3.2 (local, Ollama)"
    price= 0.0          # Requirement 4: Local model is free (price = 0)
elif task== "code":
    model= "claude (cloud, strong at code)"
    price= 2.0          # Example price for a heavy coding model
else:
    model= "small cloud model (cheap for chat)"
    price= 0.5          # Example price for a chat model

# Calculate cost based on tokens and the selected model price
cost= (tokens / 1000) * price

if tokens > 4000:
    warning = "Long request: consider shortening it."
else:
    warning = "Length is fine."

print(f"Chosen model: {model}")
print(warning)
print(f"Estimated cost: {cost:.2f} PKR")  