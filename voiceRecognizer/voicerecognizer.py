import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()


with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

response = r.recognize_google(audio)
print(response)

if(response == 'hello'):
    print("hello to you my friend how are u today ?")