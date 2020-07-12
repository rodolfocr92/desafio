import numpy as np
import threading
import time

def getRand():
  a = np.random.rand()*1.005
  if (a > 1) :
    return getRand()
  else :
    return a

def makeArray(n):
  vector = []
  for i in range(n):
    vector.append(np.random.randint(-50,50))
    #vector.append(getRand()*100 - 50)
  return vector


def runCumulative(interval, vector, N, k, **totalSum):
  lock = threading.Lock()
  if (interval != k - 1):
    for value in vector[interval*(N//k):(interval+1)*(N//k)]:
      lock.acquire()
      sumThreads['sumThreads'] += value
      lock.release()
  else: 
    for value in vector[interval*(N//k):]:
      lock.acquire()
      sumThreads['sumThreads'] += value
      lock.release()

def multiCumulative(vector, N, k, sumThreads):
  for i in range(k):
    t = threading.Thread(target=runCumulative, args=(i, vector, N, k,), kwargs=sumThreads)
    t.start()
    t.join()


def run(interval, vector, N, k, sumArray):
  if (interval != k - 1):
    for value in vector[interval*(N//k):(interval+1)*(N//k)]:
      sumArray[interval] += value
  else: 
    for value in vector[interval*(N//k):]:
      sumArray[interval] += value

def multi(vector, N, k):
  sumArray = [0] * k
  for i in range(k):
    t = threading.Thread(target=run, args=(i, vector, N, k, sumArray))
    t.start()
    t.join()
  summ = 0
  for threadSum in sumArray:
    summ += threadSum
    


#Programa para calcular média do tempo de cálculo da soma em T períodos  
  
N = 100000
k = 1
T = 1000

timeSumMulti = 0
timeSum = 0
vector = makeArray(N)


for i in range(T):

  sumThreads = {'sumThreads': 0}

  time_1 = time.time()
  multiCumulative(vector, N, k, sumThreads)
  time_2 = time.time()
  timeSumMulti += (time_2 - time_1)

  time_3 = time.time()
  multi(vector, N, k)
  time_4 = time.time()

  timeSum += (time_4 - time_3)

print("Tempo médio da soma com variável cumulativa: ", timeSumMulti/T)
print("Tempo médio da soma multi: ", timeSum/T)


