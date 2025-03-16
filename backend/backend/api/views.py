from django.http import JsonResponse
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain_ollama import OllamaLLM

def generate_response(request):
    query = request.GET.get("query", "")
    urls = [
    "https://typescriptbook.jp/overview/why-you-should-use-typescript",
    "https://typescriptbook.jp/overview/features",
    "https://typescriptbook.jp/overview/before-typescript",
    ]

    loader = UnstructuredURLLoader(urls=urls)
    print(loader.load())

    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 300,
        chunk_overlap = 0,
        length_function = len,
    )
    model = OllamaLLM(model="hf.co/mmnga/sarashina2.2-3b-instruct-v0.1-gguf")
    index = VectorstoreIndexCreator(
    vectorstore_cls=model,
    embedding=HuggingFaceEmbeddings(),
    text_splitter=text_splitter,
    ).from_loaders([loader])
    response = index.query(query)
    return JsonResponse({"response": response})