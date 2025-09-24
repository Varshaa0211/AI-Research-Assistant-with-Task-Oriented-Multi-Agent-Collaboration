class CoordinatorAgent:
    def __init__(self, reader, summarizer, qa):
        self.reader = reader
        self.summarizer = summarizer
        self.qa = qa

    def handle_task(self, file, question):
        text = self.reader.read_pdf(file)
        summary = self.summarizer.summarize(text)
        answer = self.qa.answer(question, summary)
        return {"summary": summary, "answer": answer}
