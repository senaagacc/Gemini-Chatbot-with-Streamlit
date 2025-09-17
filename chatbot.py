import google.generativeai as genai

genai.configure(api_key="AIzaSyCL4YpXB7Fx3uk5-JB4WAwZroImHURJamU")

model = genai.GenerativeModel("gemini-1.5-flash")

def get_response(user_input):
    """Kullanıcı mesajını alır ve modelden cevap döndürür."""
    response = model.generate_content(user_input)
    return response.text

