# CSC226 Final Project

## Instructions

**Author(s)**: Jayden Fleming, Alain Irumva

️**Google Doc Link**: https://docs.google.com/document/d/1PfQCP4ADzSkOFW_gapHCMgJt8FH1BvVtSwp8REpGecw/edit?usp=sharing

---

## Milestone 1: Setup, Planning, Design

️**Title**: `Cipher Tool`

**Purpose**: `GUI Cipher Tool to make encoding and decoding easy with many input/outputs types.`

**Source Assignment(s)**: `HW10 - Ciphers`

**CRC Card(s)**
Note: CRC Cards also can be found in the google-doc.
![MainWindow](image/crc_MainWindow.png "MainWindow CRC")
![MorseCipher](image/crc_MorseCipher.png "MorseCipher CRC")
![OutputGenerator](image/crc_OutputGenerator.png "OutputGenerator CRC")
![BaseCipher](image/crc_OutputGenerator.png "BaseCipher CRC")
![CaesarCipher](image/crc_CaesarCipher.png "CaesarCipher CRC")
![InputConverter](image/crc_InputConverter.png "InputConverter CRC")



**Branches**: This project will **require** effective use of git. 

Each partner should create a branch at the beginning of the project, and stay on this branch (or branches of their 
branch) as they work. When you need to bring each others branches together, do so by merging each other's branches 
into your own, following the process we've discussed in previous assignments, then re-branching out from the merged code.  

```
    Branch 1 starting name: flemingj2
    Branch 2 starting name: irumvaa1
```

### References 

- https://docs.python.org/3/library/tkinter.html
- https://tkdocs.com/tutorial/
- https://coolors.co/palettes/trending/grey
- https://www.momjunction.com/articles/secret-ciphers-codes-for-kids_00736353/

---

## Milestone 2: Code Setup and Issue Queue

Most importantly, keep your issue queue up to date, and focus on your code. 🙃

Reflect on what you’ve done so far. How’s it going? Are you feeling behind/ahead? What are you worried about? 
What has surprised you so far? Describe your general feelings. Be honest with yourself; this section is for you, not me.

```
    We started off a little behind, but as direction of project has become cleaer and we have become more organized, the timline for comepleting the project has become more manageble.
```

---

## Milestone 3: Virtual Check-In

Indicate what percentage of the project you have left to complete and how confident you feel. 

**Completion Percentage**: `60%`

**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some 
strategies you can employ to increase the likelihood that you'll be successful in completing this project 
before the deadline.

```
    Core prototype is layed out; one tactic to reduce stress in this project will be creating a bramch that has functionality separate from development branch.
```

---

## Milestone 4: Final Code, Presentation, Demo

### User Instructions

Notes: 
 - All elements of the UI are labeled.
 - Prompts will guide when errors occur.
 - IMPORTANT: Encode and Decode buttons always use the contents inside Input!
 - Not all ciphers require a key. (no prompt for this)

1. Run main.py
2. Select a Cipher Type via the dropdown
3. Enter a key if applicable
4. Write text to be encoded or decoded inside the input box
5. Selected your output type via the dropdown
   - 'text' will output content to output box
   - 'file' will output content to file in current directory called out_[somthing].txt
     - 'file' will display prompt with further info on execution of task
6. Press the 'encode' or 'decode' button respectively.
7. View contents inside output box or created file respectively.

### Errors and Constraints

- Not all ciphers require a key, the UI does not communicate this.
- Some issues with element focusing, but this problem is due to how tkinter works.
- SymbolCipher is not implemented
- Because of time constraints, we were not able to implement image encodings
- Due to time constraints, some configuration elements were ommited.
  - ability to change morse-code separation-char was not added
- UTF-8 is only supported format in exporting of files.

### Reflection

Each partner should write three to four well-written paragraphs address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?
- How well did you work with your partner? What made it go well? What made it challenging?

```
    Partner 1 (flemingj2):
    For this project we selected an application that would not be too difficult but not too simple either. We wanted something interesting, that we knew we could do given the time. The project we chose also allowed for a simple distribution of tasks which would be important in this class's case. The project roughly matched the initial design, but it evolved in some ways, and degraded in other qualities from what was envisioned.

    I learned a lot regarding layout managers in this project. I also learned about python lambda events when figuring out how to have a function call another on another with certain parameters.

    The most challenging part of this project was estimating how long something would take. Figuring out how to balance a mixed paradigm of functional and OOP was also difficult. It isn't easy to know what model will simplify a problem the most.

    In a future project, I want to ensure I streamline the documentation phase better, in this project I felt it was out of order and created unnecessary resistance.

    On the topic of my partner, I feel we worked together well. We used a combination of slack and library visits along with comments under the issue-queue to complete tasks effectively.
```

```
    Partner 2: **Replace this with your reflection
```

---