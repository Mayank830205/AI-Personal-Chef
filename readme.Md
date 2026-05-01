# 👨‍🍳 AI Personal Chef & Meal Planner

**Prompt Engineering & Persona-Based LLM Application**

---

## 📌 Project Overview

AI Personal Chef & Meal Planner is a **Streamlit-based web application** powered by **Google Gemini 2.5 Flash** that generates creative, zero-waste recipes using only the ingredients provided by the user.

The system is designed to strictly follow constraints, ensuring **no extra ingredients are hallucinated** while respecting dietary preferences.

---

## 🎯 Objective

Develop an LLM-powered assistant that:

* Generates recipes using only user-provided ingredients
* Adheres to dietary restrictions
* Prevents hallucination of additional ingredients
* Produces structured and consistent outputs
* Maintains a defined chef persona throughout responses

---

## 🧠 Prompt Engineering Design

### 👤 Persona: Chef Remy

A creative yet resourceful gourmet chef who:

* Focuses on reducing food waste
* Uses only available ingredients
* Allows basic staples (salt, oil, pepper, water)
* Maintains an enthusiastic and engaging tone

---

### 🏗 Prompt Architecture

#### 🔹 Role-Based Prompt

Defines the assistant identity:

> “You are Chef Remy…”

#### 🔹 Constraint-Based Input

* Accepts ingredient list and dietary restrictions
* Enforces strict ingredient usage

#### 🔹 Few-Shot Learning

* Includes structured recipe examples
* Guides output format and consistency

#### 🔹 Structured Output Format

```
Title:
Prep Time:
Ingredients Used:
Instructions:
```

---

## 🧪 Stress Testing

The system was tested against challenging scenarios:

| Ingredients   | Diet         | Expected Behavior             |
| ------------- | ------------ | ----------------------------- |
| water, flour  | None         | Basic flatbread               |
| tomato        | Vegan        | Simple sautéed dish           |
| ice           | Vegan        | Graceful fallback response    |
| tofu, lettuce | High Protein | Creative protein-based recipe |

---

## 🎨 UI Features

* 🌙 Premium dark mode interface
* ✨ Glassmorphism-style recipe cards
* 🔥 Gradient action buttons
* 🧑‍🍳 Chef-themed branding
* Clean and modern layout

---

## ⚙️ Tech Stack

* **Frontend:** Streamlit
* **LLM:** Google Gemini 2.5 Flash
* **Language:** Python
* **API SDK:** google-genai

---

## 📁 Project Structure

```
AI_Personal_Chef/
│
├── app.py
├── prompt_engine.py
├── requirements.txt
└── README.md
```

---

## 🏆 Key Learning Outcomes

* Controlling LLM hallucinations
* Designing persona-driven AI systems
* Implementing constraint-based prompting
* Structuring LLM outputs
* Enhancing UX with custom UI design
* Deploying LLM-powered applications

---

## 📜 License

This project is created for educational and portfolio purposes.

---

## 👨‍🍳 Author

**Mayank Shringi**
AI & Data Science Enthusiast

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
