from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

_ = load_dotenv()

llm = ChatGroq(model="qwen/qwen3-32b", temperature=0)

def generate_response(prompt):
    response = llm.invoke([
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content=f"{prompt}")
        ])
    return response.content