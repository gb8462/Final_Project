import os
import time

def clean():
    os.system('cls')

def load():
    for i in range(2):
        print("Loading", end='', flush=True)
        time.sleep(0.5)
        
        clean()

        print("Loading .", end='', flush=True)
        time.sleep(0.5)
        
        clean()

        print("Loading ..", end='', flush=True)
        time.sleep(0.5)
        
        clean()

        print("Loading ...", end='', flush=True)
        time.sleep(0.5)
        
        clean()

    print("Loading ...", end='', flush=True)
    time.sleep(0.5)
    clean()

def exiting():
    for i in range(2):
        print("Exiting", end='', flush=True)
        time.sleep(0.5)
        
        clean()

        print("Exiting .", end='', flush=True)
        time.sleep(0.5)
        
        clean()

        print("Exiting ..", end='', flush=True)
        time.sleep(0.5)
        
        clean()

        print("Exiting ...", end='', flush=True)
        time.sleep(0.5)
        
        clean()

    print("Exiting ...", end='', flush=True)
    time.sleep(0.5)
    clean()