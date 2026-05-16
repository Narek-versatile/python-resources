import random
import concurrent.futures
import time

rows = 5000
cols = 5000

def gen():
    matrix = [[random.randint(0,100) for _ in range(cols)] for _ in range(rows)]
    return matrix

def prince_igor(r1, r2):
    lst = []
    for i, j in zip(r1, r2):
        lst.append(i+j)
    return lst

if __name__ == "__main__":
    m1 = gen()
    m2 = gen()
    # print(*m1, sep = "\n")
    print("\n\n\n")
    # print(*m2, sep = "\n")

    ##METHOD 1 -> 0.5085 seconds
    with concurrent.futures.ProcessPoolExecutor() as exe:
        x = time.perf_counter()
        rslt = exe.map(prince_igor, m1, m2)
        y = time.perf_counter()
        final = [i for i in rslt]

        print(f"parallel took {y-x:.4} seconds")
        print("\n\n\n-=-=-=-=-=-RESULT TIME-=-=-=-=-=-\n\n\n")
        # print(*final, sep = "\n")

    ##METHOD 2 -> 0.9171 seconds
    # final = []
    # x = time.perf_counter()
    # for r1, r2 in zip(m1, m2):
    #     final.append(prince_igor(r1, r2))
    # y = time.perf_counter()

    # print(f"parallel took {y-x:.4} seconds")
    # print("\n\n\n-=-=-=-=-=-RESULT TIME-=-=-=-=-=-\n\n\n")
    # print(*final, sep = "\n")
