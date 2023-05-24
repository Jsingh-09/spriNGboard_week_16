import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(1)
    return f'Done sleeping for {seconds}...'

def do_something_hard(seconds):
    for _ in range(90*seconds): # enough loops to take ~1 second
        arr = []
        for x in range(100000):
            arr.append(x)
    return f'Done doing hard things for {seconds}'

with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
    results = executor.map(do_something,      [1]*10) ## LINE A
    #results = executor.map(do_something_hard, [1]*10) ## LINE B
    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')

