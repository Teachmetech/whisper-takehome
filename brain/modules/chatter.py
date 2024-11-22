import dspy
from typing import Optional
from dspy.teleprompt import KNNFewShot
from models import ChatHistory
from brain.modules.responder import ResponderModule
from utils.data_loader import ConversationLoader


class ChatterModule(dspy.Module):
    def __init__(self, examples: Optional[dict]):
        super().__init__()
        self.examples = examples
        self.responder = ResponderModule()
        self.optimize_from_examples()

    def forward(
        self,
        chat_history: ChatHistory,
    ):
        return self.responder(chat_history=chat_history)

    def optimize_from_examples(self):
        if self.examples:
            training_data, testing_data = ConversationLoader(
                self.examples
            ).get_training_data()
            self.responder = KNNFewShot(7, training_data).compile(
                student=self.responder, trainset=training_data, valset=testing_data
            )
