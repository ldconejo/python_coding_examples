# ldconejo - Demo sourced from: https://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python
import signal
import sys

def signal_handler(sig, frame):
    print("You pressed CTRL-C!!!")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print("Press CTRL-C")
signal.pause()