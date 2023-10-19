# Gaussian Input Scripts Repository

This repository serves as a central hub for a collection of scripts designed to streamline Gaussian calculations. It includes a python script for generating input files with selected keywords and two python scripts for extracting optimized Cartesian coordinates, which can be used to generate a new input file or exporting results to text files for publication.

The easiest option to set up these scripts is to directly clone from the GitHub repository (the `git clone` command). Refer to Sierra and Austin's GitHub [instructions.](https://github.com/SigmanGroup/Git-Started)

_To set up the scripts on the CHPC:_
	
- Load git on the CHPC using `module load git`
- Clone the repository from GitHub: `git clone git@github.com:SigmanGroup/input-generator`
- Move the shell scripts (*e.g.*, `g16_inpgen.py`) to your ~/bin folder. You can get rid of everything else.
- Give the scripts user executable permissions: `chmod u+x g16_inpgen.py` for example.

## Instructions for the Python scripts:

### Input Generator (g16_inpgen.py):

The `g16_inpgen.py` Python script is used to add Gaussian keywords to input files (.com), preparing them for execution.

#### Running the Script:

1. Run the script by executing the following command in the folder containing the input files (.com):
    ```shell
    python ~/bin/g16_inpgen.py
    ```
   **Note:** Ensure that the input files contain the charge and multiplicity of the molecule, and the XYZ coordinates.

2. An interactive script will open, providing options for changing the method, basis set, and keywords manually. For more details, refer to the 2023_03_08_Karas_Gaussian-Introduction workflow.

3. To proceed with the default level of theory, simply press Enter.

#### Default Options:

- Optimization and Frequency:
  
  `#N OPT FREQ Integral(Ultrafine) wB97XD def2SVP`

- Single Point job to compute NBO and Hirshfeld charges:
  
  `#N Guess=Read Geom=Check Integral(Ultrafine) Density Prop=(Potential,EFG) Volume Pop=NBO7 Pop=Hirshfeld Polar wB97XD def2TZVP`

- Single Point job to compute NMR shieldings and ChelpG charges:
  
  `#N Guess=Read Geom=Check Integral(Ultrafine) Density Pop=(ChelpG,ReadRadii) NMR wB97XD def2TZVP`
