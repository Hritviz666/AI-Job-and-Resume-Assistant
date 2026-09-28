import re

from langchain_core.documents import Document


def clean_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def clean_documents(
    documents: list[Document],
) -> list[Document]:
    cleaned = []

    for document in documents:
        text = clean_text(document.page_content)

        if text:
            cleaned.append(
                Document(
                    page_content=text,
                    metadata=document.metadata,
                )
            )

    return cleaned