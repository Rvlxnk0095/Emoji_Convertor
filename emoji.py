def emoji_convertor(message)
    Words = message.split(' ')
emojis = {
    ":(": "🙁",
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
    output += emojis.get(x, x) + " "
    return output

message = input("> ")
print(emoji_convertor(message))











