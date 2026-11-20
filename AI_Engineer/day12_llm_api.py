
import os
from dotenv import load_dotenv
from google import genai

# STEP 1: Load environment variables
load_dotenv()

# STEP 2: Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: Gemini API key not found.")
    print("Please check your .env file.")
    raise SystemExit(1)

# STEP 3: Connect to Gemini
client = genai.Client(api_key=api_key)

MODEL = "gemini-3.5-flash-lite"


# STEP 4: Create function to call Gemini
def get_ai_response(prompt):

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text or "No text response received."


# STEP 5: Create three prompt styles
def compare_prompts(question):

    prompts = {
        "SIMPLE PROMPT": f"""
        Answer the following question in simple English.
        Keep your answer short and clear.

        Question: {question}
        """,

        "DETAILED PROMPT": f"""
        Explain the following question in detail.

        Instructions:
        1. Explain step by step.
        2. Use simple English.
        3. Give at least three real-world examples.
        4. Include a short conclusion.

        Question: {question}
        """,

        "ROLE-BASED PROMPT": f"""
        Act as an experienced AI teacher.

        Your student is a complete beginner.
        Explain the following question in a friendly
        teaching style.

        Use practical examples and avoid complicated
        technical words.

        Question: {question}
        """
    }

    # STEP 6: Send all three prompts to Gemini
    for style, prompt in prompts.items():

        print("\n" + "=" * 60)
        print(style)
        print("=" * 60)

        try:
            answer = get_ai_response(prompt)
            print(answer)

        except Exception as error:
            print("API Error:", error)


# STEP 7: Main program
def main():

    print("=" * 60)
    print("       AI PROMPT COMPARISON APPLICATION")
    print("=" * 60)

    question = input("\nEnter your question: ").strip()

    if not question:
        print("Please enter a valid question.")
        return

    compare_prompts(question)

    print("\n" + "=" * 60)
    print("PROMPT COMPARISON COMPLETED")
    print("=" * 60)


# STEP 8: Run the application
if __name__ == "__main__":
    main()
