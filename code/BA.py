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


def mutate(parent):
    ind = random.randint(0, len(parent) - 1)
    cGenes = list(parent)
    ng, alter = random.sample(gSet, 2) #print("DFGH", nGene, alter) #x = []#while nGene == cGenes[ind]:
    if ng == cGenes[ind]:
        cGenes[ind] = alter
    return (cGenes)



def calculateVelocity(currentFitnessValue):
   #print('Current', currentFitnessValue)
   fi = fmin + (fmax - fmin)*random.random()
   #print('FIIIIIIIIIII', fi)
   vi = math.floor(currentFitnessValue + ((gBest - currentFitnessValue)*fi))
   #print('Viiiii', vi)
   return vi #2i

def multiPositionMutate(randomSequece, positions):
    # print("Length: " , len(fixedSlots))
    #if positions < len(fixedSlots):
      #  positions=len(randomSequece)-len(fixedSlots)
    #print("POSITION", positions)
    positionss= 2
    #randNumList = []
    for i in range(0, positions):
        while True:
            rn = randint(0, len(randomSequece)-1)
            if not (str(rn) in fixedSlots):
                #randNumList.append(str(rn))
              #  print(fixedSlots)
                randomSequece[rn] = random.choice(gSet)
                # print(randomSequece)
                # randomSequece[rn] = str(randint (1,20))
                # ng, alter = random.sample(gSet, 2)  # print("DFGH", nGene, alter) #x = []#while nGene == cGenes[ind]:
                # if ng == randomSequece[rn]:
                #     randomSequece[rn] = alter
                return randomSequence
               # break
positionBA=1
#fixedSlots=[]
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
with open("Population.txt", 'r') as f: #tokenize all the words in file guru99 into set 'a','b'
    p = f.read()
    gSet = p.split()

with open("PD.txt", 'r') as f:
    for line in f: #all the lines in f (proofs.txt)
        proof = line.split()
        gBest = len(proof)
        # print (proof)
        pBest = 0
        fixedSlots=[]
        itertaion = 0
        #randomSequence = []
        randomSequence = random.choices(gSet, k=len(proof))
#        ccccc=ccccc+1
     #   if ccccc % 10 == 0:
      #  print ("more : ", ccccc )
        while pBest < gBest:
            # print("RS: ", randomSequence)
            randomSequence= multiPositionMutate(randomSequence,positionBA)
            #print('after new position', randomSequence)

            #positionPSO= randomchange(NS)
            #multiPositionMutate(NS, positionPSO)
            itertaion=itertaion+1
            totalIterations=totalIterations+1
            if totalIterations % 500 == 0:
                print (totalIterations, pBest, (time.time() - totalstartTime))
         #   print ("RS: ", randomSequence)
         #   print("TS: ", proof)
            fv=Fitness(randomSequence, proof)
            # print("RS: ", randomSequence)
            # print (fv)
            if pBest < fv:
                #startTime=time.time()
                pBest = fv
                if pBest == gBest:
                    break
            # nextVelocity= velocity + C1 * random.random() *(pBest - fv)+ C2*random.random()*(gBest-fv)
                positionBA = calculateVelocity(fv)
                uloudenss = loudness * alpha
            #print('Loudness', uloudenss)
                ri = r0 * (1 - math.exp(-(gamma * totalIterations)))
            #print('pulse', ri)
            #print('Total', ri + uloudenss)
                rc = ri + uloudenss
                loudness = uloudenss
            #rc = randomchange(totalIterations)
                ra = random.random()
            #    print('loudness+emission', ri, loudness, rc)
            #    print('random', ra)
                if ra < rc:
                 #print('HIIIIIIIIIIII')
                 mutate(randomSequence)
            #     print('Mutated Child', mutate(randomSequence))


mem = psutil.virtual_memory()  # .total / (1024.0 ** 2)
# print(itertaion)
print('Total Itertations', totalIterations, pBest)
print("Total TimeBA:", time.time() - totalstartTime)
print("Memory Used in Mb:", mem.used >> 20)

# velocty ka function
# make other code for removed optimization
# hill climbing
# increase dataset
