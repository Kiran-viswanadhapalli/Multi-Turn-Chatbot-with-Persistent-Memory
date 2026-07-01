import os
import json
from app.sessions import ChatSession
from datetime import datetime

class Storage:
    def __init__(self):
        self.session_dir="data/sessions"
        os.makedirs(self.session_dir,exist_ok=True)

    def load_previous_session(self,session_id):
        file_path=os.path.join(self.session_dir,f"{session_id}.json")

        if not os.path.exists(file_path):
            return None
        
        with open(file_path,"r",encoding="utf-8") as file:
            session_data=json.load(file)
        
        loaded_session=ChatSession()
        loaded_session.session_id=session_data["session_id"]
        loaded_session.created_time = datetime.fromisoformat(session_data["created_time"])
        loaded_session.end_time = (
            datetime.fromisoformat(session_data["end_time"])
            if session_data["end_time"] else None
        )
        loaded_session.active = session_data["active"]
        loaded_session.conversation.system_message = session_data["system_message"]
        loaded_session.conversation.messages = session_data["messages"]


        return loaded_session


    def update_session(self,session):
        return self.save_session(session)

    def delete_session(self,session_id):
        file_path=os.path.join(self.session_dir,f"{session_id}.json")

        if(os.path.exists(file_path)):
            os.remove(file_path)
            return True
        return False


    def save_session(self,session):
        session_data={
            "session_id":str(session.session_id),
            "created_time":session.created_time.isoformat(),
            "end_time":session.end_time.isoformat() if session.end_time else None,
            "active":session.active,
            "system_message":session.conversation.system_message,
            "messages":session.conversation.messages,
        }
        file_path=os.path.join(self.session_dir,f"{session.session_id}.json")

        with open(file_path,"w",encoding="utf-8") as file:
            json.dump(session_data,file,indent=4)

        return file_path
    
    def list_sessions(self):
        session_files=[]

        for file_name in os.listdir(self.session_dir):
            if file_name.endswith(".json"):
                session_files.append(file_name)
        
        return session_files

        


