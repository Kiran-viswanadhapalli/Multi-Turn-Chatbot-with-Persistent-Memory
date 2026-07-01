from app.api_client import chat
from app.sessions import SessionManager
from app.storage import Storage
from app.summarizer import Summary
import re

def main():
    session_manager=SessionManager()
    storage=Storage()
    summary=Summary()
    current_session=None

    '''if not sessions:
        print("No sessions found")
    else:
        for index, session_file in enumerate(sessions,1):
            print(f"{index}.{session_file}")'''
    
    

    while current_session is None:
        print("\n1.start new session")
        print("2.List saved sessions")
        print("3.Load previous session")
        print("4.Delete a session")
        print("5.Exit")

        user_choice=input("choose an option: ").strip()

        if(user_choice=="1"):
            session_manager.start_new_session()
            current_session=session_manager.get_current_session()

        elif(user_choice=="2"):
            sessions=storage.list_sessions()
            if not sessions:
                print("No sessions found")
            else:
                for index,session_file in enumerate(sessions,1):
                    print(f"{index}.{session_file}")

        elif(user_choice=="3"):
            sessions=storage.list_sessions()
            if not sessions:
                print("No sessions found")
            else:
                for index,session_file in enumerate(sessions,1):
                    print(f"{index}.{session_file}")
                
                session_id=input("Enter session_id to load(without.json): ").strip()
                load_session=storage.load_previous_session(session_id)

                if load_session is None:
                    print("session not found")
                else:
                    current_session=load_session
                    session_manager.set_current_session(current_session)

                    current_session.active = True
                    current_session.end_time = None

                    print("session loaded successfully..")

        elif(user_choice=="4"):
            sessions=storage.list_sessions()
            if not sessions:
                print("no sessions found to delete")
            else:
                for index, session_file in enumerate(sessions,1):
                    print(f"{index}.{session_file}")

                session_id=input("Enter session_id to delete without.json: ").strip()

                if storage.delete_session(session_id):
                    print(f"session {session_id} has been deleted sucessfully")
                else:
                    print("session not found")
                
        elif user_choice=="5":
            print("Exiting....")
            return
        else:
            print("Invalid choice. try again")
            #terminate the chat
    
        while True:
            user_message = input("you: ").strip()

            if user_message.lower() in ["exit", "quit"]:
                print("Chat session has been ended")

                messages=current_session.conversation.messages

                session_summary = summary.create_summary(messages)
                current_session.summary = session_summary

                session_manager.end_current_session()
                storage.save_session(current_session)

                break


            if not user_message:
                print("Please type something.")
                continue

            name_match = re.search(r"\bmy name is ([A-Za-z ]+)", user_message, re.IGNORECASE)

            if name_match:
                current_session.memory["name"] = name_match.group(1).strip()

            messages = current_session.conversation.get_messages_for_api(
            user_message=user_message,
            limit=10,
            summary=current_session.summary,
            memory=current_session.memory
            )

            response = chat(messages)

            current_session.conversation.add_user_message(user_message)
            current_session.conversation.add_assistant_message(response)

            print(f"Bot: {response}")

        
        
    
