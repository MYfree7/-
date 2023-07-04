import requests

def get_public_ip_address():
    url = 'https://api.ipify.org'  # 一个提供公共IP地址的API
    response = requests.get(url)
    ip_address = response.text
    return ip_address

if __name__ == '__main__':
    ip = get_public_ip_address()
    print(f"外部的公共IP地址是：{ip}")