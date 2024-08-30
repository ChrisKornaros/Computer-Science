# Prompt the user for input
def ask_user():
    global a
    a = input("Please enter text: ")
    return a

# Add the three periods


def playback():
    b = a.replace(' ', '...')
    print(b)


ask_user()
playback()
