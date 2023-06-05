import glob

# Use glob to retrieve filenames in the current directory matching the pattern "*.sok"
filenames = glob.glob("sokobanLevels/sok_files/*.sok")

# Split the filenames into two even lists
num_files = len(filenames)
half = num_files // 2
list1 = filenames[:half]
list2 = filenames[half:]

# Save the lists to files
list1_filename = "soklist1.txt"
list2_filename = "soklist2.txt"

with open(list1_filename, "w") as file:
    file.write("\n".join(list1))

with open(list2_filename, "w") as file:
    file.write("\n".join(list2))

# Print the confirmation message
print(f"List 1 saved to: {list1_filename}")
print(f"List 2 saved to: {list2_filename}")

