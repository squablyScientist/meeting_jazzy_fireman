import os, random, pygame, time

def playRandomFile():
    file_name = random.choice(os.listdir("../audio"))
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(os.getcwd()[:-3] + "audio/" + file_name)
    pygame.mixer.music.play()
    time.sleep(5)
    pygame.mixer.music.stop()


playRandomFile()
