import dspy
from models import ChatHistory, ChatMessage
from dspy.datasets import DataLoader


class conversation_loader:
    def __init__(self, conversations):
        self.conversations = conversations

    def load_conversation_examples(self):
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

    def get_training_data(self, train_size: float = 0.0):
        formatted_conversations = self.load_conversation_examples()
        data_loader = DataLoader().train_test_split(formatted_conversations, train_size)
        return data_loader["train"], data_loader["test"]
