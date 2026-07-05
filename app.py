import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from tools import calculator

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
)

agent = create_react_agent(
    model=llm,
    tools=[calculator],
)

print("=" * 50)
print("Calculator Agent")
print("=" * 50)

while True:
    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:
        break

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question,
                }
            ]
        }
    )

    print("\nAgent:", response["messages"][-1].content)