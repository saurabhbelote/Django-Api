import easyocr
import re

reader = easyocr.Reader(['en'], gpu=False)  # Initialize EasyOCR reader

def extract_text(image):
    return reader.readtext(image)

def find_number_after_keyword(data_list, keyword):
    try:
        index = data_list.index(keyword)
        if index + 1 < len(data_list):
            next_element = data_list[index + 1]
            match = re.search(r'\d+', next_element)
            if match:
                return next_element
            else:
                return "No number found in the next element."
        else:
            return "No element follows the keyword."
    except ValueError:
        return "Keyword not found in the list."
