# Import necessary modules
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import pygame

# Step 1: Initialize the mixer
pygame.mixer.init()

# Step 2: Create the main application window
root = tk.Tk()
root.title("🎵 Tamil Music Player - by Nuwahf")
root.geometry("500x400")
root.config(bg="#1e1e2e")  # dark background

# Step 3: Create playlist list
playlist = []

# Step 4: Function to load songs from folder
def load_songs():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        playlist.clear()
        listbox.delete(0, tk.END)
        # Supported audio extensions
        supported_exts = ('.mp3', '.m4a', '.wav', '.aac', '.ogg')
        for file in os.listdir(folder_selected):
            if file.lower().endswith(supported_exts):
                playlist.append(os.path.join(folder_selected, file))
                listbox.insert(tk.END, file)
        if playlist:
            listbox.selection_set(0)  # select first song by default


# Step 5: Function to play selected song
def play_song():
    try:
        selected_index = listbox.curselection()[0]
        song_path = playlist[selected_index]
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        status_label.config(text="▶️ Playing: " + os.path.basename(song_path))
    except IndexError:
        messagebox.showwarning("Select Song", "Please select a song to play.")

# Step 6: Function to pause or unpause
is_paused = False
def pause_resume_song():
    global is_paused
    if is_paused:
        pygame.mixer.music.unpause()
        status_label.config(text="▶️ Resumed")
        is_paused = False
    else:
        pygame.mixer.music.pause()
        status_label.config(text="⏸️ Paused")
        is_paused = True

# Step 7: Function to stop music
def stop_song():
    pygame.mixer.music.stop()
    status_label.config(text="⏹️ Stopped")

# Step 8: Play next song
def next_song():
    try:
        selected_index = listbox.curselection()[0]
        next_index = (selected_index + 1) % len(playlist)
        listbox.selection_clear(0, tk.END)
        listbox.selection_set(next_index)
        play_song()
    except:
        pass

# Step 9: Play previous song
def prev_song():
    try:
        selected_index = listbox.curselection()[0]
        prev_index = (selected_index - 1) % len(playlist)
        listbox.selection_clear(0, tk.END)
        listbox.selection_set(prev_index)
        play_song()
    except:
        pass

# Step 10: Volume control function
def set_volume(val):
    volume = float(val)
    pygame.mixer.music.set_volume(volume)

# Step 11: UI Components
listbox = tk.Listbox(root, bg="#282a36", fg="white", font=("Arial", 12), selectbackground="#50fa7b", width=50, height=10)
listbox.pack(pady=10)

status_label = tk.Label(root, text="🎵 Welcome!", bg="#1e1e2e", fg="#f8f8f2", font=("Arial", 12))
status_label.pack()

# Buttons
btn_frame = tk.Frame(root, bg="#1e1e2e")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="⏮️ Prev", command=prev_song).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="▶️ Play", command=play_song).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="⏸️ Pause/Resume", command=pause_resume_song).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="⏹️ Stop", command=stop_song).grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="⏭️ Next", command=next_song).grid(row=0, column=4, padx=5)

# Volume
volume_label = tk.Label(root, text="🔊 Volume", bg="#1e1e2e", fg="white")
volume_label.pack()
volume_slider = ttk.Scale(root, from_=0, to=1, orient=tk.HORIZONTAL, command=set_volume)
volume_slider.set(0.5)
volume_slider.pack()

# Load songs button
load_btn = tk.Button(root, text="📂 Load Songs", command=load_songs, bg="#6272a4", fg="white")
load_btn.pack(pady=10)

# Start the app
root.mainloop()
