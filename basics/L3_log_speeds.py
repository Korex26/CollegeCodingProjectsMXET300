import L1_log as log
import L2_inverse_kinematics as ik
import L2_speed_control as sc
import L2_kinematics as kine
import numpy as np
import time
import L1_ina as ina
#import L1_encoder as enc                    # local library for encoders

# THIS SECTION ONLY RUNS IF THE PROGRAM IS CALLED DIRECTLY
if __name__ == "__main__":
    while True:

        voltage = ina.readVolts()
        log.tmpFile(voltage, "voltage_log.txt")

        C = kine.getMotion()  # This take approx 25.1 ms if the delay is 20ms
        B = kine.getPdCurrent() # [pdl, pdr]
        B = np.round(B, decimals=3)
        print("xdot(m/s), thetadot (rad/s):", C, "\t","deltaT: ", kine.deltaT)
        print("pdl (rad/s): ", B[0], "\tpdr (rad/s)", B[1])
        log.tmpFile(C[0], "xdot.txt")
        log.tmpFile(C[1], "thetadot.txt")
        log.tmpFile(B[0], "pdl.txt")
        log.tmpFile(B[1], "pdr.txt")


        time.sleep(0.2)
