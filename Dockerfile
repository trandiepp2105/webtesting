FROM selenium/standalone-edge

# Cài đặt Python
# Chuyển sang người dùng root
USER root

# Xóa nội dung cũ
RUN rm -rf /var/lib/apt/lists/*

# Cập nhật và cài đặt Python
RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /webtesting

COPY requirements.txt ./

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY ./ ./

ENV PYTHONPATH=/webtesting