# from langchain_google_genai import ChatGoogleGenerativeAI
# import os

# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )

# response = llm.invoke("Explain AI in 2 lines")
# print(response.content)

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

# create model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# create prompt
prompt = PromptTemplate.from_template(
    """
    Explain {topic} in:
    - 2 bullet points
    - simple language
    """
)

# chain
chain = prompt | llm

# run
response = chain.invoke({"topic": "dogs"})

# output
print(response.content)