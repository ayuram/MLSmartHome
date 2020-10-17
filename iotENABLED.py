from sprw.io import IOT, Assistant
from time import sleep
from gpiozero import LED, Button, Motor, MCP3008, PWMLED, RGBLED, DigitalInputDevice

sp_server =  IOT('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjBmMmZhY2EyZDc0YWY5ZGNiZjNjMDczYTdiZGNmZTJlMjBmYWUxMjhiODAyMDUzZDU4MjQxNjY5ZDNjOGM2OGNhMGQxZWNkM2RkZjE2M2FmIn0.eyJhdWQiOiIzIiwianRpIjoiMGYyZmFjYTJkNzRhZjlkY2JmM2MwNzNhN2JkY2ZlMmUyMGZhZTEyOGI4MDIwNTNkNTgyNDE2NjlkM2M4YzY4Y2EwZDFlY2QzZGRmMTYzYWYiLCJpYXQiOjE1NjI4MjU1NTEsIm5iZiI6MTU2MjgyNTU1MSwiZXhwIjoxNTk0NDQ3OTUxLCJzdWIiOiIxOTY3MCIsInNjb3BlcyI6W119.Y2kkNWWjoHjRJhkKGYSb8OvCDMzwhc4KWxA1jX7cw5rxTwc4rfhNQkeDA4h38TtaEjH3BXBNNpePQXvHYj750BkLeSkva1bv75kKYlQ7mIFkzNL3W74GrqZQ7ni2yeqiaF9VwiYWfFw2OAlSPsV7dDlTh-N2uViq2110jrjUUR0_PgoRs2A725QkuLfXxfHcfjQVKexEcA6heN_iSUIJOVn1kZ4SXFrdsvMkBFW_TlBNBNJqmKnkgkkqjOPH8XjyRPHvGcS0xMVMBhc-9MscgznKcunX2s-MhNV5I1hmta7vYO_d6bHuuyZgztZOvA0yFFjulemg97rV2BqhlzF0gTvJf4l7TjJOzbBPEqohKWmJbBIqW9-eQkB1ln-pN-W9pbGyp48KfYD-zemM9dX97q_y9z5KLClhdJL-lc71JMqNvwvT9f8C-HukPsUHhzOhGRiDzSVbpkZe9-3SQ9OBRn5LBqhAP4ohoxkCWCn1XETZlOd4JDU15e35bAWspw_ktqzhM8ZvenfBCjRXq_8YObfVBG0gUuTk8J3TO3oHIXhPkzg5pP2jjlbgdOjlA7c6QC4-aRxyYrA-0EJpWDXk0NOnbzqHQBfPQqmSCIBaTjptsM9HdVxbVf0Js5151FBu936DOSIh3D77yLii4JuytToHNzoreddXp_4Kzr1J2A0')
jarvis=  Assistant('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjBmMmZhY2EyZDc0YWY5ZGNiZjNjMDczYTdiZGNmZTJlMjBmYWUxMjhiODAyMDUzZDU4MjQxNjY5ZDNjOGM2OGNhMGQxZWNkM2RkZjE2M2FmIn0.eyJhdWQiOiIzIiwianRpIjoiMGYyZmFjYTJkNzRhZjlkY2JmM2MwNzNhN2JkY2ZlMmUyMGZhZTEyOGI4MDIwNTNkNTgyNDE2NjlkM2M4YzY4Y2EwZDFlY2QzZGRmMTYzYWYiLCJpYXQiOjE1NjI4MjU1NTEsIm5iZiI6MTU2MjgyNTU1MSwiZXhwIjoxNTk0NDQ3OTUxLCJzdWIiOiIxOTY3MCIsInNjb3BlcyI6W119.Y2kkNWWjoHjRJhkKGYSb8OvCDMzwhc4KWxA1jX7cw5rxTwc4rfhNQkeDA4h38TtaEjH3BXBNNpePQXvHYj750BkLeSkva1bv75kKYlQ7mIFkzNL3W74GrqZQ7ni2yeqiaF9VwiYWfFw2OAlSPsV7dDlTh-N2uViq2110jrjUUR0_PgoRs2A725QkuLfXxfHcfjQVKexEcA6heN_iSUIJOVn1kZ4SXFrdsvMkBFW_TlBNBNJqmKnkgkkqjOPH8XjyRPHvGcS0xMVMBhc-9MscgznKcunX2s-MhNV5I1hmta7vYO_d6bHuuyZgztZOvA0yFFjulemg97rV2BqhlzF0gTvJf4l7TjJOzbBPEqohKWmJbBIqW9-eQkB1ln-pN-W9pbGyp48KfYD-zemM9dX97q_y9z5KLClhdJL-lc71JMqNvwvT9f8C-HukPsUHhzOhGRiDzSVbpkZe9-3SQ9OBRn5LBqhAP4ohoxkCWCn1XETZlOd4JDU15e35bAWspw_ktqzhM8ZvenfBCjRXq_8YObfVBG0gUuTk8J3TO3oHIXhPkzg5pP2jjlbgdOjlA7c6QC4-aRxyYrA-0EJpWDXk0NOnbzqHQBfPQqmSCIBaTjptsM9HdVxbVf0Js5151FBu936DOSIh3D77yLii4JuytToHNzoreddXp_4Kzr1J2A0')

L1 = LED(22)
B1 = Button(24)
M1 = Motor(26,19)
ldr = MCP3008(channel = 6)
temp = MCP3008(channel = 7)
RGB = RGBLED(18,12,13)
ir = DigitalInputDevice(16)

received = False
Mreceived = False
prevdirect = 'BACKWARD'
now = jarvis.get_current_datetime()
fetch_time = now - jarvis.datetime_offset(minutes = 10)

while True:
    now = jarvis.get_current_datetime()
    
    L1_virtual = sp_server.get_thing_state_attributes(1571)
    RGB_virtual = sp_server.get_thing_state_attributes(1580)
    
    if(L1.value != L1_virtual.value):        
        L1.value = L1_virtual.value
        received = True
        

    if B1.value ==1:
        L1.value = 1
        M1.forward()
        prevdirect = 'FORWARD'
        sp_server.update_thing_state_attributes(1573, value = B1.value)
        sp_server.update_thing_state_attributes(1571, value = L1.value)
        sp_server.update_thing_state_attributes(1575, direction = 'FORWARD')
        received = False
        Mreceived = False
    elif B1.value == 0 and received == False and Mreceived == False:
        L1.value = 0
        M1.backward()
        prevdirect = 'BACKWARD'
        sp_server.update_thing_state_attributes(1573, value = B1.value)
        sp_server.update_thing_state_attributes(1571, value = L1.value)
        sp_server.update_thing_state_attributes(1575, direction = 'BACKWARD')

    temperature =  (temp.value*150) -3
    sp_server.update_thing_state_attributes(1579, value = temperature)
    
    if ldr.value <0.05:
        sp_server.update_thing_state_attributes(1578, value = 0)
    else:
        sp_server.update_thing_state_attributes(1578, value = 1)
        
    M1_virtual = sp_server.get_thing_state_attributes(1575)
    if(prevdirect != M1_virtual.direction):
        if(M1_virtual.direction == 'FORWARD'):
            M1.forward()
            
            Mreceived = True
        elif(M1_virtual.direction == 'BACKWARD'):
            M1.backward()
            Mreceived = True
        else:
            M1.stop()
            Mreceived = True    
        prevdirect = M1_virtual.direction
    if(now.minute - fetch_time.minute >= 10 or now.minute-fetch_time.minute < 0):
        condition = {
            'time' : jarvis.get_current_datetime() - jarvis.datetime_offset(hours = 2),
            'status' : 'ACTIVE'
            }
        virtual_assistant = sp_server.get_thing_multi_state_attributes(thing_id = 1581, reminder_condition = condition)
        fetch_time = now
    for reminder in virtual_assistant.reminders:
        if now >= reminder.time and reminder.status == 'ACTIVE':
            jarvis.speak(reminder.message)
            reminder.status = 'DISMISSED'
            sp_server.update_thing_multi_state_attributes(thing_id = 1581, reminder = reminder)
            sleep(1)
        
    sleep(1)

    

    

    


