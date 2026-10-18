# Module 1 Part 2: Design Document & Test Plan

**Business Name:** Sweet Treats Bakery

**Author:** Student

**Target File:** `code/lesson_08_mini_chatbot.py`

## 1. Intent Design Table

| 

| **Intent Name** | **Keywords / Triggers** | **Bot Response / Action** | 
| **Complaint / Human** | `refund`, `complaint`, `late`, `bad`, `issue` | A manager will call you right away. (Handled first) | 
| **Hours / Timings** | `hours`, `timings`, `open`, `schedule` | We are open daily from 9:00 AM to 10:00 PM. | 
| **Location** | `location`, `address`, `where`, `map` | We are located at Main Commercial Boulevard, Block Y. | 
| **Delivery Info** | `delivery`, `shipping`, `charges` | Delivery fee is 200 PKR, and free for orders from 3,000 PKR and above. | 
| **Menu / Items** | `menu`, `items`, `products`, `bakery` | We offer cupcakes, brownies, and chocolate cakes. Use `/quote` for pricing. | 

## 2. Business Rules Table

| **Rule Category** | **Parameter / Value** | **Description** | 
| **Item Prices** | Cupcake: 250 PKR  Brownie: 300 PKR  Chocolate Cake: 1,500 PKR | Standard unit pricing for menu items. | 
| **Bulk Discount** | 10% off (`0.10`) | Applied automatically if quantity is 10 or more items. | 
| **Delivery Policy** | Fee: 200 PKR  Free Threshold: 3,000 PKR+ | Delivery fee added unless total order meets or exceeds 3,000 PKR. | 
| **Private Words** | `phone`, `cnic`, `my address`, `credit card` | Triggers local model routing with 0.00 AI cost for privacy compliance. | 

## 3. Rule Tests Table

| **You type** | **Expected Response / Action** | **Pass?** | 
| `WHAT are your hours` | Hours (capitals and spaces handled correctly) | \[ \] | 
| `which cake is best?` | Fallback triggered, not a greeting (`hi` hides in `which`) | \[ \] | 
| `my order is late` | Manager reply (complaint rule comes first) | \[ \] | 
| `/quote` (1 expensive item: chocolate cake, qty 1) | Delivery fee charged | \[ \] | 
| `/quote` (big order above free-delivery limit: chocolate cake, qty 3) | Delivery free | \[ \] | 
| `/quote` (10 or more items: brownie, qty 10) | 10% discount applied | \[ \] | 
| `/quote` (item not on menu: pizza) | "Not on our menu", no program crash | \[ \] | 
| A question with `phone` or `cnic` | Routed to local model, cost 0.00 | \[ \] | 
| Press `Enter` with no text | Asks again / loops quietly | \[ \] | 
| `BYE` | Goodbye message + complete session report summary | \[ \] | 

