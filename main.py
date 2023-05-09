import time

import speech_recognition as sr
import openai
import pyttsx3
import sounddevice as sd
import keyboard

# Set up microphone input
r = sr.Recognizer()
mic = sr.Microphone()

# Set up text-to-speech engine
engine = pyttsx3.init()

# Set up OpenAI API credentials
openai.api_key = "skZO"

# Define a function to generate a response from OpenAI
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100 ,
        n=1,
        stop=None,
        temperature=0.2,
    )
    return response.choices[0].text.strip()




# Define a function to play speech output
def play_audio(audio_data, sample_rate):
    sd.play(audio_data, sample_rate, blocking=True)

# Main loop to listen for user commands and generate responses

engine.say("Welcome to harvis , your personal AI , ask me anything")
engine.runAndWait()
with mic as source:
    while True:
        try:
            print("Listening for command...")
            audio = r.listen(source)
            command = r.recognize_google(audio)
            print(command)
            if command == "cancel that":
                break
            elif command == "what are my plans for today" or command == "my schedules for today":
                print("loop entered")
                with open("sched.txt",'r') as schedules:
                    engine.say(schedules.read())
                    engine.runAndWait()
                continue


            print("reading")
            print(f"hari: {command}")
            response = generate_response(command)
            print(f"Harvis: {response}")
            engine.say(response)
            engine.runAndWait()


        except sr.UnknownValueError:
            print("Could not understand command")
            engine.say("Could not understand that ,please say clearly")
            engine.runAndWait()
        if keyboard.is_pressed("q"):
            print("Exiting...")
            break
