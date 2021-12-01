# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 18:48:37 2021

@author: ZTharp
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "Hello, I welcome you to Zandra's website! <h1>HELLO<h1>"
    return "Please enter your name"
    return input()

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"
    
if __name__ == "__main__":
        app.run()