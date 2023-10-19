#Gaussian .log to .txt with optimized xyz coordinates 

import os
import re

#--------------------------------------------------
periodic_table = {1: "H", 2: "He", 3: "Li", 4: "Be", 5: "B", 6: "C", 7: "N", 8: "O", 9: "F", 10: "Ne", 
                  11: "Na", 12: "Mg", 13: "Al", 14: "Si", 15: "P", 16: "S", 17: "Cl", 18: "Ar", 19: "K", 20: "Ca", 
                  21: "Sc", 22: "Ti", 23: "V", 24: "Cr", 25: "Mn", 26: "Fe", 27: "Co", 28: "Ni", 29: "Cu", 30: "Zn", 
                  31: "Ga", 32: "Ge", 33: "As", 34: "Se", 35: "Br", 36: "Kr", 37: "Rb", 38: "Sr", 39: "Y", 40: "Zr", 
                  41: "Nb", 42: "Mo", 43: "Tc", 44: "Ru", 45: "Rh", 46: "Pd", 47: "Ag", 48: "Cd", 49: "In", 50: "Sn", 
                  51: "Sb", 52: "Te", 53: "I", 54: "Xe", 55: "Cs", 56: "Ba", 57: "La", 58: "Ce", 59: "Pr", 60: "Nd", 
                  61: "Pm", 62: "Sm", 63: "Eu", 64: "Gd", 65: "Tb", 66: "Dy", 67: "Ho", 68: "Er", 69: "Tm", 70: "Yb", 
                  71: "Lu", 72: "Hf", 73: "Ta", 74: "W", 75: "Re", 76: "Os", 77: "Ir", 78: "Pt", 79: "Au", 80: "Hg", 
                  81: "Tl", 82: "Pb", 83: "Bi", 84: "Po", 85: "At", 86: "Rn", 87: "Fr", 88: "Ra", 89: "Ac", 90: "Th", 
                  91: "Pa", 92: "U", 93: "Np", 94: "Pu", 95: "Am", 96: "Cm", 97: "Bk", 98: "Cf", 99: "Es", 100: "Fm", 
                  101: "Md", 102: "No"}
#--------------------------------------------------

# Locate the directory
dir_path = os.getcwd()

# Loop through all the files in the directory

normal_termination = 0
error_termination = 0

with open("not_optimized.txt", "w") as f:
    f.write("These calculations did not conclude the optimization:\n")

for filename in os.listdir(dir_path):
    if filename.endswith(".log"):
        name_without_ext, ext = os.path.splitext(filename)
        file_path = os.path.join(dir_path, filename)

        with open(file_path, "r") as f:
            lines = f.readlines()
            line_count = 0
            for line in lines:
                line_count += 1

# Find the charge and multiplicity
        charge_multiplicity = ""
        for i, line in enumerate(lines):
            if re.search("Charge =", line):
                charge_multiplicity = line
                break

# Find the index of the first line containing the search string
        opt_index = 0
        no_opt_count = 0

        for i, line in enumerate(lines):
            no_opt_count += 1
            if re.search("Optimization completed", line):
                opt_index = i
                break
        
        if line_count == no_opt_count:
            error_termination += 1
            with open("not_optimized.txt", "a") as f:
                f.write(f"{filename}\n")
        
        else:
            normal_termination += 1
            start_index = 0
            for i, line in enumerate(lines[opt_index:]):
                if re.search("Standard orientation:", line):
                    start_index = i+5
                    break
            start_index = start_index + opt_index

            end_index = 0
            for i, line in enumerate(lines[start_index:]):
                if re.search("Rotational constants", line):
                    end_index = i-1
                    break

            final_index = start_index + end_index
# Remove all lines before the start_index and after the end_index
            lines = lines[start_index:final_index]
# Clean charge & multiplicity and coordinates
            c_m = charge_multiplicity.split()
            C_M = " ".join([c_m[2], c_m[5]])

# Save the coordinates to a xyz file:
            with open(name_without_ext+".txt", "w") as f:
                f.write(f"{name_without_ext}\n\n")
                f.write(C_M + "\n")
                for line in lines:
                    cols = line.split()
                    new_line = "    ".join([periodic_table[int(cols[1])], cols[3], cols[4], cols[5]])
                    f.write(new_line + "\n")
                f.write("\n")

print(f"{normal_termination} files were converted to .txt")  
print(f"{error_termination} not concluded optimizations. Check not_optimized.txt file!")
