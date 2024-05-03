# Pdfs-chat
---
A simple application for chatting with your document, locally and using OpenAI API

## Dependencies and Installation
---

1. First clone the repository
    ```
    git clone https://github.com/PaoloBonicco7/pdfs-chat.git
    ```

2. Create the virtual environment
    ```
    python -m venv tutorial-env
    ```

3. And Install the requirements
    ```
    pip install -r requirements.txt
    ```

4. (Optional) Add your OpenAI API key in the `.env` file
    ```
    OPENAI_API_KEY=your_api_key
    ```

## Usage
-----
To use the Chat App, follow these steps:

1. Ensure that you have installed the required dependencies and added the OpenAI API key to the `.env` file, if you 
don't want to run it locally.

2. Run the `main.py` file using the Streamlit CLI. Execute the following command:
   ```
   streamlit run app.py
   ```

3. The application will launch in your default web browser, displaying the user interface.

4. Load multiple PDF documents into the app by following the provided instructions.

5. Ask questions in natural language about the loaded PDFs using the chat interface.
