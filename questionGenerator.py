import openai
from dotenv import load_dotenv
import os
model = {3:"gpt-3.5-turbo", 4:"gpt-4-1106-preview"}
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_KEY"))
def generate_questions(user_prompt):
    messages =[{"role": "system","content": """Your response must be a list of dictionary key-value pairing related to the users input. The length of the list of dictionaries is determined by the user. The correct answer is the dictonary key's value.
    If no input is given, then default is 3 questions."""},
    {"role": "user","content": "ww1 2 questions"},
    {"role":"assistant", "content":"""[{":"Question": When did the second world war begin, "Options": ["1914", "1944", "1945", "1939"], "Answer": "1939"}, {"Question": ""Who was the leader of Nazi Germany?","Options": ["Jospeh Stalin", "Joseph Goebbels", "Heinrich Himmler", "Adolf Hitler"], "Answer": "Adolf Hitler"}]"""},
    {"role": "user","content": f"{user_prompt}"},]
    return client.chat.completions.create(
        model=model[3],
        messages = messages,
        n=1,
    ).choices[0].message.content

def main():
    user_input = input("Text: ")
    print(generate_questions(user_prompt = user_input))

if __name__ == "__main__":
    main()