import fitz

def extract_text(file_path: str) -> str:
    document = fitz.open(file_path)
    text = ''
    for page in document:
        page.get_text()
        text += page.get_text() + '\n'
    document.close()
    return text

