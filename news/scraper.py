import requests
from bs4 import BeautifulSoup

def lay_du_lieu_thoi_tiet():
    url = 'https://nchmf.gov.vn/Kttv/vi-VN/1/thoi-tiet-1-15.html'
    response = requests.get(url)
    response.encoding = 'utf-8'  # Đảm bảo mã hóa đúng

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        du_lieu_thoi_tiet = []

        # Giả sử thông tin nằm trong các thẻ <div> có class 'weather-info'
        for item in soup.find_all('div', class_='weather-info'):
            tieu_de = item.find('h3').text.strip()
            noi_dung = item.find('p').text.strip()
            du_lieu_thoi_tiet.append({
                'tieu_de': tieu_de,
                'noi_dung': noi_dung
            })

        return du_lieu_thoi_tiet
    else:
        return None
