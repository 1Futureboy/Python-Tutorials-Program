# Text To Speech With Internal Sound Of System Code

# importing speechrecognition for converting a voice into text
import speech_recognition as sr


r=sr.Recognizer()

# Here You Put Your Audio File Path
audio=("put here audio file path")

with sr.AudioFile(audio) as source:
    print("Say Something")
    audio=r.record(source)  # recording a voice 
    print("done")

try:
    text=r.recognize_google(audio)
    print(text) # printing a voice into text

except Exception as e:
    print(e)








# Text To Speech With Microphone Code


# importing speechrecognition for converting a voice into text
import speech_recognition as sr


r=sr.Recognizer()

# Here You Put Your Audio File Path
audio=("put here audio file path")

with sr.Microphone(audio) as source:
    print("Say Something")
    audio=r.audio(source)  # listen Your a voice 
    print("done")

try:
    text=r.recognize_google(audio)
    print(text) # printing a voice into text

except Exception as e:
    print(e)


