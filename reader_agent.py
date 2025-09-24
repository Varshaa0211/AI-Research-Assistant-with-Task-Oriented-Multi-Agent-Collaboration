import pdfplumber

class ReaderAgent:
    def __init__(self):
        pass

    def read_pdf(self, file):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text
