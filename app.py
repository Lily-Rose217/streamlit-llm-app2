from dotenv import load_dotenv
import os
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain.chat_models import ChatOpenAI

def generate_response(user_input, expert_type):
    if expert_type == "医療の専門家":
        system_message = "あなたは医療の専門家として、健康や病気に関する質問に的確に答えてください。"
    elif expert_type == "教育の専門家":
        system_message = "あなたは教育の専門家として、生徒の学習に関するアドバイスを丁寧に行ってください。"
    else:
        system_message = "あなたは旅行プランナーとして、旅行先の提案や観光情報をわかりやすく案内してください。"

    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_input)
    ]

    response = chat(messages)
    return response.content

st.title("専門家相談アプリ")
expert_type = st.selectbox("相談したい専門家を選択してください", ["医療の専門家", "教育の専門家", "旅行プランナー"])
st.write(f"選択された専門家: {expert_type}")    

user_input = st.text_input("相談したい内容を入力してください")
if st.button("送信") and user_input:
    response = generate_response(user_input, expert_type)
    st.write(response)
