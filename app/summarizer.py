from app.conversation import ConversationHistory
from app.prompts import SUMMARY_PROMPT
from app.api_client import chat

class Summary:
    def __init__(self):
        self.summary=""

    def message_to_summarize(self,messages):
        message_summarizer=[]
        for messages in messages:
            role=messages.get("role")
            content=messages.get("content","").strip()

            if not content:
                continue

            if role=="system":
                continue
            elif role=="user":
                message_summarizer.append(f"user:{content}")
            elif role=="assistant":
                message_summarizer.append(f"Assistant:{content}")
        
        return message_summarizer
     
    def create_summary(self,messages):
        messages_to=self.message_to_summarize(messages)
        if not messages_to:
            self.summary = "No meaningful conversation to summarize."
            return self.summary

        summary_messages = [
            {"role": "system", "content": SUMMARY_PROMPT},
            {"role": "user", "content": messages_to}
        ]

        response = chat(summary_messages)
        self.summary = response.strip()
        return self.summary


   
       
