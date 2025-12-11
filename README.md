# Project Guidelines and Tasks

This document outlines the tasks and structure for the **Product Management System** Python project. It is divided into three main sections: **Basic Exercises**, **Project & Module Work**, and **Practical Git Workflow**. Use the table of contents below to jump to different sections.

### Table of Contents
* [Part 1. Basic Exercises](#part-1-basic-exercises)
* [Part 2. Project & Module Work](#part-2-project-module-work)

---

## Part 1. Basic Exercises

[cite_start]This section focuses on implementing the core logic functions for managing inventory [cite: 5-9].

* Create a function `input_product` that allows the user to input a **product name**, **price**, and **stock quantity**. [cite_start]Store this data in a dictionary [cite: 12-14].
* [cite_start]Write a function `calculate_stock_value` that calculates the total value of the inventory (Formula: `Price * Stock`) and prints it to the console[cite: 27].
* [cite_start]Implement a function `calculate_discount` that applies a **5% discount** to products with a stock quantity of **less than 10 units**[cite: 33, 37].
* [cite_start]Create a **recursive function** `print_product_names` to display the list of all available products[cite: 42].
* [cite_start]Create a **recursive function** `find_product_by_name` to search for a specific product and display its details (Price and Stock) or report if not found[cite: 54, 60].

---

## Part 2. Project & Module Work

[cite_start]This section involves structuring the code from Part 1 into a modular project[cite: 10].

* [cite_start]Combine all the previous tasks into a structured project with the following modules [cite: 70-85]:
    * `data_input.py`: A module containing the input logic and the `demo` data generation.
    * `calculations.py`: A module for the **stock value** and **discount** formulas.
    * `general.py`: A module for the **recursive functions** (list display and search).
    * `main.py`: The entry point that imports functions and manages the program flow.
* Add **error handling**: ensure the program handles invalid inputs (e.g., if a user enters text instead of a number for the price) using `try-except` blocks.
* Implement an **infinite loop** in the `main.py` file so the user can perform multiple searches until they type `'exit'`.
