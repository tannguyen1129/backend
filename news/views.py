import requests
from bs4 import BeautifulSoup
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view


class ScrapeAndListArticlesAPI(APIView):
    """
    View để cào dữ liệu và trả về danh sách bài viết dưới dạng JSON.
    """

    BASE_URL = "https://nchmf.gov.vn/Kttv/vi-VN/1/index.html"

    def scrape_articles(self):
        """
        Hàm cào dữ liệu từ trang web và lưu vào cơ sở dữ liệu.
        """
        response = requests.get(self.BASE_URL)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.select('.grp-list-item .uk-list li a')  # Chọn các thẻ <a> chứa bài viết
            saved_count = 0

            for article in articles:
                # Lấy tiêu đề từ nội dung của thẻ <a>
                title = article.text.strip().split('(')[0].strip()  # Lấy phần trước dấu "(" để lấy tiêu đề
                link = article['href'].strip() if 'href' in article.attrs else None

                # Lấy thời gian từ nội dung trong ngoặc đơn
                time_posted = article.text.strip().split('(')[1][:-1].strip() if '(' in article.text else None

                # Lưu vào database nếu chưa tồn tại
                if not Article.objects.filter(link=link).exists():
                    Article.objects.create(
                        title=title,
                        link=link,
                        time_posted=time_posted
                    )
                    saved_count += 1

            return saved_count
        else:
            raise Exception(f"Failed to retrieve the page. Status code: {response.status_code}")

            
    def get(self, request):
        """
        Xử lý yêu cầu GET:
        1. Cào dữ liệu từ trang web và lưu vào CSDL.
        2. Trả về danh sách bài viết dưới dạng JSON.
        """
        try:
            # Gọi hàm cào dữ liệu
            saved_count = self.scrape_articles()

            # Lấy tất cả bài viết từ CSDL
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)

            # Trả về danh sách bài viết cùng số lượng bài viết đã lưu
            return Response({
                "status": "success",
                "saved_count": saved_count,
                "articles": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
