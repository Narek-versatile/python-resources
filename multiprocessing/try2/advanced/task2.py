import secrets
import string
import time
import concurrent.futures

def gen(len = 16):
    x = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(x) for _ in range(len))

# print(password()) #checking password() functionality
# print(password())


if __name__ == "__main__":
    passwords = [gen() for _ in range(1000)]
    # print(passwords)
    print(f"\n\nthere are {len(passwords)} passwords generated")
    
    ##METHOD 1 -> 0.0001035 seconds
    x = time.perf_counter()
    hashed = []
    for password in passwords:
        hashed.append(hash(password))
    y = time.perf_counter()
    print(f"there are {len(hashed)} hashed passwords")
    print(f"Method 1 took {y-x:.4} seconds")


    ##METHOD 2 -> 0.6377 seconds
    # x = time.perf_counter()
    # with concurrent.futures.ProcessPoolExecutor() as exe:
    #     result = exe.map(hash, passwords)
    #     final = [i for i in result]
    # y = time.perf_counter()

    # print(f"Method 2 took {y-x:.4} seconds")