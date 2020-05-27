#for executing the alert commands
from subprocess import Popen, check_output
#for setting up custom timer
from threading import Timer

#GLOBAL VARIABLES
__version__ = '0.1.2'
m=0
s=0
msg=''


def inform(sound_duration=0.5, notification=True, popup=True, message='Your process has completed!'):
    '''
    This method sends an alert on the screen when it gets executed.
    This method would come handy when you're working on something (a piece of code) which runs for a long time and you would like to be notified when it completes.
    An alert (sound, popup window and notification box) be sent when this method executes.
    Placing it right after the 'time consuming' piece of code would enable know 
    duration (in seconds): how long to generate the sound
    alert (bool): show the popup alert window if true, else do not show the popup window 
    '''
    try:
        #make a sound
        check_output(['( speaker-test -t sine -f 1000 )& pid=$! ; sleep '+str(sound_duration)+'s ; kill -9 $pid'], shell=True)

        #notification box
        if notification:
            Popen(['notify-send','Notification from inform_me', message])

        #popup message
        if popup:
            Popen(['zenity --info --text '+'\''+message+'\''+' --title \'Popup message from inform_me\' --width \'250\' --height \'50\' 2> /dev/null'], shell=True)
    
    except Exception as e:
        print('An error occured.\n',e)


#helper mehtod for notify_after method.
def timer():
    message=msg if msg else 'Your '+str(m)+' Minutes and '+str(s)+' Seconds timer has lapsed!'
    inform(message = message)


def inform_after(seconds=10, minutes=0, notification=True, popup=True, message=None):
    '''
    This function sends an alert (sound, popup window and notification box) when the after the specified time.
    This method can be used as a timer.
    '''
    try:
        total_sec = (minutes*60) + seconds
        t = Timer(total_sec, timer)
        t.start()
        global m
        m = minutes
        global s
        s = seconds
        global msg
        msg = message
    
    except Exception as e:
        print('An error occured.\n',e)

