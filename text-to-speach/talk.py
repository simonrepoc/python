# import the pyttsx module inside program
import pyttsx3

# initializing the module
engine = pyttsx3.init()


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1


"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[10].id)   #changing index, changes voices. 1 for female

''' RATE '''
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

# .say() function is used to speak the text you have written 
# inside the function
with open('song.txt') as f:
	song = f.readlines()
engine.say(song)

# this is used to process and run the program commands
engine.runAndWait()