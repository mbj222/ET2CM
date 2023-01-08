import tkinter
import re

root = tkinter.Tk()
output = tkinter.Text(root)


def clean(lines):
    lines = lines.splitlines()
    if "Main Deck:" in lines:
        lines.remove("Main Deck:")
    if "Extra Deck:" in lines:
        lines.remove("Extra Deck:")
    if "Side Deck:" in lines:
        lines.remove("Side Deck:")

    lines = filter(None, lines)

    listcard = list()

    for line in lines:
        listcard.append(line[-1] + " " + line[:-3])

    listcard = "\n".join(listcard)

    output.config(state=tkinter.NORMAL)
    output.delete("1.0", tkinter.END)
    output.insert(tkinter.END, listcard)
    output.config(state=tkinter.DISABLED)


input = tkinter.Text(root)
input.pack()


openBtn = tkinter.Button(
    root, text='Open', command=lambda: clean(input.get("1.0", tkinter.END)))
openBtn.pack(expand=tkinter.FALSE, fill=tkinter.X, side=tkinter.TOP)

output.pack()

root.mainloop()
