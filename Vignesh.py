import tkinter as tk
import os
# import pygame

try:
    import playsound
except ImportError:
    os.system("pip install playsound")

try:
    import speech_recognition as s_r
except ImportError:
    os.system("pip install SpeechRecognition")

try:
    from googletrans import Translator as Trans
except ImportError:
    os.system("pip install googletrans==4.0.0-rc1")

try:
    from gtts import gTTS as googleTranslatorService
except ImportError:
    os.system("pip install gTTS")
    
try:
    import pygame
except ImportError:
    os.system("pip install pygame")
# Rest of your code remains the same




lang_set = ['afrikaans', 'af', 'albanian', 'sq',
            'amharic', 'am', 'arabic', 'ar',
            'armenian', 'hy', 'azerbaijani', 'az',
            'basque', 'eu', 'belarusian', 'be',
            'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
            'bg', 'catalan', 'ca', 'cebuano',
            'ceb', 'chichewa', 'ny', 'chinese (simplified)',
            'zh-cn', 'chinese (traditional)',
            'zh-tw', 'corsican', 'co', 'croatian', 'hr',
            'czech', 'cs', 'danish', 'da', 'dutch',
            'nl', 'english', 'en', 'esperanto', 'eo',
            'estonian', 'et', 'filipino', 'tl', 'finnish',
            'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
            'gl', 'georgian', 'ka', 'german',
            'de', 'greek', 'el', 'gujarati', 'gu',
            'haitian creole', 'ht', 'hausa', 'ha',
            'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
            'hi', 'hmong', 'hmn', 'hungarian',
            'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',
            'id', 'irish', 'ga', 'italian',
            'it', 'japanese', 'ja', 'javanese', 'jw',
            'kannada', 'kn', 'kazakh', 'kk', 'khmer',
            'km', 'korean', 'ko', 'kurdish (kurmanji)',
            'ku', 'kyrgyz', 'ky', 'lao', 'lo',
            'latin', 'la', 'latvian', 'lv', 'lithuanian',
            'lt', 'luxembourgish', 'lb',
            'macedonian', 'mk', 'malagasy', 'mg', 'malay',
            'ms', 'malayalam', 'ml', 'maltese',
            'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
            'mn', 'myanmar (burmese)', 'my',
            'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
            'pashto', 'ps', 'persian', 'fa',
            'polish', 'pl', 'portuguese', 'pt', 'punjabi',
            'pa', 'romanian', 'ro', 'russian',
            'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
            'serbian', 'sr', 'sesotho', 'st',
            'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
            'slovak', 'sk', 'slovenian', 'sl',
            'somali', 'so', 'spanish', 'es', 'sundanese',
            'su', 'swahili', 'sw', 'swedish',
            'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
            'te',  'telugu',
            'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
            'ug', 'uzbek', 'uz',
            'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
            'yiddish', 'yi', 'yoruba',
            'yo', 'zulu', 'zu']



def takeInput(inp):
    r1 = s_r.Recognizer()
    with s_r.Microphone() as source:
        print("listening to the voice...")
        r1.pause_threshold = 1
        audio = r1.listen(source)

    try:
        print("Recognizing the voice...")
        task = r1.recognize_google(audio, language=inp)
        print(f"user said? {task}\n")
    except Exception as ep:
        print("The user is requested to please say that again...")
        return "Please click on the translate and speak button agian"
    return task


def destination_language():
    lang_to_be_converted = input("Please enter the language in which you want to convert the above input \
    : Ex. English, Hindi, German, French etc.")
    return lang_to_be_converted

def translate_and_speak():
    input_language = input_lang_entry.get()
    if input_language in lang_set:
        input_language = lang_set[lang_set.index(input_language) + 1]
    destination_language = dest_lang_entry.get()
    if destination_language in lang_set:
        destination_language = lang_set[lang_set.index(destination_language) + 1]
    text_to_translate = takeInput(input_language)

    # Translate the text
    translator = Trans()
    translated_text = translator.translate(text_to_translate, dest=destination_language).text

    input_text.delete(1.0,tk.END)
    input_text.insert(tk.END,text_to_translate)

    # Display the translated text in the GUI
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, translated_text)

    # Save the translated text to an audio file
    sound_path="first.mp3"
    speak = googleTranslatorService(text=translated_text, lang=destination_language, slow=False)


    sound = googleTranslatorService(translated_text, lang=destination_language)
    sound.save(sound_path)

    # Load and play the audio using pygame
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Close the pygame file
    pygame.mixer.quit()

    # Remove the first.mp3 file
    os.remove(sound_path)



# Rest of your code remains the same


# Create the main GUI window
root = tk.Tk()
root.title("Language Translator and Speech Synthesis")

# Input Language Label and Entry
input_lang_label = tk.Label(root, text="Input Language:")
input_lang_label.pack()

input_lang_entry = tk.Entry(root)
input_lang_entry.pack()

# Destination Language Label and Entry
dest_lang_label = tk.Label(root, text="Destination Language:")
dest_lang_label.pack()

dest_lang_entry = tk.Entry(root)
dest_lang_entry.pack()

# Translate Button
translate_button = tk.Button(root, text="Translate and Speak", command=translate_and_speak)
translate_button.pack()

# Input Text Label and Text Area
input_text_label = tk.Label(root, text="Input Text:")
input_text_label.pack()

input_text = tk.Text(root, height=5, width=50)
input_text.pack()

# Output Text Label and Text Area
output_text_label = tk.Label(root, text="Translated Text:")
output_text_label.pack()

output_text = tk.Text(root, height=5, width=50)
output_text.pack()

root.mainloop()