# Đề bài:
# - Đọc 1 file văn bản gồm nhiều dòng
# - Ghi ra màn hình theo thứ tự ngược lại của các dòng
# VD:
# Nam quốc sơn hà
# Nam đế cư
# ->
# Nam đế cư
# Nam quốc sơn hà

with open('test.txt', 'r') as file:
    # Đọc các dòng từ cuối lên đầu và in ra màn hình
    for line in reversed(list(file.readlines())):
        print(line.strip())
