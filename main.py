



import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# --- CONFIGURATION (Change these to generalize) ---
MODEL_NAME = "gemini-2.5-flash"
EMBEDDING_MODEL = "gemini-embedding-001"
INDEX_NAME = "research-assistant"

# This is your "System Instructions" - change this to change the AI's personality
SYSTEM_PROMPT = """
You are a highly capable AI Assistant. 
Your primary goal is to provide continuity by referencing the HISTORY provided below.
If the HISTORY contains personal details (like name, age, or goals), always acknowledge them.
If HISTORY is empty, start fresh but be ready to remember.

HISTORY:
{history}

CURRENT QUESTION: {input}
"""

# --- SETUP ---
llm = ChatGoogleGenerativeAI(model=MODEL_NAME)
embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)

vector_db = PineconeVectorStore(
    index_name=INDEX_NAME, 
    embedding=embeddings,
    pinecone_api_key=os.getenv("PINECONE_API_KEY")
)

# --- LOGIC ---
def get_memory_context(query):
    try:
        # Search the cloud for context
        docs = vector_db.similarity_search(query, k=3)
        return "\n".join([d.page_content for d in docs]) if docs else ""
    except Exception:
        return ""

def ask_ai(user_input):
    # 1. Retrieve context
    history = get_memory_context(user_input)
    
    # 2. Build Prompt
    prompt = ChatPromptTemplate.from_template(SYSTEM_PROMPT)
    
    # 3. Generate Response
    chain = prompt | llm
    response = chain.invoke({"input": user_input, "history": history})
    
    # 4. Store interaction (This makes it remember)
    interaction = f"User: {user_input}\nAI: {response.content}"
    vector_db.add_texts([interaction])
    
    return response.content

# --- EXECUTION ---
if __name__ == "__main__":
    print(f"--- AI System Online (Model: {MODEL_NAME}) ---")
    while True:
        user_msg = input("You: ")
        if user_msg.lower() in ["exit", "quit", "bye"]:
            print("AI: Goodbye!")
            break
        
        print(f"\nAI: {ask_ai(user_msg)}\n")