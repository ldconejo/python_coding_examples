import time
import sys

def main():
    try:
        while True:
            print("Still waiting for you to press CTRL-C")
            time.sleep(2)
    except KeyboardInterrupt:
        print("Goodbye!")
        sys.exit(0)
    
if __name__ == "__main__":
    main()