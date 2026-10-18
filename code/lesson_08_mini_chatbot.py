name = input("Welcome to Bright Future Tuition Centre! What is your name? ")
name = name.strip().title()

print(f"\nHello {name}Ask about timings, fees, location or appointments. Type 'bye' to exit")

message_count = 0
unanswered_count = 0

while True:
    raw_msg = input(f"{name}: ")

    msg = raw_msg.strip().lower()
    
    if msg in ["bye", "goodbye", "exit"]:
        print(f"\nBot: Goodbye {name}! Have a wonderful day.")
        break
    
    # We increment the message count for every valid query to track engagement.
    message_count += 1
    
    if "complaint" in msg or "human" in msg or "talk" in msg or "manager" in msg:
        print(f"Bot: I am connecting you with our administrator right away, {name}. Please hold.")
        
    elif "time" in msg or "timings" in msg or "hours" in msg:
        print("Bot: Classes run from 3:00 PM to 8:00 PM, Monday to Saturday.")
        
    elif "course" in msg or "subjects" in msg or "teach" in msg:
        print("Bot: We offer Math, Physics, Chemistry, and English for Grades 9 through 12.")
        
    elif "fee" in msg or "price" in msg or "cost" in msg:
        print("Bot: Monthly fee ranges from 3,000 to 5,000 PKR per subject depending on the grade.")
        
    elif "location" in msg or "address" in msg or "where" in msg:
        print("Bot: We are located near Main Market, Block C. Feel free to visit us!")
        
    else:
        unanswered_count += 1

        print("Bot [Fallback AI Prompt Simulation]:")
        print(f"-> System: You are a helpful tuition centre receptionist. Answer {name}'s query.")
        print(f"-> Question: {raw_msg}\n")


print(f"--- Session Summary for {name} ---")
print(f"Total messages sent: {message_count}")
print(f"Unanswered (fallback) queries: {unanswered_count}")
