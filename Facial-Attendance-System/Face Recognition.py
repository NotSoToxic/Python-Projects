import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import csv


#Creating the CSV FILE if the file doesnot exist for day
time_now = datetime.now()
dStr = time_now.strftime('_%d_%m_%Y')
filename = "Excel\\Attendance"+dStr+ ".csv"

path1 = 'Excel'
myList1 = os.listdir(path1)

c=0
for file in myList1:
    if (file == filename):
        c= 1
 
# writing to csv file 
if(c<1):
    with open(filename, 'w') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile)

path = 'Images'
images = []
personNames = []
myList = os.listdir(path)
print(myList)
for cu_img in myList:
    current_Img = cv2.imread(f'{path}/{cu_img}')
    images.append(current_Img)
    personNames.append(os.path.splitext(cu_img)[0])
print(personNames)


def faceEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def attendance(name):
    with open(filename , 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            time_now = datetime.now()
            tStr = time_now.strftime('%H:%M:%S')
            dStr = time_now.strftime('%d/%m/%Y')
            f.writelines(f'\n {name},{tStr},{dStr}')


encodeListKnown = faceEncodings(images)
print('All Encodings Complete!!!')

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    # faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

    facesCurrentFrame = face_recognition.face_locations(faces)
    encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

    for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = personNames[matchIndex].upper()
            # print(name)
            tStr = time_now.strftime('%H:%M')
            cv2.putText(frame, name, (30 , 50 ), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            name = name+"_time_=_"+tStr
            attendance(name)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(0) & 0xFF == ord('s'):
        name = input("Enter your name: ")
        # Saving the face as jpg file and storing the same images blob data in sql database
        cv2.imwrite("E:\\VS Code\\Project exhibition\\Images\\"+name+".jpg", frame)
        print("Face saved successfully")
        break
cap.release()
cv2.destroyAllWindows()