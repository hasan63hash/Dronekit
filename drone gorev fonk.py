from dronekit import connect , VehicleMode,LocationGlobalRelative
import time
from pymavlink import mavutil
iha = connect("127.0.0.1:14550",wait_ready = True)


def takeoff(irtifa):
    while iha.is_armable is not True:  
        print("iha arm edilebilir durumda değil")
        time.sleep(1)
    
    print("iha arm edilebilir")
    iha.mode = VehicleMode("GUIDED")
     
     print(str(iha.mode)+"moduna alındı")
     iha.armed = True
     while iha.armed is not True:   
        print("iha arm ediliyor")
        time.sleep(0.5)
    print("iha arm edildi")
    iha.simple_takeoff(irtifa)
    while iha.locaiton.global_relative_frame.alt < irtifa*0.9:
        print("iha hedefe yükseliyor")
        time.sleep(1)

def gorev_ekle():
    global komut
    komut=iha.commands
    komut.clear()
    time.sleep(1)
    

    #takeoff
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,0,0,0,0,0,0,0,0,10))
    
    #waypoint => dronenin gitmesini istediğimiz yer 
    enlem = -35.36265286
    boylam = 149.16514170
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,enlem,boylam,20))
    
     #waypoint => dronenin gitmesini istediğimiz yer 
    enlem = -35.36318559
    boylam = 149.16607666
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,enlem,boylam,30))
    
    #RTL => dronun kalktığı yere geri dönmesi
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH,0,0,0,0,0,0,0,0,0))
    
    #doğrulama
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH,0,0,0,0,0,0,0,0,0))

    
    
    #komutları araca gönderme
    komut.upload()
    print("komutlar yukleniyor...")


takeoff(10)

gorev_ekle()

#sıradaki komut 0 olsun
komut.next=0


iha.mode=VehicleMode("AUTO")

while True:
    next_waypoint=komut.next
    print(f"Sıradaki komut {next_waypoint}")
    time.sleep(1)
    
    if next_waypoint is 4 :
        print("görev bitti")
        break

print("Döngüden  çıkıldı")