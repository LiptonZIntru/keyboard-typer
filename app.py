from pynput.keyboard import Key, Controller
import time
import json
import random

keyboard = Controller()
config = json.loads(open("config.json", 'r').read())
min_speed = config['min_typing_speed']
max_speed = config['max_typing_speed']
execute_delay = int(config['startup_delay'])

for i in range(execute_delay):
    print("Program is executing in " + str(execute_delay - i - 1) + " seconds")

if(min_speed < max_speed):
    text = open('text.txt', 'r').read()
    for i in text:
        keyboard.type(i)
        time.sleep(random.randint(min_speed, max_speed) / 1000)
else:
    print("Config file error")
