

import time
import os

# 5x7 character patterns
font = {
    "H": [
        "10001",
        "10001",
        "10001",
        "11111",
        "10001",
        "10001",
        "10001"
    ],
    "E": [
        "11111",
        "10000",
        "10000",
        "11110",
        "10000",
        "10000",
        "11111"
    ],
    "L": [
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "11111"
    ],
    "O": [
        "01110",
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "01110"
    ]
}

message = "HELLO"

# Convert message into LED columns
rows = [""] * 7

for char in message:
    for i in range(7):
        rows[i] += font[char][i] + "0"

# Add blank space before and after message
for i in range(7):
    rows[i] = "00000000" + rows[i] + "00000000"

# Scroll across an 8x8 display
for position in range(len(rows[0]) - 7):

    os.system("cls" if os.name == "nt" else "clear")

    print("8x8 LED MATRIX DISPLAY")
    print("----------------------")

    for row in rows:
        frame = row[position:position + 8]
        display = ""

        for led in frame:
            display += "■ " if led == "1" else "□ "

        print(display)

    time.sleep(0.2)

print("Scrolling completed!")
