import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    c = 0
    temp = candles[0]
    for i in range(1, len(candles)):
        if candles[i] > temp:
            temp = candles[i]
    for i in range(0, len(candles)):
        if candles[i] == temp:
            c = c + 1
    return c


if __name__ == '__main__':
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    print(result)