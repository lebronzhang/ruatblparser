# Lua Table Parser
# Taylor Zhang
# Dec. 9, 2016

# Useful 
# @staticmethod; x, y, theta = state; theta = state[2]; array([g1, g2, g3]); l, r = tuple(control);self.dg_dstate; 
# self.state[0:3]; initial_state = array([500.0, 0.0, 45.0 / 180.0 * pi]); logfile.read("input.txt")
from math import *

class PyLuaTblParser:
    def __init__(self):
    	pass
        # The state. This is the core data of the Kalman filter.
        # Some constants.
        # Currently, the number of landmarks is zero.

    # def __init__(self, state):
    #     # The state. This is the core data of the Kalman filter.
    #     self.state = state

    def load(self, s):
        self.str = s

    def dump(self):
        print(self.str)

    # def loadLuaTable(self, f):

    # def dumpLuaTable(self, f):

    # def loadDict(self, d):

    def dumpDict(self): 
    	sp = self.str.split('},')
    	print(sp)

if __name__ == '__main__':

    # Setup.
    a1 = PyLuaTblParser()
    # a2 = PyLuaTblParser()
    # a3 = PyLuaTblParser()
    test_str = '{array = {65,23,5,},dict = {mixed = {43,54.33,false,9,string = "value",},array = {3,6,4,},string = "value",},}'
    a1.load(test_str)
    a1.dump()
    a1.dumpDict()
    # d1 = a1.dumpDict()

    # a2.loadDict(d1)
    # a2.dumpLuaTable(file_path)
    # a3.loadLuaTable(file_path)

    # d3 = a3.dumpDict()
    # Read data.
    """
    # Loop
    f = open("output.txt", "w")
    for i in xrange(len(logfile.motor_ticks)):
        # Prediction.
        control = array(logfile.motor_ticks[i]) * ticks_to_mm
        kf.predict(control)
        # Output the center of the scanner, not the center of the robot.
        print >> f, "F %f %f %f" % \
            tuple(kf.state[0:3] + [scanner_displacement * cos(kf.state[2]),
                                   scanner_displacement * sin(kf.state[2]),
                                   0.0])
        # Write covariance matrix in angle stddev1 stddev2 stddev-heading form
        e = PyLuaTblParser.get_error_ellipse(kf.covariance)
        print >> f, "E %f %f %f %f" % (e + (sqrt(kf.covariance[2,2]),))

    f.close()
    """