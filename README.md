# Gaussian Input Scripts Repository

This repository serves as a central hub for a collection of scripts designed to streamline Gaussian calculations. It includes a python script for generating input files with selected keywords and two python scripts for extracting optimized Cartesian coordinates, which can be used to generate a new input file or exporting results to text files for publication.

The easiest option to set up these scripts is to directly clone from the GitHub repository (the `git clone` command). Refer to Sierra and Austin's GitHub [instructions.](https://github.com/SigmanGroup/Git-Started)

_To set up the scripts on the CHPC:_
	
- Load git on the CHPC using:
  ```shell
    module load git
    ```
- Clone the repository from GitHub:
  ```shell
    git clone git@github.com:SigmanGroup/input-generator
    ```
- Move the shell scripts (*e.g.*, `g16_inpgen.py`) to your ~/bin folder.
  ```shell
    mv g16_inpgen.py ~/bin/
    ```
- Give the scripts user executable permissions, for example:
  ```shell
    chmod u+x g16_inpgen.py
    ```
## Instructions for the Python scripts:

### 1. Input Generator (g16_inpgen.py):

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

### 2. Optimized Geometry Extractor to New Input File (log_to_com.py)

The `log_to_com.py` Python script is designed to extract optimized geometries from output files (.log) and generate new input files for re-running Gaussian jobs. This can be helpful when optimization is completed, but single point calculations have failed for some reason.

#### Running the Script:

1. Run the script by executing the following command in the folder containing the output files (.log):
    ```shell
    python ~/bin/log_to_com.py
    ```
    The script will process all .log files in the folder, extracting optimized geometries from successfully terminated optimizations, and skipping files that have not terminated correctly. It will also provide a summary of how many new input files were generated and how many .log files have not terminated correctly.

   **Note:** This process will overwrite your old .com files. Remember to re-run the `g16_inpgen.py` Python script to add the necessary keywords to your new input files.

### 3. Optimized Geometry Extractor to Text File (log_to_txt.py)

The `log_to_txt.py` Python script is designed for extracting optimized geometries from output files (.log) and generating text files suitable for publication.

#### Running the Script:

1. Execute the script by running the following command in the folder containing the output files (.log):
    ```shell
    python ~/bin/log_to_txt.py
    ```
    The script will process all .log files in the folder, extracting optimized geometries from successfully terminated optimizations, and skipping files that have not terminated correctly. It will also provide a summary of how many new text files were generated and how many .log files have not terminated correctly.

   **Tips:** You can consider pushing the generated .txt files to a GitHub repository and use them as supplementary information for publication.

   

