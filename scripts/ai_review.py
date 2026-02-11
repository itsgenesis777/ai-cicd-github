from google import genai
import sys

client = genai.Client()

# Define a function that takes a code diff as input
def review_code(diff_text):

    # Write a multi-line f-string prompt that includes {diff_text}
    # Tell Gemini to act as a code reviewer and focus on security, bugs, performance
    prompt = f"""
    You are a senior code reviewer.

    Review the following code diff and focus on:
    - Security vulnerabilities
    - Bugs or logical errors
    - Performance issues
    - Code quality and best practices

    Provide clear and concise feedback.

    Code diff:
    {diff_text}
    """

    # Send the prompt to the model and get a response
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=prompt
    )

    # Return just the text from the response
    return response.text

    # Only run this code when the script is executed directlyif __name__ == "__main__":
if __name__ == "__main__":
    if len(sys.argv) > 1:
        diff_file = sys.argv[1]
        with open(diff_file, "r") as f:
            diff_content = f.read()
    else:
        diff_content = sys.stdin.read()

    review = review_code(diff_content)
    print(review)
