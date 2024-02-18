import speech_recognition as sr
from googletrans import Translator

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the translator
translator = Translator()

# Load the audio file (replace 'your_audio_file.wav' with the path to your audio file)
with sr.AudioFile("your_audio_file.wav") as source:
    # Adjust for ambient noise
    recognizer.adjust_for_ambient_noise(source)
    
    print("Transcribing audio...")

    # Record the audio
    audio_data = recognizer.record(source)

    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio_data, language="hi-IN")  # Hindi language code: hi-IN
        print("Hindi:", text)

        # Translate Hindi to English
        translation = translator.translate(text, src="hi", dest="en")
        print("English:", translation.text)

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error fetching results; {0}".format(e))
