import time
import os
from PIL import Image
from concurrent.futures import ProcessPoolExecutor

# Define your paths clearly
IMAGE_DIR = r"C:\Users\Owner\Desktop\Global\01Prog\Python\Python ACT\multiprocessing\images"
OUTPUT_DIR = r"C:\Users\Owner\Desktop\Global\01Prog\Python\Python ACT\multiprocessing\processed"

def process_image(img_name):
    try:
        input_path = os.path.join(IMAGE_DIR, img_name)
        output_path = os.path.join(OUTPUT_DIR, img_name)
        
        with Image.open(input_path) as img:
            img = img.resize((800, 800))
            img.save(output_path)
        return f"{img_name} processed"
    except Exception as e:
        return f"Error processing {img_name}: {e}"

if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    if not os.path.exists(IMAGE_DIR):
        print(f"Error: Directory not found: {IMAGE_DIR}")
    else:
        img_names = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        # 1. Sequential
        print("Starting sequential processing...")
        start_seq = time.perf_counter()
        for name in img_names:
            process_image(name)
        seq_time = time.perf_counter() - start_seq
        print(f"Sequential time: {seq_time:.2f}s")

        # 2. Parallel
        print("\nStarting parallel processing...")
        start_par = time.perf_counter()
        with ProcessPoolExecutor() as executor:
            list(executor.map(process_image, img_names))
        par_time = time.perf_counter() - start_par
        print(f"Parallel time: {par_time:.2f}s")

        print(f"\nSpeedup: {seq_time / par_time:.2f}x faster")