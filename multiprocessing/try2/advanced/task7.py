import random
import concurrent.futures

def div(n):
    if not n:
        raise ZeroDivisionError("Error: Division by zero")

    return 100 / n


if __name__ == "__main__":
    numbers = [random.randint(-100, 100) for _ in range(1000)]

    # proc_count = 5
    # last = 0
    # step = int(len(numbers)/proc_count)
    # processes = []
    # for proc in range(1, proc_count + 1):
    #     if proc == proc_count:
    #         communism[proc] = numbers[last:]
    #         last = len(numbers)
    #         # x = multiprocessing.Process(target = div, args = (communism[proc],))
    #         # x.start()
    #         # processes.append(x)
    #         break

    #     communism[proc] = numbers[last:last + step]
    #     last += step
    #     # x = multiprocessing.Process(target = div, args = (communism[proc],))
    #     # processes.append(x)
    #     # x.start()

    with concurrent.futures.ProcessPoolExecutor() as exe:
        # for i in range(1, proc_count + 1):
        
        futures = {exe.submit(div, i):i for i in numbers}

        for completed in concurrent.futures.as_completed(futures):
            try:
                result = completed.result()
                print(f"got {result:.4} after doing (100/{futures[completed]})")
            except ZeroDivisionError as msg:
                print(f"!!!cant divide for zero: {msg}")
            except Exception as msg:
                print(f"!!!got an exception: {msg}")