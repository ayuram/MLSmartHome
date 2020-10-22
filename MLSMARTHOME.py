from sprw.io import Assistant, exceptions, IOT
from gpiozero import Button, LED, MCP3008, Motor, RGBLED
from signal import pause
from time import sleep
 
sp_server= IOT('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjBmMmZhY2EyZDc0YWY5ZGNiZjNjMDczYTdiZGNmZTJlMjBmYWUxMjhiODAyMDUzZDU4MjQxNjY5ZDNjOGM2OGNhMGQxZWNkM2RkZjE2M2FmIn0.eyJhdWQiOiIzIiwianRpIjoiMGYyZmFjYTJkNzRhZjlkY2JmM2MwNzNhN2JkY2ZlMmUyMGZhZTEyOGI4MDIwNTNkNTgyNDE2NjlkM2M4YzY4Y2EwZDFlY2QzZGRmMTYzYWYiLCJpYXQiOjE1NjI4MjU1NTEsIm5iZiI6MTU2MjgyNTU1MSwiZXhwIjoxNTk0NDQ3OTUxLCJzdWIiOiIxOTY3MCIsInNjb3BlcyI6W119.Y2kkNWWjoHjRJhkKGYSb8OvCDMzwhc4KWxA1jX7cw5rxTwc4rfhNQkeDA4h38TtaEjH3BXBNNpePQXvHYj750BkLeSkva1bv75kKYlQ7mIFkzNL3W74GrqZQ7ni2yeqiaF9VwiYWfFw2OAlSPsV7dDlTh-N2uViq2110jrjUUR0_PgoRs2A725QkuLfXxfHcfjQVKexEcA6heN_iSUIJOVn1kZ4SXFrdsvMkBFW_TlBNBNJqmKnkgkkqjOPH8XjyRPHvGcS0xMVMBhc-9MscgznKcunX2s-MhNV5I1hmta7vYO_d6bHuuyZgztZOvA0yFFjulemg97rV2BqhlzF0gTvJf4l7TjJOzbBPEqohKWmJbBIqW9-eQkB1ln-pN-W9pbGyp48KfYD-zemM9dX97q_y9z5KLClhdJL-lc71JMqNvwvT9f8C-HukPsUHhzOhGRiDzSVbpkZe9-3SQ9OBRn5LBqhAP4ohoxkCWCn1XETZlOd4JDU15e35bAWspw_ktqzhM8ZvenfBCjRXq_8YObfVBG0gUuTk8J3TO3oHIXhPkzg5pP2jjlbgdOjlA7c6QC4-aRxyYrA-0EJpWDXk0NOnbzqHQBfPQqmSCIBaTjptsM9HdVxbVf0Js5151FBu936DOSIh3D77yLii4JuytToHNzoreddXp_4Kzr1J2A0')

jarvis=  Assistant('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjBmMmZhY2EyZDc0YWY5ZGNiZjNjMDczYTdiZGNmZTJlMjBmYWUxMjhiODAyMDUzZDU4MjQxNjY5ZDNjOGM2OGNhMGQxZWNkM2RkZjE2M2FmIn0.eyJhdWQiOiIzIiwianRpIjoiMGYyZmFjYTJkNzRhZjlkY2JmM2MwNzNhN2JkY2ZlMmUyMGZhZTEyOGI4MDIwNTNkNTgyNDE2NjlkM2M4YzY4Y2EwZDFlY2QzZGRmMTYzYWYiLCJpYXQiOjE1NjI4MjU1NTEsIm5iZiI6MTU2MjgyNTU1MSwiZXhwIjoxNTk0NDQ3OTUxLCJzdWIiOiIxOTY3MCIsInNjb3BlcyI6W119.Y2kkNWWjoHjRJhkKGYSb8OvCDMzwhc4KWxA1jX7cw5rxTwc4rfhNQkeDA4h38TtaEjH3BXBNNpePQXvHYj750BkLeSkva1bv75kKYlQ7mIFkzNL3W74GrqZQ7ni2yeqiaF9VwiYWfFw2OAlSPsV7dDlTh-N2uViq2110jrjUUR0_PgoRs2A725QkuLfXxfHcfjQVKexEcA6heN_iSUIJOVn1kZ4SXFrdsvMkBFW_TlBNBNJqmKnkgkkqjOPH8XjyRPHvGcS0xMVMBhc-9MscgznKcunX2s-MhNV5I1hmta7vYO_d6bHuuyZgztZOvA0yFFjulemg97rV2BqhlzF0gTvJf4l7TjJOzbBPEqohKWmJbBIqW9-eQkB1ln-pN-W9pbGyp48KfYD-zemM9dX97q_y9z5KLClhdJL-lc71JMqNvwvT9f8C-HukPsUHhzOhGRiDzSVbpkZe9-3SQ9OBRn5LBqhAP4ohoxkCWCn1XETZlOd4JDU15e35bAWspw_ktqzhM8ZvenfBCjRXq_8YObfVBG0gUuTk8J3TO3oHIXhPkzg5pP2jjlbgdOjlA7c6QC4-aRxyYrA-0EJpWDXk0NOnbzqHQBfPQqmSCIBaTjptsM9HdVxbVf0Js5151FBu936DOSIh3D77yLii4JuytToHNzoreddXp_4Kzr1J2A0')
b1 = Button(23)
b2 = Button(24)
l2 = LED(25)
l1 = LED(22)
m1 = Motor(26, 19)
rgb = RGBLED(18,12,13)
temp = MCP3008(channel = 7)
jarvis.microphone_device_index = 2
now = jarvis.get_current_datetime
daysubtract = 0
z = 0

l1keywords = [' light one ', ' light ', ' LED ', ' LEDS ']
l2keywords = [' light two ', ' light ', ' LED ', ' LEDS ']


motorkeywords = ['motor', 'rotor']

onkeywords = ['turn on', 'switch on', 'start', 'on']
offkeywords = ['turn off', 'switch off', 'stop', 'off']
devices = {0 : m1, 1 : l1, 2 : l2}


jarvis.speak("Ready", 'Brian')
def spokenday():
    global day
    global now
    global daysubtract
    global monthdays
    yester =  now.day - daysubtract
    tens = int((yester)/10)
    tenth = yester/10
    if(tenth <= 2):
        if(yester == 0):
            day = (str(monthdays) + "th")
        elif(yester == 1):
            day = "first"
        elif(yester == 2):
            day = "second"
        elif(yester == 3):
            day = "third"
        elif(yester >= 4):
            day = (str(yester) + "th")
    if(tenth > 2):
        difference = now.day - tens*10
        if(difference == 1):
            day = str(tens*10) + "first"
        elif(difference == 2):
            day = str(tens*10) + "second"
        elif(difference == 3):
            day = str(tens*10) + "third"
        else:
            day = (str(now.day) + "th")
    if(yester < 0):
        tens = int((monthdays + yester)/10)
        tenth = (monthdays + yester)/10
        nowdays = monthdays + yester
        if(tenth >= 2):
            if((nowdays - (tens*10)) == 1):
                day = str(tens*10) + "first"
            elif((nowdays - (tens*10)) == 2):
                day = str(tens*10) + "second"
            elif((nowdays - (tens*10)) == 3):
                day = str(tens*10) + "third"
            else:
                day = str(nowdays) + "th"
        else:
            if(nowdays == 1):
                day = "first"
            elif(nowdays == 2):
                day = "second"
            elif(nowdays == 3):
                day == "third"
            elif(nowdays >= 4):
                day = str(nowdays) + "th"
                
                
def monthdays():
    global monthdays
    global now
    prevmonth = now.month - 1
    if(prevmonth % 2 ==0):
        if(prevmonth != 2):
            monthdays = 30
        elif(prevmonth == 2):
            if(now.year % 4 == 0):
                monthdays = 29
            else:
                monthdays = 28
    else:
        monthdays = 31
def pulse():
    global rgb
    rgb.pulse(fade_in_time=2, fade_out_time=2, on_color=(1,0,0), off_color = (0,0,0), n=None, background=True)
def speak():
    global rgb
    rgb.pulse(fade_in_time=1, fade_out_time=1, on_color=(1,0,1), off_color = (0,0,0), n=None, background=True)
def idle():
    global rgb
    rgb.pulse(fade_in_time=10, fade_out_time=10, on_color=(0,0,0), off_color = (0,0,0), n=None, background=True)
while True:
    temperature = int((temp.value*150) - 3)
    lightkeywords = ['lights'] + l1keywords + l2keywords
    idle()
    if(b1.value == 1):
        try:
            pulse()
            text = jarvis.recognize_speech(language = 'en-US')
            print(text)
            now = jarvis.get_current_datetime()
        
            month = jarvis.get_month_in_words(now.month)
            fetch_time = now - jarvis.datetime_offset(minutes = 10)
            
            

            if any(word in text for word in onkeywords) or any(word in text for word in offkeywords):     
                if any(word in text for word in lightkeywords):
                    if any(word in text for word in l1keywords):
                        if any (word in text for word in onkeywords):
                            l1.on()
                            
                        elif(' off ' in text):
                            l1.off()
                            
                    elif any(word in text for word in l2keywords):
                        if any (word in text for word in onkeywords):
                            l2.on()
                            
                        elif(' off ' in text):
                            l2.off()
                    else:
                        if any (word in text for word in onkeywords):
                            l2.on()
                            l1.on()
                        elif(' off ' in text):
                            l2.off()
                            l1.off()
                elif any(word in text for word in motorkeywords):
                    if any(word in text for word in onkeywords):
                        m1.forward()
                       
                    elif any(word in text for word in offkeywords):
                        m1.stop()
                        
                        
                else:
                    numbergen = 0
                    p = False
                    for numbergen in range(0, (len(devices))):
                        if(p == False):
                            z = devices.get(numbergen)
                            if(z == l1):
                                objectname = "l1"
                            elif(z == l2):
                                objectname = "l2"
                            elif(z == m1):
                                objectname = "m1"
                            greaterline = "Did you mean to ask me to adjust " + objectname
                            speak()
                            jarvis.speak(greaterline, 'Brian')
                            sleep(2)
                            if(b1.value == 1) and ('the' in text):
                                newtext = text.split(' the ')
                                print(newtext[1])
                                p = True
                                if(z == l1):
                                    l1keywords.insert(0, str(newtext[1]))
                                elif(z == l2):
                                    l2keywords.insert(0, str(newtext[1]))
                                if(z == m1):
                                    motorkeywords.insert(0, str(newtext[1]))
                                    if any(word in text for word in onkeywords):
                                        z.forward()
                                    elif any(word in text for word in offkeywords):
                                        z.stop()
                                elif(z != m1):
                                    if('turn on' in text) or ('switch on' in text): 
                                        z.on()
                                    elif('turn off' in text) or('switch off' in text):
                                        z.off()
                                if(z == m1):
                                    motorkeywords.insert(0, str(newtext[1]))
                                sleep(1)
                            elif(b1.value == 1):
                                newtext = text.split( )
                                textlength = len(newtext)
                                meantnumber = textlength - 1
                                print(newtext[meantnumber])
                                #for later
                                p = True
                                if(z == l1):
                                    l1keywords.insert(0, str(newtext[meantnumber]))
                                elif(z == l2):
                                    l2keywords.insert(0, str(newtext[meantnumber]))
                                if(z == m1):
                                    motorkeywords.insert(0, str(newtext[meantnumber]))
                                    if any(word in text for word in onkeywords):
                                        z.forward()
                                    elif any(word in text for word in offkeywords):
                                        z.stop()
                                elif(z != m1):
                                    if('turn on' in text) or ('switch on' in text): 
                                        z.on()
                                    elif('turn off' in text) or('switch off' in text):
                                        z.off()
                                sleep(1)
                            else:
                                numbergen = numbergen + 1
                        else:
                            numbergen = len(devices)
                        
                            
                                

                    
            if ('temperature' in text) or ('weather' in text) or ('hot' in text) or ('cool' in text):
                line = "The room temperature is " + str(temperature) + " degrees celsius."
                speak()
                jarvis.speak(line, 'Brian')



                
            if('reminder' in text) and ('set' in text):
                time = jarvis.get_datetime_from_text(text)
                if('remind me to' in text):
                    sentence = text.split('remind me to')
                    reminder_message = sentence[1]
                else:
                    reminder_message = "You're supposed to be doing something right now"
                new_reminder = {'name': 'Reminder from speech', 'time':time, 'message': reminder_message, 'status':'ACTIVE'}
                sp_server.update_thing_multi_state_attributes(thing_id= 1581, reminder = new_reminder)
                jarvis.speak("Reminder set!", 'Brian')
                if(now.minute - fetch_time.minute >= 10 or now.minute-fetch_time.minute < 0):
                    condition = {
                'time' : jarvis.get_current_datetime() - jarvis.datetime_offset(hours = 2),
                'status' : 'ACTIVE'
                }
                    virtual_assistant = sp_server.get_thing_multi_state_attributes(thing_id = 1581, reminder_condition = condition)
                    fetch_time = now
                for reminder in virtual_assistant.reminders:
                    if now >= reminder.time and reminder.status == 'ACTIVE':
                        speak()
                        jarvis.speak(reminder.message, 'Brian')
                        reminder.status = 'DISMISSED'
                        sp_server.update_thing_multi_state_attributes(thing_id = 1581, reminder = reminder)
                        sleep(1)


            if('day' in text) or ('date' in text):
                    
                if('day before yesterday' in text):
                    daysubtract = 2
                    spokenday()
                    spokenx = "Day before yesterday was the " + str(day) + " of " + str(month)
                    speak()    
                    jarvis.speak(spokenx, 'Brian')
                elif('days before yesterday' in text):
                    daysmeant = text.split( )
                    dayvalue = daysmeant.index('days') - 1
                    daysubtract = int(daysmeant[dayvalue]) + 1
                    spokenday()
                    spokenx = "That day was the " + str(day) + " of " + str(month)
                    speak()    
                    jarvis.speak(spokenx, 'Brian')
                elif('days before today' in text):
                    daysmeant = text.split( )
                    dayvalue = daysmeant.index('days') - 1
                    daysubtract = int(daysmeant[dayvalue])
                    spokenday()
                    spokenx = "That day was the " + str(day) + " of " + str(month)
                    speak()
                    jarvis.speak(spokenx, 'Brian')
                elif('today'in text) or ("today's" in text):
                    daysubtract = 0
                    spokenday()
                    spokenx = "Today is the " + str(day) + " of " + str(month)
                    speak()
                    jarvis.speak(spokenx, 'Brian')
                
                elif('yesterday' in text) or ("yesterday's"):
                    daysubtract = 1
                    spokenday()
                    spokenx = "Yesterday was the " + str(day) + " of " + str(month)
                    speak()
                    jarvis.speak(spokenx, 'Brian')
                else:
                    daysubtract = 0
                    spokenday()
                    spokenx = "Today is the " + str(day) + " of " + str(month)
                    speak()
                    jarvis.speak(spokenx, 'Brian')
                    
        except exceptions.SpeechRecognitionError as error:
            jarvis.speak("Repeat that", 'Brian')
            print(error)
pause()
            
        
