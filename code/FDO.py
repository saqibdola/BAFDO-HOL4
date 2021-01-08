import random
from random import randint
import math
import time
import psutil

def Fitness(guess,targetProof):
    fitness = 0
   # print("Guess",len(guess))
    for i in range(len(guess)):
        if guess[i] == targetProof[i]:
            if not (str(i)in fixedSlots):
                fixedSlots.append(str(i))
                # print(guess, fixedSlots)
            fitness+=1
 #  print(fitness)
    return fitness


def calculateVelocity(currentFitnessValue):
    pace =0
    y = random.uniform(1, -1)
    #z = random.uniform(1, 0)
    if currentFitnessValue == 0:
        fw = gBest
    else:
        fw = gBest / (currentFitnessValue)
    #print('FW', fw)
    #print('ASDF', math.floor((math.floor(gBest - pBest)) - fw))  # andom.uniform(1,0
    #return math.floor((math.floor(gBest - pBest) - fw))#andom.uniform(1,0
    #print('ASDF', math.floor((math.floor(gBest - pBest)) - fw))#andom.uniform(1,0
        #pace = x
   # print('FW', fw)
    #print('RANDOM', y)
    if (fw == 1 or fw == 1):
        x = math.floor(currentFitnessValue * y)
        pace = x
    elif ((0 < fw or fw < 1) and y < 0):
        x = math.floor((currentFitnessValue - gBest) * fw * y)
        pace = x
    elif ((0 < fw and fw < 1) and y >= 0):
        x = math.floor((currentFitnessValue -gBest) * fw)
        pace = x

    #print('pace', pace)
    return pace
    #    print('pace', pace)


def multiPositionMutate(randomSequece, positions):
    # print("Length: " , len(fixedSlots))
    #if positions < len(fixedSlots):
      #  positions=len(randomSequece)-len(fixedSlots)
    #print("POSITION", positions)
    positionss= 2
    randNumList = []
    for i in range(0, positions):
        while True:
            rn = randint(0, len(randomSequece)-1)
            if not (str(rn) in randNumList or str(rn) in fixedSlots):
                #randNumList.append(str(rn))
              #  print(fixedSlots)
                randomSequece[rn] = random.choice(gSet)
                # print(randomSequece)
                # randomSequece[rn] = str(randint (1,20))
                # ng, alter = random.sample(gSet, 2)
                # print("DFGH", nGene, alter) #x = []#while nGene == cGenes[ind]:
                # if ng == randomSequece[rn]:
                #     randomSequece[rn] = alter
                break

#velocity=1
#nextVelocity=0
positionFDO=1
#ite = []
totalIterations = 0
#gBest=0
itertaion=0
startTime = time.time()
STime = time.time()
#ccccc=0
#pace = 0


with open("Population.txt", 'r') as f: #tokenize all the words in file guru99 into set 'a','b'
    p = f.read()
    gSet = p.split()

with open("PD.txt", 'r') as f:
    for line in f: #all the lines in f (proofs.txt)
        startTime = time.time()
        proof = line.split()
        gBest = len(proof)
        # print (proof)
        pBest = 0
        fixedSlots=[]
        #itertaion = 0
        randomSequence = []
        randomSequence = random.choices(gSet, k=len(proof))
#        ccccc=ccccc+1
     #   if ccccc % 10 == 0:
      #  print ("more : ", ccccc )
        while pBest < gBest:
            # print("RS: ", randomSequence)
            multiPositionMutate(randomSequence,positionFDO)
            itertaion=itertaion+1
            totalIterations=totalIterations+1
            if totalIterations % 500 == 0:
                print (totalIterations, pBest) #, (time.time()-startTime))
         #   print ("RS: ", randomSequence)
         #   print("TS: ", proof)
            fv=Fitness(randomSequence, proof)
            # print("RS: ", randomSequence)
            # print (fv)
            if pBest < fv:
         #       ccccc=ccccc+1
             #   if (ccccc<=81):
            #        print (ccccc, " ",time.time()-startTime )
                startTime=time.time()
                pBest = fv
                if pBest == gBest:
                    break
            # nextVelocity= velocity + C1 * random.random() *(pBest - fv)+ C2*random.random()*(gBest-fv)
            positionFDO = calculateVelocity(fv)
mem = psutil.virtual_memory()  # .total / (1024.0 ** 2)
# print(itertaion)
print('Total Itertations', totalIterations, pBest)
print("Total Time:", time.time() - STime)
print("Memory Used in Mb:", mem.used >> 20)

# velocty ka function
# make other code for removed optimization
# hill climbing
# increase dataset
