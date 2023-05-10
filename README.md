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
 
