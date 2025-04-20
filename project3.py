import pygame
import time
import random
import  os
import  math

pygame.mixer.init(frequency= 22050, size = -16, channels = 1,buffer = 512)

emotion_notes = {
    "happy":[440,494,523,587,659,698,784],
    "sad": [261,293,311,349,415,466],
    'angry':[220,233,246,261,277,393,311],
    "relaxed":[220,294,330,349,392]
    }

def generate_melody(emotion,length=8):
    notes = emotion_notes.get(emotion.lower(),emotion_notes["happy"])
    MELODY = [random.choice(notes) for _ in range(length)]
    return MELODY

def play_tone(frequency,duration= 300):
    sample_rate = 44100
    n_sample = int(round(duration*sample_rate/1000))
    buf = bytearray()


    for s in range(n_sample):
        t= float(s)/sample_rate
        value = int(32767*0.5*math.sin(2.0*math.pi*frequency*t))
        buf += value.to_bytes(2,byteorder = "little",signed = True)
    

    sound = pygame.mixer.Sound(buffer = buf)
    sound.play()
    time.sleep(duration/1000)

def ascii_wave(frequency,duration):
    os.system("cls" if os.name == "nt" else "clear")
    width = 40
    samples = int(frequency/20)
    for _ in range(samples):
        amp = int((width/2)* random.random())
        print(''* amp + '*')
        time.sleep(duration/(samples *1000))


def main():
    emotion = input("Enter an emotion (HAPPY,SAD,ANGRY,RELAXED):").strip().lower()

    print(f"\n Generating melody for emotion.{emotion}\n)") 
    melody = generate_melody(emotion)


    for note in melody:
        play_tone(note)
        ascii_wave(note,300)


print("\n Melody complete!")

if  __name__ == "__main__":
    main()
