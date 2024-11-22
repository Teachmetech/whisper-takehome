from pydantic import BaseModel
from typing import List
from datetime import datetime


class ChatMessage(BaseModel):
    from_creator: bool
    content: str
    time_stamp: datetime = datetime.now()

    def __str__(self):
        role = "YOU" if self.from_creator else "THE FAN"
        message = f"{role} : {self.content} sent at: {self.time_stamp.strftime("%Y-%m-%d %H:%M:%S")}"
        return message


class ChatHistory(BaseModel):
    messages: List[ChatMessage] = []
    created_at: datetime = datetime.now()

    def __str__(self):
        messages = []
        for _, message in enumerate(self.messages):
            message_str = str(message)
            messages.append(message_str)
        return f"started_at: {self.created_at.strftime("%Y-%m-%d %H:%M:%S")}\n {"\n".join(messages)}"

    def model_dump_json(self, **kwargs):
        return str(self)
