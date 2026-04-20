

# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import PromptTemplate
# from dotenv import load_dotenv

# from langchain_core.output_parsers import JsonOutputParser            #CONVERT that JSON → Python dict
# import os

# load_dotenv()

# # create model
# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )

# # create prompt
# prompt = PromptTemplate.from_template(
#     """
#     Explain {topic} in:
#     - 2 bullet points
#     - simple language
#     """
# )

# # chain
# chain = prompt | llm

# # run
# response = chain.invoke({"topic": "dogs"})

# # output
# print(response.content)

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser               #CONVERT that JSON → Python dict
from dotenv import load_dotenv
import os

load_dotenv()

# 1. LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# 2. Parser
parser = JsonOutputParser()            

# 3. Prompt      #FORCE model to output JSON (using prompt)


prompt = PromptTemplate(
    template="""
You are a helpful assistant.

Explain {topic} simply.

Format your response EXACTLY as JSON:

{{
  "topic_name": "...",
  "facts": ["...", "..."],                    
  "fun_fact": "..."
}}

Do not write anything outside JSON.
""",
    input_variables=["topic"]
)

# 4. Chain
chain = prompt | llm | parser

# 5. Run
response = chain.invoke({"topic": "Quantum Computing"})

# 6. Output
print(type(response))
print(response)
print(response["facts"])