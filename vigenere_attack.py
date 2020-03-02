import math
import sys


def Rotate(l, n):  # Rotates List L by N positions
    l = list(l)
    Shifted = l[n:] + l[:n]
    return Shifted


def Frequency(p, k):  # Finds the Frequency of K in set P
    p = p.upper()
    pLength = len(p)
    CharacterCountArray = [0] * 26
    ActualFrequency = [0] * 26
    PossibleProbability = [0] * 26
    for i in range(0, pLength):
        CharacterCountArray[ord(p[i]) - 65] = CharacterCountArray[ord(p[i]) - 65] + 1
    for x in range(0, 26):
        ActualFrequency[x] = CharacterCountArray[x] / pLength
    return ActualFrequency


def CyclicShift(p, n):  # Shifts set P by N movements and returns matches
    p = p.upper()
    OriginalText = list(p)
    ShiftedText = Rotate(OriginalText, n)
    pLength = len(p)
    TotalMatches = 0
    for i in range(0, pLength):
        if OriginalText[i] == ShiftedText[i]:
            TotalMatches = TotalMatches + 1
    return TotalMatches


# Actual Program starts here
with open("ciphertext.txt", "r") as myfile:
    ChiperText = myfile.read().replace('\n', '')
KeyLengthArray = [0] * 27
for x in range(1, 27):
    CurrentKeyLength = CyclicShift(ChiperText, x)
    KeyLengthArray[x] = CurrentKeyLength
HighestKeyCount = max(KeyLengthArray)
KeyLength = KeyLengthArray.index(HighestKeyCount)
print("Key length is : " + str(KeyLength))
