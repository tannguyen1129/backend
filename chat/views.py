from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
import requests
import os
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

# API URL và Token của Hugging Face
API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
API_TOKEN = os.getenv('HUGGINGFACE_API_KEY')

def query_huggingface(payload):
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        print(f"Error from Hugging Face API: {response.json()}")
        return {"error": "API Hugging Face không khả dụng."}
    return response.json()

@api_view(['POST'])
def ask_question(request):
    try:
        question = request.data.get('question')
        if not question:
            return Response({"error": "Câu hỏi không được để trống."}, status=400)

        # Kiểm tra trong database
        faq = FAQ.objects.filter(question__icontains=question).first()
        if faq:
            serializer = FAQSerializer(faq)
            return Response(serializer.data)

        # Gửi request đến Hugging Face API
        payload = {"inputs": {"question": question, "context": ""}}
        result = query_huggingface(payload)
        answer = result.get('answer', None)
        if not answer:
            answer = "Không tìm thấy câu trả lời phù hợp."

        # Lưu vào database
        new_faq = FAQ.objects.create(question=question, answer=answer)
        serializer = FAQSerializer(new_faq)

        return Response(serializer.data)
    except Exception as e:
        print("Error:", str(e))
        return Response({"error": "Internal Server Error."}, status=500)
