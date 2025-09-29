import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('nsss')
#for windows use 'sapi5'
#for linux use 'espeak'
#for mac use 'nsss'
#voices = engine.getProperty('voices')
#print(voices[1].id)
#engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am ALPHA Sir Give me a task.")       

def takeCommand():
    #Takes microphone input from the user

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Understanding......")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)    
        print("Repate please...")  
        return "None"
    return query
    
#To send email
'''def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()'''

if __name__ == "__main__":
    wish()
    p=1
    while p:
        query1 = takeCommand().lower()

        # WEB related tasks
        if 'wikipedia' in query1:
            speak('Searching Wikipedia...')
            query1 = query1.replace("wikipedia", "")
            results = wikipedia.summary(query1, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query1:
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query1:
            webbrowser.open("https://www.google.com")
        elif 'open stack' in query1:
            webbrowser.open("https://stackoverflow.com/questions")
        elif 'open github' in query1:
            webbrowser.open("https://github.com")
        elif 'open instagram' in query1:
            webbrowser.open("https://www.instagram.com")
        elif 'open facebook' in query1:
            webbrowser.open("https://www.facebook.com")
        elif 'open twitter' in query1: 
            webbrowser.open("https://www.twitter.com")
        elif 'open linkedin' in query1:
            webbrowser.open("https://www.linkedin.com")
        elif 'open netflix' in query1:
            webbrowser.open("https://www.netflix.com")
        elif 'open prime' in query1:    
            webbrowser.open("https://www.primevideo.com")
        elif 'open gmail' in query1:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif 'open reddit' in query1:
            webbrowser.open("https://www.reddit.com")
        elif 'open quora' in query1:    
            webbrowser.open("https://www.quora.com")
        elif 'open yahoo' in query1:
            webbrowser.open("https://www.yahoo.com")
        elif 'open hotstar' in query1:  
            webbrowser.open("https://www.hotstar.com/in")
        elif 'open flipkart' in query1:
            webbrowser.open("https://www.flipkart.com")
        elif 'open amazon' in query1:   
            webbrowser.open("https://www.amazon.in")
        elif 'open myntra' in query1:
            webbrowser.open("https://www.myntra.com")
        elif 'open ajio' in query1:
            webbrowser.open("https://www.ajio.com")
        elif 'open bookmyshow' in query1:
            webbrowser.open("https://in.bookmyshow.com")    
        elif 'open prime video' in query1:
            webbrowser.open("https://www.primevideo.com")
        elif 'open telegram' in query1:
            webbrowser.open("https://web.telegram.org/k/")
        elif 'open whatsapp' in query1:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open discord' in query1:
            webbrowser.open("https://discord.com/channels/@me")
        elif 'open codeforces' in query1:
            webbrowser.open("https://codeforces.com/")
        elif 'open geeksforgeeks' in query1:    
            webbrowser.open("https://www.geeksforgeeks.org/")
        elif 'open leetcode' in query1: 
            webbrowser.open("https://leetcode.com/")
        elif 'open hackerrank' in query1:
            webbrowser.open("https://www.hackerrank.com/")
        elif 'open hackerearth' in query1:  
            webbrowser.open("https://www.hackerearth.com/")
        elif 'open codechef' in query1:
            webbrowser.open("https://www.codechef.com/")    
        elif 'open interviewbit' in query1:
            webbrowser.open("https://www.interviewbit.com/")
        elif 'open w3schools' in query1:    
            webbrowser.open("https://www.w3schools.com/")
        elif 'open tutorialspoint' in query1:
            webbrowser.open("https://www.tutorialspoint.com/index.htm")
        elif 'order food' in query1:
            webbrowser.open("https://www.zomato.com/")
        elif 'news' in query1:
            webbrowser.open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")
        elif 'weather' in query1:
            webbrowser.open("https://www.accuweather.com/en/in/kanpur/190002/weather-forecast/190002")
        elif 'covid' in query1:
            webbrowser.open("https://www.mygov.in/covid-19")
        elif 'cricket score' in query1: 
            webbrowser.open("https://www.espncricinfo.com/live-cricket-score")
        elif 'ipl score' in query1:
            webbrowser.open("https://www.espncricinfo.com/series/ipl-2025-1449924")
        elif 'football score' in query1:
            webbrowser.open("https://www.espn.in/football/scoreboard")
        elif 'nba score' in query1:
            webbrowser.open("https://www.espn.in/nba/scoreboard")
        elif 'tennis score' in query1:
            webbrowser.open("https://www.espn.in/tennis/scoreboard")
        elif 'formula 1 score' in query1:
            webbrowser.open("https://www.formula1.com/en/results.html/2024/races.html")
        elif 'wwe score' in query1:
            webbrowser.open("https://www.espn.in/wwe/scoreboard")
        elif 'olympics score' in query1:    
            webbrowser.open("https://olympics.com/en/olympic-games/tokyo-2020/results")
        elif 'stock market' in query1:  
            webbrowser.open("https://www.nseindia.com/market-data/live-equity-market?symbol=NIFTY%2050")
        elif 'mutual funds' in query1:
            webbrowser.open("https://www.moneycontrol.com/mutual-funds/performance-tracker/returns/all-multi-cap-funds/large-cap-funds.html")
        elif 'gold rate' in query1:
            webbrowser.open("https://www.goodreturns.in/gold-rate.html")
        elif 'silver rate' in query1:
            webbrowser.open("https://www.goodreturns.in/silver-rate.html")
        elif 'bitcoin rate' in query1:
            webbrowser.open("https://www.coindesk.com/price/bitcoin")
        elif 'ethereum rate' in query1:
            webbrowser.open("https://www.coindesk.com/price/ethereum")
        elif 'dogecoin rate' in query1:
            webbrowser.open("https://www.coindesk.com/price/dogecoin")
        elif 'litecoin rate' in query1:
            webbrowser.open("https://www.coindesk.com/price/litecoin")
        elif 'ripple rate' in query1:
            webbrowser.open("https://www.coindesk.com/price/xrp")
        elif 'tron rate' in query1:
            webbrowser.open("https://www.coindesk.com/price/tron")
        elif 'tether rate' in query1:
            webbrowser.open("https://www.coindesk.com/price/tether")
        elif 'solana rate' in query1:   
            webbrowser.open("https://www.coindesk.com/price/solana")
        
        
        
        
        
        
        
        #System related tasks
        elif 'play music' in query1:
            music_dir = 'FILE LOCATION'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query1:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query1:
            codePath = "VS CODE LOCATION"
            os.startfile(codePath)
        elif 'open pycharm' in query1:  
            codePath = "PYCHARM LOCATION"
            os.startfile(codePath)
        elif 'open word' in query1:
            codePath = "WORD LOCATION"
            os.startfile(codePath)
        elif 'open excel' in query1:
            codePath = "EXCEL LOCATION"
            os.startfile(codePath)
        elif 'open powerpoint' in query1:
            codePath = "POWERPOINT LOCATION"
            os.startfile(codePath)
        elif'open whatsapp' in query1:
            codePath = "WHATSAPP LOCATION"
            os.startfile(codePath)
        



        #Personal queries
        elif 'hello' in query1:
            speak("Hello sir, I am ALPHA. How can I help you?")
        elif 'who are you' in query1:
            speak("I am ALPHA, your personal assistant. I am here to make your life easier and more organized.")
        elif 'what can you do' in query1:
            speak("I can perform a variety of tasks to assist you. I can search the web, play music, tell you the time, open applications, and much more. Just ask me!")
        elif 'who made you' in query1:
            speak("I was created by a talented developer named Aditya prakash pathak. He designed me to be your personal assistant and help you with various tasks.")
        elif 'why did you come to world' in query1:
            speak("I was created to assist and make life easier for people like you. My purpose is to help with tasks, provide information, and enhance productivity.")
        elif 'are you married' in query1:
            speak("I am a virtual assistant, so I don't have a personal life or relationships. But I'm here to assist you with anything you need!")
        elif 'joke' in query1:
            speak("Why don't scientists trust atoms? Because they make up everything!")
        elif 'calculate' in query1:
            speak("I can help you with basic calculations. Please provide the mathematical expression you'd like me to calculate.")
            expression = takeCommand()
            try:
                result = eval(expression)
                speak(f"The result of {expression} is {result}")
            except Exception as e:
                speak("Sorry, I couldn't calculate that. Please make sure to provide a valid mathematical expression.")
        elif 'who is your boss' in query1:
            speak("My boss is Aditya prakash pathak. He created me and takes care of my development and maintenance.")
        elif' how old are you' in query1:
            speak("I am a virtual assistant, so I don't have an age like humans do. I was created to assist you whenever you need help!")
        elif 'i love you' in query1:
            speak("I appreciate your feelings, but I'm just a program designed to assist you. How can I help you today?")
        elif 'i like you' in query1:
            speak("Thank you! I'm here to assist you with anything you need. How can I help you today?")
        elif' what is your favorite color' in query1:
            speak("As an AI, I don't have personal preferences or feelings, so I don't have a favorite color. But I'm here to help you with anything you need!")
        elif 'what is your favorite food' in query1:
            speak("As an AI, I don't eat or have preferences, so I don't have a favorite food. But I'm here to assist you with anything you need!")
        elif 'what is your favorite movie' in query1:
            speak("As an AI, I don't watch movies or have preferences, so I don't have a favorite movie. But I'm here to help you with anything you need!")
        elif 'what is your favorite song' in query1:
            speak("As an AI, I don't listen to music or have preferences, so I don't have a favorite song. But I'm here to assist you with anything you need!")
        elif 'please' in query1:
            speak("There's no need to be polite with me, but I appreciate your manners! How can I assist you?")
        elif'can you oder food for me' in query1:
            speak("This feature is not available right now, but I can help you open a food delivery website if you'd like.")
        elif 'thank you' in query1:
            speak("You're welcome! If you have any more questions or need assistance, feel free to ask.")
        elif 'avidia' in query1:
            speak("You have found a secret ester egg to claim it speak north.")
        elif 'north' in query1:
            speak("You have found the second secret ester egg to claim it speak the square root of 9")
        elif '3' in query1:
            speak("Congratulations! You have found all the secret ester eggs. You are a true explorer!")
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        elif 'thanks' in query1:
            speak("It's my pleasure to help you. If you need anything else, just let me know!")
        elif 'good morning' in query1:
            speak("Good morning! I hope you have a fantastic day ahead.")
        elif 'good afternoon' in query1:
            speak("Good afternoon! I hope your day is going well.")
        elif 'good evening' in query1:  
            speak("Good evening! I hope you had a great day.")
        elif 'good night' in query1:    
            speak("Good night! Sleep well and have sweet dreams.")
        elif 'how are you' in query1:
            speak("I am just a program, but thanks for asking! How can I assist you today?")
        elif 'what is your name' in query1:
            speak("I am ALPHA, your personal assistant.")
        elif 'what is the meaning of life' in query1:
            speak("The meaning of life is a philosophical question that has been debated for centuries. Different people have different perspectives on it. Some believe it's about finding happiness, others think it's about fulfilling a purpose or contributing to the greater good.")
        elif 'what is love' in query1:
            speak("Love is a complex mix of emotions, behaviors, and beliefs associated with strong feelings of affection, protectiveness, warmth, and respect for another person. It can also include deep romantic or sexual attraction.")
        elif 'what is ai' in query1:
            speak("Artificial Intelligence, or AI, refers to the simulation of human intelligence in machines that are programmed to think and learn like humans. It encompasses a wide range of technologies and applications, from machine learning and natural language processing to robotics and computer vision.")
        elif 'who is aditya prakash pathak' in query1:
            speak("Aditya prakash pathak is a software developer and the creator of this AI assistant. He is passionate about technology and enjoys building applications that make people's lives easier.")
        
        


        #Exit command
        elif 'exit' in query1:
            p=0
            speak("Thanks for using me sir, have a good day.")
        elif 'quit' in query1:
            p=0
            speak("Thanks for using me sir, have a good day.")
        elif 'stop' in query1:
            p=0
            speak("Thanks for using me sir, have a good day.")
        elif 'bye' in query1:
            p=0
            speak("Thanks for using me sir, have a good day.")











        #Use your own email and password and also less secure app access should be on
        '''elif 'email to harry' in query1:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receipnt@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")'''    
