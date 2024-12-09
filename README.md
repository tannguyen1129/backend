# BACKEND RESCURE SYSTEM - UMT.NEWMOUNTAIN

<a href="https://github.com/tannguyen1129/umtnewmountain/issues/new?assignees=&labels=bug&projects=&template=bug_report.md&title=%5BBug%5D%3A+%3CM%C3%B4+t%E1%BA%A3+ng%E1%BA%AFn+g%E1%BB%8Dn+v%E1%BB%81+l%E1%BB%97i%3">Báo cáo lỗi (Bug Report)🆘🆘
</a>

Ứng dụng hỗ trợ điều phối, thông báo, cập nhật thông tin ứng phó thiên tai, tham họa.

Phát triển hệ thống ứng dụng công nghệ thông tin trong ứng phó và hỗ trợ khắc phục thiên tai.

Dự án được thực hiện nhằm mục đích tham gia bảng [Phần mềm Nguồn Mở](https://www.olp.vn/procon-pmmn/ph%E1%BA%A7n-m%E1%BB%81m-ngu%E1%BB%93n-m%E1%BB%9F) trong khuôn khổ [Kỳ thi Olympic Tin học sinh viên Việt Nam lần thứ 33](https://www.olp.vn/olympic-tin-h%E1%BB%8Dc-sinh-vi%C3%AAn) tổ chức tại [Trường Đại học Công nghiệp Hà Nội](https://www.haui.edu.vn/vn) từ ngày 10/12/2024 đến ngày 13/12/2024.

Phần mềm được đội ngũ tác giả của UMT.NewMountain open source theo giấy phép [The MIT License](https://opensource.org/license/mit)

## Mục lục tài liệu

1. [Giới Thiệu](#1-giới-thiệu)
2. [Các APIs](#2-các-apis)
3. [Hướng dẫn cài đặt](#hướng-dẫn-cài-đặt)
    - [📋 Yêu Cầu - Prerequisites](#yêu-cầu-📋)
    - [🔨 Cài Đặt](#🔨-cài-đặt)
4. [License (Giấy phép)](#7-License-(-Giấy-phép-))
5. [Đóng góp](5-đóng-góp)
6. [Liên hệ](6-liên-hệ)

### 1. Giới thiệu

Đây là backend của hệ thống cứu hộ khẩn cấp được xây dựng bằng Appsmith và Django. Với chủ đề năm nay là ứng dụng LCDP, nhóm tác giả đã sử dụng Django - một web framework mã nguồn mở để dựng APIs cho Rescue System

### 2. Các APIs

`app/userauths`: Xác thực đăng nhập người dùng, tạo tài khoản cho cơ quan cứu trợ.

`app/image`: Tải ảnh và lấy ảnh.

`app/maps`: 

- Lấy danh sách tất cả các vùng thiên tai.
- Thêm mới vùng thiên tai.
- Xóa vùng thiên tai theo ID.

`app/resources`:

- Công dân xem danh sách thông báo khẩn cấp.
- Agency xem danh sách thông báo và tạo thông báo mới.
- Agency cập nhật hoặc xóa thông báo cụ thể.
- Quản lý tài nguyên, nhân lực, phân công, yêu cầu điều phối và phân công trạng thái cho Agency.
- Quản lý tài nguyên và yêu cầu điều phối, phê duyệt yêu cầu điều phối cho Authority.

`app/subcriptions`:

- Lấy danh sách các đăng ký nhận tin.
- Đăng ký nhận tin và lưu thông tin vào cơ sở dữ liệu.

`app/support`:

- Cho phép công dân gửi yêu cầu hỗ trợ, không cần đăng nhập.
- Cho phép Agency hoặc Admin xem tất cả yêu cầu hỗ trợ, yêu cầu đăng nhập và có quyền Agency.



### 3. Hướng dẫn cài đặt

#### 3.1. Yêu cầu

Để có thể sử dụng tốt bạn cần chuẩn bị một máy ảo VPS và một domain (nếu bạn thích có domain). Nếu không có domain thì dùng địa chỉ IP máy chủ để thay thế.

Cấu hình máy chủ VPS tối thiểu, phù hợp cho thử nghiệm:

CPU: 1 Core
RAM: 1GB
Dung lượng đĩa: 20GB SSD
Hệ điều hành: Ubuntu 20.04 LTS hoặc Debian 11
Băng thông: 1TB/tháng

Trước khi bắt đầu, hãy cài đặt đầy đủ [Docker](https://docs.docker.com/get-started/get-docker/) (version 20.10.7 or later) và [Docker-compose](https://docs.docker.com/compose/install/) (version 1.29.2 or later)

#### 3.2. Hướng dẫn cài đặt

Cài đặt Python và các công cụ liên quan:
```
sudo apt update && sudo apt upgrade -y
sudo apt install build-essential python3 python3-pip python3-venv -y
```
Gán python3 thành python:
```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
sudo update-alternatives --config python
```

Đầu tiên hãy tạo thư mục trong máy ảo bằng lệnh `mkdir rescue` sau đó truy cập thư mục bằng lệnh `cd rescue`. Trong thư mục `rescue` hãy tạo một môi trường và kích hoạt môi trường bằng câu lệnh sau: 

```
python -m venv my_env (`my_env` có thể thay đổi bằng tên khác).
source my_env/bin/activate
```

Tiếp theo sao chép kho lưu trữ sau:
```
git clone --recursive https://github.com/tannguyen1129/backend.git
cd backend
```
Kế tiếp các bạn tạo môi trường bằng lệnh `python -m venv my_env` (`my_env` là tên môi trường, bạn có thể thay đổi)

Sau bước này, chạy lệnh để cài đặt các thư viện, sau đó chạy lệnh migrate dữ liệu:

```
pip install -r requirements.txt
python manage.py migrate
```

Tiếp theo, định cấu hình các file sau trong backend và bỏ đuôi `.example`: `nginx.conf.example`,`docker-compose.yml.example` và `.env.example`

```
cp nginx.conf.example nginx.conf
cp docker-compose.yml.example docker-compose.yml
cp .env.example .env
```

Sau khi cấu hình xong, thì bắt đầu chạy lệnh Docker:

```
docker-compose build
docker-compose up -d
```
Bước tiếp theo, bạn dùng lệnh để tạo superuser:

```
python manage.py createsuperuser
```

Đến đây là hoàn thành, có thể truy cập từ địa chỉ của máy chủ, truy cập bảng điều khiển của admin bằng địa chủ máy chủ. Ví dụ `10.11.12.13/admin` hoặc truy cập API thông qua các urls

<img width="956" alt="image" src="https://github.com/user-attachments/assets/53736c0f-136a-47fd-9cd7-2aecc85b67ed">

<img width="946" alt="image" src="https://github.com/user-attachments/assets/2cf4aded-ee46-454d-b626-e27260f47a6e">

Cách sử dụng:

1. Nếu bạn muốn bắt đầu, hãy dùng câu lệnh: `docker-compose up -d`
2. Nếu bạn muốn dừng, hãy dùng câu lệnh: `docker-compose down`

### 4. License

Dự án này được cấp phép theo Giấy phép MIT - xem tệp [LICENSE](LICENSE) để biết chi tiết.

### 5. Đóng góp

### 6. Liên hệ
