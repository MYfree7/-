import socket

def main():
    while True:
        print("欢迎使用系统程序")
        print("1. 选项一")
        print("2. 选项二")
        print("3. 退出")

        choice = input("请选择一个选项：")

        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '3':
            break
        else:
            print("无效的选择，请重新输入")

def option1():
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address
if __name__ == '__main__':
    ip = get_ip_address()
    print(f"当前设备的IP地址是：{ip}")
    # 执行选项一的相关操作

def option2():
    print("选择了选项二")
    # 执行选项二的相关操作

if __name__ == '__main__':
    main()