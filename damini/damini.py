# import chainlit as cl
# import google.generativeai as genai
# import os
# from langchain_groq import ChatGroq
#
# # Configure GenAI for the chatbot
# groq_api_key = os.getenv("GROQ_API_KEY")
#
# def reply(user_message):
#     # Set up the model (Use the appropriate model for your chatbot)
#     model = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma2-9b-it")
#
#     # Start conversation and get response
#     response = model.invoke(user_message)  # This returns the response directly
#
#     # Get the response text from the model's output
#     return response.content  # Return the generated response text directly
#
# # Chainlit interface setup
# @cl.on_message
# async def main(message: cl.Message):
#     # Extract the actual text content from the message object
#     user_message = message.content
#
#     # Process the user's message and get a reply
#     response = reply(user_message)
#
#     # Send the response message
#     await cl.Message(content=response).send()


import chainlit as cl
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field  # Ensure compatibility with Pydantic v2

# Configure GenAI for the chatbot
groq_api_key = "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"


# Set up your other LLM here (e.g., using OpenAI's API)
# This is a placeholder, replace it with your actual LLM setup
other_llm = None  # Initialize your preferred LLM

def reply(user_message):
    # Set up the model (Use the appropriate model for your chatbot)
    model = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma2-9b-it", temperature=0.8)

    # Start conversation and get response
    response = model.invoke(user_message)  # This returns the response directly

    # Get the response text from the model's output
    return response.content  # Return the generated response text directly

# Chainlit interface setup
@cl.on_message
async def main(message: cl.Message):
    if message.content:
        # Treat the content as text
        text_input = message.content  # Extract the text content
        # Process the text with your ChatGroq model
        response = reply(text_input)
        await cl.Message(content=response).send()
    else:
        await cl.Message(content="No message content received.").send()
