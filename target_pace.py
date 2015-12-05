#! /usr/bin/env python

import unittest
import math

class TestAllMethods(unittest.TestCase):

    def test_sec_to_minsec(self):
        self.assertEqual(sec_to_minsec(336), '5:36')
        self.assertEqual(sec_to_minsec(0), '0:0')

    def test_calc_pace(self):
        self.assertEqual(calc_pace(5, 28), '5:36')

def sec_to_minsec(secs):

    mins = int(math.floor(secs/60))
    secs = int(secs - mins*60)

    return str(mins) + ":" + str(secs)

def calc_pace(distance, target_time):
    target_time_secs = target_time * 60
    reqd_pace = target_time_secs/distance

    return sec_to_minsec(reqd_pace)


if __name__ == '__main__':

    distance = float(raw_input("Enter the distance you want to run (in kms): "))
    target_time = int(raw_input("In how many mins do you want to cover %d km? " %
        (distance)))

    print
    print

    print "Your pace should be", calc_pace(distance, target_time), "mins/km"

    print
    print
    unittest.main()
