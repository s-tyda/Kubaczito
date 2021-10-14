from tkinter import *
import re

DARK = '#2E2E2B'
LIGHT_DARK = '#3a3a37'
WHITE = 'white'
LIGHT = '#5b5b59'


def press(number):
    global num
    global equal
    global is_dec
    if len(num) > 0 and number == '(' and num[-1] not in ['+', '-', '*', '/']:
        return
    if number == ')' and (len(num) == 0 or num[-1] in ['+', '-', '*', '/', '(']):
        return
    if not is_dec and number not in ['0', '1']:
        return
    if equal:
        equal = False
        num = ''
    num = num + str(number)
    scr_lbl['text'] = num


def sign(char):
    global num
    global equal
    if len(num) == 0 or num[-1] in ['+', '-', '*', '/', '(']:
        return
    if len(num) > 0 and num[-1] in ['+', '-', '*', '/']:
        num = num[:-1]
    if '(' not in num and ')' not in num:
        eval_expression()
    if equal:
        equal = False
    num = num + str(char)
    scr_lbl['text'] = num


def clear_scr():
    global equal
    global num
    equal = False
    num = ''
    scr_lbl['text'] = num


def eval_expression():
    try:
        global num
        global equal
        global is_dec
        if is_dec:
            splitted = re.split(r'([-+*/])', num)
            if len(splitted) > 0:
                operation = str(eval(num))
            else:
                operation = num
        else:
            splitted = re.split(r'([-+*/])', num)
            if len(splitted) > 1:
                left = str(int(splitted[0], 2))
                right = str(int(splitted[2], 2))
                operation = f'{eval(left + splitted[1] + right):b}'
            else:
                operation = num
        scr_lbl['text'] = operation
        equal = True
        num = operation
    except:
        scr_lbl['text'] = 'error'
        num = ''


def bin_mode():
    global is_dec
    is_dec = False
    key_bin['bg'] = LIGHT_DARK
    key_dec['bg'] = DARK
    key_2['fg'] = LIGHT_DARK
    key_3['fg'] = LIGHT_DARK
    key_4['fg'] = LIGHT_DARK
    key_5['fg'] = LIGHT_DARK
    key_6['fg'] = LIGHT_DARK
    key_7['fg'] = LIGHT_DARK
    key_8['fg'] = LIGHT_DARK
    key_9['fg'] = LIGHT_DARK


def dec_mode():
    global is_dec
    is_dec = True
    key_dec['bg'] = LIGHT_DARK
    key_bin['bg'] = DARK
    key_2['fg'] = WHITE
    key_3['fg'] = WHITE
    key_4['fg'] = WHITE
    key_5['fg'] = WHITE
    key_6['fg'] = WHITE
    key_7['fg'] = WHITE
    key_8['fg'] = WHITE
    key_9['fg'] = WHITE


def to_bin():
    global is_dec
    global num
    global equal
    if len(num) == 0:
        bin_mode()
    if is_dec and num[-1] not in ['+', '-', '*', '/']:
        num = f'{eval(num):b}'
        scr_lbl['text'] = num
        equal = True
        bin_mode()


def to_dec():
    global is_dec
    global num
    global equal
    if len(num) == 0:
        dec_mode()
    if not is_dec and num[-1] not in ['+', '-', '*', '/']:
        num = str(int(num, 2))
        scr_lbl['text'] = num
        equal = True
        dec_mode()


def new_button(frame, char, cmd='number', bg='#2E2E2B', fg='white'):
    if cmd == 'number':
        cmd = lambda: press(str(char))
    elif cmd == 'sign':
        cmd = lambda: sign(char)
    key = Button(frame,
                 text=str(char),
                 font=('Arial', 18),
                 border=0,
                 relief=GROOVE,
                 bg=bg,
                 fg=fg,
                 width=2,
                 activebackground=LIGHT,
                 activeforeground=WHITE,
                 command=cmd)
    key.pack(expand=True, fill=BOTH, side=LEFT)
    return key


ws = Tk()
ws.title('Calculator')
ws.geometry('250x400')
ws.resizable(0, 0)
num = ''
equal = False
is_dec = True
var = StringVar()

frame_1 = Frame(ws)
frame_1.pack(expand=True, fill=BOTH)

frame_2 = Frame(ws)
frame_2.pack(expand=True, fill=BOTH)

frame_3 = Frame(ws)
frame_3.pack(expand=True, fill=BOTH)

frame_4 = Frame(ws)
frame_4.pack(expand=True, fill=BOTH)

scr_lbl = Label(
    frame_1,
    textvariable='',
    font=('Arial', 22),
    anchor=SE,
    bg=DARK,
    height=2,
    pady=3,
    fg=WHITE
)

scr_lbl.pack(fill=BOTH)

key_7 = new_button(frame_1, 7)
key_8 = new_button(frame_1, 8)
key_9 = new_button(frame_1, 9)
key_add = new_button(frame_1, '+', 'sign')
left_brack = new_button(frame_1, '(')

key_4 = new_button(frame_2, 4)
key_5 = new_button(frame_2, 5)
key_6 = new_button(frame_2, 6)
key_sub = new_button(frame_2, '-', 'sign')
right_brack = new_button(frame_2, ')')

key_1 = new_button(frame_3, 1)
key_2 = new_button(frame_3, 2)
key_3 = new_button(frame_3, 3)
key_mul = new_button(frame_3, '*', 'sign')
key_dec = new_button(frame_3, 'D', to_dec, bg=LIGHT_DARK)

key_clr = new_button(frame_4, 'C', clear_scr)
key_0 = new_button(frame_4, 0)
key_res = new_button(frame_4, '=', eval_expression)
key_div = new_button(frame_4, '/', 'sign')
key_bin = new_button(frame_4, 'B', to_bin)

ws.mainloop()
