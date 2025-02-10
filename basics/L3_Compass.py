import time
import L2_compass_heading as comp_head
import L1_log as log
import L2_telemetry as tele
import L1_ina as ina

'''
def getComp():
    head = comp_head.get_heading()
    return head
'''
def direct(index):
    
    if (index > -23 and index < 23):
        direction2 = "North"
    elif (index > 23 and index < 77):
        direction2 = "North West"
    elif (index > 77 and index < 113):
        direction2 = "West"
    elif (index > 113 and index < 157):
        direction2 = "South West"
    elif (index > 157 and index < 177):
        direction2 = "South"
    elif (index > -180 and index < -157):
        direction2 = "South East"
    elif (index > -157 and index < -113):
        direction2 = "East"
    elif (index > -113 and index < -77):
        direction2 = "North East"
    elif (index > -77 and index < -23):
        direction2 = "North East"

    log.stringTmpFile(direction2, "direction0.txt")
    
    return direction2

def heading(value):

    log.tmpFile(value, "heading.txt")

    return comp_head.get_heading()


while (1):
    
    heading(comp_head.get_heading())
    direct(comp_head.get_heading())

    time.sleep(1)
    
    
    
