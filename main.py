import ctypes
from flask import Flask
from flask import render_template as rt
from tkinter import messagebox as mbox
import os, time, interception

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	#os.startfile('winscreenlock.py')
	ctypes.windll.user32.LockWorkStation()
	#return "HELLO WORLD"	

@app.route('/unlock',methods=['GET','POST'])
def unlock():

	interception.auto_capture_devices()

	interception.press('enter')

	time.sleep(1)

	interception.key_down('shift')
	text="your-windows-password"
	for char in text:
		interception.press(char)
		time.sleep(0.12)
	interception.press('enter')
app.run(debug=True,host="0.0.0.0",port=80)
