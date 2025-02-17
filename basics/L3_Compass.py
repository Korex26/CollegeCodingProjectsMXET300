import time
import L2_compass_heading as comp_head
import L1_log as log
import L1_ina as ina

'''
def getComp():
    head = comp_head.get_heading()
    return head
'''
def direct(index):
    
    if (index > -23 and index < 23):
        direction2 = "North"
    elif (index > 23 and index <= 68):
        direction2 = "North East"
    elif (index > 68 and index <= 113):
        direction2 = "East"
    elif (index > 113 and index <= 157):
        direction2 = "South East"
    elif (index > 157 and index <= 180):
        direction2 = "South"
    elif (index > -180 and index <= -157):
        direction2 = "South"
    elif (index > -157 and index <= -113):
        direction2 = "South West"
    elif (index > -113 and index <= -68):
        direction2 = "West"
    elif (index > -68 and index <= -23):
        direction2 = "North West"

    log.stringTmpFile(direction2, "direction0.txt")
    
    return direction2

def heading(value):

    log.tmpFile(value, "heading.txt")

    return comp_head.get_heading()


while (1):
    
    #heading(comp_head.get_heading())
    print("Hello!")
    direct(comp_head.get_heading())
    log.tmpFile(comp_head.get_heading(), "heading.txt")
    voltage = ina.readVolts()
    log.tmpFile(voltage, "voltage_log.txt")
    time.sleep(1)
'''
if __name__ == "__main__":
    while True:
        #print(round(comp_head.get_heading(),2))           # Print the compass heading in degrees
        print("Hello!")
        time.sleep(0.1)  
'''