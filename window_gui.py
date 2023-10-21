########## IMPORTING NECESSARY MODULES ###############
from keras.models import load_model
from time import sleep
from tensorflow.keras.utils import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import pandas as pd
import tkinter
from tkinter import *
import random



############## SUGGESTING FUNCTIONS #####################

def suggest_movie():
    angry=['Gone Girl','The Belko Experiment','He Never Died and She Never Died','Mom and Dad','Happy Gilmore','Mayhem','Upgrade','Falling Down','Jolt','Dear Comrade','Naa Peru surya -Naa Illu India','The Map of Tiny Perfect Things','Sin Filtro','Raging Bull','Oldboy']
    disgusted=['San Andreas','Deep Impact','Hours','Twister','The Day After Tomorrow','The Wave','The Finest Hours','Only the Brave','Poseidon','Men in Black(Netflix)','The Mummy Returns(Netflix)','Journey to the Center of the Earth(Prime)','Fantastic Beasts:The Crimes of Grindelwald']
    fearful=['The Conjuring 2(Netflix)','Creep(Netflix)','Fear Stret(Netflix)','His House(Netflix)','IT(Netflix)','Rosemarrys Baby(Netflix)','It Follows(Prime)','The Witch(Netflix)','Good Night Mommy','Thirst','The Babadock(Prime video)','Pulse','Lights Out(Prime Video)','Malignant']
    happy = ['Tu Hai Mera Sunday(Netflix|Hindi)','50/50(Netflix|English)','Rhythm(Youtube|Tamil)','The Secret Life of Walter Mitty(Youtube|english','The Neighbour Totoro(Netflix|Japanese)','Jerry Maguire(Prime|English)','Moneyball(Netflix|English)','School of Rock(Netflix|English)','Almost Famous(Prime|English)','Begin again(Netflix|English)','The Terminal(Netflix|English)','Cast Away(Netflix/Prime|English)','Forrest Gump(Netflix/Prime|English)','Big(Disney+Hotstar|English)']
    neutral=['Warcraft','The Green Kinght(Prime)','Pets Dragon(Disney+Hotstar)','The Jungle Book(Disney+Hotstar)','Mary Poppins Returns(Hotstar)','A Monster Calls','Jumanji(Disney+Hotstar)','Life of Pi(Hotstar)','Harry Potter(Prime)','The Loard of The Rings(Prime)','Edge of Tomorrow','Coherence','Star Wars','Minority Report']
    sad=['777 Charlie(Voot)','50/50(Netflix)','Dallas Buyers Club(Netflix)','Manchester By the Sea(Netflix)','The Florida Project(Netflix)','The pursuit of Happiness(Netflix)','La La Land(Netflix)','The Fault in Our Stars(Netflix)','Moonlight(Netflix)','Tamasha(Netflix)','500 Days of Summer','Dear Zindagi(Netflix)','Dev D(Netflix)','Karwaan(Prime)','The Secret Life of Walter Mitty']
    surprize=['Arrival(Netflix|English)','Dango Unchained(Netflix|Hindi)','Hereditary(Prime|English)','The Wolf of Wall Street(Prime)','Inception(Prime)','Interstellar(prime)','Mad Max:Fury Road(Prime)','Get Out','The Social Network(Netflix)','The Sucide Squad(HBO Max)','Jungle Cruise(Disney+Hotstar)','There Will Be Blood','Black Panther(Disney+Hotstar)']
    if label == 'Neutral':
        x = random.choice(neutral)
        return x
                
    elif label == 'Angry':
        x = random.choice(angry)
        return x

    elif label == 'Disgust':
        x = random.choice(disgusted)
        return x

    elif label == 'Fear':
        x = random.choice(fearful)
        return x
    
    elif label == 'Happy':
        x = random.choice(happy)
        return x

    elif label == 'Sad':
        x = random.choice(sad)
        return x
    elif label == 'Surprise':
        x = random.choice(surprize)
        return x

def suggest_song():
    angry=['Sick Thoughts','Mo Bamba','MONTERO (Call Me By Your Name)','Foot Fungus','Shhh (Pew Pew) - Slowed + Reverb','Rasputin','Astronaut In The Ocean','Whoopty','Streets','Goosebumps - Remix','Paparazzi']
    disgusted=['Get You The Moon (feat. SnÃ¸w)','Jocelyn Flores','Someone You Loved','how to live','Its You','Loosing Interest','Tell Me Goodbye','Dead and Cold','Heather','Reckless','paradise']
    fearful=['Fearless Pt. II','Fearless','Ark','Supersonic','Fearless Pt. II','Mortals','Horizon','Fearless','Ark','Ark','Mortals','Horizon','Supersonic','Feel Good','Fearless Pt. II','Horizon']
    happy=['Leave The Door Open','Dynamite','Levitating (feat. DaBaby)','Kiss Me More (feat. SZA)','Perfect','GIRL LIKE ME','We Need Love - Cabu Remix','Dance Monkey','Uptown Funk (feat. Bruno Mars)','Sugar','Girls Like You (feat. Cardi B)','Ice Cream (with Selena Gomez)','Useless','Roar','The Lazy Song']
    neutral=['Heathens','Attention','Theres Nothing Holdin Me Back','Believer','Galway Girl','Faded','Symphony (feat. Zara Larsson)','Fight Song','Rockabye (feat. Sean Paul & Anne-Marie)','Shape of You','Something Just Like This','Treat You Better','Thunder']
    sad=['Get You The Moon (feat. SnÃ¸w)','Jocelyn Flores','Someone You Loved','how to live','Its You','Loosing Interest','Tell Me Goodbye','Dead and Cold','Heather','Reckless','paradise','Me Too','Six Feet Under']
    surprize=['good 4 u','Todo De Ti','MONTERO (Call Me By Your Name)','Yonaguni','Kiss Me More (feat. SZA)','Beggin','deja vu','Butter','Levitating (feat. DaBaby)','Peaches (feat. Daniel Caesar & Giveon)','I WANNA BE YOUR SLAVE','traitor','QuÃ© MÃ¡s Pues?','happier','Save Your Tears (with Ariana Grande) (Remix)']
    if label == 'Neutral':
        x = random.choice(neutral)
        return x
                
    elif label == 'Angry':
        x = random.choice(angry)
        return x

    elif label == 'Disgust':
        x = random.choice(disgusted)
        return x

    elif label == 'Fear':
        x = random.choice(fearful)
        return x
    
    elif label == 'Happy':
        x = random.choice(happy)
        return x

    elif label == 'Sad':
        x = random.choice(sad)
        return x
    elif label == 'Surprise':
        x = random.choice(surprize)
        return x

def suggest_book(label):
    angry=['The Art of War','The Count of Monte Cristo','Autobiography of Yogi','Tween Snow Fire','A Tale of Two Cities Walden','Anne of Green gables','The Story of My life','The Picture Of Dorian Gray','Acres Of Diamonds']
    disgusted=['The Communist Manifesto','Macbeth','The Age Of reason','Siddhartha','The Sense Of Beauty','The Analects of Confucius','Palmistry for all','The Analysis of Mind','Analysing Character','The Bhabavad Gita','Meditations']
    fearful=['the call of cthulhu','The Best Ghost Stories','Dracula','the invisible man','Collected Works of Poe','The Woman In white','The Phantom Of the Opera','Clarimonde','Grimms Fairy Tales','Metamorphosis','The After House']
    happy=['Emma','The 300 Beequest','adventures of huckleberry finn','Three men in a boat','the importance of Being Earnest','the CanterVille ghost','eves Diary','the hackers Dictionary','Pygmalion','a comedy of errors in seven acts','An ideal Husband']
    neutral=['The Arabian Nights Entertainments','The Arabian Nights Entertainments','Stories By German Authors','the book of thousand Nights and One Night','Cindrella','seven icelandic s','Love and Friendship and other Early Works','the grim smile of the five towns','Winesburg,ohio','the moon endureth','can such things be']
    sad=['cranford','Criminal Sociology','The Rubaiyat of Omar Khayam','North of Boston','The Golden Sayings of Epictetus','Prufrock and Other Observsations','Sidelights on Relativity','Fables for the frivolous','The Hunting of the Snark','The Orgin and nature of emotions']
    surprize=['The Arabian Nights Entertainments','The Atomic Bombings ','Stammering its cause and cure','Hunger','The Psychology of Revolution','The Moon Endureth','Chess History And Reminiscences','Beasts of Tarzan','Jungle Tales Of Tarzon','Tarzon and the Jewels of Opar']
    if label == 'Neutral':
        x = random.choice(neutral)
        return x
                
    elif label == 'Angry':
        x = random.choice(angry)
        return x

    elif label == 'Disgust':
        x = random.choice(disgusted)
        return x

    elif label == 'Fear':
        x = random.choice(fearful)
        return x
    
    elif label == 'Happy':
        x = random.choice(happy)
        return x

    elif label == 'Sad':
        x = random.choice(sad)
        return x
    elif label == 'Surprise':
        x = random.choice(surprize)
        return x



############### FUNCTION CAPTURE ########################

def capture(option):
    face_classifier = cv2.CascadeClassifier(r'C:\Users\shiva\OneDrive\Desktop\major\book reccomendation system/haarcascade_frontalface_default.xml')
    classifier =load_model(r'C:\Users\shiva\OneDrive\Desktop\major\book reccomendation system/model.h5')

    emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']

    cap = cv2.VideoCapture(0)



    FLAG = 1
    while FLAG:
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
                cv2.imshow('Emotion Detector',frame)

                val = ''
                
                if option == 'MOVIE':
                    val = suggest_movie(label)

                elif option == 'SONG':
                    val = suggest_song(label)

                elif option == 'BOOK':
                    val = suggest_book(label)
                    
                print(val)
                return val
                
            
            else:
                cv2.putText(frame,'No Faces',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        
        FLAG = 0
        if cv2.waitKey(0) & 0xFF == ord('q'):
            exit()

    cap.release()
    cv2.destroyAllWindows()

    


######### FUNCTIONS FOR BUTTONS ###########

def recommend_movie():
    res = capture('MOVIE')

    book_lbl = Label(window, text = "The MOVIE that you can see right now is : ")
    book_lbl.place(x = 100, y = 500)
    book_lbl.configure(font=("Montserrat Bold", 18 * -1),fg="#171435")


    book_suggested = Label(window, text = res)
    book_suggested.place(x = 450, y = 500)
    book_suggested.configure(font=("Montserrat Bold", 20 * -1),fg="red")
    

def recommend_song():
    res = capture('SONG')

    book_lbl = Label(window, text = "The SONG that you can listen read right now is : ")
    book_lbl.place(x = 100, y = 500)
    book_lbl.configure(font=("Montserrat Bold", 18 * -1),fg="#171435")


    book_suggested = Label(window, text = res)
    book_suggested.place(x = 450, y = 500)
    book_suggested.configure(font=("Montserrat Bold", 20 * -1),fg="red")

def recommend_book():
    res = capture('BOOK')

    book_lbl = Label(window, text = "The BOOK that you can read right now is : ")
    book_lbl.place(x = 100, y = 500)
    book_lbl.configure(font=("Montserrat Bold", 18 * -1),fg="#171435")


    book_suggested = Label(window, text = res)
    book_suggested.place(x = 450, y = 500)
    book_suggested.configure(font=("Montserrat Bold", 20 * -1),fg="red")




############ WINDOW ################

window = Tk()
window.geometry("770x750")



lbl = Label(window, text = "Recommendation System")
lbl.place(x = 200, y = 50)
lbl.configure(font=("Montserrat Bold", 26 * -1),fg="#171435")


select_type = Label(window, text = "Select any of these things")
select_type.place(x = 0, y = 150)
select_type.configure(font=("Montserrat Bold", 18 * -1),fg="#171435")



## MOVIE
btn = Button(window, text = "MOVIE",command = recommend_movie )
#command = capture
btn.place(x = 150, y = 200)
btn.configure(font=("Montserrat Bold", 24 * -1),fg="#171435")

##SONG
btn = Button(window, text = "SONG", command = recommend_song )
#command = capture
btn.place(x = 300, y = 200)
btn.configure(font=("Montserrat Bold", 24 * -1),fg="#171435")

##BOOK
btn = Button(window, text = "BOOK", command = recommend_book )
#command = capture
btn.place(x = 450, y = 200)
btn.configure(font=("Montserrat Bold", 24 * -1),fg="#171435")



window.mainloop()










