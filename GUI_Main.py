import tkinter
import GUI

def main():
    root = tkinter.Tk()
    app = GUI.Application(master=root)
    app.master.title("Sistemas - L")
    app.master.minsize(320,600)
    icone = tkinter.PhotoImage(file = 'Imagens/icone.png')
    root.tk.call("wm","iconphoto",root._w,icone)
    app.master.resizable(False,False)
    app.mainloop()

if __name__ == '__main__':
    main()
