import speech_recognition as sr
import pyttsx3
import os
import cases
import whisper
import tempfile
import cases

def main():
    rec = sr.Recognizer()
    mic = sr.Microphone()

    source = mic.__enter__()

    engine = pyttsx3.init()

    # Load whisper model once
    model = whisper.load_model("base")  # tiny / base / small

    print("Preparing your mic please wait...")
    rec.adjust_for_ambient_noise(source, duration=1)

    while True:

        print("Listening...")
        audio = rec.listen(source)

        try:
            # Save microphone audio temporarily as WAV
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
                f.write(audio.get_wav_data())
                temp_audio_path = f.name

            # Transcribe using Whisper
            result = model.transcribe(temp_audio_path, language="mr")
            text = result["text"].strip()

            print(text.lower())

            cases.cases(text)

            rec.adjust_for_ambient_noise(source, duration=0.2)

            command = text.lower()
            if command == "exit":
                print("Okay, Good Bye")
                break

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()