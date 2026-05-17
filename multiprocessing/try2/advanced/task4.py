import os
import random
import concurrent.futures
from datetime import datetime
import math

def div(n):
    lst = []

    if n <= 0:
        raise ValueError(f"cannot calculate for {n}")

    for i in range(1, int(n / 2 + 1)):
        if n % i == 0:
            lst.append(i)

    return lst + [n]


if __name__ == "__main__":
    todo = [random.randint(1,100) for _ in range(5)]

    with concurrent.futures.ProcessPoolExecutor() as exe:

        db = dict()

        for do in todo:
            db[exe.submit(div, do)] = do
            rn = datetime.now()
            print(f"Task [{do}] started //\\\\// (PID: {os.getpid()}, Start Time: {rn.hour}:{rn.minute}:{rn.second})")

        for done in concurrent.futures.as_completed(db):
            try:
                rslt = done.result()
            except ValueError as msg:
                rslt = msg
            except Exception as msg:
                rslt = msg

            rn = datetime.now()
            print(f"Task [{db[done]}] finished //!!// (End Time: {rn.hour}:{rn.minute}:{rn.second}, Result: {rslt})")
            
