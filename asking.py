# This function is to read the inforamation of processor and benchmarks from the user
def Variables():

    ProsNum=input('Please enter the number of processors to be evaluated?')
    Pro=[] #names of the processors will be saved in Pro
    for pros in range(int(ProsNum)):
        Pro.append(input(f'What is the name of processor#{pros+1}:'))

    BenchMarkNum=input('Please enter the number of benchmark programs run on each processor?')
    BenchMark=[] #names of the benchmarks will be saved in BenchMark
    for bench in range(int(BenchMarkNum)):
        BenchMark.append(input(f'What is the name of benchmark#{bench+1}:'))
    Result=[Pro,BenchMark]
    
     
    for i in range(int(ProsNum)):
        ExTime=[]#execution times will be saved in ExTime
        for j in range(int(BenchMarkNum)):
            ExTime.append(input(f'Please enter the execution time (in sec) for running benchmark {BenchMark[j]} on processor {Pro[i]}: '))
            
        Result.append(ExTime)
    
    return(Result)


