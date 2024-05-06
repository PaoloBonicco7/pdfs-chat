from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from typing import List

vectorstore = Chroma.from_documents(documents=splits,
                                    embedding=OpenAIEmbeddings())

retriever = vectorstore.as_retriever()


def get_vectorstore(text_chunks: List[str], embedder: str) -> Chroma:
    """
    Create a vector store from text chunks

    :param text_chunks: list of text chunks
    :param embedder: the embedding model to use, either "openai" or "ollama"
    :return: vector store
    """
    if embedder == "openai":
        embeddings = OpenAIEmbeddings()
    elif embedder == "ollama":
        embeddings = OllamaEmbeddings(model="nomic-embed-text")
    else:
        raise ValueError("Invalid embedder")

    vectorstore = Chroma.from_texts(texts=text_chunks, collection_name="pdf_collection", embedding=embeddings)
    return vectorstore


# More info on how to setup retriever :
# https://api.python.langchain.com/en/latest/vectorstores/langchain_chroma.vectorstores.Chroma.html#langchain_chroma.vectorstores.Chroma.as_retriever
def get_retriever(vectorstore: Chroma, n_chunks: int = 4) -> Chroma:
    """
    Create a retriever from a vector store

    :param vectorstore:
    :param n_chunks: number of relevant chunk you want to returb
    :return: the retriver Object
    """
    retriever = vectorstore.as_retriever(search_kwargs={"k": n_chunks})

    return retriever
