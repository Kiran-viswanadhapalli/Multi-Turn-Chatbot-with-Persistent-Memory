# 🤖 CLI Multi-Turn Chatbot with Persistent Memory

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![CLI](https://img.shields.io/badge/Interface-Command%20Line-green?style=for-the-badge)
![Memory](https://img.shields.io/badge/Memory-Persistent-purple?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

**A Python CLI chatbot that supports multi-turn conversations, persistent memory, session storage, and conversation summarization.**

</div>

---

## 📌 Project Overview

This project is a **command-line based AI chatbot** built using Python. It is designed to support **multi-turn conversations**, meaning the chatbot can remember previous messages during a conversation and respond with context.

The main highlight of this project is **persistent memory**. Conversations can be saved locally and loaded again later, allowing users to continue previous sessions instead of starting from zero every time.

This project demonstrates how a chatbot can manage:

| Feature                  | Description                               |
| ------------------------ | ----------------------------------------- |
| 💬 Multi-turn chat       | Maintains context during the conversation |
| 🧠 Persistent memory     | Saves conversation history locally        |
| 📁 Session management    | Organizes conversations into sessions     |
| 📝 Summarization         | Summarizes long conversations             |
| 🔐 Environment variables | Keeps API keys private                    |
| 🧩 Modular structure     | Cleanly separates project logic           |

---

## ✨ Key Features

### 💬 Command-Line Chat Interface

The chatbot runs directly in the terminal. Users can type messages and receive chatbot responses through a simple CLI interface.

### 🧠 Persistent Memory

The chatbot stores conversation history locally so that previous sessions can be continued later.

### 🔁 Multi-Turn Conversation Support

The chatbot keeps track of previous messages, allowing it to understand follow-up questions.

### 📂 Session-Based Storage

Each conversation can be stored as a session, making it easier to manage multiple chats.

### 📝 Conversation Summarization

Long conversations can be summarized to keep context smaller and more efficient.

### 🔐 Secure Configuration

API keys and private configuration values are stored in a `.env` file and excluded from GitHub using `.gitignore`.

### 🧩 Modular Python Codebase

The project is divided into separate files for API handling, conversation logic, prompts, storage, sessions, and summarization.

---

## 🏗️ Project Architecture

```text
┌──────────────────────┐
│      User Input      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│     CLI Interface    │
│      app/main.py     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Conversation Manager │
│ app/conversation.py  │
└──────────┬───────────┘
           │
           ├───────────────┐
           ▼               ▼
┌──────────────────┐  ┌──────────────────┐
│ Prompt Handling  │  │ Session Manager  │
│ app/prompts.py   │  │ app/sessions.py  │
└──────────┬───────┘  └──────────┬───────┘
           │                     │
           ▼                     ▼
┌──────────────────┐  ┌──────────────────┐
│    API Client    │  │ Local Storage    │
│ app/api_client.py│  │ app/storage.py   │
└──────────┬───────┘  └──────────┬───────┘
           │                     │
           ▼                     ▼
┌──────────────────┐  ┌──────────────────┐
│ Language Model   │  │ data/sessions/   │
│      API         │  │ Saved Memory     │
└──────────────────┘  └──────────────────┘
```

---

## 🔄 How the Chatbot Works

```text
1. User starts the chatbot using python run.py
2. The application loads configuration and session data
3. User enters a message in the terminal
4. The conversation manager updates the message history
5. Prompt instructions are added to guide the chatbot
6. The API client sends the request to the language model
7. The chatbot response is returned
8. The response is displayed in the terminal
9. Conversation history is saved locally
10. The session can be continued later
```

---

## 📁 Project Structure

```text
multi-turn-persistent-chatbot/
│
├── app/
│   ├── __init__.py
│   ├── api_client.py
│   ├── conversation.py
│   ├── main.py
│   ├── prompts.py
│   ├── sessions.py
│   ├── storage.py
│   └── summarizer.py
│
├── data/
│   └── sessions/
│       └── .gitkeep
│
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

---

## 🧾 File Explanation

| File / Folder            | Purpose                                                       |
| ------------------------ | ------------------------------------------------------------- |
| `run.py`                 | Main entry point used to start the chatbot                    |
| `app/__init__.py`        | Marks the `app` folder as a Python package                    |
| `app/main.py`            | Controls the CLI flow and user interaction                    |
| `app/api_client.py`      | Handles communication with the language model API             |
| `app/conversation.py`    | Manages message history and multi-turn conversation logic     |
| `app/prompts.py`         | Stores system prompts and chatbot instructions                |
| `app/sessions.py`        | Creates, loads, and manages chat sessions                     |
| `app/storage.py`         | Saves and loads conversation data from local storage          |
| `app/summarizer.py`      | Summarizes long conversations to keep context efficient       |
| `data/sessions/`         | Stores saved chat session files                               |
| `data/sessions/.gitkeep` | Keeps the sessions folder available in Git                    |
| `.env.example`           | Shows required environment variables without exposing secrets |
| `.gitignore`             | Prevents private or unnecessary files from being pushed       |
| `requirements.txt`       | Lists required Python dependencies                            |
| `README.md`              | Project documentation                                         |

---

## 🧠 Memory Workflow

```text
┌───────────────┐
│ User Message  │
└───────┬───────┘
        ▼
┌──────────────────────┐
│ Update Conversation  │
│      History         │
└───────┬──────────────┘
        ▼
┌──────────────────────┐
│ Generate Bot Reply   │
└───────┬──────────────┘
        ▼
┌──────────────────────┐
│ Save Session Locally │
└───────┬──────────────┘
        ▼
┌──────────────────────┐
│ Continue Later Using │
│ Persistent Memory    │
└──────────────────────┘
```

---

## 🛠️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

### 2. Navigate to the Project Folder

```bash
cd YOUR_REPO_NAME
```

### 3. Create a Virtual Environment

For Windows:

```bash
python -m venv venv
```

For macOS/Linux:

```bash
python3 -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root folder.

You can copy the example file:

```bash
cp .env.example .env
```

Then add your actual API key inside `.env`.

Example:

```env
API_KEY=your_api_key_here
```

> ⚠️ Never upload your real `.env` file to GitHub.

---

## ▶️ How to Run

Start the chatbot with:

```bash
python run.py
```

Or:

```bash
python3 run.py
```

---

## 💻 Example Conversation

```text
╔════════════════════════════════════╗
║     CLI Persistent Chatbot         ║
╚════════════════════════════════════╝

User: Hello
Bot: Hello! How can I help you today?

User: My name is Kiran.
Bot: Nice to meet you, Kiran.

User: What is my name?
Bot: Your name is Kiran.

User: What project am I working on?
Bot: You are working on a CLI-based multi-turn chatbot with persistent memory.

User: exit
Bot: Conversation saved. Goodbye!
```

---

## ⚙️ Functionalities Implemented

| Functionality           | Status | Description                                     |
| ----------------------- | -----: | ----------------------------------------------- |
| CLI chatbot interface   |      ✅ | Allows chatting through the terminal            |
| Multi-turn conversation |      ✅ | Maintains context during a session              |
| Persistent memory       |      ✅ | Saves conversations locally                     |
| Session management      |      ✅ | Supports saved chat sessions                    |
| Local storage           |      ✅ | Stores data inside `data/sessions/`             |
| Prompt management       |      ✅ | Uses separate prompt templates                  |
| API client module       |      ✅ | Handles model API communication                 |
| Summarization support   |      ✅ | Summarizes long conversations                   |
| Environment config      |      ✅ | Uses `.env` for private keys                    |
| GitHub-ready structure  |      ✅ | Includes `.gitignore`, README, and requirements |

---

## 🧩 Module Responsibilities

### `main.py`

Handles the overall chatbot loop.

```text
Start app → Read user input → Send message → Show response → Save session
```

### `conversation.py`

Maintains the conversation history.

```text
User message + previous context → prepared message list → chatbot response
```

### `api_client.py`

Connects the app to the language model API.

```text
Prepared conversation → API request → AI-generated response
```

### `storage.py`

Handles saving and loading data.

```text
Conversation history → local file → reusable memory
```

### `sessions.py`

Manages different chat sessions.

```text
Create session → load session → update session → save session
```

### `summarizer.py`

Compresses long conversations.

```text
Long chat history → summarized memory → smaller context
```

---

## 🔒 Security Notes

* Keep your real `.env` file private.
* Do not commit API keys.
* Do not upload private chat session files if they contain personal data.
* Use `.env.example` to show required variables safely.
* Keep virtual environment folders out of GitHub.

---

## 📚 What I Learned

Through this project, I learned how to:

* Build a Python CLI chatbot
* Manage multi-turn conversation history
* Save and load persistent memory
* Work with local file storage
* Use environment variables safely
* Organize a project into clean modules
* Prepare and push a project to GitHub
* Write professional project documentation

---

## 🚀 Future Improvements

* Add a web interface using Flask, FastAPI, or Streamlit
* Add database support with SQLite or PostgreSQL
* Add semantic memory search
* Add user authentication
* Add commands to list, rename, or delete sessions
* Add chat export as `.txt`, `.json`, or `.pdf`
* Add unit tests
* Add Docker support
* Add better error handling
* Add support for multiple users

---

## 👨‍💻 Author

**YOUR NAME**

GitHub: [Kiran-viswanadhapalli](https://github.com/Kiran-viswanadhapalli)

---

## 📌 Repository

```text
https://github.com/Kiran-viswanadhapalli/Multi-Turn_Presistent_Chatbot
```

---

## 📄 License

This project is Licensed under the MIT License.


<div align="center">

### ⭐ If you like this project, consider giving it a star on GitHub!

**Built with Python, persistence, and clean chatbot architecture.**

</div>
