model_name = "llama3.2"         
context_window = 12800
price_per_1k_tokens = 0.5            
runs_locally = False    
## Why: int() is used because input() always return a string but we need an integer number to perfrm division and multiplication.
tokens_used = int(input("How many tokens did your chat use ?:"))

## Why: We divide by 1000 because the price is defined per 1,000 tokens,allowing us to find the exact frational cost multiplier.
cost = (tokens_used / 1000) * price_per_1k_tokens

print(f"Estimated cost: {round(cost, 2)} PKR")     
print(f"--{model_name} --")
print(f"Model Name: {model_name} {type(model_name)}")
print(f"Context Window: {context_window} tokens {type(context_window)}")
print(f"Price per 1K tokens: {price_per_1k_tokens} PKR {type(price_per_1k_tokens)}")
print(f"Runs Locally: {runs_locally} {type(runs_locally)}")

