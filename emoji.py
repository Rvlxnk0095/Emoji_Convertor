message = input("> ")
Words = message.split(' ')
emojis = {
    ":(": "☹",
    ":)": "😊",
    ";)": "😉",
    "u_u": "😌",
    ":D": "😂",
    ":-o": "😱",
    ":P": "😛",
    ":-3": "😘",
    '¬_¬': "😒",
    "*_*": "🤩",
    ">_<": "😡",
}
output = " "
for x in Words:
    print(emojis.get(x, x), end="" + " ")










