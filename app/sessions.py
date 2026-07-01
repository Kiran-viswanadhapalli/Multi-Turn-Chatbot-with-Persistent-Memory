from app.conversation import ConversationHistory
from datetime import datetime
import uuid

class ChatSession:
    def __init__(self):
        self.session_id=str(uuid.uuid4())
        self.created_time=datetime.now()
        self.end_time=None
        self.active=True
        self.conversation=ConversationHistory()
        self.summary=""
        self.memory={}

    def end_session(self):
        self.active=False
        self.end_time=datetime.now()
        
class SessionManager:
    def __init__(self):
        self.current_session=None

    def start_new_session(self):
        self.current_session=ChatSession()
        return self.current_session

    def get_current_session(self):
        return self.current_session
    
    def set_current_session(self, session):
        self.current_session = session
    
    def end_current_session(self):
        # check for current active sessions if active end it
        if(self.current_session is not None):
            self.current_session.end_session()

    



        