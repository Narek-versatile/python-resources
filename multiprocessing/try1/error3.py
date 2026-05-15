import time
from concurrent.futures import ProcessPoolExecutor, as_completed

def do_something_with_error(seconds):
    if seconds == 3:
        raise ValueError("Boom!")
    time.sleep(seconds)
    return f"Finished {seconds}"

if __name__ == "__main__":
    secs = [5, 4, 3, 2, 1]

    with ProcessPoolExecutor() as executor:
        print("--- Testing submit() + as_completed() with try/except ---")
        futures = {executor.submit(do_something_with_error, s): s for s in secs}
        
        for future in as_completed(futures):
            s = futures[future]
            try:
                result = future.result()
                print(result)
            except Exception as e:
                print(f"Task with {s} seconds generated an error: {e}")

        print("\n--- Testing map() (Will raise exception when iterating) ---")
        results = executor.map(do_something_with_error, secs)
        try:
            for r in results:
                print(r)
        except Exception as e:
            print(f"Map crashed with: {e}")