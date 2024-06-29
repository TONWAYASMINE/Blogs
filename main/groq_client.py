
from groq import Groq

class GroqClient:
    def __init__(self):
        self.client = Groq(api_key="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")

    def send_message(self, message: str) -> str:
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content