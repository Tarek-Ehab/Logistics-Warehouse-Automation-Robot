from channels.generic.websocket import WebsocketConsumer
from .models import CarDrop,Order
import json
cars = {}
class PracticeConsumer(WebsocketConsumer):

    def connect(self): 
        if self.scope['user'].is_anonymous:
            self.close()
        else:
            self.accept()
            cars[self.scope['user'].username]=self
            car_model = CarDrop.objects.get(drop_name=self.scope['user'].username)
            car_model.delivery_status = 'In active'
            car_model.save()


    def receive(self, text_data=None, bytes_data=None, **kwargs):
        car_model = CarDrop.objects.get(drop_name=self.scope['user'].username)
        data = json.loads(text_data)
        print(data)
        if data.get('status') == 'Active':
            car_model.delivery_status = 'Active'
            car_model.save()
            
        elif data.get('status') == 'OrderArrived':
            print ('aa')
            order_model = Order.objects.get(pk=data.get('order_id'))
            print ('yy')
            order_model.delivery_status='arrived'
            order_model.save()

        self.send(text_data=json.dumps({"status":"ok"}))
        
    def disconnect(self, code):
        print('disconnect')
        cars.pop(self.scope['user'].username)
        car_model = CarDrop.objects.get(drop_name=self.scope['user'].username)
        car_model.delivery_status = 'Disconnect'
        car_model.save()
        return super().disconnect(code)

    @staticmethod
    def send_data(car_name, text_data=None, bytes_data=None, close=False):
        print(type(car_name),".",car_name)
        car = cars.get(car_name,None)
        print("send data",car_name ,  cars ,car)
        if car is not None:
            print(text_data)
            car.send(json.dumps(text_data),bytes_data,close)
