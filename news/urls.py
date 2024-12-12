from django.urls import path
from . import views 

urlpatterns = [
    # URL cho view cào dữ liệu và trả về bài viết
    path('fetch-news/', views.ScrapeAndListArticlesAPI.as_view(), name='scrape_and_list_articles')
]
