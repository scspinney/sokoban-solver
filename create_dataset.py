import os
import re

# specify the directory containing the X.sok files
dir_name = "sokobanLevels/sok_files"

# iterate over the X.sok files in the directory
for data_file in os.listdir(dir_name):
    if data_file.endswith(".sok"):
        batch_num = data_file.split(".")[0] 
        with open(os.path.join(dir_name, data_file), "r") as f:
            input_text = f.read()

        # use regex to extract the levels and their maps
        levels = re.findall(r";(\d+)\n([\s\S]*?)(?=;\d|\Z)", input_text)

        print(f"Found {len(levels)} levels in {data_file}")
        # iterate over the levels and save each map to a separate file
        for i, level in enumerate(levels):
            print(f"Creating level {i}")
            level_num = level[0]
            level_map = level[1].strip()
            batch_dir = f"sokobanLevels/batch{batch_num}"
            fname = os.path.join(batch_dir,f"level{level_num}.txt")
            if not os.path.exists(batch_dir):
                os.makedirs(batch_dir)
            
            with open(fname, "w") as f:
                f.write(level_map)
    break

print("Done")
