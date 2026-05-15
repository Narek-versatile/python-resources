import os
import time
from PIL import Image
from itertools import repeat
import concurrent.futures

size = (16000, 16000)

def resize(filename, input_dir, output_dir):
    with Image.open(f"{input_dir}{filename}") as img:
        print(f"started doing {filename}")
        temp = img.resize(size, Image.Resampling.LANCZOS)
        temp.save(f"{output_dir}{filename}")
        print(f"finished doing {filename}")
        

if __name__ == "__main__":
    input_dir = f"{os.path.dirname(os.path.abspath(__file__))}\\images\\"
    print(f"set input to {input_dir}")
    output_dir = f"{os.path.dirname(os.path.abspath(__file__))}\\edited_images\\"
    print(f"set output to {output_dir}")

    

    if os.path.exists(input_dir):
        print("found input dir")
        
    if os.path.exists(output_dir):
        print("found output dir")
    else:
        os.makedirs(output_dir)
        print("made output dir")

    imgs = [i for i in os.listdir(input_dir)]
    print(f"starting operation with", *imgs)

    ##METHOD 1 -> 29.996 seconds
    # x = time.perf_counter()

    # for i in imgs:
    #     resize(i, input_dir, output_dir)

    # y = time.perf_counter()
    # print(f"done in {(y-x):.4}")

    ##METHOD 2 -> 20.79 seconds
    # x = time.perf_counter()

    # with concurrent.futures.ProcessPoolExecutor() as exe:
    #     exe.map(resize, imgs, repeat(input_dir), repeat(output_dir))

    # y = time.perf_counter()
    # print(f"done in {(y-x):.4}")