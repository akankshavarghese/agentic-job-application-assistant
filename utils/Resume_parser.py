from pypdf import PdfReader


def extract_resume_text(pdf_path):
    """Extract text from a resume PDF."""
    
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


if __name__ == "__main__":
    resume_path = "data/resume.pdf"

    resume_text = extract_resume_text(resume_path)

    print(resume_text)
