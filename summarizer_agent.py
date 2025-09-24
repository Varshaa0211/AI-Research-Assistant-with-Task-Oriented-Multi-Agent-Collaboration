from transformers import pipeline

class SummarizerAgent:
    def __init__(self):
        self.summarizer = pipeline("summarization")

    def summarize(self, text):
        if len(text) > 1000:  # truncate for safety
            text = text[:1000]
        summary = self.summarizer(text, max_length=200, min_length=50, do_sample=False)
        return summary[0]['summary_text']
