# Import libraries
import os
from gtts import gTTS as google_text_to_speech


def text_to_speech():
    '''
    define language as English
    Ask user for text to be converted
    Ask user for what to save file to  
    build object of google text to speech class
    save object to mp3 file
    save object to wav file
    informational message
    standard function return
    '''
    language = 'en'
    
    print('\nwrite text you want converted', end=': ')
    your_text = input()
    
    print('name wav file', end=': ')
    filename = input()
    mp3 = filename + '.mp3'
    wav = filename + '.wav'

    noise_obj = google_text_to_speech(text=your_text, lang=language, slow=False)

    noise_obj.save(mp3)
    noise_obj.save(wav)

    print('\n' + mp3 + ' successfully built')
    print(wav + ' successfully built')

    return


# Call text to speech function
text_to_speech()