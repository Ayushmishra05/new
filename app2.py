from langchain_groq import ChatGroq
import streamlit as st 
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

model = ChatGroq(model = 'llama-3.1-70b-versatile' , 
        api_key = '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')

messages = [ ]

while True:
    query = str(input('What is your Query ? '))
    messages.append(HumanMessage(query))
    result = model.invoke(messages)
    print(result.content)
    messages.append(AIMessage(result.content))

