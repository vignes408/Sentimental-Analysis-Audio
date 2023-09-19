from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print('Clearing Background Noise....')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print('Waiting for the message')
    recordedaudio=recognizer.listen(source)
    print('Done recording')
try:
    print("Message")
    text=recognizer.recognize_google(recordedaudio,language='en-us')
    print('Your Message:{}'.format(text))
except Exception as ex:
    print(ex)

Sentence=[str(text)]
analyzer=SentimentIntensityAnalyzer()
for i in Sentence:
    v=analyzer.polarity_scores(i)
    print(v)