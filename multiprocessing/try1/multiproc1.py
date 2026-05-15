import time
import os
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor, as_completed

def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f"Finished {seconds}"

if __name__ == "__main__":
    secs = [5, 4, 3, 2, 1]

    # 1. Sequential
    print("--- 1. Sequential Execution ---")
    start = time.perf_counter()
    for s in secs:
        print(do_something(s))
    print(f"Sequential took {time.perf_counter() - start:.2f}s\n")

    # 2. Multiprocessing.Process
    print("--- 2. Multiprocessing.Process ---")
    start = time.perf_counter()
    processes = []
    for s in secs:
        p = Process(target=do_something, args=(s,))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()
    print(f"Multiprocessing.Process took {time.perf_counter() - start:.2f}s\n")

    # 3. ProcessPoolExecutor
    print("--- 3. ProcessPoolExecutor ---")
    with ProcessPoolExecutor() as executor:
        # Տարբերակ Ա: map
        print("Using executor.map():")
        results = executor.map(do_something, secs)
        for r in results:
            print(r)

        # Տարբերակ Բ: submit + as_completed
        print("\nUsing executor.submit() + as_completed():")
        futures = [executor.submit(do_something, s) for s in secs]
        for f in as_completed(futures):
            print(f.result())