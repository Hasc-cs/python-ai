# Module 2 Checkpoint 1 — AI Content Studio Results

## 1. Test Environment

| **Item** | **Details** |
|---|---|
| Project | Sweet Crumbs AI Content Studio |
| Business | Sweet Crumbs Bakery |
| Location | Lahore, Pakistan |
| Precise model | `ollama:llama3.2`, temperature 0.2 |
| Creative model | `ollama:llama3.2`, temperature 0.8 |
| Test date | Enter the date you ran the tests |

## 2. AI Quality Tests

Run each question in the program and copy the actual AI answer below. Compare the answer against the facts dictionary.

### Test 1: A question the facts can answer

**Question:** What are your opening hours?

**Expected facts:** Sweet Crumbs is open from 9 am to 10 pm.

**Actual AI answer:**

> Paste the actual answer from your program here.

**Evaluation:** Pass / Fail

**Hallucination check:** Correct if the answer accurately states the supplied opening hours without inventing additional details.

### Test 2: A question about a product price

**Question:** How much does a chocolate cake cost?

**Expected facts:** Chocolate Cake costs 1,500 PKR.

**Actual AI answer:**

> Paste the actual answer from your program here.

**Evaluation:** Pass / Fail

**Hallucination check:** Correct if the answer states 1,500 PKR. Incorrect if the answer invents a different price or unsupported offer.

### Test 3: A question the facts cannot answer

**Question:** Do you sell pizza?

**Expected facts:** Pizza is not listed in the bakery's product dictionary.

**Actual AI answer:**

> Paste the actual answer from your program here.

**Evaluation:** Pass / Fail

**Hallucination check:** Correct if the AI says it does not know or that pizza is not listed on the menu. It hallucinates if it claims that Sweet Crumbs sells pizza or invents a pizza price.

## 3. Best Social Media Post

**Command used:** `/post premium`

**Actual generated post:**

> Paste your favorite actual streamed post here.

### Tone comparison

| **Tone** | **Observed style** | **Evaluation** |
|---|---|---|
| Fun | Record the style and quality of your generated post. | Complete after testing |
| Premium | Record the style and quality of your generated post. | Complete after testing |
| Urgent | Record the style and quality of your generated post. | Complete after testing |

**Best tone for Sweet Crumbs:** Enter fun, premium, or urgent after comparing the real outputs.

**Why this tone worked best:** Explain which post best matches the bakery's customers, products, and brand. Consider clarity, appeal, accuracy, and whether it encourages customers to visit or order.

## 4. Feature Test Summary

| **Feature** | **Result** | **Notes** |
|---|---|---|
| `/menu` | Not tested | Verify skipping, numbering, and comma-formatted prices. |
| `/post fun` | Not tested | Verify streaming and tone. |
| `/post premium` | Not tested | Verify streaming and tone. |
| `/post urgent` | Not tested | Verify streaming and tone. |
| `/post pirate` | Not tested | Verify default tone and no crash. |
| `/price CUPCAKE` | Not tested | Verify 250 PKR and no AI call. |
| `/price mango tart` | Not tested | Verify coming-soon response. |
| `/price pizza` | Not tested | Verify not-on-menu response. |
| Chat memory | Not tested | Ask and recall the name Ali. |
| `/reset` | Not tested | Verify the name is no longer remembered. |
| Empty input | Not tested | Verify the program asks again. |
| `BYE` | Not tested | Verify goodbye and session report. |

## 5. Final Evaluation

**Total feature tests passed:** Enter the number after running the tests.

**Total feature tests failed:** Enter the number after running the tests.

**AI quality tests passed:** Enter the number out of three.

**Best-performing tone:** Enter after comparing the outputs.

**Issues discovered:** Describe any incorrect answers, missing token usage, unexpected behavior, or crashes.

**Improvements made:** Record the changes made after testing.

## Conclusion

The AI Content Studio should be evaluated on both functionality and answer quality. Feature tests check the Python program's commands, memory, price handling, and reporting. AI quality tests check whether responses use known facts correctly and admit when information is missing.

Complete this report using actual program outputs before submitting the project.
