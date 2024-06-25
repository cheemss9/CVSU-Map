from tkinter import *
import tkinter
import pyttsx3
import webbrowser
#import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
#import os
#import sys
#import pygame
from PIL import ImageTk, Image
#import csv


root = Tk()
root.title('GIS CHATBOT WITH VOICE RECOGNITION')
root.config(background='black')
root.geometry('1480x710')
root.resizable(1, 1)


img= ImageTk.PhotoImage(Image.open("ADMIN.jpg"))
img1 = ImageTk.PhotoImage(Image.open('ccj.jpg'))
img2 =ImageTk.PhotoImage(Image.open('BioSci.jpg'))
img4=ImageTk.PhotoImage(Image.open('CAFENR.jpg'))
img5=ImageTk.PhotoImage(Image.open('CAS.jpg'))
img6=ImageTk.PhotoImage(Image.open('ced.jpg'))
img7=ImageTk.PhotoImage(Image.open('CEMDS.jpg'))
img8=ImageTk.PhotoImage(Image.open('CIVIL.jpg'))
img9=ImageTk.PhotoImage(Image.open('CONN.jpg'))
img10=ImageTk.PhotoImage(Image.open('DCEE.jpg'))
img11=ImageTk.PhotoImage(Image.open('DIT.jpg'))
img12=ImageTk.PhotoImage(Image.open('Dorm.jpg'))
img13=ImageTk.PhotoImage(Image.open('grandstand.jpg'))
img14=ImageTk.PhotoImage(Image.open('gym.jpg'))
img15=ImageTk.PhotoImage(Image.open('Highschool.jpg'))
img16=ImageTk.PhotoImage(Image.open('house2.jpg'))
img17=ImageTk.PhotoImage(Image.open('infirmary.jpg'))
img18=ImageTk.PhotoImage(Image.open('library.jpg'))
img19=ImageTk.PhotoImage(Image.open('MARKETING.jpg'))
img20=ImageTk.PhotoImage(Image.open('OSAS.jpg'))
img21=ImageTk.PhotoImage(Image.open('PHYSCI.jpg'))
img22=ImageTk.PhotoImage(Image.open('QUAD.jpg'))
img23=ImageTk.PhotoImage(Image.open('ROlle.jpg'))
img24=ImageTk.PhotoImage(Image.open('Saliysoy.jpg'))
img25=ImageTk.PhotoImage(Image.open('Umall.jpg'))
img26=ImageTk.PhotoImage(Image.open('VET.jpg'))
img27 =ImageTk.PhotoImage(Image.open('Untitleddesign.png'))
img28 = ImageTk.PhotoImage(Image.open('malayakana.png'))
img29 = ImageTk.PhotoImage(Image.open('threed.png'))

engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('JW6Y7Q-GKWVR76AJG')
voices = engine.getProperty('voices')

#Na class na 
def speak(audio):
    print('' + audio)
    engine.setProperty('voice', voices[len(voices) - 3].id)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')




def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
  
    try:
        
        query = r.recognize_google(audio, language='en-in')
        print('You: ' + query + '\n')
        

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Please speak again!')
        pass

    return query

#def Find_Student():
    
##def Stundent_number():
##    
##
##    mtext = ment.get()
##    csv_file = csv.reader(open('C:/Users/Vince/OneDrive/Desktop/attachments/allcvsustudents.csv','r'))
##    for row in csv_file:
##        if mtext == row[1]:
##            a = row
##            
##    #mlabel2 = Label(mGui, text = mtext).pack()
##    mlabel3 = Label(mGui, text = a).pack()
##    print (mtext)
##    return mlabel3
##
##
##mGui = Tk()
##ment = StringVar()
##
##mGui.geometry('300x200')
##mGui.title('Student Section')
##
##mlabel = Label(mGui, text = 'Enter your Student Number').pack()
##
##mbutton = Button (mGui, text = 'OK', command= Stundent_number, fg = 'black', bg = 'green').pack()
##
##mEntry = Entry(mGui, textvariable = ment).pack()
        

#Different window
class Tkinter_interface():

    def __init__(self):

       #vince = Stundent_number
       self.FlashText = StringVar()
       self.FlashText.set('VINCE GALLARDO')
       compFrame = LabelFrame(root, text="CHATBOT", font=('Times New Roman', 10, 'bold'))
       compFrame.pack(fill="both", expand="yes")
       label = Label(root, image = img27).place(x=1, y = 15)
       label = Label(root, image = img28).place(x=1, y = 110)
       label = Label(root, image = img27).place(x=1210, y = 15)
       label = Label(root, image = img28).place(x=1210, y = 110)
       label = Label(root, image = img29).place(x=145, y = 17)
       #label = Label(root, image = img1).place(x=155, y = 110)
       left1 = Message(compFrame, textvariable=self.FlashText, bg='black',fg='white')
       left1.config(font=("Comic Sans MS", 10, 'bold'))
       left1.pack(fill='both', expand='yes')
       btn = Button(root, text='Click here to start the voice speech!', font=('Black ops one', 10, 'bold'), bg='blue', fg='white', command=self.clicked).pack(fill='x', expand='no')
       #btn1 =Button(root, text = 'Click here to find a student', font=('Black ops one',10, 'bold'), bg ='black', fg= 'white', command =vince).pack(fill ='x', expand='no')
       btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), bg='black', fg='white', command=root.destroy).pack(fill='x', expand='no')
      
        

       speak('Hello Sir, I am your digital assistant')
       speak('How may I help you?')
       self.FlashText.set('Hello, What should I do for You?')
       root.bind("<Return>", self.clicked)
       
       root.mainloop()

##    def Find_Student(self):
##        
##       def Stundent_number():
##            
##
##            mtext = ment.get()
##            csv_file = csv.reader(open('C:/Users/Vince/OneDrive/Desktop/attachments/allcvsustudents.csv','r'))
##            for row in csv_file:
##                if mtext == row[1]:
##                    a = row
##    
##            #mlabel2 = Label(mGui, text = mtext).pack()
##            mlabel3 = Label(mGui, text = a).pack()
##            return mlabel3
##
##
##       mGui = Tk()
##       ment = StringVar()
##
##       mGui.geometry('300x200')
##       mGui.title('Student Section')
##
##       mlabel = Label(mGui, text = 'Enter your Student Number').pack()
##
##       mbutton = Button (mGui, text = 'OK', command= Stundent_number, fg = 'black', bg = 'green').pack()
##
##       mEntry = Entry(mGui, textvariable = ment).pack()
##        
        
#ikaclass   
    def clicked(self):
        label = Label(root, image = img29).place(x=145, y = 17)
        print('Working')
        query = myCommand()
        ('Listening...')
        query = query.lower()
        
   
        if 'please introduce your name' in query or 'introduce yourself' in query or ' first of all introduce your self' in query:
            #label = Label(root, image = img27, text = 'vincepogi').place(x=100, y = 80)
            available_answer = [('Again I am your Digital Assistant Alternatively referred to as a virtual digital assitance, I am computer program designed to assist a user by answering questions and performing basic tasks.')]
            self.FlashText.set(available_answer)
            speak(random.choice(available_answer))
        elif 'find the location of admin' in query or 'location of admin' in query or 'admin' in query:
            #admin
            label = Label(root, image = img).place(x=155, y = 110)
            speak('here is the College Administration')
        elif 'find the location of college of biological sciences' in query or 'where is the college of biological sciences' in query:
            #biosci
            label = Label(root, image = img2).place(x=155, y = 110)
            speak('here is the College of Biological sciences')
        elif 'find the location of college of agriculture forestry environment and natural resources' in query or 'find the location of cafenr' in query or 'where is the college of agriculure of forestry environement and natural resources' in query:
            #cafenr
            label = Label(root, image = img4).place(x=155, y = 110)
            speak('here is the College of Agriculture forestry, Environment and natural resources ')
        elif 'find the location of college of arts and sciences' in query or 'find the location of cas' in query or 'where is the college of arts and sciences' in query:
            #cas
            label = Label(root, image = img5).place(x=155, y = 110)
            speak('here is the College of Arts and Sciences')
        elif 'find the location of college of education' in query or 'find the location of ced' in query or 'where is the college of education' in query:
            #ced
            label = Label(root, image = img6).place(x=155, y = 110)
            speak('here is the College of Education')
        elif 'find the location of cemds' in query or 'find the location of college of economics management and development studies' in query or 'where is the college of economics management and development studies' in query:
            #cemds
            label = Label(root, image = img7).place(x=155, y = 110)
            speak('here is the College of Criminal Justice')
        elif 'find the location of deparment of civil engineering' in query or 'where is the department of civil engineering' in query:
            #civil
            label = Label(root, image = img8).place(x=155, y = 110)
            speak('here is the Deparment of Civil Engineering')
        elif 'find the location of con' in query or 'find the location of college of nursing' in query or 'where is the college of nursing' in query:
            #con
            label = Label(root, image = img9).place(x=155, y = 110)
            speak('here is the College of Nursing')
        elif 'find the location of department of electronics and computer engineering' in query or 'where is the department of electronics and computer engineering' in query:
            #dcee
            label = Label(root, image = img10).place(x=155, y = 110)
            speak('here is the Department of Electronics and Computer Engineering')
        elif 'find the location of department of information technology' in query or 'where is the department of information technology' in query:
            #dit
            label = Label(root, image = img11).place(x=155, y = 110)
            speak('here is the Department of Information Technology')
        elif 'find the location of dormitory' in query or 'find the location of dorm' in query or 'dorm' in query or 'where is the dormitory' in query:
            #dorm
            label = Label(root, image = img12).place(x=155, y = 110)
            speak('here is the location of dormitory')
        elif 'find the location of grandstand' in query or 'grandstand' in query :
            #admin
            label = Label(root, image = img13).place(x=155, y = 110)
            speak('here is the location of Grandstand')
        elif 'find the location of gym' in query or 'find the location of gymnasium' in query or 'where is the gymnasium' in query:
            #gym
            label = Label(root, image = img14).place(x=155, y = 110)
            speak('here is the location of Gymnasium')
        elif 'find the location of highshool' in query or 'where is the highschool' in query:
            #higschool
            label = Label(root, image = img15).place(x=155, y = 110)
            speak('here is the Location of Highschool')
        elif 'find the location of international house' in query or 'where is the international house' in query:
            #international house
            label = Label(root, image = img16).place(x=155, y = 110)
            speak('here is the International House')
        elif 'find the location of infirmary' in query or 'where is  the infirmary' in query:
            #infirmary
            label = Label(root, image = img17).place(x=155, y = 110)
            speak('here is the Infirmary')
        elif 'find the location of library' in query or 'where is the library' in query:
            #location library
            label = Label(root, image = img18).place(x=155, y = 110)
        elif 'find the location of marketing' in query or 'where is the marketing' in query:
            #marketing
            label = Label(root, image = img19).place(x=155, y = 110)
            speak('here is the Marketing')
        elif 'find the location of osas' in query or 'find the location of office of student affairs and services' in query or 'where is the office of student affairs and services' in query:
            #osa
            label = Label(root, image = img20).place(x=155, y = 110)
            speak('here is the lacation of student affairs and services')
        elif 'find the location of physci' in query or 'find the location of department of physical science' in query or 'where is the department of physical science' in query:
            #physci
            label = Label(root, image = img21).place(x=155, y = 110)
            speak('here is the Department of Physical Sciences')
        elif 'find the location of quad' in query or 'find the location of quadrangle' in query or 'where is the quadrangle' in query:
            #quad
            label = Label(root, image = img22).place(x=155, y = 110)
            speak('here is the Quadrangle')
        elif 'find the location of rolle' in query or 'find the location of rolle hall' in query or 'where is the rolle hall' in query:
            #rolle
            label = Label(root, image = img23).place(x=155, y = 110)
            speak('here is Rolle Hall')
        elif 'find the location of saluysoy' in query:
            #saluysoy
            label = Label(root, image = img24).place(x=155, y = 110)
            speak('here is the College of Saluysoy')
        elif 'find the location of umall' in query or 'find the location university mall' in query or 'where is the university mall' in query:
            #umall
            label = Label(root, image = img25).place(x=155, y = 110)
            speak('here is the University Mall')
        #elif 'students in college of veterinary and biomedical sciences' in query or 'how many students are there in college of veterinary and biomedical sciences' in query:
            
        elif 'find the location of vet' in query or 'find the location of college of veterinary and biomedical sciences' in query or 'college of veterinary and biomedical sciences' in query:
            #vet
            label = Label(root, image = img26).place(x=155, y = 110)
            speak('here is the College of Veterinary and Biomedical Sciences')                       
        elif 'find the location of college of criminal justice' in query or 'college of criminal justice' in query:
            #ccj
            label = Label(root, image = img1).place(x=155, y = 110)
            speak('here is the College of Criminal Justice')
        #courses in ceit
        elif 'what is the available courses in college of engineering and information technology' in query or 'available courses in college of engineering and infortion technology' in query:
            speak('Thank you very much sir! Here is the result')
            speak('The available courses in college of engineering and information technology are: ')
        #courses in con
        elif 'what is the available courses in college of nursing' in query or 'available courses in college of nursing' in query:
            speak('Thank you very much sir! Here is the result')
            speak('The available courses in college of nursing are: ')
            
        #courses in cafenr
        elif 'what is the available courses in college of agriculture forestry environment and natural resources' in query or 'available courses in college of agriculture forestry environment and natural resources' in query:
            speak('Thank you very much sir! Here is the result')
            speak('The available courses in college of agriculture forestry environment and natural resources are: ')
            
        #courses in cas
        elif 'what is the available courses in college of arts and sciences' in query or 'available courses in college of arts and sciences' in query:
            speak('Thank you very much sir! Here is the result')
            speak('The available courses in college of arts and sciences are: ')
            
        #courses in ccj
        elif 'what is the available courses in college of criminal justice' in query or 'available courses in college of criminal justice' in query:
            speak('Thank you very much sir! Here is the result')
            speak('The available courses in college of criminal justice are: ')
            
        #courses in ced
        elif 'what is the availbale courses in college of education' in query or 'available courses in college of education' in query:
            speak('Thank you very much sir! Here is the result')
            speak('The available courses in college of education are: ')
            
        #courses in cemds
        elif 'what is the available courses in college of economics management and development studies' in query or 'college of economics management and development studies' in query:
            speak('Thank you very much sir! Here is the result')
            speak('The available courses in college of economics management and development studies are: ')
            
        #courses in cvmbs
        elif 'what is the available courses in college of veterinary and biomedical sciences' in query or 'available courses in college of veterinary and biomedical sciences' in query:
            speak('Thank you very much sir! Here is the result')
            speak('The available courses in college of veterinry medecine and biomedical sciences are: ')
            
        elif "what\'s up" in query or 'how are you' in query:
            available_answer = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            #self.FlashText.set(random.choice(available_answer))
            speak(random.choice(available_answer))

        elif "who's my instructor" in query or "who's my teacher" in query or "who's my favorite teacher" in query:
            available_answer = ['Sir Joven Ramos!', 'Mr. Joven Ramos']
            #self.FlashText.set(random.choice(available_answer))
            speak (random.choice(available_answer))
                
        elif "who made this program" in query or "who made you" in query:
            available_answer = ['This Program was made by: Vince Gallardo, Ceasar Operiano, James Eneria, Larry Simoun Palattao, and Leonard Mangayao']
            #self.FlashText.set(available_answer)
            speak (random.choice(available_answer))

        elif "what is my name" in query:
            speak("I don't know your name, but I know that Vince Gallardo and His Team Made me to fullfil the needs of humans")
            #self.FlashText.set("I don't know your name, but I know that Vince Gallardo and His Team Made me to fullfil the needs of humans")
        
        elif "what is the date today" in query:
            now = datetime.datetime.now()
            speak(now.strftime("%y-%m-%d "))
            #self.FlashText.set(now.strftime("%y-%m-%d "))
        
            
        elif 'tell me the time today' in query or 'tell me the time' in query:
            now = datetime.datetime.now()
            speak(now.strtime("%H:%M:%S"))
            #self.FlashText.set(now.strtime("%H:%M:%S"))
         
            
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            self.FlashText.set('Okay')
            speak('okay')
            #self.FlashText.set('Bye Sir, have a good day.')
            speak('Bye Sir, have a good day.')
            sys.exit()
            
        elif 'hello' in query:
            #self.FlashText.set('Hello Sir')
            speak('Hello Sir')

        elif 'bye' in query:
            #self.FlashText.set('Bye Sir, have a good day.')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'play a music' in query:
            music_folder = 'C:\\Users\\Vince\\OneDrive\\Desktop\\musicnoone\\'
            music = ['music1']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
            #self.FlashText.set('Okay, here is your music! Enjoy!')
            speak('Okay, here is your music! Enjoy!')

        else:
            query = query
            speak('Wait a minute sir')

            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    #self.FlashText.set(results)
                    speak('Got it.')

                    speak(results)

                        

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    self.FlashText.set(results)
                    speak(results)

            

            except:
                webbrowser.open('www.google.com')

        speak('Next Command! Sir!')

##    def Find_Student(self):
##            
##        def Stundent_number():
##                
##
##            mtext = ment.get()
##            csv_file = csv.reader(open('C:/Users/Vince/OneDrive/Desktop/attachments/allcvsustudents.csv','r'))
##            for row in csv_file:
##                if mtext == row[1]:
##                    a = row
##        
##                #mlabel2 = Label(mGui, text = mtext).pack()
##            mlabel3 = Label(mGui, text = a).pack()
##            return mlabel3
##
##
##        mGui = Tk()
##        ment = StringVar()
##
##        mGui.geometry('300x200')
##        mGui.title('Student Section')
##
##        mlabel = Label(mGui, text = 'Enter your Student Number').pack()
##
##        mbutton = Button (mGui, text = 'OK', command= Stundent_number, fg = 'black', bg = 'green').pack()
##
##        mEntry = Entry(mGui, textvariable = ment).pack()
                        


##if __name__ == '__main__':
##
##    greetMe()
##
##    widget = Tkinter_interface()
##    
##    
