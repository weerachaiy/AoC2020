import sys
import re

def checkPassport(DictA):
  if checkInvalid(DictA['byr'], 1920, 2002):
    return True
  if checkInvalid(DictA['iyr'], 2010, 2020):
    return True
  if checkInvalid(DictA['eyr'], 2020, 2030):
    return True
  if not DictA['ecl'] in EyeColors:
    return True
  if not DictA['hgt'][-2:] in HeightUnits:
    return True
  if DictA['hgt'][-2:] == "cm" and checkInvalid(DictA['hgt'][:-2], 150, 193):
    return True
  if DictA['hgt'][-2:] == "in" and checkInvalid(DictA['hgt'][:-2], 59, 76):
    return True
  if not re.findall(r'^#[0-9a-f]{6}$', DictA['hcl']):
    return True
  if not re.findall(r'^\d{9}$', DictA['pid']):
    return True
  return False

def checkInvalid(ID, start, end):
  if (int(ID) < start or int(ID) > end):
    return True
  return False

counter1 = counter2 = 0
HeightUnits = ['cm', 'in']
EyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
SetA = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
for line in open(sys.argv[1]).read().split("\n\n"):
  for x in line.replace("\n", " ").split("\n"):
    DictA = dict([y.split(":") for y in x.split()])
    SetB = set(DictA)
    if len(SetA & SetB) < 7:
      break
    counter1 += 1
    if checkPassport(DictA):
      break
    counter2 += 1
print(counter1, counter2)
