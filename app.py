from flask import Flask, request, render_template
from ultralytics import YOLO
import cv2
import numpy as np
from face_capture import capture
from id_recognition import id_capture
from text_extraction import pancard,aadharcard
import pandas as pd
from fetch import verification
import os
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'button1' in request.form:
            # Button 1 was clicked
            a=capture()
            print(a)
        elif 'button2' in request.form:
            b=id_capture()
            print(b)
        elif 'button3' in request.form:
            l,m,n=pancard()
            w,x,y,z=aadharcard()
            d={'pan_name':[l],'dob':[m],'pan_number':[n],'aadhar_name':[w],'aadhar_gender':[x],'aadhar_dob':[y],'aadhar_number':[z]}
            d=pd.DataFrame(d)
            d.to_csv('out.csv', index=False) 
            print(verification())
            os.remove(r"C:\Users\Asus\PycharmProjects\chatbot_project\user_details.csv")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
