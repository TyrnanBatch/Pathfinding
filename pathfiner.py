import random

lineLen = random.randint(4, 6)

slot = [" "," "," "," "," "," "," "," "," "," ",
        " "," "," "," "," "," "," "," "," "," ",
        " "," "," "," "," "," "," "," "," "," ",
        " "," "," "," "," "," "," "," "," "," ",
        " "," "," "," "," "," "," "," "," "," ",
        " "," "," "," "," "," "," "," "," "," ",
        " "," "," "," "," "," "," "," "," "," ",
        " "," "," "," "," "," "," "," "," "," ",
        " "," "," "," "," "," "," "," "," "," ",
        " "," "," "," "," "," "," "," "," "," ",
        " "," "," "," "," "," "," "," "," "," ",]

def slotFunc():
    print("/--------------------\\")
    print("|" + str(slot[1]) + " " + str(slot[2]) + " " + str(slot[3]) + " " + str(slot[4]) + " " + str(slot[5]) + " " + str(slot[6]) + " " + str(slot[7]) + " " + str(slot[8]) + " " + str(slot[9]) + " " + str(slot[10]) + " " + "|")
    print("|" + str(slot[11]) + " " + str(slot[12]) + " " + str(slot[13]) + " " + str(slot[14]) + " " + str(slot[15]) + " " + str(slot[16]) + " " + str(slot[17]) + " " + str(slot[18]) + " " + str(slot[19]) + " " + str(slot[20]) + " " + "|")
    print("|" + str(slot[21]) + " " + str(slot[22]) + " " + str(slot[23]) + " " + str(slot[24]) + " " + str(slot[25]) + " " + str(slot[26]) + " " + str(slot[27]) + " " + str(slot[28]) + " " + str(slot[29]) + " " + str(slot[30]) + " " + "|")
    print("|" + str(slot[31]) + " " + str(slot[32]) + " " + str(slot[33]) + " " + str(slot[34]) + " " + str(slot[35]) + " " + str(slot[36]) + " " + str(slot[37]) + " " + str(slot[38]) + " " + str(slot[39]) + " " + str(slot[40]) + " " + "|")
    print("|" + str(slot[41]) + " " + str(slot[42]) + " " + str(slot[43]) + " " + str(slot[44]) + " " + str(slot[45]) + " " + str(slot[46]) + " " + str(slot[47]) + " " + str(slot[48]) + " " + str(slot[49]) + " " + str(slot[50]) + " " + "|")
    print("|" + str(slot[51]) + " " + str(slot[52]) + " " + str(slot[53]) + " " + str(slot[54]) + " " + str(slot[55]) + " " + str(slot[56]) + " " + str(slot[57]) + " " + str(slot[58]) + " " + str(slot[59]) + " " + str(slot[60]) + " " + "|")
    print("|" + str(slot[61]) + " " + str(slot[62]) + " " + str(slot[63]) + " " + str(slot[64]) + " " + str(slot[65]) + " " + str(slot[66]) + " " + str(slot[67]) + " " + str(slot[68]) + " " + str(slot[69]) + " " + str(slot[70]) + " " + "|")
    print("|" + str(slot[71]) + " " + str(slot[72]) + " " + str(slot[73]) + " " + str(slot[74]) + " " + str(slot[75]) + " " + str(slot[76]) + " " + str(slot[77]) + " " + str(slot[78]) + " " + str(slot[79]) + " " + str(slot[80]) + " " + "|")
    print("|" + str(slot[81]) + " " + str(slot[82]) + " " + str(slot[83]) + " " + str(slot[84]) + " " + str(slot[85]) + " " + str(slot[86]) + " " + str(slot[87]) + " " + str(slot[88]) + " " + str(slot[89]) + " " + str(slot[90]) + " " + "|")
    print("|" + str(slot[91]) + " " + str(slot[92]) + " " + str(slot[93]) + " " + str(slot[94]) + " " + str(slot[95]) + " " + str(slot[96]) + " " + str(slot[97]) + " " + str(slot[98]) + " " + str(slot[99]) + " " + str(slot[100]) + " " + "|")
    print("\--------------------/")

def randMap():
    topRowAdj = random.randint(1, 4)
    topRow = random.randint(1, 3)
    slot[topRow] = "#"
    count = 1
    while count < lineLen:
        
        if topRowAdj == 1:
            topRow = topRow - 1
            topRowDig1 = str(topRow)[0]
            if int(topRowDig1) <= count:
                if not topRow <= 9:
                    topRow = topRow + 1
            slot[topRow] = "#"

        if topRowAdj == 2:
            topRow = topRow + 1
            topRowDig1 = str(topRow)[0]
            if int(topRowDig1) <= count:
                if not topRow <= 9:
                    topRow = topRow + 1
            slot[topRow] = "#"

        if topRowAdj == 3 or topRowAdj == 4:
            topRow = topRow + 10
            slot[topRow] = "#"

        topRowAdjRand1 = random.randint(1, 4)
        while topRowAdjRand1 == topRowAdj:
            topRowAdjRand1 = random.randint(1, 4)
        topRowAdj = topRowAdjRand1

        count = count + 1

    topRowAdj = random.randint(1, 4)
    topRow = random.randint(4, 7)
    slot[topRow] = "#"
    count = 1
    while count < lineLen:
        
        if topRowAdj == 1:
            topRow = topRow - 1
            topRowDig1 = str(topRow)[0]
            if int(topRowDig1) <= count:
                if not topRow <= 9:
                    topRow = topRow + 1
            slot[topRow] = "#"

        if topRowAdj == 2:
            topRow = topRow + 1
            topRowDig1 = str(topRow)[0]
            if int(topRowDig1) <= count:
                if not topRow <= 9:
                    topRow = topRow + 1
            slot[topRow] = "#"

        if topRowAdj == 3 or topRowAdj == 4:
            topRow = topRow + 10
            slot[topRow] = "#"

        topRowAdjRand1 = random.randint(1, 4)
        while topRowAdjRand1 == topRowAdj:
            topRowAdjRand1 = random.randint(1, 4)
        topRowAdj = topRowAdjRand1

        count = count + 1

    topRowAdj = random.randint(1, 4)
    topRow = random.randint(8, 10)
    slot[topRow] = "#"
    count = 1
    while count < lineLen:
        
        if topRowAdj == 1:
            topRow = topRow - 1
            topRowDig1 = str(topRow)[0]
            if int(topRowDig1) <= count:
                if not topRow <= 9:
                    topRow = topRow + 1
            slot[topRow] = "#"

        if topRowAdj == 2:
            topRow = topRow + 1
            topRowDig1 = str(topRow)[0]
            if int(topRowDig1) <= count:
                if not topRow <= 9:
                    topRow = topRow + 1
            slot[topRow] = "#"

        if topRowAdj == 3 or topRowAdj == 4:
            topRow = topRow + 10
            slot[topRow] = "#"

        topRowAdjRand1 = random.randint(1, 4)
        while topRowAdjRand1 == topRowAdj:
            topRowAdjRand1 = random.randint(1, 4)
        topRowAdj = topRowAdjRand1

        count = count + 1

    botRowAdj = random.randint(1, 4)
    botRow = random.randint(91, 93)
    slot[botRow] = "#"
    count = 1
    while count < lineLen:
        
        if botRowAdj == 1:
            botRow = botRow - 1
            botRowDig1 = str(botRow)[0]
            if int(botRowDig1) <= count:
                if not botRow <= 9:
                    botRow = botRow + 1
            slot[botRow] = "#"

        if botRowAdj == 2:
            botRow = botRow + 1
            botRowDig1 = str(botRow)[0]
            if int(botRowDig1) <= count:
                if not botRow <= 9:
                    botRow = botRow + 1
            slot[botRow] = "#"

        if botRowAdj == 3 or botRowAdj == 4:
            botRow = botRow - 10
            slot[botRow] = "#"

        botRowAdjRand1 = random.randint(1, 4)
        while botRowAdjRand1 == botRowAdj:
            botRowAdjRand1 = random.randint(1, 4)
        botRowAdj = botRowAdjRand1

        count = count + 1

    botRowAdj = random.randint(1, 4)
    botRow = random.randint(94, 97)
    slot[botRow] = "#"
    count = 1
    while count < lineLen:
        
        if botRowAdj == 1:
            botRow = botRow - 1
            botRowDig1 = str(botRow)[0]
            if int(botRowDig1) <= count:
                if not botRow <= 9:
                    botRow = botRow + 1
            slot[botRow] = "#"

        if botRowAdj == 2:
            botRow = botRow + 1
            botRowDig1 = str(botRow)[0]
            if int(botRowDig1) <= count:
                if not botRow <= 9:
                    botRow = botRow + 1
            slot[botRow] = "#"

        if botRowAdj == 3 or botRowAdj == 4:
            botRow = botRow - 10
            slot[botRow] = "#"

        botRowAdjRand1 = random.randint(1, 4)
        while botRowAdjRand1 == botRowAdj:
            botRowAdjRand1 = random.randint(1, 4)
        botRowAdj = botRowAdjRand1

        count = count + 1

    botRowAdj = random.randint(1, 4)
    botRow = random.randint(98, 100)
    slot[botRow] = "#"
    count = 1
    while count < lineLen:
        
        if botRowAdj == 1:
            botRow = botRow - 1
            botRowDig1 = str(botRow)[0]
            if int(botRowDig1) <= count:
                if not botRow <= 9:
                    botRow = botRow + 1
            slot[botRow] = "#"

        if botRowAdj == 2:
            botRow = botRow + 1
            botRowDig1 = str(botRow)[0]
            if int(botRowDig1) <= count:
                if not botRow <= 9:
                    botRow = botRow + 1
            slot[botRow] = "#"

        if botRowAdj == 3 or botRowAdj == 4:
            botRow = botRow - 10
            slot[botRow] = "#"

        botRowAdjRand1 = random.randint(1, 4)
        while botRowAdjRand1 == botRowAdj:
            botRowAdjRand1 = random.randint(1, 4)
        botRowAdj = botRowAdjRand1

        count = count + 1

slotFunc()