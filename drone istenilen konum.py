from dronekit import connect , VehicleMode,LocationGlobalRelative
import time

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
    

    
 takeoff(10)
 enlem = -35.36223671
 boylam = 149.16509335
 irtifa = 20
 konum = LocationGlobalRelative(enlem,boylam,irtifa)
 
 iha.simple_goto(konum)
         