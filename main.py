from gopigo import *
import time

class Piggy(object):

    def __init__(self):
        print("I AM ALIVE")

# pulse
    def pulse(self):
        """check for obstacles, drive fixed amount forward"""
        look = us_dist(15)  # store the distance reading
        if look > 80:
            fwd()
            time.sleep(1)
            stop()
# cruise
    def cruise(self):
        """drive fwd, stop if sensor detects obstacle"""
        fwd()
        while(True):
            if us_dist(15) < 30:
                stop()
            time.sleep(.2)
# servo_sweep
    def servo_sweep(self):
        """loops in a 120 degree arc and moves servo"""
        for ang in range(20, 160, 2):
            servo(ang)
            time.sleep(.2)


def menu():
    while True:
        input = raw_input("Press 1 for cruise \nPress 2 for pules \nPress 3 for sweep\n")
        if "1" in input:
            p.cruise()
        elif"2" in input:
            p.pulse()
        elif "3" in input:
            p.servo_sweep()



p = Piggy()


try:
    menu()
except(KeyboardInterrupt, SystemExit):
    from gopigo import *
    stop()
