from dronekit import connect , VehicleMode
from pymavlink import mavutil
import time

drone = connect('127.0.0.1:14550', wait_ready=True)


ef takeoff(irtifa):
	while drone.is_armable:
		print("drone arm edilebilir")
		drone.mode = VehicleMode(GUIDED)
		time.sleep(1)
		print(str(drone.mode)+ "moduna alındı")
		
		drone.armed = True
		while drone.armed is not True : 
			print("drone arm ediliyor)
			time.sleep(1)

		print("drone arm edildi")
		drone.simple_takeoff(irtifa)
		break
	print("drone arm edilebilir değil")
	time.sleep(1)
    
def condition_yaw(heading, relative=False):
    if relative:
        is_relative=1 #yaw relative to direction of travel
    else:
        is_relative=0 #yaw is an absolute angle
    # create the CONDITION_YAW command using command_long_encode()
    msg = drone.message_factory.command_long_encode(
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_CMD_CONDITION_YAW, #command
        0, #confirmation
        heading,    # param 1, yaw in degrees
        0,          # param 2, yaw speed deg/s
        1,          # param 3, direction -1 ccw, 1 cw
        is_relative, # param 4, relative offset 1, absolute angle 0
        0, 0, 0)    # param 5 ~ 7 not used
    # send command to vehicle
    drone.send_mavlink(msg)
    
  #drone döndürme
condition_yaw(180, True) 
takeoff(15)