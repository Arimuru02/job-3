#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

a = float(input("Введите число а: "))
x = int(input("Введите число х: "))
num = a-x
i=x-2
if x-2 < 0:
    print("Задача не имеет решения! из-за х-2<0")
elif num < 0:
    print("Задача не имеет решения! из-за а-х<0")
else:
    t = math.sqrt(num)
    print("Ответ  выражения √(а-х)>(х-2): {0}>{1} ".format(t, i))