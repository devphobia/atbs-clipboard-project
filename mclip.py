#! python3 – A multi-clipboard program.

import sys, time, pyperclip

ANSWERS = {
    "gaming" : "Yep. It's gaming time.",
    "sheets" : "Here are the sheets you wanted."
    }

def invalid_usage():
    print("Usage: python mclip.py [keyphrase] [client_name (optional)] [intro (optional)] - copy phrase text")
    time.sleep(1)
    sys.exit()
    

def add_work_intro(text, client_name):
    intro = f"Good evening, {client_name}!\n"
    outro = f"\nMany thanks,\ndevphobia"

    new_text = intro + text + outro

    return new_text


while True:
    if len(sys.argv) < 4:
        sys.argv.append(None)
    else:
        break

if len(sys.argv) == 4:
    keyphrase, client_name, intro = sys.argv[1::]
else:
    invalid_usage()

if keyphrase == None:
    invalid_usage()
elif keyphrase not in ANSWERS:
    print("Keyphrase not found!")
else:
    answer = ANSWERS[keyphrase]

if intro != None:
    answer = add_work_intro(answer, client_name)

pyperclip.copy(answer)

print(f"{keyphrase} answer copied to the clipboard!")

