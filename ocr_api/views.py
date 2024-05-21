import easyocr
import re
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

reader = easyocr.Reader(['en'])

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

class OCRView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file', None)
        if not file_obj:
            return JsonResponse({'error': 'File is missing.'}, status=status.HTTP_400_BAD_REQUEST)


        results = reader.readtext(file_obj.read())
        extracted_texts = [result[1] for result in results]
        #number_after_keyword1 = find_number_after_keyword(extracted_texts, 'VOLTS')
        #number_after_keyword2 = find_number_after_keyword(extracted_texts, 'PH')
        #number_after_keyword3 = find_number_after_keyword(extracted_texts, 'AMPS')

        return JsonResponse({
            'number_after_keyword': extracted_texts
        }, status=status.HTTP_200_OK)
