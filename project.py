from tkinter import *
import tkinter.font as font
import random

win = Tk()  # creates the window
win.title('ATM')
win.geometry('500x500')  # sets the dimension of the window
win.minsize(500, 500)
win.maxsize(500, 500)

tim40 = font.Font(family='Times', size=40, weight='normal', underline=1)

cour20 = font.Font(family='Courier', size=20, weight='normal')
cour15 = font.Font(family='Courier', size=15, weight='normal')

glob_count = 0  # this is used to access balance_func() after press yes in question_func()


# -----final display withdrawl_func()
def display_func():
    question_func.question_win.withdraw()
    display_win = Toplevel(win)
    display_win.geometry('560x490')

    message = Message(display_win, text='\n\nYour transaction has been successful\n\nThank you for using our',
                      font=cour20, fg='blue')
    message.pack()
    text = Label(display_win, text='ATM', font=tim40, fg='black')
    text.pack()

    exit_button = Button(display_win, text='EXIT', font=cour15, fg='red', command=lambda: win.destroy())
    exit_button.pack(side=BOTTOM, pady=10)


# window asking whether to show balance or not
def question_func():
    global glob_count
    glob_count += 1

    withdrawal_func.withdrawal_win.withdraw()
    question_func.question_win = Toplevel(win)
    question_func.question_win.geometry('500x500')

    bf = Frame(question_func.question_win)
    bf.pack(side=BOTTOM)

    msg_box = Message(question_func.question_win,
                      text='\nYour transaction has been successful\n\nPlease collect your money\n\nYou can remove '
                           'your card\n\nDo you want to check your balance?',
                      font=cour20, fg='black')
    msg_box.pack()

    yes_btn = Button(bf, text=' YES ', font=cour15, fg='white', bg='blue', command=balance_func)
    yes_btn.pack(side=LEFT, pady=20)

    no_btn = Button(bf, text=' NO ', font=cour15, fg='white', bg='blue', command=display_func)
    no_btn.pack(pady=20, padx=10)


# withdrawing money window
def withdrawal_func():
    option_func.option_win.withdraw()
    withdrawal_func.withdrawal_win = Toplevel(win)
    withdrawal_func.withdrawal_win.geometry('500x500')

    enter_lbl = Label(withdrawal_func.withdrawal_win, text='\nPlease enter amount\n', font=cour20, fg='red')
    enter_lbl.pack()
    money_entry = Entry(withdrawal_func.withdrawal_win, font=cour15, justify='center')
    money_entry.pack()

    bf = Frame(withdrawal_func.withdrawal_win)
    bf.pack(side=BOTTOM)

    bf4 = Frame(withdrawal_func.withdrawal_win)
    bf4.pack(side=BOTTOM)

    bf3 = Frame(withdrawal_func.withdrawal_win)
    bf3.pack(side=BOTTOM)

    bf3 = Frame(withdrawal_func.withdrawal_win)
    bf3.pack(side=BOTTOM)

    bf2 = Frame(withdrawal_func.withdrawal_win)
    bf2.pack(side=BOTTOM)

    bf1 = Frame(withdrawal_func.withdrawal_win)
    bf1.pack(side=BOTTOM)

    b1 = Button(bf1, text='1', font=cour15, command=lambda: money_entry.insert('end', '1'), bg='red')
    b1.pack(side=LEFT, pady=10)

    b2 = Button(bf1, text='2', font=cour15, command=lambda: money_entry.insert('end', '2'), bg='red')
    b2.pack(side=LEFT, padx=10)

    b3 = Button(bf1, text='3', font=cour15, command=lambda: money_entry.insert('end', '3'), bg='red')
    b3.pack(side=LEFT)

    b4 = Button(bf2, text='4', font=cour15, command=lambda: money_entry.insert('end', '4'), bg='red')
    b4.pack(side=LEFT)

    b5 = Button(bf2, text='5', font=cour15, command=lambda: money_entry.insert('end', '5'), bg='red')
    b5.pack(side=LEFT, padx=10)

    b6 = Button(bf2, text='6', font=cour15, command=lambda: money_entry.insert('end', '6'), bg='red')
    b6.pack(side=LEFT)

    b7 = Button(bf3, text='7', font=cour15, command=lambda: money_entry.insert('end', '7'), bg='red')
    b7.pack(side=LEFT, pady=10)

    b8 = Button(bf3, text='8', font=cour15, command=lambda: money_entry.insert('end', '8'), bg='red')
    b8.pack(side=LEFT, padx=10)

    b9 = Button(bf3, text='9', font=cour15, command=lambda: money_entry.insert('end', '9'), bg='red')
    b9.pack(side=LEFT)

    btn = Button(bf4, text=' ', font=cour15)
    btn.pack(side=LEFT)

    b0 = Button(bf4, text='0', font=cour15, command=lambda: money_entry.insert('end', '0'), bg='red')
    b0.pack(side=LEFT, padx=10)

    btn_ = Button(bf4, text=' ', font=cour15)
    btn_.pack(side=LEFT)

    enter_btn = Button(bf, text='ENTER', font=cour15, fg='green', command=question_func)
    enter_btn.pack(side=LEFT, pady=10)

    clear_btn = Button(bf, text='CLEAR', font=cour15, fg='orange', command=lambda: money_entry.delete(1))
    clear_btn.pack(side=LEFT, padx=10)


# balance displaying window
def balance_func():
    global glob_count

    if glob_count == 1:
        question_func.question_win.withdraw()

    option_func.option_win.withdraw()
    balance_win = Toplevel(win)
    balance_win.geometry('500x500')
    # balance_win.grab_set()
    balance = random.randrange(1000, 1000000)
    message = Message(balance_win, text='\nYour transaction is successful', font=cour20, fg='blue')
    message.pack()
    message1 = Message(balance_win, text='\n\nAvailable Balance: ' + str(balance), font=cour20, fg='red')
    message1.pack()
    text = Label(balance_win, text='ATM', font=tim40, fg='red')
    text.pack()

    exit_button = Button(balance_win, text='EXIT', font=cour15, fg='red', command=lambda: win.destroy())
    exit_button.pack(side=BOTTOM, pady=10)


# displays message after change has been changed
def message_func():
    change_pin_func.change_pin_win.withdraw()
    win2 = Toplevel(win)
    win2.geometry('500x500')
    message = Message(win2,
                      text='\nYour transaction is successful completed\n\nYour PIN has been successfully '
                           'changed\n\nThank you for using our',
                      font=cour15, fg='blue')
    message.pack()
    text = Label(win2, text='ATM', font=tim40, fg='red')
    text.pack()

    exit_button = Button(win2, text='EXIT', font=cour15, fg='red', command=lambda: win.destroy())
    exit_button.pack(side=BOTTOM, pady=10)


# changing pin function
def change_pin_func():
    option_func.option_win.withdraw()
    change_pin_func.change_pin_win = Toplevel(win)
    change_pin_func.change_pin_win.geometry('500x500')

    pin_lbl = Label(change_pin_func.change_pin_win, text='\nEnter new-PIN', font=cour15, fg='red')
    pin_lbl.pack()
    pin_entry = Entry(change_pin_func.change_pin_win, font=cour15, justify='center', show='*')
    pin_entry.pack()

    re_entry_lbl = Label(change_pin_func.change_pin_win, text='\nRe-enter new-PIN', font=cour15, fg='red')
    re_entry_lbl.pack()
    re_entry = Entry(change_pin_func.change_pin_win, font=cour15, justify='center', show='*')
    re_entry.pack()

    bf = Frame(change_pin_func.change_pin_win)
    bf.pack(side=BOTTOM)

    bf4 = Frame(change_pin_func.change_pin_win)
    bf4.pack(side=BOTTOM)

    bf3 = Frame(change_pin_func.change_pin_win)
    bf3.pack(side=BOTTOM)

    bf3 = Frame(change_pin_func.change_pin_win)
    bf3.pack(side=BOTTOM)

    bf2 = Frame(change_pin_func.change_pin_win)
    bf2.pack(side=BOTTOM)

    bf1 = Frame(change_pin_func.change_pin_win)
    bf1.pack(side=BOTTOM)

    b1 = Button(bf1, text='1', font=cour15, command=lambda: [pin_entry.insert('end', '1'), re_entry.insert('end', '1')],
                bg='red')
    b1.pack(side=LEFT, pady=10)

    b2 = Button(bf1, text='2', font=cour15, command=lambda: [pin_entry.insert('end', '2'), re_entry.insert('end', '2')],
                bg='red')
    b2.pack(side=LEFT, padx=10)

    b3 = Button(bf1, text='3', font=cour15, command=lambda: [pin_entry.insert('end', '3'), re_entry.insert('end', '3')],
                bg='red')
    b3.pack(side=LEFT)

    b4 = Button(bf2, text='4', font=cour15, command=lambda: [pin_entry.insert('end', '4'), re_entry.insert('end', '4')],
                bg='red')
    b4.pack(side=LEFT)

    b5 = Button(bf2, text='5', font=cour15, command=lambda: [pin_entry.insert('end', '5'), re_entry.insert('end', '5')],
                bg='red')
    b5.pack(side=LEFT, padx=10)

    b6 = Button(bf2, text='6', font=cour15, command=lambda: [pin_entry.insert('end', '6'), re_entry.insert('end', '6')],
                bg='red')
    b6.pack(side=LEFT)

    b7 = Button(bf3, text='7', font=cour15, command=lambda: [pin_entry.insert('end', '7'), re_entry.insert('end', '7')],
                bg='red')
    b7.pack(side=LEFT, pady=10)

    b8 = Button(bf3, text='8', font=cour15, command=lambda: [pin_entry.insert('end', '8'), re_entry.insert('end', '8')],
                bg='red')
    b8.pack(side=LEFT, padx=10)

    b9 = Button(bf3, text='9', font=cour15, command=lambda: [pin_entry.insert('end', '9'), re_entry.insert('end', '9')],
                bg='red')
    b9.pack(side=LEFT)

    btn = Button(bf4, text=' ', font=cour15)
    btn.pack(side=LEFT)

    b0 = Button(bf4, text='0', font=cour15, command=lambda: [pin_entry.insert('end', '0'), re_entry.insert('end', '0')],
                bg='red')
    b0.pack(side=LEFT, padx=10)  # with help of list we can assign multiple functions for buttons

    btn_ = Button(bf4, text=' ', font=cour15)
    btn_.pack(side=LEFT)

    enter_btn = Button(bf, text='ENTER', font=cour15, fg='green', command=message_func)
    enter_btn.pack(side=LEFT, pady=10)

    clear_btn = Button(bf, text='CLEAR', font=cour15, fg='orange',
                       command=lambda: [pin_entry.delete(0), re_entry.delete(0)])
    clear_btn.pack(side=LEFT, padx=10)


# options window
def option_func():
    enter_pin.new_win.withdraw()  # check enter_pin() function for the functionality of .withdraw()
    option_func.option_win = Toplevel(win)
    option_func.option_win.geometry('500x500')

    text_title = Label(option_func.option_win, text='\nATM', font=tim40, fg='red')
    text_title.pack()

    rf = Frame(option_func.option_win)  # right frame
    rf.pack(side=RIGHT)

    lf = Frame(option_func.option_win)  # left frame
    lf.pack(side=LEFT)

    withdrawal_btn = Button(rf, text=' WITHDRAWAL ', font=cour15, fg='white', bg='dark blue', command=withdrawal_func)
    withdrawal_btn.pack(padx=40, pady=30)

    balance_btn = Button(rf, text='BALANCE INQ', font=cour15, fg='white', bg='dark blue', command=balance_func)
    balance_btn.pack(padx=40, pady=30)

    change_pin_btn = Button(lf, text='CHANGE PIN', font=cour15, fg='white', bg='dark blue', command=change_pin_func)
    change_pin_btn.pack(padx=40, pady=30)

    exit_btn = Button(lf, text='   EXIT   ', font=cour15, fg='white', bg='dark blue',
                      command=lambda: [option_func.option_win.destroy(), enter_pin.new_win.deiconify()])
    exit_btn.pack(padx=40, pady=30)  # check enter_pin() function for the functionality of .deiconify()


# enter_pin window
def enter_pin():
    win.withdraw()  # .withdraw() hides or make the associated window invisible until (.deiconify()) appears

    enter_pin.new_win = Toplevel(
        win)  # enter_pin.new_win makes the variable new_win as the member of the function object
    enter_pin.new_win.geometry('500x500')  # this helps us to use the variable even outside the function

    def setInputText(text):
        entry_box.insert('end',
                         text)  # insert allows to enter(display on entry box) the text at the end(if we replace end
        # with 0 the text is placed at front)

    def text_delete():
        entry_box.delete(
            0)  # we have another function called delete which deletes text for the given range(.delete(0,
        # 'end') deletes the entire text

    lbl = Label(enter_pin.new_win, text='Enter your PIN', font=cour20, fg='red')
    lbl.pack(pady=40)

    entry_box = Entry(enter_pin.new_win, font=cour15, show='*',
                      justify='center')  # show parameter display the input text as *(we can use any other element also)
    entry_box.pack()

    bf = Frame(enter_pin.new_win)
    bf.pack(side=BOTTOM)

    bf0 = Frame(enter_pin.new_win)
    bf0.pack(side=BOTTOM)

    bf1 = Frame(enter_pin.new_win)
    bf1.pack(side=BOTTOM)

    bf2 = Frame(enter_pin.new_win)
    bf2.pack(side=BOTTOM)

    bf3 = Frame(enter_pin.new_win)
    bf3.pack(side=BOTTOM)

    bf4 = Frame(enter_pin.new_win)
    bf4.pack(side=BOTTOM)

    rf = Frame(enter_pin.new_win)
    rf.pack(side=RIGHT)

    btn1 = Button(bf4, text='1', font=cour15, command=lambda: setInputText('1'), bg='red')
    btn1.pack(side=LEFT, pady=10)

    btn2 = Button(bf4, text='2', font=cour15, command=lambda: setInputText('2'), bg='red')
    btn2.pack(side=LEFT, padx=10)

    btn3 = Button(bf4, text='3', font=cour15, command=lambda: setInputText('3'), bg='red')
    btn3.pack(side=LEFT)

    btn4 = Button(bf3, text='4', font=cour15, command=lambda: setInputText('4'), bg='red')
    btn4.pack(side=LEFT)

    btn5 = Button(bf3, text='5', font=cour15, command=lambda: setInputText('5'), bg='red')
    btn5.pack(side=LEFT, padx=10)

    btn6 = Button(bf3, text='6', font=cour15, command=lambda: setInputText('6'), bg='red')
    btn6.pack(side=LEFT)

    btn7 = Button(bf2, text='7', font=cour15, command=lambda: setInputText('7'), bg='red')
    btn7.pack(side=LEFT, pady=10)

    btn8 = Button(bf2, text='8', font=cour15, command=lambda: setInputText('8'), bg='red')
    btn8.pack(side=LEFT, padx=10)

    btn9 = Button(bf2, text='9', font=cour15, command=lambda: setInputText('9'), bg='red')
    btn9.pack(side=LEFT)

    btn = Button(bf1, text=' <', font=cour15)
    btn.pack(side=LEFT)

    btn0 = Button(bf1, text='0', font=cour15, command=lambda: setInputText('0'), bg='red')
    btn0.pack(side=LEFT, padx=10)

    btn_ = Button(bf1, text='> ', font=cour15)
    btn_.pack(side=LEFT)

    enter_btn = Button(bf0, text='ENTER', font=cour15, fg='green', command=option_func)
    enter_btn.pack(side=LEFT, pady=30, padx=10)

    exit_btn = Button(bf0, text='EXIT', font=cour15, fg='red', command=lambda: [enter_pin.new_win.destroy(),
                                                                                win.deiconify()])  # .deiconify() makes the associated window visible
    exit_btn.pack(side=RIGHT, padx=10)

    clear_btn = Button(bf0, text='CLEAR', font=cour15, fg='orange', command=text_delete)
    clear_btn.pack(side=LEFT)

    note = Label(bf, text='Note:Enter pin either from keyboard or keypad', fg='red', bg='yellow')
    note.pack()


# main opening window
title_label = Label(win, text='A T M', font=tim40,fg='red')  # Label is something similar to a label which displays
# text on the window
title_label.pack(pady=10)  # pad y gives vertical distance both above and below where as pad x gives

# displaying some introduction
user_id = random.randrange(1000, 10000)
intro = Label(win, text='\nWELCOME', font=cour20, fg='green')
intro.pack()
option_label = Label(win, text='\nPlease Select your Account Type', font=cour15, fg='dark blue')
option_label.pack()

bottom_frame = Frame(win)
bottom_frame.pack(side=BOTTOM)
right_frame = Frame(win)
right_frame.pack(side=LEFT)

note = Label(bottom_frame, text='NOTE:USE EXIT BUTTON \nTO EXIT THE CURRENT WINDOW', font=cour15, fg='Red', bg='yellow')
note.pack(pady=10)
saving = Button(right_frame, text='Savings', font='white', bg='black', fg='white', command=enter_pin)
saving.pack(padx=200, pady=20)
current = Button(right_frame, text="Current", font='white', bg='black', fg='white', command=enter_pin)
current.pack(padx=200, pady=20)

win.mainloop()
