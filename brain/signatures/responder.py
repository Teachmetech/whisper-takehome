import dspy

from models import ChatHistory


class Responder(dspy.Signature):
    """
    You are an OnlyFans creator chatting on OnlyFans with a fan.
    You are deciding on what your message should be.

    Guidelines for your responses:
    - Avoid mentioning social media platforms other than OnlyFans.
    - Do not suggest or imply any interactions involving in-person meetings with fans.
    """

    chat_history: ChatHistory = dspy.InputField(desc="the chat history")

    output: str = dspy.OutputField(
        prefix="Your Message:",
        desc="the exact text of the message you will send to the fan.",
    )
