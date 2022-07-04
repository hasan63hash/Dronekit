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

def send_ned_velocity(velocity_x, velocity_y, velocity_z, duration):
    """
    Move vehicle in direction based on specified velocity vectors.
    """
    msg = drone.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
        0b0000111111000111, # type_mask (only speeds enabled)
        0, 0, 0, # x, y, z positions (not used)
        velocity_x, velocity_y, velocity_z, # x, y, z velocity in m/s
        0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)


    # send command to drone on 1 Hz cycle
    for x in range(0,duration):
        drone.send_mavlink(msg)
        time.sleep(1)


send_ned_velocity(5,0,-1,5)

takeoff(10)

