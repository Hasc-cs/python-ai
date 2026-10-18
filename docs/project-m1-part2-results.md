## 3. Rule Tests Table

| You type | Expected | Pass? |
| :--- | :--- | :--- |
| `WHAT are your hours` | Hours (capitals and spaces handled) | Yes |
| `which cake is best?` | Fallback, **not** a greeting (`"hi"` hides in `"which"`) | Yes |
| `my order is late` | Manager reply (complaint rule first) | Yes |
| `/quote` , 1 of your most expensive item | Delivery fee charged | Yes |
| `/quote` , a big order above the free-delivery limit | Delivery free | Yes |
| `/quote` , 10 or more items | Discount applied | Yes |
| `/quote` , an item not on your menu | `"Not on our menu"`, no crash | Yes |
| `A question with "phone" or "cnic"` | Routed to the local model, cost 0 | Yes |
| `Press Enter with no text` | Asks again | Yes |
| `BYE` | Goodbye + session report | Yes |