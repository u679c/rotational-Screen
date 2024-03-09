from socket import *
import subprocess


def udp_server(host, port):
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind((host, port))
    print(f"正在监听UDP端口{host}:{port}...")
    while True:
        data, addr = udp_socket.recvfrom(1024)
        if data.decode('utf-8') == "旋转屏幕":
            script_path = './main.sh'
            subprocess.run(['bash', script_path])
        else:
            print("Wi-Fi连接失败 请重启设备")


if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 5555

    udp_server(HOST, PORT)
