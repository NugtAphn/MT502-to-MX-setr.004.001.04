from File.SplitString import *
from File.OpenFile import *

line = readFile()
splitBlock1(line)
splitBlock2(line)
splitBlock4(line)

window = Tk()
button = Button(text="open", command=readFile)
button.pack()
window.mainloop()
