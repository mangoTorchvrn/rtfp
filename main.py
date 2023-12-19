import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(image_path):
    print(f"Проверяемый путь: {image_path}")  # Для отладки

    # Проверка существования файла
    if not os.path.exists(image_path):
        return "Файл не найден"

    try:
        # Открыть изображение для чтения
        image = Image.open(image_path)
        # Использование Tesseract для распознавания текста
        text = pytesseract.image_to_string(image, lang='rus')
        return text
    except Exception as e:
        return f"Произошла ошибка: {e}"

# Пример использования
image_path = 'C:\\Users\\User\\PycharmProjects\\ocrbro\\diplom.jpg'  # Уточните имя пользователя и путь
print(extract_text(image_path))
  