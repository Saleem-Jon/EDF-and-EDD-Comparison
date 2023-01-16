# -*- coding: utf-8 -*-
"""EDF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RY6PbtaYaAqySi9eIHrw6oiBG5hBD1aO

# **FUNCTIONS & CLASSES**

---
"""

import random 
import tracemalloc
import time

class Tasks:
    def __init__(self, ai, ci, di):
        self.ai = ai
        self.ci = ci
        self.di = di
        self.li = ci
    


def makeTasks(n,EDF = True):
    tasks = []
    ai = 0
    ci = 0
    di = 0
    for i in range(n):
        ci = random.randint(1, 6)
        di = random.randint(ci+(ai+ci), ci*(ai+2+n))
        t = Tasks(ai, ci, di)   
        
        if EDF:
          ai = random.randint(0, n)
        else:
          ai = 0
        tasks.append(t)
    return tasks





#Printing the Tasks
def printTasks(tasks,flag = False):
    if flag:
        print("{:^20s}{:^20s} {:^20s} {:^20s}{:^20s}".format("","Arrival Time :"," computation Time :"," Deadline :"," Computation left"))
        n = 0
        for i in tasks:
            n +=1
            
            print("{:^20s}{:^20s} {:^20s} {:^20s}{:^20s}".format(("Task "+str(n)),str(i.ai), str(i.ci), str(i.di), str(i.li)))
    if not flag:
        print("{:^20s}{:^20s} {:^20s} {:^20s}".format("","Arrival Time :"," computation Time :"," Deadline "))
        n = 0
        for i in tasks:
            n +=1
            
            print("{:^20s}{:^20s} {:^20s} {:^20s}".format(("Task "+str(n)),str(i.ai), str(i.ci), str(i.di)))


#Sorts the task according to deadline time
def scheduleTasks_d(tasks):
    sTasks = tasks
    for i in range(len(sTasks)):
        for j in range(i,len(sTasks)):
            if sTasks[i].di > sTasks[j].di:
                x = sTasks[i]
                sTasks[i] = sTasks[j]
                sTasks[j] = x
    return sTasks




#Sorts the task according to Arrival time
def scheduleTasks(tasks):
    sTasks = scheduleTasks_d(tasks)
    for i in range(len(sTasks)):
        for j in range(i,len(sTasks)):
            if sTasks[i].ai > sTasks[j].ai:
                x = sTasks[i]
                sTasks[i] = sTasks[j]
                sTasks[j] = x
    return sTasks




def find_deadline(tasks):
    deadline = 0
    for i in tasks:
        if i.di > deadline:
            deadline = i.di
    return deadline


#Schedules with EDF
def EDF(tasks,step = 1):
    steps = step
    tasks_a = scheduleTasks(tasks)
    deadline = find_deadline(tasks)
    iteration = 0
    
    for i in range(0,deadline,steps): #acts as a counter and stepper
    #check if all tasks are done
     
        
        execute = 0 #The task to be executed
        stop = True # this will stop the scheduling if all tasks are done
        for t in range(0,len(tasks_a)):
            if tasks_a[t].li > 0:
                stop = False
                if (tasks_a[execute].li <=0  and tasks_a[t].ai <= i) or (tasks_a[execute].ai >= i and tasks_a[t].ai <= i):
                    execute = t
                    
                    break
        print("\n\n")      
        print("Iteration "+str(iteration))
        print("Time "+str(i)) 
        printTasks(tasks_a,True)            
        iteration +=1
        
        
        
        for j in range(0,len(tasks_a)): #checks for earliest deadline task availability
            if tasks_a[j].ai <= i and tasks_a[j].li > 0: 
                for k in range(j,len(tasks_a)):
                    if tasks_a[k].ai <= i and tasks_a[k].li > 0:
                        if tasks_a[k].di < tasks_a[j].di :
                            if tasks_a[k].di < tasks_a[execute].di:
                                
                                execute = k
                                print("ARRIVAL "+ str(tasks_a[execute].ai))
                                print("TASK " + str(k+1))
                            # else:
                            #     execute = k
                            #     print("In ELSE : ARRIVAL "+ str(tasks_a[execute].ai))
                            #     print("In ELSE :  TASK " + str(k+1))
               
                
            
           
        
        if tasks_a[execute].li >0:
            tasks_a[execute].li = tasks_a[execute].li - step
        if stop:
            return tasks_a
    return tasks_a




def EDD(task):
    tasks = scheduleTasks_d(task)
    iteration = 0
    for i in range(0,len(tasks)):
       
        tasks[i].li = 0 
        print("\n\n")      
        print("Iteration "+str(iteration))
        print("Time "+str(i)) 
        printTasks(tasks,True)            
        iteration +=1
        printTasks(tasks,True)

"""# **MAIN**

---

*EDF IMPLEMENTED*
"""

#-----------------------------------MAIN----------------------------------------
number_of_tasks = 10


tasks = makeTasks(number_of_tasks)
# tasks = []

# for i in range(0,10,2):
#     task = Tasks(0+i, 2, i+3)
#     tasks.append(task)
    
printTasks(tasks)
print('\n\n')

# scheduledTasks = scheduleTasks(tasks)
# print("Scheduled Tasks")
# printTasks(scheduledTasks)
# print('\n\n')


# scheduledTasks = scheduleTasks_d(tasks)
# print("Scheduled Tasks")
# printTasks(scheduledTasks)



# get the start time
st = time.time()
tracemalloc.start()


edf = EDF(tasks)
# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print("\n")
print('Execution time:', elapsed_time, 'seconds')

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")

print("Memory used "+str(peak/ 10**6 -current/ 10**6)+" MB")

tracemalloc.stop()


# c_time = 0
# d_time = 0
# for i in tasks:
#     c_time += i.ci
#     # if d_time < i.di:
#     #     d_time = i.di
#     d_time +=i.di
# print(c_time)

# print(d_time/len(tasks))

"""# **EDD**

---


"""

number_of_tasks = 10

tasks = []
tasks = makeTasks(number_of_tasks,False)
printTasks(tasks)
# get the start time
st = time.time()
tracemalloc.start()
EDD(tasks)
# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print("\n")
print('Execution time:', elapsed_time, 'seconds')

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")

print("Memory used "+str(peak/ 10**6 -current/ 10**6)+" MB")

tracemalloc.stop()

"""# **GRAPH**

---


"""

import matplotlib.pyplot as plt

def runcomparison():
  number_of_tasks = 0
  x = []
  y = []
  z = []
  for i in range(20):
   
    number_of_tasks += 5
    
    tasks = []
    tasks = makeTasks(number_of_tasks,False)
    # get the start time
    st = time.time()
    tracemalloc.start()
    EDD(tasks)
    # get the end time
    et = time.time()

    # get the execution time
    elapsed_time = et - st
    y.append(elapsed_time)
    x.append(number_of_tasks)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")

    print("Memory used "+str(peak/ 10**6 -current/ 10**6)+" MB")
    z.append((peak/ 10**6 -current/ 10**6))
    tracemalloc.stop()

  return x,y,z


  
xpoints,ypoints ,zpoints= runcomparison()
plt.plot(xpoints, ypoints)
plt.plot(xpoints, zpoints)
plt.show()

"""# Comparison of both EDD and EDF
*Different Task sets*
"""

import matplotlib.pyplot as plt

def runComparison_differentTaskSet(flag = True):
  number_of_tasks = 0
  x = []
  y = []
  z = []
  for i in range(1000):
    number_of_tasks += 5
    
    tasks = []
    
    tasks = makeTasks(number_of_tasks,flag)
    # get the start time
    st = time.time()
    tracemalloc.start()
    if flag:
      EDF(tasks)
    else:
      EDD(tasks)
    # get the end time
    et = time.time()

    # get the execution time
    elapsed_time = et - st
    y.append(elapsed_time)
    x.append(number_of_tasks)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")

    print("Memory used "+str(peak/ 10**6 -current/ 10**6)+" MB")
    z.append((peak/ 10**6 -current/ 10**6))
    tracemalloc.stop()

  return x,y,z


  
xpoints,ypoints ,zpoints= runComparison_differentTaskSet(True)


plt.subplot(1, 2, 1) # row 1, col 2 index 1
plt.plot(xpoints, ypoints, label="Time")
plt.plot(xpoints, zpoints, label="Space")
plt.title("EDF")
plt.xlabel(' Tasks ')
plt.ylabel(' Time ')
  
xpoints,ypoints ,zpoints= runComparison_differentTaskSet(False) 

plt.subplot(1, 2, 2) # index 2
plt.plot(xpoints, ypoints, label="Time")
plt.plot(xpoints, zpoints, label="Space")
plt.title("EDD")
plt.xlabel(' Tasks ')
plt.ylabel(' Time ')






plt.show()

"""# Comparison of both EDD and EDF
*Same Task sets*
"""

import matplotlib.pyplot as plt

def runcomparison_sameTaskSet():
  number_of_tasks = 0
  edf_x = []
  edf_y = []
  edf_z = []
  edd_x = []
  edd_y = []
  edd_z = []
  for i in range(100):
    number_of_tasks += 5
    
    tasks_edd = []
    tasks_edf = makeTasks(number_of_tasks,True)
    for i in tasks_edf:
      i_t = i 
      i_t.ai = 0
      tasks_edd.append(i_t)
    # get the start time

    st = time.time()
    tracemalloc.start()
    EDF(tasks_edf)
    # get the end time
    et = time.time()

  

    # get the execution time
    elapsed_time = et - st
    edf_y.append(elapsed_time)
    edf_x.append(number_of_tasks)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")

    print("Memory used "+str(peak/ 10**6 -current/ 10**6)+" MB")
    edf_z.append((peak/ 10**6 -current/ 10**6))
    tracemalloc.stop()


    st = time.time()
    tracemalloc.start()
    EDD(tasks_edd)
   # get the end time
    et = time.time()

    # get the execution time
    elapsed_time = et - st
    edd_y.append(elapsed_time)
    edd_x.append(number_of_tasks)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")

    print("Memory used "+str(peak/ 10**6 -current/ 10**6)+" MB")
    edd_z.append((peak/ 10**6 -current/ 10**6))
    tracemalloc.stop()
  return edf_x,edf_y,edf_z,edd_x,edd_y,edd_z


  
edf_x,edf_y,edf_z,edd_x,edd_y,edd_z= runcomparison_sameTaskSet()

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.subplot(1, 2, 1) # row 1, col 2 index 1
plt.plot(edf_x, edf_y, label="Time")
plt.plot(edf_x, edf_z, label="Space")
plt.title("EDF")
plt.xlabel(' Tasks ')
plt.ylabel(' Time ')
  


plt.subplot(1, 2, 2) # index 2
plt.plot(edd_x, edd_y, label="Time")
plt.plot(edd_x, edd_z, label="Space")
plt.title("EDD")
plt.xlabel(' Tasks ')
plt.ylabel(' Time ')






plt.show()

"""# **Experimental** **Cell**"""

import random 
import tracemalloc
import time
import matplotlib.pyplot as plt

#Sorts the task according to deadline time
def scheduleTasks_d(tasks):
    sTasks = tasks
    for i in range(len(sTasks)):
        for j in range(i,len(sTasks)):
            if sTasks[i].di > sTasks[j].di:
                x = sTasks[i]
                sTasks[i] = sTasks[j]
                sTasks[j] = x
    return sTasks

def find_deadline(tasks):
    deadline = 0
    for i in tasks:
        if i.di > deadline:
            deadline = i.di
    return deadline


#Sorts the task according to Arrival time
def scheduleTasks(tasks):
    sTasks = scheduleTasks_d(tasks)
    for i in range(len(sTasks)):
        for j in range(i,len(sTasks)):
            if sTasks[i].ai > sTasks[j].ai:
                x = sTasks[i]
                sTasks[i] = sTasks[j]
                sTasks[j] = x
    return sTasks

class Tasks:
    def __init__(self, ai, ci, di):
        self.ai = ai
        self.ci = ci
        self.di = di
        self.li = ci
    


def makeTasks(n,EDF = True):
    tasks = []
    ai = 0
    ci = 0
    di = 0
    for i in range(n):

        ci = 1 #random.randint(1, 6)
        di = random.randint(ci+(ai+ci), ci*(ai+2+n))
        t = Tasks(ai, ci, di)   
        
        if EDF:
          ai = random.randint(0, n)
        else:
          ai = 0
        tasks.append(t)
    return tasks


def EDD(task):
    tasks = scheduleTasks_d(task)
    
    for i in range(len(tasks)):
        tasks[i].li = 0 
        


#Schedules with EDF
def EDF(tasks,step = 1):
    steps = step
    tasks_a = scheduleTasks(tasks)
    deadline = find_deadline(tasks)
    iteration = 0
     #The task to be executed
    for i in range(deadline): #acts as a counter and stepper
    #check if all tasks are done
        execute = tasks_a[0]
        
       
        stop = True # this will stop the scheduling if all tasks are done
        for t in tasks_a:
            if t.li > 0:
                stop = False
                if (execute.li <=0  and t.ai <= i) or (execute.ai >= i and t.ai <= i):
                    execute = t        
                    break
            else:
                tasks_a.remove(t)
                
        iteration +=1
        
        
        
        for j in tasks_a: #checks for earliest deadline task availability
            if j.ai <= i and j.li > 0: 
                for k in tasks_a:
                    if k.ai <= i and k.li > 0:
                        if k.di < j.di :
                            if k.di < execute.di:
                                
                                execute = k
                                
    
        
        if execute.li >0:
            execute.li = execute.li - step
        if stop:
            return tasks_a
    return tasks_a




def runcomparison():
  number_of_tasks = 100
  x = []
  y = []
  z = []
  
   
    
  tasks = []
  tasks = makeTasks(number_of_tasks,False)
  # get the start time
  st = time.time()

  EDD(tasks)
  # get the end time
  et = time.time()

  # get the execution time
  elapsed_time = et - st
  y.append(elapsed_time)
  x.append(number_of_tasks)
    

  print(y[0])
  return x,y,z


  
xpoints,ypoints ,zpoints= runcomparison()
#plt.plot(xpoints, ypoints)
#plt.plot(xpoints, zpoints)
#plt.show()