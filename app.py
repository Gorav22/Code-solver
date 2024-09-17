import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
from PIL import Image
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input_prompt,image,input):
    model=genai.GenerativeModel('gemini-1.5-pro-exp-0827')
    response=model.generate_content([input_prompt,image[0],input])
    return response.text

def input_image_setup(uploaded_file):
    if(uploaded_file is not None):
        bytes_data=uploaded_file.getvalue()

        image_parts=[
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data

            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")
    

st.set_page_config(page_title="GLORIO- THE CODE SOLVER")

st.header("Glorio- CODE SOLVER APP")
uploaded_file=st.file_uploader("Choose an image", type=["jpg","jpeg","png"])
input=st.text_input("Enter the prompt here")
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

submit=st.button("Tell me Solution ")

input_prompt="""
You are an expert Coder that can solve any coding problem as well as you can also tell the code error with its solution.
help the students by tell the coding solution of the problem given below but before that please remember that  if i give you to write the code then please give the code in minimum 
time complexity or in the given time complexity. and use cpp as programming language but if student wanted the code in any another language then give the solution in that language only don't refuge the 
the students to give answer of any coding problem.
"""

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Code solution is")
    st.write(response)

