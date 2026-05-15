import multiprocessing
from concurrent.futures import ProcessPoolExecutor, as_completed
import time

def slp(i):
    print(f"slping {i} seconds")
    time.sleep(i)
    # print(f"slpt {i} seconds")
    return f"slpt {i} seconds"


if __name__ == "__main__":
    secs = [5, 4, 3, 2, 1]

    ##METHOD 1
    # for i in secs:
    #     slp(i)

    # #METHOD 2
    # processes = []

    # for i in secs:
    #     temp = multiprocessing.Process(target = slp, args=(i,))
    #     temp.start()
    #     processes.append(temp)
        
    # for process in processes:
    #     process.join()
        
    ##METHOD 3A
    # with ProcessPoolExecutor() as exe:
    #     results = exe.map(slp, secs)
    #     for result in results:
    #         print(result)

    ##METHOD 3B
    # with ProcessPoolExecutor() as exe:
    #     futuress = [exe.submit(slp, i) for i in secs]
    #     print(f"futures: {futuress}")

    #     for i in as_completed(futuress):
    #         print(i.result())

        