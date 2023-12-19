# OCRBro

OCRBro is a Python script for extracting text from images using the Tesseract OCR library.

## Dependencies

Make sure you have the following libraries installed before running the script:

```bash
pip install pytesseract Pillow

Also, you need to install Tesseract OCR and specify the path to the executable in the code:

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

Usage

Simply specify the path to the image in the image_path variable in the code and run the script:

python your_script_name.py

Example

# Example usage
image_path = 'path/to/your/image.jpg'
print(extract_text(image_path))

Note

Adjust the image path (image_path) according to your actual paths. Be careful with escaping backslashes in the file path

License
This project is distributed under the MIT License.
