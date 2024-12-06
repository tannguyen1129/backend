# BACKEND RESCURE SYSTEM - UMT.NEWMOUNTAIN

<a href="https://github.com/tannguyen1129/umtnewmountain/issues/new?assignees=&labels=bug&projects=&template=bug_report.md&title=%5BBug%5D%3A+%3CM%C3%B4+t%E1%BA%A3+ng%E1%BA%AFn+g%E1%BB%8Dn+v%E1%BB%81+l%E1%BB%97i%3">Báo cáo lỗi (Bug Report)🆘🆘
</a>

Ứng dụng hỗ trợ điều phối, thông báo, cập nhật thông tin ứng phó thiên tai, tham họa.

Phát triển hệ thống ứng dụng công nghệ thông tin trong ứng phó và hỗ trợ khắc phục thiên tai.

Dự án được thực hiện nhằm mục đích tham gia bảng [Phần mềm Nguồn Mở](https://www.olp.vn/procon-pmmn/ph%E1%BA%A7n-m%E1%BB%81m-ngu%E1%BB%93n-m%E1%BB%9F) trong khuôn khổ [Kỳ thi Olympic Tin học sinh viên Việt Nam lần thứ 33](https://www.olp.vn/olympic-tin-h%E1%BB%8Dc-sinh-vi%C3%AAn) tổ chức tại [Trường Đại học Công nghiệp Hà Nội](https://www.haui.edu.vn/vn) từ ngày 10/12/2024 đến ngày 13/12/2024.

Phần mềm được đội ngũ tác giả của UMT.NewMountain open source theo giấy phép [The MIT License](https://opensource.org/license/mit)

## Mục lục tài liệu

1. [Giới Thiệu](#1-Giới-thiệu)
2. [Cấu trúc thư mục dự án](#4-Cấu-trúc-thư-mục-dự-án)
3. [Hướng dẫn cài đặt](#hướng-dẫn-cài-đặt)
    - [📋 Yêu Cầu - Prerequisites](#yêu-cầu-📋)
    - [🔨 Cài Đặt](#🔨-cài-đặt)
4. [License (Giấy phép)](#7-License-(-Giấy-phép-))

### 1. Giới thiệu

Đây là backend của hệ thống cứu hộ khẩn cấp được xây dựng bằng Appsmith và Django. Với chủ đề năm nay là ứng dụng LCDP, nhóm tác giả đã sử dụng Django - một web framework mã nguồn mở để dựng APIs cho Rescue System

### 2. Cấu trúc thư mục dự án

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
sudo apt install python3 python3-pip python3-venv -y
```
Gán python3 thành python:
```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
sudo update-alternatives --config python
```

Đầu tiên hãy tạo thư mục trong máy ảo bằng lệnh `mkdir rescue` sau đó truy cập thư mục bằng lệnh `cd rescue`. Trong thư mục `rescue` hãy tạo một môi trường bằng câu lệnh `python -m venv my_env` (`my_env` có thể thay đổi bằng tên khác. Cuối cùng kích hoạt môi trường `source my_env/bin/activate`

Tiếp theo sao chép kho lưu trữ sau:
```
 git clone --recursive https://github.com/tannguyen1129/backend.git
cd backend
```



### 4. License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
