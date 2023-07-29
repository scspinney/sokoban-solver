# sokoban-solver
Sokoban solver written in python with accompanying SLURM scripts. Modified from: https://github.com/KnightofLuna/sokoban-solver/blob/master/sokoban.py.

**Note**

This will only run properly on Sokoban-small-v0 levels of size 7. The output of the algorithm would just need to be adjusted.


## Installtion on SLURM

```
module load python/3.8
virtialenv env
source env/bin/activate
pip install numpy
```

## Usage

To test, you can run the python command directly. It looks in sokobanLevels directory for files named "levelX.txt" where X is the file number. 

```
python sokoban.py -l level0.txt -m astar

```

## Updated info

Instructions for dataset creation Sokoban

1. Create levels using generate_maps.py under sokoban-gym (core)

2. Compress the maps into a tar file on Mila cluster and transfer to Cedar

3. Uncompress dataset, and run create_solver_dataset.sh to create all the sok files used by the solver, with the appropriate header

4. Run create_dataset.py (or _mp version, maybe also compress_existing_batches_mp.py if running after) which takes each sok file, splits each level into an individual file, then compresses the directory as a batch with batch_num

5. Combine all batches into one zipped file by running combine_batches.py and getting a combined_batches.zip file

6. Run the solver on the zipped combined file: solve_zipped_dataset.py. This takes in the combined_batches.zip file, processes each batch found in the zipped file using multiprocessing in batches, compresses the solution into solutions_zipped subdirectory (sokobanLevels), then removes the tmp unzipped directory used by the solver (sokoban.py). This takes time. A progress bar is shown.

7. Run X.py to combine all the solutions from each batch into one combined_solutions.zip file




X. Combine solutions into single file

## Older info

It will print the solution to the terminal, and also save to sokobanLevels/solutions. To run the slurm script as an array job you can run:

```
sbatch --array=1-$(find sokobanLevels/ -maxdepth 1 -type f | wc -l) run_solver_all_slurm
```

and inside that script you can change the number of jobs (default: 10) that are run simultaneously. OR 

```
sbatch --array=1-$(find sokobanLevels/ -maxdepth 1 -type f | wc -l) run_solver_all_slurm_safe
```
For a version that skips existing files that have a solution file already. If you want to run not as an array job but interactively (sometimes faster) run the folling:

```
 bash run_solver_all
 ```
 
 ## Unpack dataset
 
 You will probably have to unpack the dataset. If it's the tar file then run the following (so the output is under sokobanLevels):
 
 ```
 tar -xzvf sok_files.tar.gz
```
Followd by:

```
python create_dataset.py

```
 
