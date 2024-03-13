from File.SplitString import *
from File.OpenFile import *
import xml.dom.minidom

line = readFile()
splitBlock1(line)
splitBlock2(line)
splitBlock4(line)


tree = ET.ElementTree(main)
xml_string = ET.tostring(main, encoding="utf-8")
dom = xml.dom.minidom.parseString(xml_string)
final_xml = dom.toprettyxml(indent="  ")
# with open("new_file.xml", "w") as file:
#     file.write(final_xml)
print(final_xml)

window = Tk()
button = Button(text="open", command=readFile)
button.pack()
window.mainloop()
