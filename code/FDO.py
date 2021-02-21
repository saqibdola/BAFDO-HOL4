import random
from random import randint
import math
import time
import psutil

def Fitness(guess,targetProof):
    fitness = 0
    for i in range(len(guess)):
        if guess[i] == targetProof[i]:
            if not (str(i)in fixedSlots):
                fixedSlots.append(str(i))
                # print(guess, fixedSlots)
            fitness+=1
    return fitness


def calculateVelocity(currentFitnessValue):
    pace =0
    y = random.uniform(1, -1)
    if currentFitnessValue == 0:
        fw = gBest
    else:
        fw = gBest / currentFitnessValue
    if (fw == 1 or fw == 0):
        x = math.floor(currentFitnessValue * y)
        pace = x
    elif ((0 < fw or fw < 1) and y < 0):
        x = math.floor((currentFitnessValue - gBest) * fw * (-1))
        pace = x
    elif ((0 < fw and fw < 1) and y >= 0):
        x = math.floor((currentFitnessValue -gBest) * fw)
        pace = x

    return pace


def multiPositionMutate(randomSequece, positions):
    for i in range(0, positions):
        while True:
            rn = randint(0, len(randomSequece)-1)
            if not (str(rn) in fixedSlots):
                randomSequece[rn] = random.choice(gSet)
                return randomSequence


            
positionFDO=1
#ite = []
totalIterations = 0
totalstartTime=time.time()
itertaion=0
startTime = time.time()
STime = time.time()


with open("Population.txt", 'r') as f: 
    p = f.read()
    gSet = p.split()


with open("PD.txt", 'r') as f:
    for line in f: #all the lines in f (proofs.txt)
        startTime = time.time()
        proof = line.split()
        gBest = len(proof)
        pBest = 0
        fixedSlots=[]
        randomSequence = []
        randomSequence = random.choices(gSet, k=len(proof))

        while pBest < gBest:
            multiPositionMutate(randomSequence,positionFDO)
            itertaion=itertaion+1
            totalIterations=totalIterations+1
            if totalIterations % 500 == 0:
                print (totalIterations, pBest, (time.time() - totalstartTime)) 
            fv=Fitness(randomSequence, proof)
            if pBest < fv:
                pBest = fv
                if pBest == gBest:
                    break
            positionFDO = calculateVelocity(fv)

            
mem = psutil.virtual_memory()  # .total / (1024.0 ** 2)
print('Total Itertations', totalIterations, pBest)
print("Total Time:", time.time() - STime)
print("Memory Used in Mb:", mem.used >> 20)
