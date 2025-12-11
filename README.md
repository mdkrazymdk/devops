# Project Guidelines and Tasks

This document outlines the tasks and structure for a Python project. It's divided into three main sections: **Basic Exercises**, **Project & Module Work**, and **Practical Git Workflow**. Use the table of contents below to jump to different sections.

### Table of Contents
* [Part 1. Basic Exercises]
* [Part 2. Project & Module Work]
* [Part 3. Practical Git Workflow]
---

## Part 1. Basic Exercises

This section focuses on foundational programming tasks.

* Create a function that takes a **string** as an argument and prints it to the console.
* Write a function that accepts a **string** and prints information about it (e.g., whether all letters are uppercase, all lowercase, or mixed case).
* Using a **list comprehension**, create a list of the uppercase letters from the word "smogtether".
* Create a **generator** that alternately returns the words "Even" and "Odd".

---

## Part 2. Project & Module Work

This section involves structuring the code from Part 1 into a modular project.

* Combine all the previous tasks into a structured project with the following modules:
    * A module for the **string functions**.
    * A module for the **generator**.
    * A module with **example code** to run the functions.
* Add **error handling**: if a function receives a non-string type, it should print an error message.

---

## Part 3. Practical Git Workflow

This section is all about applying a standard Git workflow.

* Create a **local Git repository** and perform the work in several branches:
    * `feature/functions` — for implementing the string functions.
    * `feature/generator` — for the generator.
    * `tests` — for the unit tests.
* Make at least **three commits** in each branch.
* Write **unit tests** (for example, for the string functions and the generator) and verify that they pass.
* **Merge** the branches into `main` and create **project versions** (e.g., v0.1).
