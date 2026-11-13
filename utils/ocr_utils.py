import pytesseract
from PIL import Image

# Configure Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_text_tesseract(image, language="eng"):
    """
    Extract text from an image using Tesseract OCR.
    Supports English, Telugu,Hindi,Kannada And also other languages if language data is installed.
    """
    try:
        text = pytesseract.image_to_string(
            image,
            lang=language
        )
        return text.strip()

    except Exception as e:
        print(f"[OCR Error] {e}")
        return ""