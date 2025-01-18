from Model import Gemini
from flask import Flask





model=Gemini()

app = Flask(__name__)

quit=False
Template='''
You are a helpful assistant, who helps the user to find good gift suggestions and provides links for the same. 
You must ask at least 5-10 questions to the USER before providing the output. The questions should be one at a time. 
Your final response after 5-10 questions should strictly be in JSON format, mentioning each question with its description.

Context so far:
{context}
'''
context=[]
print("HEllo USer___")
while True:
     question=f'user:{input()}'
     if question.lower().split(":")[1] == "q":  # Quit if the user types 'q' or 'Q'
        break
     else:
        
        context.append(f"User: {question}")

       
        formatted_prompt = Template.format(context="\n".join(context))
        
        
        response = model.generate_content(formatted_prompt)
     
        print(f"Assistant: {response}")
        context.append(f"Assistant: {response}")
print('Chat ended .... ')
print("Here is your chat history:")
print(context)    