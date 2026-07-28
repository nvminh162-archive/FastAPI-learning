# Book Management API

Dự án thực hành FastAPI, SQLAlchemy, Alembic và ánh xạ dữ liệu xuống MySQL.

## Công nghệ sử dụng

- Python
- FastAPI
- SQLAlchemy
- Alembic
- MySQL 8.4
- Docker Compose

## Yêu cầu

Máy cần cài đặt:

- Python
- Docker Desktop

## Chạy dự án sau khi clone

### 1. Tạo và kích hoạt môi trường ảo

```powershell
python -m venv venv
venv\Scripts\activate
```

### 2. Cài đặt thư viện

```powershell
python -m pip install "fastapi[standard]" sqlalchemy alembic pymysql python-multipart
```

### 3. Khởi động MySQL

```powershell
docker compose up -d --wait
```

### 4. Tạo cấu trúc bảng từ các migration có sẵn

```powershell
alembic upgrade head
```

### 5. Khởi động FastAPI

```powershell
uvicorn app.main:app --reload
```

Sau khi ứng dụng chạy:

- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Thông tin MySQL

| Thuộc tính | Giá trị |
|---|---|
| Host | `localhost` |
| Port | `33067` |
| Database | `fastapi_books` |
| User | `fastapi_user` |
| Password | `fastapi_password` |

MySQL sử dụng cổng `33067` trên máy để hạn chế trùng với các dự án khác. Bên trong container, MySQL vẫn chạy ở cổng mặc định `3306`.

## Làm việc với Alembic

Thư mục `migrations/` đã tồn tại trong repository, vì vậy sau khi clone **không chạy lại**:

```powershell
alembic init migrations
```

Khi thay đổi các SQLAlchemy model, tạo một migration mới:

```powershell
alembic revision --autogenerate -m "mo ta thay doi"
```

Sau đó áp dụng migration xuống MySQL:

```powershell
alembic upgrade head
```

Xem migration hiện tại:

```powershell
alembic current
```

Xem lịch sử migration:

```powershell
alembic history
```

## Quản lý MySQL container

Dừng container nhưng giữ lại dữ liệu:

```powershell
docker compose down
```

Khởi động lại:

```powershell
docker compose up -d --wait
```

Xóa container và toàn bộ dữ liệu MySQL:

```powershell
docker compose down -v
```

> Lệnh `docker compose down -v` xóa volume chứa dữ liệu và không thể khôi phục từ Docker.
