import time
import random

def speed_typing_test():
    sentences = ["The quick brown fox jumps over the lazy dog", 
                 "Pack my box with five dozen liquor jugs", 
                 "How vexingly quick daft zebras jump", 
                 "Bright vixens jump; dozy fowl quack", 
                 "Sphinx of black quartz, judge my vow"]

    random_sentence = random.choice(sentences)
    print(f"Type this: '{random_sentence}'")

    input("Press enter when ready: ")

    start_time = time.time()
    user_input = input()
    end_time = time.time()

    speed = len(user_input) / (end_time - start_time)
    print(f"Your average speed was {speed} characters per second")

    if user_input == random_sentence:
        print("Well done! You typed the sentence correctly.")
    else:
        print("You made a mistake, try again.")

if __name__ == "__main__":
    speed_typing_test()