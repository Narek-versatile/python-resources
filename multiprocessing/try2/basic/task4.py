from datetime import datetime
import time
import os
import concurrent.futures
import multiprocessing

def task(n):
    # print(f"start {n} sleep")
    time.sleep(n)
    # print(f"finish {n} sleep")


if __name__ == "__main__":
    secs = [1, 2, 1, 4, 3, 10, 5, 3]
    processes = []
    for i in secs:
        z = multiprocessing.Process(target = task, args = (i,))
        x = z._args[0]
        processes.append((z, x))
        z.start()
        rn = datetime.now()
        print(f"task {x} started (PID : {z.pid}, Start Time: {rn.hour}:{rn.minute}:{rn.second})")

    for i, x in processes:
        i.join()
        rn = datetime.now()
        print(f"task {x} finished (Finish Time: {rn.hour}:{rn.minute}:{rn.second}, Result: Finished {x})")

    # with concurrent.futures.ProcessPoolExecutor() as exe:
    #     temp = exe.map(task, secs)
    #     print(temp)