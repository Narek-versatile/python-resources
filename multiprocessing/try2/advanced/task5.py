import random
import multiprocessing
import re

def match(wanted, dna, offset, tell):
    matches = re.finditer(re.escape(wanted), dna)
    
    if not matches:
        tell.put(None)
        return

    tell.put([(match.start() + offset, match.end() + offset) for match in matches])
    # ...
    # found = [] #inside there will be tuples of indexes (start, finish)

    # if len(found) == 0:
    #     return None

    # return found

if __name__ == "__main__":
    tell = multiprocessing.Queue()

    dna_lenght = 600
    dna = ''.join(random.choice("ACTG") for _ in range(dna_lenght))

    wanted_lenght = 4
    wanted = ''.join(random.choice("ACTG") for _ in range(wanted_lenght))

    proc_count = 6

    #dna parts
    last = 0
    step = int((len(dna) - (len(wanted) - 1)) / proc_count)
    proc_no = 0
    parts = dict()
    part_start = dict()
    while last < len(dna):
        proc_no += 1
        if (len(dna) - last < step + len(wanted) + 1) or proc_no == proc_count:
            parts[proc_no] = dna[last:]
            part_start[proc_no] = last
            print(f"proc {proc_no} got the part [{last}:]")
            print(":::", parts[proc_no])

            last = len(dna)
            break
        
        parts[proc_no] = dna[last:last+step+len(wanted) - 1]
        part_start[proc_no] = last

        print(f"proc {proc_no} got the part [{last}:{last+step+len(wanted) - 1}]")
        print(":::", parts[proc_no])

        last+=step


    print(f"\n\nstarting the search for ::: {wanted} :::\n\n")
    proc_pool = []
    
    last_checked = 0
    for pt in range(proc_count):
        x = multiprocessing.Process(target = match, args = (wanted, parts[pt + 1], part_start[pt + 1], tell))
        proc_pool.append(x)
        x.start()
        print(f"started process no{pt+1} with args ; ({wanted}, {parts[pt + 1]}, {part_start[pt + 1]})\n\n")
   

    results = [tell.get() for _ in proc_pool]

    for proc in proc_pool:
        proc.join()

    print(results)

    print("\n\n\n")
    #printing out
    for lst in results:
        if not len(lst):
            continue
        for tpl in lst:
            if not len(tpl):
                continue
            print(f"found {dna[tpl[0]:tpl[1]]} in indexes [{tpl[0]}:{tpl[1]}] :::searched for [{wanted}]")