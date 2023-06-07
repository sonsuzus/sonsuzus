import pyttsx3 as tts

def main():
    engine = tts.init()
    text = input('Which word or sentence do you want to spell?: ')
    mode = input('slow mode or fast mode (s/f)?: ')
    if mode == 's':
        for i in text.upper():
            engine.say(i)
            engine.runAndWait()
    elif mode == 'f':
        organized_text = ' '.join(list(text.upper()))
        engine.say(organized_text)
        engine.runAndWait()
    engine.stop()

if __name__ == '__main__':
    main()