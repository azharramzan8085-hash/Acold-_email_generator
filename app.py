import streamlit as st
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("📧 AI Cold Email Generator")

name = st.text_input("Your Name")
company = st.text_input("Company Name")
role = st.text_input("Job Role")
skills = st.text_area("Your Skills")
experience = st.text_area("Your Experience")

if st.button("Generate Email"):
    prompt = f"""
    Write a professional cold email for a job application.

    Name: {name}
    Company: {company}
    Role: {role}
    Skills: {skills}
    Experience: {experience}

    Mention resume attachment and end politely.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    st.text_area("Generated Email", response.choices[0].message.content, height=300)
