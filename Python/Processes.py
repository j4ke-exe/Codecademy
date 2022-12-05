import multiprocessing
 
processes = []

# list of arguments to use
args = [arg1, arg2, arg3]

# iterate through the length of arguments
for i in range(len(args)):
  
  # create process
  p = multiprocessing.Process(target=target_function, args=(args[i],)
                              
  # add process to processes list
  processes.append(p)
                              
  # start process
  p.start()
                              
# join each process
for p in processes:
  p.join()
