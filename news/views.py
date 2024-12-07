import http.client
import json
import urllib.request
import urllib.parse
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import DisasterNews
from .serializers import DisasterNewsSerializer


class DisasterNewsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API ViewSet để lấy danh sách tin tức bão lũ từ cơ sở dữ liệu.
    """
    queryset = DisasterNews.objects.all().order_by('-published_at')
    serializer_class = DisasterNewsSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']  # Hỗ trợ tìm kiếm theo tiêu đề và nội dung

def fetch_disaster_news():
    """
    Hàm cập nhật tin tức thiên tai, thảm họa, dịch bệnh, và bão lũ liên quan đến Việt Nam.
    """
    base_url = "https://newsapi.org/v2/everything"
    params = {
        "q": "bão OR lũ lụt OR động đất OR sạt lở OR cháy rừng OR lốc xoáy OR ngập lụt OR covid OR dịch bệnh OR đại dịch OR bệnh truyền nhiễm OR bệnh cúm OR virus OR thảm họa OR thiên tai",
        "language": "vi",  # Chỉ lấy tin tiếng Việt
        "apiKey": "033b04a5cd6942218322118be24c6233"
    }
    
    # Mã hóa URL
    encoded_url = f"{base_url}?{urllib.parse.urlencode(params)}"
    print(f"Encoded URL: {encoded_url}")  # In ra URL để kiểm tra

    try:
        with urllib.request.urlopen(encoded_url) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                
                # Lọc các tin tức liên quan
                relevant_keywords = ["bão", "lũ lụt", "động đất", "sạt lở", "cháy rừng", "lốc xoáy", "ngập lụt",
                                     "covid", "dịch bệnh", "đại dịch", "bệnh truyền nhiễm", "bệnh cúm", "virus",
                                     "thảm họa", "thiên tai"]

                for article in data.get('articles', []):
                    title = article.get('title', '').lower()
                    description = article.get('description', '').lower()

                    # Lọc theo từ khóa
                    if any(keyword in title or keyword in description for keyword in relevant_keywords):
                        DisasterNews.objects.update_or_create(
                            title=article['title'],
                            defaults={
                                'description': description,
                                'url': article['url'],
                                'image_url': article.get('urlToImage'),
                                'published_at': article['publishedAt'],
                            }
                        )
                print("Successfully fetched and updated relevant news.")
            else:
                print(f"Error: Unable to fetch news. Status code {response.status}")
    except Exception as e:
        print(f"Error occurred: {e}")