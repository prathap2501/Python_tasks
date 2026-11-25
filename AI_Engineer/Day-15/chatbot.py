
from google import genai
from dotenv import load_dotenv
import json
import os

# ==========================================
# STEP 1: LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. Please check your .env file."
    )

# Create Gemini AI client
client = genai.Client(api_key=api_key)


# ==========================================
# STEP 2: SYSTEM PERSONA
# ==========================================

system_prompt = """
You are AutoExpert.

You are a friendly AI assistant.
You explain automobile topics in simple English.
You give clear answers with examples.
You answer questions about cars, bikes, engines,
electric vehicles, automobile technology and maintenance.
"""


# ==========================================
# STEP 3: CONVERSATION HISTORY
# ==========================================

messages = [
    {
        "role": "system",
        "content": system_prompt
    }
]


# ==========================================
# STEP 4: LOAD PREVIOUS CONVERSATION
# ==========================================

def load_history():

    global messages

    if os.path.exists("chat_history.json"):

        try:

            with open("chat_history.json", "r") as file:
                saved_messages = json.load(file)

            if isinstance(saved_messages, list):

                messages = [messages[0]] + [
                    item for item in saved_messages
                    if isinstance(item, dict)
                    and item.get("role") in ["user", "assistant"]
                    and isinstance(item.get("content"), str)
                ]

            print("Previous conversation loaded!")

        except (json.JSONDecodeError, OSError):

            print("Could not load previous history.")


# ==========================================
# STEP 5: SAVE CONVERSATION
# ==========================================

def save_history():

    try:

        with open("chat_history.json", "w") as file:

            json.dump(
                messages[1:],
                file,
                indent=4
            )

        print("Conversation saved successfully!")

    except OSError as e:

        print("File saving error:", e)


# ==========================================
# STEP 6: CONVERT HISTORY TO GEMINI FORMAT
# ==========================================

def convert_history():

    conversation = []

    for message in messages[1:]:

        role = (
            "user"
            if message["role"] == "user"
            else "model"
        )

        conversation.append({

            "role": role,

            "parts": [
                {
                    "text": message["content"]
                }
            ]

        })

    return conversation


# ==========================================
# STEP 7: CHATBOT FUNCTION
# ==========================================

def chat():

    print("\n================================")
    print("       AUTOEXPERT AI CHATBOT")
    print("================================")

    load_history()

    print("\nWelcome to AutoExpert!")
    print("Ask me anything about automobiles.")

    print("\nCommands:")
    print("Type 'save' to save conversation.")
    print("Type 'exit' to stop the chatbot.")
    print("Type 'clear' to clear conversation history.")

    while True:

        user_input = input("\nYou: ").strip()

        # Check empty input
        if not user_input:

            print("Please enter a message.")
            continue

        # Exit chatbot
        if user_input.lower() == "exit":

            save_history()

            print("AI: Goodbye! Have a great day!")

            break

        # Save conversation
        if user_input.lower() == "save":

            save_history()

            continue

        # Clear conversation history
        if user_input.lower() == "clear":

            messages.clear()

            messages.append({
                "role": "system",
                "content": system_prompt
            })

            save_history()

            print("Conversation history cleared!")

            continue

        # Add user message
        messages.append({

            "role": "user",
            "content": user_input

        })

        try:

            # Convert messages to Gemini format
            conversation = convert_history()

            # Send conversation to Gemini AI
            response = client.models.generate_content(

                model="gemini-3.8-flash",

                contents=conversation,

                config={
                    "system_instruction": system_prompt
                }

            )

            # Get AI response
            answer = response.text

            if not answer:
                raise ValueError("Gemini returned an empty response.")

            # Display AI response
            print("\nAI:", answer)

            # Store AI response
            messages.append({

                "role": "assistant",
                "content": answer

            })

        except Exception as e:

            # Remove unanswered user message
            messages.pop()

            print("\nAPI Error:", e)


# ==========================================
# STEP 8: RUN CHATBOT
# ==========================================

if __name__ == "__main__":

    chat()
