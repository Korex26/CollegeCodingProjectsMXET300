import time
import L1_ina as ina
import L1_log as log


while True:
    voltage = ina.readVolts()
    log.tmpFile(voltage, "voltage_log.txt")
    #log.logArray(voltage)
    time.sleep(1)