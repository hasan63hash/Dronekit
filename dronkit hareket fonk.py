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


def goto_position_target_local_ned(north, east, down):
    """
    Send SET_POSITION_TARGET_LOCAL_NED command to request the drone fly to a specified
    location in the North, East, Down frame.
    """
    msg = drone.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
        0b0000111111111000, # type_mask (only positions enabled)
        north, east, down,
        0, 0, 0, # x, y, z velocity in m/s  (not used)
        0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)
    # send command to drone
    drone.send_mavlink(msg)
    

takeoff(15)

goto_position_target_local_ned(5,5,-1)