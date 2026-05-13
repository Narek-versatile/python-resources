import multiprocessing
import time


#define 2 functions that take time
def cook1():
    print("start cook1")
    time.sleep(3)
    print("finish cook1")

def cook2():
    print("start cook2")
    time.sleep(6)
    print("finish cook2")


if __name__ == "__main__":
            
    start = time.perf_counter()

    #create objects
    proc1 = multiprocessing.Process(target = cook1)
    proc2 = multiprocessing.Process(target = cook2)

    #start processes
    proc1.start()
    proc2.start()

    #make sure all processes are finished before going on
    proc1.join()
    proc2.join()

    #measure time
    end = time.perf_counter()

    #show time
    print(f"Execution time: {end - start:.4f} seconds")


    