import openai
import os


class ChatBot:
    def __init__(self):
        openai.api_key = os.getenv("chatbot_gpt_gui")

    def get_response(self, user_input):
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].message.content
        return response


if __name__ == "__main__":
    chatbot = ChatBot()
    response = chatbot.get_response("Tell me a joke")
    print(response)
