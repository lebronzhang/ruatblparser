# Lua Table Parser
# Taylor Zhang
# Dec. 9, 2016

# Useful 
# @staticmethod; x, y, theta = state; theta = state[2]; array([g1, g2, g3]); l, r = tuple(control);self.dg_dstate; 
# self.state[0:3]; initial_state = array([500.0, 0.0, 45.0 / 180.0 * pi]); logfile.read("input.txt")
from math import *

class PyLuaTblParser:
    def __init__(self, state):
        # The state. This is the core data of the Kalman filter.
        self.state = state
        # Some constants.
        # Currently, the number of landmarks is zero.

    def load(self, s):

    def dump(self):

    def loadLuaTable(self, f):

    def dumpLuaTable(self, f):

    def loadDict(self, d):

    def dumpDict(self):  

if __name__ == '__main__':

    # Setup.
    kf = PyLuaTblParser(initial_state)
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