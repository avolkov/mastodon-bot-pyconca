#!/usr/bin/env python3

import io
import os


tty_file = io.FileIO(os.open("/dev/ttyACM0", os.O_NOCTTY | os.O_RDWR), "r+")

tty_wrapper = io.TextIOWrapper(tty_file)

#import ipdb; ipdb.set_trace()

print(tty_wrapper.readline())