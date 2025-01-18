import google.generativeai as genai
from dotenv import load_dotenv
import os



load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



class Gemini():
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        print("model loaded.....")
        
    def generate_content(self,question):
        response =  self.model.generate_content(question)
        return response.text