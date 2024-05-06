




def get_conversation_chain(vectorstore):
    """
    Create a conversation chain

    :param vectorstore: vector store
    :return: conversation chain
    """
    # llm = ChatOpenAI()
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})
    llm = Ollama(model="phi3")

    # For storing messages and then extracts the messages in a variable
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)

    # This chain can be used to have conversations with a document.
    # It takes in a question and (optional) previous conversation history.
    # If there is previous conversation history, it uses an LLM to rewrite the conversation
    # into a query to send to a retriever (otherwise it just uses the newest user input).
    # It then fetches those documents and passes them (along with the conversation) to an LLM to respond.
    # TODO - This Method is deprecated
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )

    return conversation_chain

