# Discount Management System

## Student Information

- **Name:** Yogesh kumar saini
- **Course:** Python Programming
- **Assignment:** 2


---

# Project Overview

This project demonstrates the use of Python control flow statements including:

- if / elif / else
- for loop
- while loop
- break
- continue

No functions, classes, external libraries, or file operations are used as per the assignment instructions.

---

# Task 1: Discount Rules (if / elif / else)

## Objective

Create a program that reads an order amount from the user and applies the appropriate discount.

### Discount Rules

| Order Amount | Discount |
|--------------|----------|
| ≥ 2000 | 15% |
| 1500–1999 | 10% |
| 1000–1499 | 7% |
| Below 1000 | 0% |

### Features

- Accept order amount from the user.
- Validate user input.
- Calculate discount.
- Display discount amount and final payable amount.
- Handle invalid (non-numeric) input.

---

# Task 2: Process Multiple Orders (for loop)

## Objective

Process multiple customer orders using a for loop.

### Features

- Store order amounts in a list.
- Apply discounts to every order.
- Display:
  - Original Order
  - Discount Percentage
  - Final Amount
- Calculate total revenue after discounts.
- (Optional) Count discounted orders.

---

# Task 3: User Menu (while loop + break/continue)

## Objective

Create a menu-driven program using a while loop.

### Menu Options

1. Add a new order amount.
2. Display all orders and total amount after discounts.
3. Quit the program.

### Features

- Repeatedly display menu until user quits.
- Use **continue** for invalid menu choices.
- Use **break** when user selects Quit.
- Maintain a running list of orders.

---

# Task 4: Loop Control with Conditions (break & continue)

## Objective

Practice using break and continue inside a for loop.

### Sales Data

```python
daily = [200, 150, 0, 400, 50, -1, 300]
```

### Rules

- If value is **-1**
  - Stop processing using **break**.
- If value is **0**
  - Skip processing using **continue**.
- Otherwise
  - Add sales to total revenue.
  - Display running total.

### Output

Display the final total sales after processing.

---
