from websocket import create_connection 
import requests
import json
import time 

 
user_name = 'car2'
passwrod = '1234'
is_connected = False

def get_access(host_ip):
    print('befoer respinces ')
    print(f'http://{host_ip}/api/Signin/')
    respone = requests.post(f'http://{host_ip}/api/Signin/',{'username':user_name,'password':passwrod})
    print('aftera respinces ')
    if respone.status_code == 200 :
        data = respone.json()
        print(data)
        return data['access']
    return ''

class Socket_clinet():
    def __init__(self , access , host_ip) -> None:
        self._host_ip = host_ip
        self._access = access
        self.ws = create_connection(f"ws://{self._host_ip}/ws/socket-server/?token={self._access}")
        self.order_data ={}

    def recive_data(self):
        result = json.loads(self.ws.recv())
        if result.get('id') != None:
            self.order_data = result
        return True 
    
    def send_data(self, data:dict):
        self.ws.send(json.dumps(data))
    
    def set_active(self):
        self.send_data({'status':'Active'})

    def set_ordere_arrrived(self):
        self.send_data({'status':'OrderArrived','order_id':self.order_data['id']})

    def close_connection(self):
        self.ws.close()

if __name__ == '__main__':
    host_ip = '192.168.100.24:8000'
    print(host_ip)
    access = get_access(host_ip)
    socket_connection = Socket_clinet(access, host_ip)
    if socket_connection.recive_data():
        print(socket_connection.order_data)
        socket_connection.set_active()
        time.sleep(10)
        socket_connection.set_ordere_arrrived() 

