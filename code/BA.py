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
             fitness+=1
     return fitness


def mutate(parent):
    ind = random.randint(0, len(parent) - 1)
    cGenes = list(parent)
    ng, alter = random.sample(gSet, 2) 
    if ng == cGenes[ind]:
        cGenes[ind] = alter
    return (cGenes)


def calculateVelocity(currentFitnessValue):
   fi = fmin + (fmax - fmin)*random.random()
   vi = math.floor(currentFitnessValue + ((gBest - currentFitnessValue)*fi))
   return vi


def multiPositionMutate(randomSequece, positions):
    for i in range(0, positions):
        while True:
            rn = randint(0, len(randomSequece)-1)
            if not (str(rn) in fixedSlots):
                randomSequece[rn] = random.choice(gSet)
                return randomSequence
               

                
positionBA=1
totalIterations = 0
totalstartTime=time.time()
startTime = time.time()
fmin = 0
fmax =10
ccccc=0
alpha = 0.8;
gamma = 0.9;
loudness = 1
r0 = 0.2


with open("Population.txt", 'r') as f: 
    p = f.read()
    gSet = p.split()


with open("PD.txt", 'r') as f:
    for line in f: #all the lines in f (proofs.txt)
        proof = line.split()
        gBest = len(proof)
        pBest = 0
        fixedSlots=[]
        itertaion = 0
        randomSequence = random.choices(gSet, k=len(proof))

        while pBest < gBest:
            randomSequence= multiPositionMutate(randomSequence,positionBA)
            itertaion=itertaion+1
            totalIterations=totalIterations+1
            if totalIterations % 500 == 0:
                print (totalIterations, pBest, (time.time() - totalstartTime))
            fv=Fitness(randomSequence, proof)
        
            if pBest < fv:
                pBest = fv
                if pBest == gBest:
                    break
            
                positionBA = calculateVelocity(fv)
                uloudenss = loudness * alpha
                ri = r0 * (1 - math.exp(-(gamma * totalIterations)))
                rc = ri + uloudenss
                loudness = uloudenss
                ra = random.random()
                if ra < rc:
                 mutate(randomSequence)
            

mem = psutil.virtual_memory()  
print('Total Itertations', totalIterations, pBest)
print("Total TimeBA:", time.time() - totalstartTime)
print("Memory Used in Mb:", mem.used >> 20)
