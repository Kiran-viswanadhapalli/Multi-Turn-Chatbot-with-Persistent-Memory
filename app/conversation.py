from app.prompts import MEMORY_CONTEXT_PROMPT,SYSTEM_PROMPT
class ConversationHistory:
    
    def __init__(self):
        self.system_message = {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
        self.messages = []
    
    def add_user_message(self, text):
        self.messages.append({"role": "user", "content": text})
    
    def add_assistant_message(self, text):
        self.messages.append({"role": "assistant", "content": text})

    def get_messages(self):
        return [self.system_message] + self.messages
        
    def get_previous_messages(self, n):
        if n <= 0:
            return []
        if(n%2!=0):
            n-=1
        if n >= len(self.messages):
            return self.messages
        return self.messages[-n:]
    
    def get_messages_for_api(self, user_message, limit=10, summary="", memory=None):
        messages = []

        if summary:
            messages.append({
                "role": "system",
                "content": f"Conversation summary: {summary}"
            })

        if memory:
            facts = []
            for key, value in memory.items():
                facts.append(f"{key}: {value}")

            messages.append({
                "role": "system",
                "content": "Known user facts:\n" + "\n".join(facts)
            })

        for message in self.messages[-limit:]:
            messages.append({
                "role": message["role"],
                "content": message["content"]
            })

        messages.append({
            "role": "user",
            "content": user_message
        })
        return messages


#conversation = ConversationHistory()
"""conversation.add_user_message("Hi")
conversation.add_assistant_message("i am good")
print(conversation.get_messages())
print(conversation.get_previous_messages(10))
print(conversation.get_messages_for_api("What are you doing?", 2))"""