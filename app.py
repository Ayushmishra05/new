from langchain_groq import ChatGroq
import streamlit as st 

model = ChatGroq(model = 'llama-3.1-70b-versatile' , 
        api_key = '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')

# query = 'What is the Capital of India ?'
st.title("Langchain Workshop")
query = st.text_input('What is your Query ? ')
result = model.invoke(query)
st.write(result.content)