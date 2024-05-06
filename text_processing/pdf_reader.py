from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List


def pdf2text(pdfs_path: [str]) -> str:
    """
    Extract text from pdf files

    :type pdfs_path: str
    :param pdfs_path: list of pdf files path
    :return: text extracted from the pdf files
    """
    text = ""
    for pdf in pdfs_path:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text()
    return text


def splitter(text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> List[str]:
    """
    Split text into chunks

    :param text: text to split
    :param chunk_overlap: length of overlap between chunks
    :param chunk_size: size of each chunk
    :return: list of text chunks
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )

    splits = text_splitter.split_text(text)
    return splits
