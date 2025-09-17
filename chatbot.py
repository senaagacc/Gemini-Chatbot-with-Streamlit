import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def get_response(user_input):
    """Kullanıcı mesajını alır ve modelden cevap döndürür."""
    response = model.generate_content(user_input)
    return response.text

