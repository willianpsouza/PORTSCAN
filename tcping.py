import json
import socket

def tcpconn(host,port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(2)
    if not sock.connect_ex((host,port)):
        return True
    else:
        return False

def main(host='127.0.0.1'):
    ret = {'host' : host, 'open_ports' : [], 'closed_ports' : [] }
    ports = [1,7,22,23,80,137,138,139,445,3389,1433,8081,3128]
    for c in ports:
        if tcpconn(host,c):
            ret['open_ports'].append(c)
        else:
            ret['closed_ports'].append(c)
    return json.dumps(ret)

print(main())

