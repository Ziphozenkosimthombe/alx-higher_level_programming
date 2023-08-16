#!/usr/bin/python3

def subtract(num):
    subtractTo = 0
    maximumList = max(num)

    for i in num:
        if maximumList > i:
            subtractTo += i
    return maximumList - subtractTo


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0


    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    listForKeys = list(rom.keys())

    number = 0
    lastRom = 0
    num = [0]

    for j in roman_string:
        for r in listForKeys:
            if r == j:
                if rom.get(j) <= lastRom:
                    number += subtract(num)
                    num = [rom.get(j)]
                else:
                    num.append(rom.get(j))

                lastRom = rom.get(j)

    number += subtract(num)

    return number
