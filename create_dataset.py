import os
import re
import shutil
import zipfile
from tqdm import tqdm

# specify the directory containing the X.sok files
dir_name = "/home/spinney/scratch/sokoban-solver/sokobanLevels/sok_files/Sokoban-small-v0"
base_dir = "/home/spinney/scratch/sokoban-solver/sokobanLevels/batchlevels/Sokoban-small-v0"

# iterate over the X.sok files in the directory
for data_file in tqdm(os.listdir(dir_name), desc="Processing files"):
    if data_file.endswith(".sok"):
        batch_num = data_file.split(".")[0] 
        with open(os.path.join(dir_name, data_file), "r") as f:
            input_text = f.read()

        # use regex to extract the levels and their maps
        levels = re.findall(r";(\d+)\n([\s\S]*?)(?=;\d|\Z)", input_text)

        tqdm.write(f"Found {len(levels)} levels in {data_file}")

        # create the batch directory
        batch_dir = os.path.join(base_dir, f"batch{batch_num}")
        os.makedirs(batch_dir, exist_ok=True)

        for i, level in enumerate(tqdm(levels, desc="Creating levels")):
            level_num = level[0]
            level_map = level[1].strip()
            fname = os.path.join(batch_dir, f"level{level_num}.txt")
            with open(fname, "w") as f:
                f.write(level_map)

        # compress the batch directory
        zip_file = f"{batch_dir}.zip" #os.path.join(base_dir, f"batch{batch_num}.zip")
        with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(batch_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, batch_dir)
                    zipf.write(file_path, arcname)

        # remove the uncompressed batch directory
        shutil.rmtree(batch_dir)

print("Done")
