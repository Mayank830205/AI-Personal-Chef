👨‍🍳 AI Personal Chef & Meal Planner
Prompt Engineering & Persona-Based LLM Application
📌 Project Overview

AI Personal Chef & Meal Planner is a Streamlit-based web application powered by Google Gemini (2.5 Flash) that generates creative, zero-waste recipes strictly based on available ingredients and dietary restrictions.

This project demonstrates:

Prompt Engineering

Persona Design

Constraint-based generation

Few-shot learning

LLM output structuring

UI customization (Dark-mode premium design)

🎯 Objective

Build an LLM-powered assistant that:

Generates recipes only from user-provided ingredients

Respects dietary restrictions

Avoids hallucinating extra ingredients

Follows a strict structured output format

Maintains a consistent enthusiastic chef persona

🧠 Prompt Engineering Design
👤 Persona: Chef Remy

A Creative but Frugal Gourmet Chef who:

Is passionate about reducing food waste

Uses only provided ingredients

Allows only basic staples (salt, oil, pepper, water)

Maintains enthusiastic, resourceful tone

🏗 Prompt Architecture

Role-Based Prompt

“You are Chef Remy…”

Constraint-Based Input

Accepts:

Ingredient list

Dietary restriction

Strict ingredient usage logic

Few-Shot Learning

Two structured recipe examples included in prompt

Guides model output formatting

Structured Output Format

Title:
Prep Time:
Ingredients Used:
Instructions:

🧪 Stress Testing

Tested with difficult scenarios:

Ingredients	Diet	Expected Behavior
water, flour	None	Basic flatbread
tomato	Vegan	Simple sautéed dish
ice	Vegan	Graceful fallback message
tofu, lettuce	High Protein	Creative protein-based recipe
🎨 UI Features

🌙 Premium Dark Mode

✨ Glassmorphism recipe cards

🔥 Gradient action buttons

🧑‍🍳 Chef-branded styling

Clean and professional layout

⚙️ Tech Stack

Frontend: Streamlit

LLM: Google Gemini 2.5 Flash

Language: Python

API SDK: google-genai

📁 Project Structure
AI_Personal_Chef/
│
├── app.py
├── prompt_engine.py
├── requirements.txt
└── README.md


🏆 Key Learning Outcomes

Controlling LLM hallucinations

Designing persona-driven systems

Implementing constraint-based prompting

Structuring LLM outputs

Improving UX with custom UI design

Deploying LLM applications


📜 License

This project is built for educational and portfolio purposes.

👨‍🍳 Author

Mayank Shringi
AI & Data Science Enthusiast