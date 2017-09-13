from gopigo import *
import time

class Piggy(object):

    def __init__(self):

        print("Hello sir, I am your robot")
        self.dance()

    def dance(self):
        fwd()
        time.sleep(1.5)
        right.rot()
        time.sleep(.5)
        stop()

##########app

lucky = Piggy()