from keras.models import load_model
from time import sleep
from tensorflow.keras.utils import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import pandas as pd
import gunicorn
from flask import Flask, Response, jsonify, render_template

from camera import *
app = Flask(__name__)

face_classifier = cv2.CascadeClassifier(r'D:/book reccomend system/book reccomendation system/haarcascade_frontalface_default.xml')
classifier =load_model(r'D:/book reccomend system/book reccomendation system/model.h5')

emotion_labels = ['Angry  ','Disgust','Fear','Happy ','Neutral', 'Sad', 'Surprise']

cap = cv2.VideoCapture(0)



while True:
    _, frame = cap.read()
    labels = []
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)



        if np.sum([roi_gray])!=0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi,axis=0)

            prediction = classifier.predict(roi)[0]
            label=emotion_labels[prediction.argmax()]
            label_position = (x,y)
            cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            angry=['The Art of War','The Count of Monte Cristo','Autobiography of Yogi','Tween Snow Fire','A Tale of Two Cities Walden','Anne of Green gables','The Story of My life','The Picture Of Dorian Gray','Acres Of Diamonds']
            disgusted=['The Communist Manifesto','Macbeth','The Age Of reason','Siddhartha','The Sense Of Beauty','The Analects of Confucius','Palmistry for all','The Analysis of Mind','Analysing Character','The Bhabavad Gita','Meditations']
            fearful=['the call of cthulhu','The Best Ghost Stories','Dracula','the invisible man','Collected Works of Poe','The Woman In white','The Phantom Of the Opera','Clarimonde','Grimms Fairy Tales','Metamorphosis','The After House']
            happy=['Emma','The 300 Beequest','adventures of huckleberry finn','Three men in a boat','the importance of Being Earnest','the CanterVille ghost','eves Diary','the hackers Dictionary','Pygmalion','a comedy of errors in seven acts','An ideal Husband']
            neutral=['The Arabian Nights Entertainments','The Arabian Nights Entertainments','Stories By German Authors','the book of thousand Nights and One Night','Cindrella','seven icelandic s','Love and Friendship and other Early Works','the grim smile of the five towns','Winesburg,ohio','the moon endureth','can such things be']
            sad=['cranford','Criminal Sociology','The Rubaiyat of Omar Khayam','North of Boston','The Golden Sayings of Epictetus','Prufrock and Other Observsations','Sidelights on Relativity','Fables for the frivolous','The Hunting of the Snark','The Orgin and nature of emotions']
            surprize=['The Arabian Nights Entertainments','The Atomic Bombings ','Stammering its cause and cure','Hunger','The Psychology of Revolution','The Moon Endureth','Chess History And Reminiscences','Beasts of Tarzan','Jungle Tales Of Tarzon','Tarzon and the Jewels of Opar']
            if label == 'Neutral':
                for i in neutral:
                    print(i.to_json(orient='records'))
                    return render_template('index.html', headings=headings, data=i)
                break
            elif label == 'Angry':
                for i in angry:
                    print(i)
                break
            elif label == 'Disgust':
                for i in disgust:
                    print(i)
                break
            elif label == 'Fear':
                for i in fearful:
                    print(i)
                break
            elif label == 'Happy':
                for i in happy:
                    print(i)
                break
            elif label == 'Sad':
                for i in sad:
                    print(i)
                break
            elif label == 'Surprise':
                for i in surprize:
                    print(i)
                break
        else:
            cv2.putText(frame,'No Faces',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow('Emotion Detector',frame)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        exit()

cap.release()
cv2.destroyAllWindows()