
from google import genai
import json
import os

# Get Gemini API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not configured.")

# Create Gemini client
client = genai.Client(api_key=api_key)


# Movie recommendation function
def recommend_movies(genre, mood):

    prompt = f"""
    You are a movie recommendation assistant.

    Recommend exactly 3 movies.

    Genre: {genre}
    Mood: {mood}

    Return valid JSON in this format:
    {{
        "movies": [
            {{
                "name": "Movie name",
                "genre": "Movie genre",
                "reason": "Why this movie matches the mood"
            }}
        ]
    }}

    Return exactly 3 movies.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    result = response.text

    if not result:
        raise ValueError("Gemini returned an empty response.")

    return json.loads(result)


# Main program
try:
    # Get user input
    genre = input("Enter movie genre: ")
    mood = input("Enter your mood: ")

    # Get recommendations
    movies = recommend_movies(genre, mood)

    # Display results
    print("\nMovie Recommendations:")

    for movie in movies["movies"]:
        print("\nMovie:", movie["name"])
        print("Genre:", movie["genre"])
        print("Reason:", movie["reason"])

except json.JSONDecodeError:
    print("Error: Gemini returned invalid JSON.")

except Exception as e:
    print("Error:", e)
