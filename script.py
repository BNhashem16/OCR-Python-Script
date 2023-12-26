from PIL import Image
import pytesseract
import os
from dotenv import load_dotenv
from database import save_to_database

load_dotenv()

# Function to perform OCR on an image
def perform_ocr(image_path):
    try:
        # Perform OCR using Tesseract
        text = pytesseract.image_to_string(Image.open(image_path), lang='eng')
        return text.strip()
    except Exception as e:
        print(f"Error during OCR: {e}")
        return None

if __name__ == "__main__":
    image_path = os.getenv('IMAGE_PATH')

    # Perform OCR
    extracted_data = perform_ocr(image_path)

    if extracted_data:
        print("Extracted data:")
        print(extracted_data)

        # Save data to the database
        save_to_database(extracted_data)
        print("Data saved to the database.")
    else:
        print("No text extracted from the image.")
