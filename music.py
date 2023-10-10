import pygame
import os

# Initialize Pygame
pygame.init()

# Create a function to play music
def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Main loop
while True:
    print("Simple Music Player")
    print("1. Play Music")
    print("2. Stop Music")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        music_file = input("Enter the path to the music file: ")
        if os.path.exists(music_file):
            play_music(music_file)
        else:
            print("File not found.")
    elif choice == "2":
        pygame.mixer.music.stop()
    elif choice == "3":
        pygame.mixer.quit()
        pygame.quit()
        break
    else:
        print("Invalid choice. Please try again.")
