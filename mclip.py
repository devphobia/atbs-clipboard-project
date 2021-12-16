#! python3 – A multi-clipboard program.

import sys, time, pyperclip

ANSWERS = {
    "together" : "https://youtu.be/yPYZpwSpKmA"
    }

def invalid_usage():
    print("Usage: python mclip.py [keyphrase] - copy phrase text")
    time.sleep(1)
    sys.exit()

if len(sys.argv) != 2:
    print("Invalid number of arguments!")
    invalid_usage()
elif sys.argv[1] not in ANSWERS:
    print("Invalid keyphrase!")

keyphrase = sys.argv[1]     #first command line = keyphrase
pyperclip.copy(ANSWERS[keyphrase])
print(f"{keyphrase} answer copied to clipboard!")
