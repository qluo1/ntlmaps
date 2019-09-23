"""

"""
import socket


def send_connect(host, port):
    """ """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    msg = """
CONNECT gitlab.gs.com:443 HTTP/1.1
Host: gitlab.gs.com:443
#User-Agent: Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)
#Proxy-Connection: Keep-Alive
#Accept-Language: en-US
#Pragma: no-cache
#Accept: image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-excel, application/msword, application/vnd.ms-powerpoint, */*

"""

    for ln in msg.split("\n"):
        ln = ln.strip()
        if ln.startswith("#"):
            continue
        if ln:
            ln = ln + "\r\n"
            print ln,
        sock.send(ln)

    sock.send("\r\n")
    print("recv..")
    data = sock.recv(10000)
    print(data)


if __name__ == "__main__":
    send_connect("gitlab.gs.com", 443)
