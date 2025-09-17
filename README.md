# 🌟 Mini Gemini Chatbot with Streamlit

A mini chatbot using **Google Gemini API** built with **Streamlit**.  
Quick, clean and interactive demo to show how you can connect a Streamlit UI with Google’s Gemini model.

---

![Demo](./assets/demo.gif)

---

## 🔎 About
This project showcases a lightweight chat application where users can interact with a Google Gemini model in real time via a Streamlit interface. It is ideal as a demo, portfolio item, or starting point for production-grade assistants.

---

## ✨ Features
- 🧠 Powered by **Google Gemini 1.5 Turbo** via `google-generativeai`
- 🖥️ Modern and minimal **Streamlit** UI with `st.chat_message` & `st.chat_input`
- 💬 Multiple conversations handled using `st.session_state`
- 📝 Easy configuration via environment variables or Streamlit secrets
- 🎥 Demo GIF included for instant visual impression

---

## 🚀 Quick start

### Prerequisites
- Python 3.9+
- A Google Cloud API key for the Gemini/Generative AI service

### Install
```bash
git clone https://github.com/your-username/mini-gemini-chatbot.git
cd mini-gemini-chatbot
pip install -r requirements.txt
