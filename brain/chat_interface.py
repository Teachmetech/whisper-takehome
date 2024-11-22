import dspy
from lms.together import Together
from modules.chatter import ChatterModule
from models import ChatMessage, ChatHistory
from utils.data_loader import ConversationLoader

# Configure the language model
dspy.settings.configure(
    lm=Together(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        temperature=0.5,
        max_tokens=1000,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1.2,
        stop=["<|eot_id|>", "<|eom_id|>", "\n\n---\n\n", "\n\n---", "---", "\n---"],
    )
)

chat_history = ChatHistory()
chatter = ChatterModule(examples=ConversationLoader().conversations)

# Interactive chat loop
while (user_input := input("You: ")) != "exit":
    # Update chat history and generate response
    chat_history.messages.append(ChatMessage(from_creator=False, content=user_input))
    response = chatter(chat_history=chat_history).output
    chat_history.messages.append(ChatMessage(from_creator=True, content=response))

    # Display response
    print(f"\nResponse: {response}\n")
