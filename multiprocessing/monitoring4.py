import os
import time
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor, as_completed

def monitored_task(n):
    pid = os.getpid()
    start_time = datetime.now().strftime("%H:%M:%S")
    print(f"● Task [{n}] started (PID: {pid}, Start Time: {start_time})")
    
    time.sleep(n) # Սիմուլյացիա
    
    end_time = datetime.now().strftime("%H:%M:%S")
    result = f"Finished {n}"
    print(f"● Task [{n}] finished (End Time: {end_time}, Result: {result})")
    return result

if __name__ == "__main__":
    tasks = [2, 4, 1, 3]
    print(f"Main Process PID: {os.getpid()}\n")
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(monitored_task, t) for t in tasks]
        # Սպասում ենք բոլորի ավարտին
        for f in as_completed(futures):
            f.result()