import os
import re

# specify the path to the file containing sok file paths
sok_list_file = "soklist1.txt"

# read the sok file paths from the file
with open(sok_list_file, "r") as f:
    sok_files = f.read().splitlines()

# iterate over the sok files
for sok_file in sok_files:
    if sok_file.endswith(".sok"):
        batch_num = os.path.basename(sok_file).split(".")[0]
        with open(sok_file, "r") as f:
            input_text = f.read()

        # use regex to extract the levels and their maps
        levels = re.findall(r";(\d+)\n([\s\S]*?)(?=;\d|\Z)", input_text)

        print(f"Found {len(levels)} levels in {sok_file}")
        # iterate over the levels and save each map to a separate file
        for i, level in enumerate(levels):
            #print(f"Creating level {i}")
            level_num = level[0]
            level_map = level[1].strip()
            batch_dir = f"sokobanLevels/batch{batch_num}"
            fname = os.path.join(batch_dir, f"level{level_num}.txt")
            if not os.path.exists(batch_dir):
                os.makedirs(batch_dir)

            with open(fname, "w") as f:
                f.write(level_map)

print("Done")

