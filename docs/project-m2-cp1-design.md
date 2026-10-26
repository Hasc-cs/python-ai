# Module 2 Checkpoint 1 — AI Content Studio Design

## 1. Project Overview

**Project name:** Sweet Crumbs AI Content Studio  
**Business:** Sweet Crumbs Bakery  
**Location:** Lahore, Pakistan

**Purpose:** The studio generates bakery product descriptions, streams social media posts in different tones, answers customer questions using business facts, maintains short conversation memory, and tracks AI token usage and execution time.

**Technology:** Python, LangChain, and Ollama.

## 2. Facts

The `facts` dictionary stores the bakery's business information. The AI must use only these facts and must say when it does not know an answer.

| **Key** | **Value** |
|---|---|
| `name` | Sweet Crumbs |
| `business` | Bakery |
| `city` | Lahore |
| `hours` | 9 am to 10 pm |
| `delivery` | 200 PKR; free for orders from 3,000 PKR |
| `prices` | Nested dictionary of four products and their prices |

### Product prices

| **Product** | **Price (PKR)** | **Status** |
|---|---:|---|
| Chocolate Cake | 1,500 | Available |
| Cupcake | 250 | Available |
| Brownie | 300 | Available |
| Mango Tart | 0 | Coming soon |

A price of zero means coming soon, not free.

## 3. Tones

The `tones` dictionary defines the styles available for social media posts.

| **Tone** | **Description sent to the AI** |
|---|---|
| `fun` | Playful, cheerful, and catchy |
| `premium` | Elegant and calm, focused on quality |
| `urgent` | Exciting and persuasive, encouraging customers to order soon |

If an unknown tone is entered, the program uses a friendly, clear, and engaging default.

## 4. Which Model for Which Job

Both models are created once at the beginning of the program using `init_chat_model()`.

| **Job** | **Model and temperature** | **Why** |
|---|---|---|
| Menu descriptions | `creative`, 0.8 | Marketing descriptions benefit from varied language. |
| Social media posts | `creative`, 0.8 | Produces engaging posts and supports streaming. |
| Customer chat | `precise`, 0.2 | Encourages focused answers based on business facts. |
| Product price lookup | No AI model | Retrieves fixed prices directly from Python. |
| Session report | No AI model | Calculates statistics from recorded usage. |

### System message

The system message is built from the `facts` dictionary using an f-string. It instructs the AI to use only the provided facts, avoid inventing details, say when information is unknown, and treat price zero as coming soon.

## 5. Command Design

| **Command** | **Function** | **Uses AI?** |
|---|---|---|
| `/menu` | Generates descriptions for available products and displays a numbered menu. | Yes, creative |
| `/post fun` | Creates a post in the fun tone. | Yes, creative |
| `/post premium` | Creates a post in the premium tone. | Yes, creative |
| `/post urgent` | Creates a post in the urgent tone. | Yes, creative |
| `/post pirate` | Uses the default tone because pirate is not configured. | Yes, creative |
| `/price <item>` | Returns a price, coming-soon status, or not-on-menu message. | No |
| `/reset` | Clears conversation history but preserves the system message. | No |
| `bye` | Ends the program and prints the session report. | No |
| Other text | Sends a customer question to the precise model with conversation memory. | Yes |

Commands should work regardless of capitalization. Empty input should ask the user to enter something. `BYE` should end the program.

## 6. Menu Generation

When `/menu` is entered:

1. Loop through `facts["prices"].items()`.
2. Skip products with a price of zero using `continue`, before calling the AI.
3. Use the creative model to generate one sentence for each available product.
4. Store generated results in a list of dictionaries.
5. Use `enumerate()` to display a numbered menu.
6. Format prices with commas, such as `1,500 PKR`.
7. Add the token usage and elapsed time of every completed AI call to the session totals.

## 7. Streaming Social Media Posts

The `/post <tone>` command retrieves the requested tone with `tones.get()` and a default value.

The creative model uses `.stream()` to generate text chunks. Each chunk is printed as it arrives. The program measures the elapsed time and records token usage when the model exposes streaming usage metadata.

## 8. Chat Memory

The `messages` list stores the system message and recent user and assistant messages.

For every chat question:

1. Append the user's question.
2. Trim old messages while preserving the system message and the configured recent-message limit.
3. Call the precise model.
4. Append the assistant's reply.
5. Print the memory size and tokens sent.

The `/reset` command restores the conversation to the system message. Memory is temporary and does not persist after the program exits.

## 9. Session Statistics

The `stats` dictionary tracks the following values.

| **Statistic** | **Purpose** |
|---|---|
| `chat_answers` | Number of customer chat answers. |
| `menu_descriptions` | Number of generated menu descriptions. |
| `posts` | Number of social media posts generated. |
| `price_answers` | Number of `/price` requests. |
| `total_tokens` | Accumulated reported AI token usage. |
| `total_seconds` | Accumulated elapsed time for AI calls. |

The program uses `time.perf_counter()` to measure elapsed time. The final report formats total tokens with commas and total time to one decimal place.

Direct price lookups do not call the AI and do not add AI tokens or AI execution time.

## 10. Feature Tests

Run every test in the program. Enter the actual outcome in the Pass? column after testing.

| **You type** | **Expected** | **Pass?** |
|---|---|---|
| `/menu` | Price-zero item skipped before AI call; numbered menu; prices formatted with commas. | Not tested |
| `/post fun` | Post streams and uses a playful style. | Not tested |
| `/post premium` | Post streams and uses an elegant, quality-focused style. | Not tested |
| `/post urgent` | Post streams and uses an energetic, persuasive style. | Not tested |
| `/post pirate` | Default tone used without a `KeyError`. | Not tested |
| `/price CUPCAKE` | Correct price: 250 PKR, without an AI call. | Not tested |
| `/price mango tart` | Mango Tart is coming soon. | Not tested |
| `/price pizza` | Not on our menu; no crash. | Not tested |
| `My name is Ali`, then `What is my name?` | The tutor remembers Ali while the message remains in memory. | Not tested |
| `/reset`, then `What is my name?` | The tutor says it does not know the name. | Not tested |
| Press Enter without text | Asks again instead of making an AI call. | Not tested |
| `BYE` | Goodbye message and session report with all statistics. | Not tested |

### How to mark the tests

- **Pass:** The observed behavior matches the expected result.
- **Fail:** The program crashes or the observed behavior differs from the expected result.
- **Not tested:** The test has not yet been run.

If a test fails, fix the code, rerun the test, and update the result.

## 11. Implementation Checklist

- [x] Module docstring describing the studio and business.
- [x] Configuration dictionary with model names and memory size.
- [x] Facts dictionary with at least five keys.
- [x] Nested prices dictionary with at least four products, including a zero-price item.
- [x] Three social media tones.
- [x] Two model instances created once with different temperatures.
- [x] System message built using an f-string and factual restrictions.
- [x] Command loop with `/menu`, `/post`, `/price`, `/reset`, and `bye`.
- [x] Price-zero products skipped before AI calls.
- [x] Menu results collected as dictionaries and printed with `enumerate()`.
- [x] Streaming social media generation with a default tone.
- [x] Direct dictionary-based price lookup.
- [x] Bounded chat memory and reset functionality.
- [x] Token and elapsed-time tracking.
- [x] Final session report.
- [x] Feature-test table added.

## Conclusion

Sweet Crumbs AI Content Studio demonstrates how Python can combine fixed business facts with AI-generated content. Creative generation handles marketing tasks, the precise model handles customer questions, and Python handles price lookups and session statistics without unnecessary AI calls.

Feature tests and AI quality tests should be completed by running the program. Actual results must be recorded rather than assumed.
