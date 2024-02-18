# DARGPH-speech-to-text



---

**Speech-to-Text Translator**

This Python script utilizes the `speech_recognition` library to transcribe speech from an audio file (in this case, assumed to be in Hindi) and then translates the transcription into English using the `googletrans` library.

**Description:**
- The script initializes a speech recognizer and a translator object.
- It loads an audio file and adjusts for ambient noise.
- The audio data is recorded and then recognized using Google Speech Recognition with the language set to Hindi (hi-IN).
- If successful, the recognized Hindi text is translated to English using the `googletrans` library.
- Finally, the original Hindi text and its English translation are printed.

**Usage:**
- Replace `"your_audio_file.wav"` with the path to the actual audio file you want to transcribe and translate.

**Dependencies:**
- `speech_recognition`
- `googletrans`

**Note:**
- Ensure that the required audio file is in a format supported by `speech_recognition`.
- Internet connectivity is required for using Google Speech Recognition and Google Translate services.

---
