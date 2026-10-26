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
# Sweet Crumbs AI Content Studio 🍰

An AI-powered content studio for **Sweet Crumbs**, a bakery based in Lahore, Pakistan. This project uses Python, LangChain, and Ollama to generate product descriptions, create social media posts, answer customer questions, and provide accurate product prices from a predefined facts dictionary.

## 📌 Project Overview

The Sweet Crumbs AI Content Studio combines AI-generated content with direct business data lookup.

It demonstrates:
- Python loops, dictionaries, lists, functions, and string formatting.
- AI model configuration with different temperature settings.
- Conversation memory and message history management.
- Streaming AI responses.
- Direct price lookup without unnecessary AI calls.
- Token usage and execution-time tracking.
- Feature testing and AI answer quality evaluation.

## ✨ Features

### 1. Interactive Chat

- Answers customer questions about the bakery.
- Uses business facts provided in the system message.
- Maintains conversation history so the AI can remember earlier messages.
- Supports `/reset` to clear conversation history while keeping the system instructions.
- Limits stored conversation messages to control memory usage.

### 2. Product Menu — `/menu`

- Generates a one-sentence AI description for each available product.
- Skips products whose price is `0`, because they are not yet available.
- Displays a numbered menu.
- Formats prices with commas for readability.
- Uses the creative model to produce engaging descriptions.

### 3. Social Media Posts — `/post <tone>`

Generates social media content in different styles:

| Tone | Purpose |
|---|---|
| `fun` | Playful, cheerful, and catchy content |
| `premium` | Elegant content that emphasizes quality |
| `urgent` | Persuasive content that encourages customers to order soon |

The post is streamed so the text appears as the model generates it.

Example:

```text
/post fun
/post premium
/post urgent
```

An unrecognized tone uses the default tone instead of causing a `KeyError`.

### 4. Product Price Lookup — `/price <item>`

Retrieves prices directly from the business dictionary without calling the AI model.

Example commands:

```text
/price Chocolate Cake
/price CUPCAKE
/price Mango Tart
/price Pizza
```

The application handles three situations:

- **Available product:** Displays its price.
- **Coming-soon product:** Displays a coming-soon message when its price is `0`.
- **Unknown product:** Displays `Not on our menu`.

### 5. Session Statistics

At the end of the session, the application reports:

- Number of chat answers.
- Number of menu descriptions generated.
- Number of social media posts generated.
- Number of price queries answered.
- Total AI tokens used.
- Total AI execution time in seconds.

## 🏪 Business Information

The application uses the following predefined facts:

| Key | Value |
|---|---|
| Business Name | Sweet Crumbs |
| Business Type | Bakery |
| City | Lahore |
| Opening Hours | 9 AM – 10 PM |
| Delivery Fee | PKR 200 |
| Free Delivery | Orders of PKR 3,000 or more |

### Product Prices

| Product | Price |
|---|---:|
| Chocolate Cake | PKR 1,500 |
| Cupcake | PKR 250 |
| Brownie | PKR 300 |
| Mango Tart | Coming Soon |

These facts provide the source of truth for business-related answers. The AI should not invent missing prices, services, or business details.

## 🤖 AI Models

The project creates two model instances with different temperature settings.

| Model | Temperature | Used For |
|---|---:|---|
| Precise Model | `0.2` | Customer chat and factual answers |
| Creative Model | `0.8` | Product descriptions and social media posts |
| No AI Model | — | Direct price lookup |

The precise model is configured for more consistent answers, while the creative model is configured for more varied content.

**Note:** The exact model name depends on the configuration in the Python code and the model available through Ollama.

## 💻 Available Commands

| Command | Description |
|---|---|
| `/menu` | Generate and display the product menu |
| `/post <tone>` | Generate a post using a selected tone |
| `/price <item>` | Check a product's price |
| `/reset` | Clear conversation history |
| `bye` | Exit the application and display session statistics |
| Any other text | Ask the AI a customer question |

Commands are intended to work regardless of capitalization. Blank input should be handled without sending an unnecessary AI request.

## 🛠️ Technologies Used

- **Python** — Application logic and data structures.
- **LangChain** — Model initialization and interaction.
- **Ollama** — Access to the configured language model.
- **Markdown** — Project documentation and test reports.

## 📂 Project Structure

The relevant files are organized as follows:

```text
python-ai/
├── code/
│   └── lesson_2_5_ai_content_studio.py
├── docs/
│   ├── project-m2-cp1-design.md
│   └── project-m2-cp1-results.md
├── README.md
├── pyproject.toml
└── uv.lock
```

*The Python filename and project structure should match the files actually present in your repository.*

## ⚙️ Installation and Setup

### Prerequisites

Make sure Python, `uv`, and Ollama are installed and available on your computer. You also need the model specified in your configuration.

### 1. Clone the repository

```bash
git clone https://github.com/Hasc-cs/python-ai.git
cd python-ai
```

### 2. Install project dependencies

```bash
uv sync
```

### 3. Make sure Ollama is ready

Start Ollama and ensure the model configured in the Python file is available. If your configuration uses a cloud model, follow the required Ollama account and authentication setup.

### 4. Run the application

Run the Python file using its actual filename:

```bash
uv run code/lesson_2_5_ai_content_studio.py
```

Follow the terminal prompts to interact with the application.

## 🧪 Testing

The project includes a feature-testing plan and a results document.

- [`docs/project-m2-cp1-design.md`](docs/project-m2-cp1-design.md) — Design decisions, business facts, model selection, and feature test cases.
- [`docs/project-m2-cp1-results.md`](docs/project-m2-cp1-results.md) — Test results, AI answer quality checks, and the best generated social media post.

Important test cases include:

- `/menu` skips the zero-price product and displays numbered items.
- `/post fun`, `/post premium`, and `/post urgent` generate different styles.
- An unknown tone uses the default tone.
- `/price` handles available, coming-soon, and unknown products.
- Conversation memory remembers information until `/reset`.
- Blank input and uppercase `BYE` are handled correctly.
- AI answers are checked for factual accuracy and hallucinations.

**Testing status:** Update the results document after actually running the tests. Do not mark a test as passed until you have verified its output.

## 🎯 Learning Objectives

This project demonstrates how to combine Python fundamentals with AI applications, including:

1. Managing business information using dictionaries.
2. Building an interactive command loop.
3. Selecting models for different tasks.
4. Maintaining and resetting conversation memory.
5. Streaming generated content.
6. Tracking AI usage and execution time.
7. Testing application features and checking AI responses against known facts.

## 📌 Important Note

AI-generated descriptions and posts may vary between runs. Business prices and other fixed details should come from the predefined facts rather than being invented by the model.

---

**Project:** Sweet Crumbs AI Content Studio  
**Module:** Python for AI — Module 2  
**Purpose:** Practice Python programming and AI integration through a practical bakery content application.
