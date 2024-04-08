import os
from flask import Flask
app = Flask(__name__)

if __name__ == "__main__":
    print("Hi, I'm main!!!")
else:
    print(f"Hi, I'm {__name__}")