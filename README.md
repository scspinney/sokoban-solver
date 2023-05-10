# sokoban-solver
Sokoban solver written in python with accompanying SLURM scripts. Modified from: https://github.com/KnightofLuna/sokoban-solver/blob/master/sokoban.py


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

It will print the solution to the terminal, and also save to sokobanLevels/solutions
