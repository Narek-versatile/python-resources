import math
import multiprocessing

def check(num):
    if num < 0:
        return False

    temp = math.isqrt(num)
    return temp * temp == num


def sqrange(start, end, mail):
    rslt = []
    for i in range(start, end):
        if check(i):
            rslt.append(i)
    if len(rslt) == 0:
        mail.put([])
        return 
    mail.put(rslt)
    return 


if  __name__ == "__main__":
    rng = (100, 10000)
    
    #
    start = rng[0]
    end = rng[1]

    #
    proc_count = 7

    communism = dict()
    step = int((end - start)/proc_count)
    last = start
    proc_no = 0
    proc_pool = []
    tell = multiprocessing.Queue()
    while last < end:
        proc_no += 1
        if proc_no == proc_count:
            communism[proc_no] = (last, end)
            print(f"proc {proc_no} will handle range [{communism[proc_no][0]}:{communism[proc_no][1]}]")
            temp = multiprocessing.Process(target = sqrange, args = (communism[proc_no][0], communism[proc_no][1], tell))
            proc_pool.append(temp)
            temp.start()
            last = end
            break
        
        #will need to save tuple for each process number
        communism[proc_no] = (last, last + step)
        last += step
        temp = multiprocessing.Process(target = sqrange, args = (communism[proc_no][0], communism[proc_no][1], tell))
        proc_pool.append(temp)
        temp.start()

        print(f"proc {proc_no} will handle range [{communism[proc_no][0]}:{communism[proc_no][1]}]")


    temp = []

    for proc in proc_pool:
        temp.append(tell.get())

    for proc in proc_pool:
        proc.join()

    final = []
    for i in temp:
        final = final + i
    print(f"\n\n\nProgram executed successfully.\nResult:::{final}:::")