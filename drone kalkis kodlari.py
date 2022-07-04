


from dronekit import connect
from dronekit import VehicleMode
import time


iha = connect('127.0.0.1:14550', wait_ready=True)




def takeoff(irtifa):
	while iha.is_armable:
		print("İha arm edilebilir")
		iha.mode = VehicleMode(GUIDED)
		time.sleep(1)
		print(str(iha.mode)+ "moduna alındı")
		
		iha.armed = True
		while iha.armed is not True :
			print("iha arm ediliyor")
			time.sleep(1)

		print("İha arm edildi")
		iha.simple_takeoff(irtifa)
		break
	print("iha arm edilebilir değil")
	time.sleep(1)
takeoff(15)




