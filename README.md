# Gaussian Script Repository

This repository serves as a central hub for a collection of scripts designed to streamline Gaussian calculations. It includes a python script for generating input files with selected keywords and two python scripts for extracting optimized Cartesian coordinates, which can be used to generate a new input file or exporting results to text files for publication.

The easiest option to set up these scripts is to directly clone from the GitHub repository (the git clone command). Refer to Sierra and Austin's GitHub instructions.

_To set up submit scripts on the CHPC:_
	
 	Load git on the CHPC using module load git
	Clone the repository from GitHub: git clone git@github.com:SigmanGroup/CHPC_Submit_Scripts.git
	Move the shell scripts (e.g., subg16) to your ~/bin folder. You can get rid of everything else.
	Give the scripts user executable permissions: chmod u+x subg16 for example.
