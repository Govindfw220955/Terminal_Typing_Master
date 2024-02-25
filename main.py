from tkinter import *  # importing all the classes and methods of tkinter module
import random
import ttkthemes
from tkinter import ttk
from time import sleep
import threading

# Functionality Part
totaltime = 60
time = 0
wrongwords = 0
elapsedtimeinminutes = 0


def start_timer():
    startButton.config(state=DISABLED)
    global time
    textarea.config(state=NORMAL)
    textarea.focus()

    for time in range(1, 61):
        elapsed_timer_label.config(text=time)
        remainingtime = totaltime - time
        remaining_timer_label.config(text=remainingtime)
        sleep(1)
        root.update()

    textarea.config(state=DISABLED)
    resetButton.config(state=NORMAL)


def count():
    global wrongwords
    while time != totaltime:
        entered_paragraph = textarea.get(1.0, END).split()
        totalwords = len(entered_paragraph)

    totalwords_count_label.config(text=totalwords)

    para_word_list = label_paragraph['text'].split()

    for pair in list(zip(para_word_list, entered_paragraph)):
        if pair[0] != pair[1]:
            wrongwords += 1

    wrongwords_count_label.config(text=wrongwords)

    elapsedtimeinminutes: float = time / 60
    wpm = (totalwords - wrongwords) / elapsedtimeinminutes
    wpm_count_label.config(text=wpm)
    gross_wpm = totalwords / elapsedtimeinminutes
    accuracy = wpm / gross_wpm * 100
    accuracy = round(accuracy)
    accuracy_percent_label.config(text=str(accuracy) + '%')


def start():
    t1 = threading.Thread(target=start_timer)
    t1.start()

    t2 = threading.Thread(target=count)
    t2.start()


def reset():
    global time, elapsedtimeinminutes
    time = 0
    elapsedtimeinminutes = 0
    startButton.config(state=NORMAL)
    resetButton.config(state=DISABLED)
    textarea.config(state=NORMAL)
    textarea.delete(1.0, END)
    textarea.config(state=DISABLED)

    elapsed_timer_label.config(text='0')
    remaining_timer_label.config(text='0')
    wpm_count_label.config(text='0')
    accuracy_percent_label.config(text='0')
    totalwords_count_label.config(text='0')
    wrongwords_count_label.config(text='0')


# GUI Part

root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('940x735+200+10')
root.resizable(0, 0)
root.overrideredirect(True)

mainframe = Frame(root, bd=4)
mainframe.grid()

titleframe = Frame(mainframe, bg='orange')
titleframe.grid()

titleLabel = Label(titleframe, text='Master Typing', font=('algerian', 28, 'bold'), bg='goldenrod3', fg='white', width=38, bd=10)
titleLabel.grid(pady=5)

paragraph_frame = Frame(mainframe)
paragraph_frame.grid(row=1, column=0)

paragraph_list = [
    ' I failed the first quarter of a class in middle school, so I made a fake report card. I did this every quarter that year. I forgot that they mail home the end-of-year cards, and my mom got it before I could intercept with my fake. She was PISSED—at the school for their error. The teacher also retired that year and had already thrown out his records, so they had to take my mother’s “proof” (the fake ones I made throughout the year) and “correct” the “mistake.” ',

    ' In my junior year of high school, this guy asked me on a date. He rented a Redbox movie and made a pizza. We were watching the movie and the oven beeped so the pizza was done. He looked me dead in the eye and said, “This is the worst part.” I then watched this boy open the oven and pull the pizza out with his bare hands, rack and all, screaming at the top of his lungs. We never had a second date.Ok so then what is i cannot tell you because that didnt happen.',

    'I went to this girl’s party the week after she beat the shit out of my friend. While everyone was getting trashed, I went around putting tuna inside all the curtain rods and so like weeks went by and they couldn’t figure out why the house smelled like festering death. They caught me through this video where these guys at the party were singing Beyonce while I was in the background with a can of tuna.This is what happened in this short funny story if you like.',

    'One time way back in sixth grade math class I had to fart really bad. Me being the idiot that I am decided that it would be silent. Big surprise it wasn’t. The only person talking was the teacher and she was interrupted by freaking cannon fire farts. She said she was disappointed I couldn’t hold it in and proceeded to tell a story of how she taught a famous athlete who did nearly the same thing.I felt ashamed then everyone laughed and at the end I also laughed.',

    'So a couple weeks ago, me and my friends were sitting on this cement kind of pedestal (as we called it) It’s basically the steps up to the portable. (classroom that no one uses) and this weird supply French teacher comes up to us and says: you shouldn’t be sitting on this ground, it’s too cold and it’s bad for your ovaries. I asked her how or why and she said that if children sit on cold ground their ovaries will freeze and that we won’t be able to have kids.',
    'One of the most valuable possession of human life is its health. With good health, one can attain everything in life. In order to perform an important work effectively, one has to be in sound health. Nowadays, everyone is suffering from some sort of mental, health, chronic or physical illness, which however deprives them. Often bad habits such as smoking have brought upon diseases and weakness upon a person which he is not aware of and are of no value to their family and society.',
    'Alcohol is taken in almost all cool and cold climates, and to a very much less extent in hot ones. It is taken by people who live in the Himalaya Mountains, but not nearly so much by those who live in the plains of India. Alcohol is not necessary in any way to anybody. The regular use of alcohol, even in small quantities, tends to cause mischief in many ways to various organs of the body. It affects the liver, it weakens the mental powers, and lessens the energy of the body.',

    'The Computer is an automatic device that performs mathematical calculations and logical operations. They are being put to use in widely divergent fields such as book-keeping, spaceflight controls, passanger reservation service, language translation etc. There are two categories: analog and digital. The former represents numbers by some physical quantity such as length, angular relation or electric current whereas the latter represent numbers by seperate devices for each digit.'
    ]

random.shuffle(paragraph_list)

label_paragraph = Label(paragraph_frame, text=paragraph_list[0], wraplength=912, justify=LEFT,
                        font=('arial', 14, 'bold'))
label_paragraph.grid(row=0, column=0)

textarea_frame = Frame(mainframe)
textarea_frame.grid(row=2, column=0)

textarea = Text(textarea_frame, font=('arial', 12, 'bold'), width=100, height=7, bd=4, relief=GROOVE, wrap='word', state=DISABLED)
textarea.grid()

frame_output = Frame(mainframe)
frame_output.grid(row=3, column=0)

elapsed_time_label = Label(frame_output, text='Elapsed Time', font=('Tahoma', 12, 'bold'), fg='red')
elapsed_time_label.grid(row=0, column=0, padx=5)

elapsed_timer_label = Label(frame_output, text='0', font=('Tahoma', 12, 'bold'))
elapsed_timer_label.grid(row=0, column=1, padx=5)

remaining_time_label = Label(frame_output, text='Remaining Time', font=('Tahoma', 12, 'bold'), fg='red')
remaining_time_label.grid(row=0, column=2, padx=5)

remaining_timer_label = Label(frame_output, text='60', font=('Tahoma', 12, 'bold'))
remaining_timer_label.grid(row=0, column=3, padx=5)

wpm_label = Label(frame_output, text='WPM', font=('Tahoma', 12, 'bold'), fg='red')
wpm_label.grid(row=0, column=4, padx=5)

wpm_count_label = Label(frame_output, text='0', font=('Tahoma', 12, 'bold'))
wpm_count_label.grid(row=0, column=5, padx=5)

totalwords_label = Label(frame_output, text='Total Words', font=('Tahoma', 12, 'bold'), fg='red')
totalwords_label.grid(row=0, column=6, padx=5)

totalwords_count_label = Label(frame_output, text='0', font=('Tahoma', 12, 'bold'))
totalwords_count_label.grid(row=0, column=7, padx=5)

wrongwords_label = Label(frame_output, text='Wrong Words', font=('Tahoma', 12, 'bold'), fg='red')
wrongwords_label.grid(row=0, column=8, padx=5)

wrongwords_count_label = Label(frame_output, text='0', font=('Tahoma', 12, 'bold'))
wrongwords_count_label.grid(row=0, column=9, padx=5)

accuracy_label = Label(frame_output, text='Accuracy', font=('Tahoma', 12, 'bold'), fg='red')
accuracy_label.grid(row=0, column=10, padx=5)

accuracy_percent_label = Label(frame_output, text='0', font=('Tahoma', 12, 'bold'))
accuracy_percent_label.grid(row=0, column=11, padx=5)

buttons_Frame = Frame(mainframe)
buttons_Frame.grid(row=4, column=0)

startButton = ttk.Button(buttons_Frame, text='Start', command=start)
startButton.grid(row=0, column=0, padx=10)

resetButton = ttk.Button(buttons_Frame, text='Reset', state=DISABLED, command=reset)
resetButton.grid(row=0, column=1, padx=10)

exitButton = ttk.Button(buttons_Frame, text='Exit', command=root.destroy)
exitButton.grid(row=0, column=2, padx=10)

keyboard_frame = Frame(mainframe)
keyboard_frame.grid(row=5, column=0)

frame1to0 = Frame(keyboard_frame)
frame1to0.grid(row=0, column=0, pady=3)

label1 = Label(frame1to0, text='1', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
label2 = Label(frame1to0, text='2', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
label3 = Label(frame1to0, text='3', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
label4 = Label(frame1to0, text='4', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
label5 = Label(frame1to0, text='5', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
label6 = Label(frame1to0, text='6', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
label7 = Label(frame1to0, text='7', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
label8 = Label(frame1to0, text='8', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
label9 = Label(frame1to0, text='9', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
label0 = Label(frame1to0, text='0', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)

label1.grid(row=0, column=0, padx=5)
label2.grid(row=0, column=1, padx=5)
label3.grid(row=0, column=2, padx=5)
label4.grid(row=0, column=3, padx=5)
label5.grid(row=0, column=4, padx=5)
label6.grid(row=0, column=5, padx=5)
label7.grid(row=0, column=6, padx=5)
label8.grid(row=0, column=7, padx=5)
label9.grid(row=0, column=8, padx=5)
label0.grid(row=0, column=9, padx=5)

frameqtop = Frame(keyboard_frame)
frameqtop.grid(row=1, column=0, pady=3)
labelQ = Label(frameqtop, text='Q', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelW = Label(frameqtop, text='W', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelE = Label(frameqtop, text='E', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelR = Label(frameqtop, text='R', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelT = Label(frameqtop, text='T', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelY = Label(frameqtop, text='Y', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelU = Label(frameqtop, text='U', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelI = Label(frameqtop, text='I', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelO = Label(frameqtop, text='O', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelP = Label(frameqtop, text='P', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)

labelQ.grid(row=0, column=0, padx=5)
labelW.grid(row=0, column=1, padx=5)
labelE.grid(row=0, column=2, padx=5)
labelR.grid(row=0, column=3, padx=5)
labelT.grid(row=0, column=4, padx=5)
labelY.grid(row=0, column=5, padx=5)
labelU.grid(row=0, column=6, padx=5)
labelI.grid(row=0, column=7, padx=5)
labelO.grid(row=0, column=8, padx=5)
labelP.grid(row=0, column=9, padx=5)

frameatol = Frame(keyboard_frame)
frameatol.grid(row=2, column=0, pady=3)
labelA = Label(frameatol, text='A', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelS = Label(frameatol, text='S', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelD = Label(frameatol, text='D', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelF = Label(frameatol, text='F', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelG = Label(frameatol, text='G', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelH = Label(frameatol, text='H', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelJ = Label(frameatol, text='J', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelK = Label(frameatol, text='K', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelL = Label(frameatol, text='L', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)

labelA.grid(row=0, column=0, padx=5)
labelS.grid(row=0, column=1, padx=5)
labelD.grid(row=0, column=2, padx=5)
labelF.grid(row=0, column=3, padx=5)
labelG.grid(row=0, column=4, padx=5)
labelH.grid(row=0, column=5, padx=5)
labelJ.grid(row=0, column=6, padx=5)
labelK.grid(row=0, column=7, padx=5)
labelL.grid(row=0, column=8, padx=5)

frameztom = Frame(keyboard_frame)
frameztom.grid(row=3, column=0, pady=3)
labelZ = Label(frameztom, text='Z', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelX = Label(frameztom, text='X', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelC = Label(frameztom, text='C', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelV = Label(frameztom, text='V', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelB = Label(frameztom, text='B', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelN = Label(frameztom, text='N', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)
labelM = Label(frameztom, text='M', bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10,
               relief=GROOVE)

labelZ.grid(row=0, column=0, padx=5)
labelX.grid(row=0, column=1, padx=5)
labelC.grid(row=0, column=2, padx=5)
labelV.grid(row=0, column=3, padx=5)
labelB.grid(row=0, column=4, padx=5)
labelN.grid(row=0, column=5, padx=5)
labelM.grid(row=0, column=6, padx=5)

spaceFrame = Frame(keyboard_frame)
spaceFrame.grid(row=4, column=0, pady=3)

labelSpace = Label(spaceFrame, bg='black', fg='white', font=('arial', 10, 'bold'), width=40, height=2, bd=10,
                   relief=GROOVE)
labelSpace.grid(row=0, column=0)


def changeBG(widget):
    widget.config(bg='blue')
    widget.after(100, lambda: widget.config(bg='black'))


label_numbers = [label1, label2, label3, label4, label5, label6, label7, label8, label9, label0]

label_alphabets = [labelA, labelB, labelC, labelD, labelE, labelF, labelG, labelH, labelI, labelJ, labelK, labelL,
                   labelM, labelN,
                   labelO, labelP, labelQ, labelR, labelS, labelT, labelU, labelV, labelW, labelX, labelY, labelZ]

space_label = [labelSpace]

binding_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

binding_capital_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T',
                             'U', 'V', 'W', 'X', 'Y', 'Z']

binding_small_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't',
                           'u', 'v', 'w', 'x', 'y', 'z']

for numbers in range(len(binding_numbers)):
    root.bind(binding_numbers[numbers], lambda event, label=label_numbers[numbers]: changeBG(label))

for capital_alphabets in range(len(binding_capital_alphabets)):
    root.bind(binding_capital_alphabets[capital_alphabets],
              lambda event, label=label_alphabets[capital_alphabets]: changeBG(label))

for small_alphabets in range(len(binding_small_alphabets)):
    root.bind(binding_small_alphabets[small_alphabets],
              lambda event, label=label_alphabets[small_alphabets]: changeBG(label))

root.bind('<space>', lambda event: changeBG(space_label[0]))
root.mainloop()
