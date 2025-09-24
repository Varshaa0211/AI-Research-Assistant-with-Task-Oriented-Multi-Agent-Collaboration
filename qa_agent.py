from langchain.llms import OpenAI

class QAAgent:
    def __init__(self, api_key):
        self.llm = OpenAI(openai_api_key=api_key)

    def answer(self, question, context):
        prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
        return self.llm(prompt)
