from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
)


def load_document(file_path: str):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    loaders = {
        ".pdf": PyPDFLoader,
        ".docx": Docx2txtLoader,
        ".txt": TextLoader,
    }

    loader_class = loaders.get(path.suffix.lower())

    if loader_class is None:
        raise ValueError(
            f"Unsupported file type: {path.suffix}"
        )

    loader = loader_class(str(path))
    return loader.load()