import random
import string
import concurrent.futures

def parse_number(s):
    return int(s)

def gen(len = 100):
    return ''.join(random.choices(string.digits, k=len))

def gen_bad(len = 100):
    return ''.join(random.choices(string.digits + string.ascii_letters, k=len))

if __name__ == "__main__":
    # str1 = gen()
    # print(str1)
    # str2 = gen_bad()
    # print(str2) #testing gen() and gen_bad()

    megastr = ''.join([gen() for _ in range(5)] + [gen_bad() for _ in range(2)] + [gen() for _ in range(4)])
    # print(megastr)
    # for i in range(0, len(megastr), 100):
    #     print(megastr[i:i+100])

    with concurrent.futures.ProcessPoolExecutor() as exe:
        
        ##METHOD 1 -> if there is a single error, everything crashes
        # x = exe.map(parse_number, [megastr[i:i+100] for i in range(0, len(megastr), 100)])

        # for i in x:
        #     print(i)

        ##METHOD 2 -> in this case 6th and 7th reported about the error, others submitted their results
        bright_futures = dict()
        for i in range(0, len(megastr), 100):
            bright_futures[exe.submit(parse_number, megastr[i:i+100])] = i/100

        for i in concurrent.futures.as_completed(bright_futures):
            no = bright_futures[i]
            try:
                rslt = i.result()
                print(f"\n\nsuccessfully converted No{no+1} part of the string to int:\n{rslt}")
            except ValueError as f:
                print(f"seems like you got a ValueError for the No{no+1} part: {f}")
            except Exception as f:
                print(f"you've got an exception for the No{no+1} part: {f}")

                