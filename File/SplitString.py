import re
from Tree.ElementTree import *


def splitBlock1(line):
    listLine1 = re.findall(r'{([^{}]+)}', line[0])
    block1 = []
    for i in listLine1:
        if i[0:2] == '1:':
            block1.append(i[2:27])
    appID = block1[0][2:3]
    serviceID = block1[0][3:5]
    BIC = block1[0][5:16]
    sessionDigit = block1[0][17:21]
    sequenceDigit = block1[0][21:27]


def splitBlock2(line):
    listLine1 = re.findall(r'{([^{}]+)}', line[0])
    block2 = []

    for i in listLine1:
        if i[0:2] == '2:':
            block2.append(i[:])

    io = block2[0][2:3]
    mt = block2[0][3:6]
    BIC = ''

    for i in block2[0][6:-1]:
        if i.isalpha():
            BIC += i

    priority = block2[0][-1:]


def splitBlock4(line):
    tags = ['11A', '12a', '13a', '16R', '16S',
            '17B', '19A', '20C', '22F', '22a',
            '23G', '35B', '36B', '70a', '70E',
            '70C', '90a', '92A', '92B', '92a',
            '94a', '94B', '95a', '97a', '98a',
            '98A', '99B']
    characters = ['{', ':', '-']
    block4 = []

    for i in line:
        if i[1:4] in tags:
            block4.append(i[:])
        elif i[0] not in characters:
            if len(block4) != 0:
                block4[-1] += i

    for i in block4:
        if i[1:4] == '20C':
            branch_1_sub_1.text = i[12:]

    final_xml(ET.tostring(main))


