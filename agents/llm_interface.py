import os

from flask import current_app
from openai import OpenAI
from werkzeug.exceptions import ServiceUnavailable


class LLMInterface:
    def __init__(self, api_key=None, model="gpt-4"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model
        self.client = OpenAI(api_key=self.api_key)

    def generate_text(self, messages):
        try:
            if not isinstance(messages, list) or not all(isinstance(message, dict) for message in messages):
                raise ValueError("The 'messages' parameter must be an array of objects.")
            
            batch_size = 5
            responses = []
            for i in range(0, len(messages), batch_size):
                batch = messages[i:i+batch_size]
                response = self.client.chat.completions.create(model=self.model, messages=batch)
                for choice in response.choices:
                    responses.append(choice.message.content.strip())
            return responses
        except Exception as e:
            current_app.logger.error(f"Error generating text: {e}", exc_info=True)
            raise ServiceUnavailable("Unable to generate text at this time. Please try again later.")