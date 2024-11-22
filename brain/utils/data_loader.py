import dspy
from models import ChatHistory, ChatMessage
from dspy.datasets import DataLoader
import os
import json


class ConversationLoader:
    def __init__(self, conversations=None):
        self.conversations = (
            conversations if conversations else self.load_data_from_json()
        )

    def _load_conversation_examples(self):
        return [
            dspy.Example(
                chat_history=ChatHistory(
                    messages=[
                        ChatMessage(
                            from_creator=msg["from_creator"], content=msg["content"]
                        )
                        for msg in conversation["chat_history"]["messages"]
                    ]
                ),
                output=f"Your message: {conversation['output']}",
            ).with_inputs("chat_metadata", "chat_history", "sentiment")
            for conversation in self.conversations
        ]

    def get_training_data(self, train_size: float = 0.3):
        formatted_conversations = self._load_conversation_examples()
        data_loader = DataLoader().train_test_split(formatted_conversations, train_size)
        return data_loader["train"], data_loader["test"]

    def load_data_from_json(self):
        file_path = os.path.abspath("training_data/conversations.json")
        with open(file_path, "r") as file:
            return json.load(file)
