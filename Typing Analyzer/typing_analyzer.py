from pynput import keyboard
import collections
import re

# Dictionary to store word frequency
word_frequency = collections.Counter()

current_word = ""

def on_key_release(key):
    global current_word

    try:
        if key.char:
            current_word += key.char.lower()
            print_most_typed_words()

    except AttributeError:
        if key == keyboard.Key.space or key == keyboard.Key.enter:
            if current_word:
                # Remove non-alphanumeric characters from the word
                current_word = re.sub(r'[^a-zA-Z0-9]', '', current_word)
                word_frequency.update([current_word])
                current_word = ""
                print_most_typed_words()

def print_most_typed_words():
    most_common = word_frequency.most_common(5)  # Get the 5 most common words
    print("Most typed words:")
    for word, count in most_common:
        print(f"{word}: {count}")

# Start listening to keyboard events
with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()
