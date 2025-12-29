import requests

RAG_SERVICE_URL = "https://just-a-noob-maternalai-rag.hf.space/chat"
TIMEOUT = 20  # seconds


def ask_rag_service(question: str):
    payload = {"question": question}

    response = requests.post(
        RAG_SERVICE_URL,
        json=payload,
        timeout=TIMEOUT
    )

    response.raise_for_status()  # raises error if 4xx / 5xx
    return response.json()
