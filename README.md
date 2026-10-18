This AI Prompt Kit helps small businesses save time, create engaging marketing content, improve customer service, and discover affordable AI tools to grow their business within their monthly budget.
##
Intent Name,Trigger Keywords,Bot Response / Action
1. Complaint / Human,"complaint, human, talk, manager",Transfers to the administration / human desk. (Handled first)
2. Timings,"time, timings, hours, schedule","""Classes run from 3:00 PM to 8:00 PM, Monday to Saturday."""
3. Courses,"course, subjects, teach, classes","""We offer Math, Physics, Chemistry, and English for Grades 9 through 12."""
4. Fees,"fee, price, cost, charges","""Monthly fee ranges from 3,000 to 5,000 PKR per subject depending on the grade."""
5. Location,"location, address, where, map","""We are located near Main Market, Block C. Feel free to visit us!"""
##
# Python for AI - Module 1 Final: Sweet Treats Bakery Chatbot

A smart, rule-based command-line chatbot and fallback AI router built for **Sweet Treats Bakery** as part of the Module 1 final project (`python-ai`).

---

## Project Structure
- `code/lesson_08_mini_chatbot.py` - Main interactive chatbot script.
- `docs/project-m1-part2-design.md` - Design document featuring intent and business rule tables.
- `docs/project-m1-part2-results.md` - AI test prompts and Ollama evaluation results.

---

## 1. Intent Design Table

| Intent Name | Keywords / Triggers | Bot Response / Action |
| :--- | :--- | :--- |
| **Complaint / Human** | `refund`, `complaint`, `late`, `bad`, `issue` | A manager will call you right away. (Handled first) |
| **Hours / Timings** | `hours`, `timings`, `open`, `schedule` | We are open daily from 9:00 AM to 10:00 PM. |
| **Location** | `location`, `address`, `where`, `map` | We are located at Main Commercial Boulevard, Block Y. |
| **Delivery Info** | `delivery`, `shipping`, `charges` | Delivery fee is 200 PKR, and free for orders from 3,000 PKR and above. |
| **Menu / Items** | `menu`, `items`, `products`, `bakery` | We offer cupcakes, brownies, and chocolate cakes. Use `/quote` for pricing. |

---

## 2. Business Rules Table

| Rule Category | Parameter / Value | Description |
| :--- | :--- | :--- |
| **Item Prices** | Cupcake: 250 PKR <br> Brownie: 300 PKR <br> Chocolate Cake: 1,500 PKR | Standard unit pricing for menu items. |
| **Bulk Discount** | 10% off (`0.10`) | Applied automatically if quantity is 10 or more items. |
| **Delivery Policy** | Fee: 200 PKR <br> Free Threshold: 3,000 PKR+ | Delivery fee added unless total order meets or exceeds 3,000 PKR. |
| **Private Words** | `phone`, `cnic`, `my address`, `credit card` | Triggers local model routing with 0.00 AI cost for privacy compliance. |

---

## How to Run
Make sure you have `uv` installed, then run the chatbot script from your terminal:

```bash
uv run code/lesson_08_mini_chatbot.py