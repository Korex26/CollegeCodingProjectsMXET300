import L2_vector as vec
import L1_log as log
import L1_ina as ina
import time


while True:
    voltage = ina.readVolts()
    
    vec_dist = vec.getNearest()
    vec_dist2 = vec.polar2cart(vec_dist[0], vec_dist[1])

    log.tmpFile(vec_dist[0], "L2_dist.txt")
    log.tmpFile(vec_dist[1], "L2_angle.txt")

    log.tmpFile(vec_dist2[0], "L2_x.txt")
    log.tmpFile(vec_dist2[1], "L2_y.txt")

    log.tmpFile(voltage, "voltage_log.txt")
    time.sleep(0.1)