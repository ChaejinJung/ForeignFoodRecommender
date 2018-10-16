# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from typing import Any, Union, List, Iterable

input = pd.read_excel('input.xlsx')
output = pd.read_excel('output.xlsx')

# add another column 'score'
output['score'] = 0

input_name = input['Name']
input_category = input['Category']
input_main1 = input['MainIngredient1']
input_main2 = input['MainIngredient2']
input_main3 = input['MainIngredient3']
input_sub1 = input['SubIngredient1']
output_name = output['Name']
output_category = output['Category']
output_main1 = output['MainIngredient1']
output_main2 = output['MainIngredient2']
output_main3 = output['MainIngredient3']
output_sub1 = output['SubIngredient1']
temp = []
temp2 = []  # type: List[Any]

print(input)
print(output)

##Categorizing
for i in input_category:
    for j in output_category:
        if i == j:
            temp = np.where(output_category != j)

categorized = output.drop(temp[0], 0)
categorized = categorized.reset_index(drop=True)

print(categorized)

temp = []
temp2 = []

##Main1
for i in input_main1:
    for j in categorized['MainIngredient1']:
        if i == j and temp != None:
            temp = np.where(categorized['MainIngredient1'] == i)
        elif i != j and temp2 != None:
            temp2 = np.where(categorized['MainIngredient1'] != i)

if temp or temp2 == True:
    categorized['score'][temp[0]] += 30
    categorized['score'][temp2[0]] += 5

print(categorized)



temp = []
temp2 = []

##Main2
for i in input_main2:
    for j in categorized['MainIngredient2']:
        if i == j:
            temp = np.where(categorized['MainIngredient2'] == i)
        else:
            temp2 = np.where(categorized['MainIngredient2'] != i)

print(temp)
print(temp2)

if temp == True:
    categorized['score'][temp[0]] += 20
elif temp2 != None:
    categorized['score'][temp2[0]] += 5

print('MAIN2222')
print(input)
print(categorized)

temp = []
temp2 = []

##Main2 & 3 comparing
for i in input_main2:
    for j in categorized['MainIngredient3']:
        if i == j:
            temp = np.where(categorized['MainIngredient3'] == i)
        else:
            temp2 = np.where(categorized['MainIngredient3'] != i)

if temp or temp2 == True:
    categorized['score'][temp[0]] += 7
    categorized['score'][temp2[0]] += 0

print(temp)
print(temp2)
print('MAIN23')
print(input)
print(categorized)

temp = []
temp2 = []

##Main3
for i in input_main3:
    for j in categorized['MainIngredient3']:
        if i == j:
            temp = np.where(categorized['MainIngredient3'] == i)
        else:
            temp2 = np.where(categorized['MainIngredient3'] != i)

print(temp)
print(temp2)

if temp == True:
    categorized['score'][temp[0]] += 10
elif temp2 != None:
    categorized['score'][temp2[0]] += 5

print('MAIN333')
print(input)
print(categorized)

temp = []
temp2 = []

##Main3 & 2 comparing
for i in input_main3:
    for j in categorized['MainIngredient2']:
        if i == j:
            temp = np.where(categorized['MainIngredient2'] == i)

if temp or temp2 == True:
    categorized['score'][temp[0]] += 4
    categorized['score'][temp2[0]] += 0

temp = []
temp2 = []

##Sub1
for i in input_sub1:
    for j in categorized['SubIngredient1']:
        if i == j:
            temp = np.where(categorized['SubIngredient1'] == i)
        else:
            temp2 = np.where(categorized['SubIngredient1'] != i)


categorized['score'][temp[0]] += 10


print('SUB1')
print(input)
print(categorized)

categorized = categorized.sort_values(["score"], ascending=[False])

print('sort')
print(categorized)
print('')
print('########RESULT########')
print(categorized['Name'])
