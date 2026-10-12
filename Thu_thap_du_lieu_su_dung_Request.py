import requests
import json

def fetch_and_save_requests():
    url = "https://jsonplaceholder.typicode.com/posts?_limit=5"
    print(f"Đang lấy dữ liệu từ {url}...")
    
    response = requests.get(url)
    data = response.json()
    
    # Lưu vào file JSON
    file_name = "requests_data.json"
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print(f"Thành công! Đã lưu {len(data)} bản ghi vào {file_name}")

fetch_and_save_requests()
