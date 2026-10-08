from loaders.file_loader import load_document
from processing.document_cleaner import clean_documents
from chains.job_chain import analyze_job


def process_job(file_path: str):
    documents = load_document(file_path)
    documents = clean_documents(documents)

    text = "\n\n".join(
        document.page_content
        for document in documents
    )

    return analyze_job(text)