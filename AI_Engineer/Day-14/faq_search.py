
from google import genai
import numpy as np
import os
from dotenv import load_dotenv

# Step 1: Load environment variables from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Step 2: Connect to Gemini
client = genai.Client(api_key=api_key)

print("Gemini API connected successfully!")

# Step 3: Create FAQ database
faqs = [
    "How can I reset my password?",
    "How do I create a new account?",
    "How can I change my email address?",
    "How do I install Python?",
    "What is machine learning?",
    "How can I learn Python programming?",
    "How do I update my profile?",
    "What is artificial intelligence?",
    "How can I contact customer support?",
    "How do I delete my account?",
    "What is deep learning?",
    "How do I install VS Code?",
    "How can I change my password?",
    "What is an API?",
    "How do I learn SQL?",
    "What is a Python function?",
    "How can I recover my account?",
    "What is Generative AI?",
    "How do I upload code to GitHub?",
    "What is an embedding?"
]

# Step 4: Convert text into embeddings
def create_embeddings(texts):

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=texts
    )

    return np.array([
        item.values for item in response.embeddings
    ])

# Step 5: Generate FAQ embeddings
print("Creating FAQ embeddings...")

faq_embeddings = create_embeddings(faqs)

print("FAQ embeddings created successfully!")

# Step 6: Search FAQ function
def search_faq(question):

    question_embedding = create_embeddings([question])[0]

    # Calculate cosine similarity
    similarities = np.dot(
        faq_embeddings,
        question_embedding
    ) / (
        np.linalg.norm(faq_embeddings, axis=1)
        * np.linalg.norm(question_embedding)
    )

    # Get top 3 matching FAQs
    top_indices = np.argsort(similarities)[::-1][:3]

    print("\nTop 3 Similar FAQs:")

    for index in top_indices:
        print(
            f"{faqs[index]} | Similarity: "
            f"{similarities[index]:.3f}"
        )

# Step 7: Get user question
question = input("\nAsk your question: ")

# Step 8: Search FAQs
search_faq(question)
