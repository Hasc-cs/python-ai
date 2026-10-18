raw_name = input("Your name: ")
raw_question = input("Your question: ")
name = raw_name.strip().title()
clean = raw_question.strip().capitalize()
# Why: Character count measures the text length, and dividing by 4 provides a standard estimation for LLM token consumption.
char_count = len(clean)
estimated_tokens = round(char_count / 4)

# 4. Print whether the question mentions pytho (any capitals), using in
# Why: Converting to lowercase ensures we catch any capitalization variant 

mentions_python = "python" in clean.lower()

# 5. Build and print a multi-line f-string prompt that greets the user by name 
# and limits the question to 150 characters
prompt = f"""
--- AI Prompt ---
   Hello {name}! 
You are a helpful Python tutor. Answer in 3 lines.
Question: {clean[:150]}
-----------------
"""

print(prompt)