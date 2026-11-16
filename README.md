**Programmable LED Display for Messages Using LED Matrix**

**Project Overview**
The **Programmable LED Display for Messages Using LED Matrix** is an embedded systems project developed using Arduino UNO and a MAX72XX LED matrix display.

The system displays the predefined message **"HELLO WORLD"** on an LED matrix. The message is displayed horizontally and scrolls from right to left, making it easier to read. Arduino controls the LED matrix through serial communication using the MAX72XX interface.

 **Objectives**
- To develop a programmable message display system.
- To interface an LED matrix display with Arduino UNO.
- To display complete text messages using LED patterns.
- To implement horizontal scrolling of messages.
- To understand serial communication and embedded display control.

**Components Used**
- Arduino UNO
- MAX72XX LED Matrix Display
- Connecting wires
- Arduino IDE
- SimulIDE

**Software Used**
- Arduino IDE – for writing and compiling the Arduino program.
- SimulIDE – for circuit simulation and output verification.
- LedControl Library – for controlling the MAX72XX LED matrix.

**Working**
1. Arduino UNO initializes the MAX72XX LED matrix display.
2. The predefined message "HELLO WORLD" is stored in the Arduino program.
3. Each character is converted into a corresponding LED dot pattern.
4. The character patterns are converted into column data.
5. Arduino sends the display data to the LED matrix.
6. The message scrolls horizontally from right to left.
7. The scrolling message repeats continuously.

**Output**
The LED matrix displays the message:

**HELLO WORLD**

The characters appear horizontally and scroll continuously from right to left.

**Outcomes**
- Arduino UNO programming
- LED matrix interfacing
- MAX72XX communication
- Character-to-LED pattern conversion
- Horizontal scrolling implementation
- Embedded system simulation using SimulIDE



## Author
Embedded Systems Project
