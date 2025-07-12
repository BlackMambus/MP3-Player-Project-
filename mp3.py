import tkinter as tk
from tkinter import filedialog
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Create the main window
root = tk.Tk()
root.title("Python MP3 Player")
root.geometry("400x200")

# Global variable to track pause state
paused = False

# Function to load an MP3 file
def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if file_path:
        pygame.mixer.music.load(file_path)
        song_label.config(text=os.path.basename(file_path))
        play_button.config(state="normal")
        pause_button.config(state="normal")
        stop_button.config(state="normal")

# Function to play the loaded song
def play_music():
    pygame.mixer.music.play()

# Function to pause/resume music
def pause_music():
    global paused
    if not paused:
        pygame.mixer.music.pause()
        pause_button.config(text="Resume")
        paused = True
    else:
        pygame.mixer.music.unpause()
        pause_button.config(text="Pause")
        paused = False

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()

# GUI Elements
song_label = tk.Label(root, text="No song loaded", font=("Arial", 12))
song_label.pack(pady=10)

load_button = tk.Button(root, text="Load MP3", command=load_file)
load_button.pack(pady=5)

play_button = tk.Button(root, text="Play", command=play_music, state="disabled")
play_button.pack(pady=5)

pause_button = tk.Button(root, text="Pause", command=pause_music, state="disabled")
pause_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_music, state="disabled")
stop_button.pack(pady=5)

# Run the application

