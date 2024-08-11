import datetime
import os
import webbrowser  # pip download webbrowser
import instaloader as instaloader
import pyautogui
from re import search
from keyboard import press, press_and_release
from pyautogui import click, write
from time import sleep
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
from bs4 import BeautifulSoup
from playsound import playsound
from pywikihow import search_wikihow
from speech_recognition import Microphone
from GoogleNews import GoogleNews
import phonenumbers


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()




def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning ")
        speak("have a nice day,")

    elif hour>=12 and hour<15:
        speak("good afternoon")

    elif hour>=15 and hour<19:
        speak("good eveing ")

    elif hour>=19 and hour<24:
        speak("Good night "
              "sweet Dreams")

def time():
    time=datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"the current time is {time}")
    print(",,,,,,,>",time)



def date():
    date=datetime.datetime.now().strftime("%D")
    speak(f"the current date is {date}")
    print(",,,,,,,,,>",date)


def takecommand():
    r=sr.Recognizer()
    source: Microphone
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)


    try:
        print("wait for few Moments")
        query=r.recognize_google(audio,language='en-in')
        print("user said", query)

    except Exception as e:
        print(e)
        query="nothing"
    return query




if __name__ == '__main__':
    wishme()
    time()
    date()
    speak("welcome Back")
    takecommand()





    while True:
        query=takecommand().lower()
        if "wake up in query":
            speak("yes tell me what can i do")

            while True:
                query = takecommand().lower()

                if 'wikipedia' in query or 'collect data' in query or 'data' in query:
                    try:
                        speak('searching in wikipedia sir...')
                        query = query.replace("wikipedia","")
                        results = wikipedia.summary(query, sentences=2)
                        speak("According to wikipedia")
                        speak(results)
                        print(results)
                    except Exception as e:
                        speak("there is no data")
                        pass
                elif 'open notepad' in query:
                    os.startfile("C:\\WINDOWS\\system32\\notepad")
                elif 'open powershell' in query:
                    speak("opening powershell")
                    os.startfile('C:\\Windows\\System32\\WindowsPowerShell\x0b1.0')
                elif 'temperature' in query:
                    try:
                        search = "temperature"
                        url = f"https://www.google.com/search?q={search}"
                        r = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div",class_ = "BNeawe").text
                        speak(f"current{search} is {temp}")
                    except Exception as e:
                        speak("sorry sir , due to network issue i am not able to find the temperature.")
                        pass

                elif 'Weather' in query:
                    try:
                        search = "Weather"
                        url = f"https://www.google.com/search?q={search}"
                        r = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        Weath = data.find("div",class_ = "BNeaWE").text
                        speak(f"current{search} is {Weath}")
                    except Exception as e:
                        speak("sorry sir , due to network issue i am not able to find the Weather.")
                        pass


                elif 'volume up' in query:
                    pyautogui.press("volumeup")
                elif 'volume down' in query:
                    pyautogui.press("volumedown")
                elif 'volume mute' in query:
                    pyautogui.press("volumemute")
                elif 'hello ' in query or 'hi ' in query:
                    speak("hello sir , how are you")
                elif 'open command prompt' in query or 'open cmd' in query:
                    speak("opening command prompt")
                    os.startfile("C:\\WINDOWS\\system32\\cmd")
                elif 'what is time now ' in query or 'what is time ' in query:
                    time()
                elif 'play next song' in query or 'play next song' in query:
                   musicdir = ("Enter the path where you located your songs")
                   songs = os.listdir(musicdir)
                   print(songs)
                   os.startfile(os.path.join(musicdir, songs[11]))
                elif 'open map' in query:
                    webbrowser.open_new_tab("https://www.google.com/maps")
                elif 'open mail' in query:
                    speak("opening mail ")
                    webbrowser.open_new_tab("https://mail.google.com")
                elif 'open google' in query:
                    speak("opening google ")
                    webbrowser.open_new_tab("https://google.com")
                elif 'open youtube' in query:
                    speak("opening youtube sir")
                    webbrowser.open_new_tab("https://youtube.com")
                if 'pause' in query or 'pass' in query:
                    press('space bar')

                elif 'resume' in query:
                    press('space bar')

                elif 'save' in query or 'save it' in query or 'save as' in query:
                    press_and_release('ctrl+S')

                elif 'full screen' in query:
                    press('t')

                elif 'skip' in query:
                    press('l')

                elif 'back' in query:
                    press('j')

                elif 'copy' in query:
                    press_and_release('ctrl+c')

                elif 'paste' in query:
                    press_and_release('ctrl+v')

                elif 'cut' in query:
                    press_and_release('ctrl+x')

                elif 'increase' in query:
                    press_and_release('shift +,')

                elif 'decrease' in query:
                    press_and_release('shift + ,')

                elif 'previous' in query:
                    press_and_release('shift + P')

                elif 'next' in query:
                    press_and_release('shift + N')

                elif 'search' in query:
                    click(x=667, y=146)

                    speak = takecommand()

                    write(search)

                    sleep(0.8)

                    press('enter')

                elif 'mute' in query:
                    press('m')

                elif 'unmute' in query:
                    press('m')

                elif 'go to search box' in query:
                    press('/')

                elif 'press 1' in query:
                    press('1')

                elif 'press 2' in query:
                    press('2')

                elif 'press 3' in query:
                    press('3')

                elif 'press 4' in query:
                    press('4')

                elif 'press 5' in query:
                    press('5')

                elif 'press 6' in query:
                    press('6')

                elif 'press 7' in query:
                    press('7')

                elif 'press 8' in query:
                    press('8')

                elif 'press 9' in query:
                    press('9')

                elif 'press 10' in query:
                    press('10')

                elif 'press 0' in query:
                    press('0')


                elif 'open chrome' in query:
                    speak("opening chrome")
                    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\Chrome")
                elif 'alarm' in query:
                    speak(" Enter The Time !")
                    Time = input(": Enter The Time :")

                    while True:
                        Time_Ac = datetime.datetime.now()
                        now = Time_Ac.strftime("%H:%M:%S")

                        if now == Time:
                            speak("Time To Wake Up Sir!")
                            playsound('iron.mp3')
                            speak("Alarm Closed!")

                        elif now>Time:
                            break
                elif "where i am" in query or "where we are" in query:
                    try:
                        search = "my location"
                        url = f"https://www.google.com/search?q={search}"
                        r = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        Loc = data.find("div",class_ = "BNeawe").text
                        print(Loc)
                    except Exception as e:
                        speak("sorry sir , due to network issue i am not able to find where we are.")
                        pass

                elif "take screenshot" in query or "take a screenshot" in query:
                    try:
                        speak("sir,please tell me the name for this screenshot file")
                        name = takecommand().lower()
                        speak("please sir hold the screen for few seconds, i am taking screenshot")
                        time.sleep(3)
                        img = pyautogui.screenshot()
                        img.save(f"{name}.png")
                        speak("i am done sir, the screenshot is saved in our folder")
                    except Exception as e:
                        speak("sorry sir , screenshot option is not able this computer.")
                        pass

                elif 'open google meet' in query:
                    speak("opening google meet sir")
                    webbrowser.open_new_tab("https://meet.google.com")
                elif "instagram profile" in query or "profile on instagram" in query:
                    try:
                        speak("sir please enter the user name correctly")
                        name = input("enter username here:" or takecommand())
                        webbrowser.open(f"www.instagram.com/{name}")
                        speak(f"sir here is here is the profile of the user {name}")
                        speak("sir would you like to download profile picture of this account")
                        condition = takecommand().lower()
                        if "yes" in condition:
                            mod = instaloader.Instaloader() #pip install instadowbloader
                            mod.download_profile(name, profile_pic_only=True)
                            speak("i am done sir, profile picture is saved in our main folder.")
                        else:
                            pass
                    except Exception as e:
                        speak("sorry sir , due to network issue i am not able to take the profile.")
                        pass
                elif 'play previous song ' in query or 'play previous song' in query:
                    musicdir = ("Enter the path where you located your songs")
                    songs = os.listdir(musicdir)
                    print(songs)
                    os.startfile(os.path.join(musicdir, songs[3]))



                elif 'play song ' in query or 'play song' in query:
                    musicdir = ("Enter the path where you located your songs")
                    songs = os.listdir(musicdir)
                    print(songs)
                    os.startfile(os.path.join(musicdir, songs[21]))

                elif 'play next song ' in query or 'play next song' in query:
                    musicdir = ("Enter the path where you located your songs")
                    songs = os.listdir(musicdir)
                    print(songs)
                    os.startfile(os.path.join(musicdir, songs[20]))

                elif 'change song ' in query or 'change the song' in query:
                    musicdir = ("Enter the path where you located your songs")
                    songs = os.listdir(musicdir)
                    print(songs)
                    os.startfile(os.path.join(musicdir, songs[50]))

                elif 'active how to do mode' in query:
                    speak("How to do mode is activated please tell me what you want to know sir")
                    how = takecommand()
                    max_results = 1
                    how_to = search_wikihow(how, max_results)
                    assert len(how_to) == 1
                    how_to[0].print()
                    speak(how_to[0].summary)


                elif 'how to' in query:
                    speak("Getting Data From The Internet  !")
                    op = query.replace("hi", "")
                    max_result = 1
                    how_to_func = search_wikihow(op, max_result)
                    assert len(how_to_func) == 1
                    how_to_func[0].print()
                    speak(how_to_func[0].summary)

                elif 'remember that' in query:
                    remeberMsg = query.replace("remember that","")
                    remeberMsg = remeberMsg.replace("remember","")
                    speak("You Tell Me To Remind You That :"+remeberMsg)
                    remeber = open('data.txt','w')
                    remeber.write(remeberMsg)
                    remeber.close()

                elif 'what do you remember' in query:
                    remeber = open('data.txt','r')
                    speak('You Tell Me That' + 'remeber')

                elif 'Where is Phone ' in query or '`trace phone number' in query:
                    from phonenumbers import geocoder
                    speak('tell me phone number to trace it')
                    number = takecommand()
                    ch_nmber = phonenumbers.parse(number, "CH")
                    print(geocoder.description_for_number(ch_nmber, "en"))
                    speak(ch_nmber)

                    from phonenumbers import carrier
                    service_nmber = phonenumbers.parse(number, "RO")
                    print(carrier.name_for_number(service_nmber, "en"))
                    speak(service_nmber)

                elif 'news update' in query or 'today news' in query:
                    googlenews = GoogleNews()
                    googlenews.get_news('Tech')
                    googlenews.result()
                    a = googlenews.gettext()
                    print(*a[1:5], sep=',')
                    speak(a+takecommand())
                    if 'wait' in query or 'stop' in query:
                        exit(a)

                elif 'quit' in query or 'stop' in query or 'exit' in query or 'power off' in query:
                    speak("quitting")
                    wishme()
                    speak("bye sir!")
                    quit()


