#Gaussian Input Generator v.01
#--------------------------------------------------
import os
import re
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

###### CHANGE HERE IF YOU NEED TO CHANGE THE DEFAULT ######

method_OPT_def = "wB97XD"
basis_set_OPT_def = "def2SVP"
method_SP_def = "wB97XD"
basis_set_SP_def = "def2TZVP"
SP_1_def = "#N Guess=Read Geom=Check Integral(Ultrafine) Density Prop=(Potential,EFG) Volume Pop=NBO7 Pop=Hirshfeld Polar"
SP_2_def = "#N Guess=Read Geom=Check Integral(Ultrafine) Density Pop=(ChelpG,ReadRadii) NMR"
calc_fc_def = False
calc_all_def = False
SCRF_def = False
solvent_def = ""
#solvent_def = "SCRF(IEFPCM,solvent=water)"

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

###### NO CHANGES NEEDED BEYOND THIS POINT ######

#Methods: 
D3_methods = ["m062x"]
D3BJ_methods = ["b3lyp", "pbe1pbe", "cam-b3lyp"]
wrong_dic = {"m06-2x":"M062X","mo6-2x":"M062X","mo62x":"M062X","pbe0":"PBE1PBE","wb97x-d":"wB97XD","camb3lyp":"CAM-B3LYP"}
#--------------------------------------------------
#Properties:
NBO = "Pop=NBO7 "
Hirshfeld = "Pop=Hirshfeld "
ChelpG = "Pop=(ChelpG,ReadRadii) "
NMR = "NMR "
Prop = "Prop=(Potential,EFG) "
Volume = "Volume "
Polar = "Polar "
#--------------------------------------------------
#vdW radii: 
atoms_radius_dic = {"K":2.75,"Ni":1.63, "Cu":1.40, "Zn":1.39, "Br":1.85, "Pd":1.63, "Ag":1.72, "Sn":1.98, "I":1.98, "Pt":1.75, "Au":1.66}
vdw_rad = "vdW radii used in the ChelpG calculation for some atoms, ref: A. Bondi. van der Waals Volumes and Radii. J. Phys. Chem. 1964, 68, 441-451."
#--------------------------------------------------
#Heavy atoms:
heavy_atoms = ["Cr","Mn","Fe","Co","Ni","Cu","Zn","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","W","Re","Os","Ir","Pt","Au","Hg"]
heavy_basis = ["def2SVP","def2TZVP","def2TZVPP","LANL2DZ"]
#--------------------------------------------------
print("...............................................................................")
print(".                                                                             .")
print(".                           Gaussian Input Generator                          .")
print(".                                                                             .")
print("...............................................................................")

print("\nThe default is your fault :)\n")
if calc_fc_def:
    print(f"#N OPT=(CalcFC,Tight) FREQ Integral(Ultrafine) {method_OPT_def} {basis_set_OPT_def}")
elif calc_all_def:
    print(f"#N OPT=(CalcAll,Tight) FREQ Integral(Ultrafine) {method_OPT_def} {basis_set_OPT_def}")
else:
    print(f"#N OPT FREQ Integral(Ultrafine) {method_OPT_def} {basis_set_OPT_def}")
if SCRF_def:
    print(f"{SP_1_def} {method_SP_def} {basis_set_SP_def} {solvent_def}")
    print(f"{SP_2_def} {method_SP_def} {basis_set_SP_def} {solvent_def}")
else:
    print(f"{SP_1_def} {method_SP_def} {basis_set_SP_def}")
    print(f"{SP_2_def} {method_SP_def} {basis_set_SP_def}")
        
default_ans = input("\nDo you want to proceed with the default [RECOMMENDED IF YOU ARE NOT FAMILIAR WITH METHODS AND BASIS SETS] [y/n]? ")

if default_ans.lower() == "yes" or default_ans.lower() == "y" or default_ans == "":
    default = True
else:
    default = False

#--------------------------------------------------
# DEFAULT CHECK

######### USER ASKED FOR DEFAULT: 

if default:
    method = method_OPT_def
    basis_set = basis_set_OPT_def
    method_post = method_SP_def
    basis_set_post = basis_set_SP_def
    SP_1 = SP_1_def
    SP_2 = SP_2_def
    calc_fc = []
    calc_all = []
    if calc_fc_def:
        calc_fc = True
    if calc_all_def:
        calc_all = True

######### USER ASKED FOR NO-DEFAULT: 

else:

#### METHOD AND BASIS

    method_ans = input("\nInput the method for OPT and FREQ [default = wB97XD]: ")
    if method_ans == "":
        method = "wB97XD"
    elif method_ans.lower() in [key for key in wrong_dic]:
        method = wrong_dic[method_ans.lower()]
        print(f"\n\033[1;31mWARNING! You spelled the method incorrectly! It was corrected to: {wrong_dic[method_ans.lower()]}\033[0m")
    else:
        method = method_ans

    if method.lower() in D3_methods:
        dispersion_ans = input("\nWould you like to add dispersion [y/n]? ")
        if dispersion_ans.lower() == "no" or dispersion_ans.lower() == "n":
            method += ""
        else:
            method += " EmpiricalDispersion=GD3"

    if method.lower() in D3BJ_methods:
        dispersion_ans = input("\nWould you like to add dispersion [y/n]? ")
        if dispersion_ans.lower() == "no" or dispersion_ans.lower() == "n":
            method += ""
        else:
            method += " EmpiricalDispersion=GD3BJ"

    basis_set_ans = input("\nInput basis set [default = def2SVP]: ")
    if basis_set_ans == "":
        basis_set = "def2SVP"
    else:
        basis_set = basis_set_ans
    
    difficult_opt_ans = input("\nDo you think your optimization will be difficult to converge [y/n]: ")
    calc_fc = []
    calc_all = []
    if difficult_opt_ans == "yes" or difficult_opt_ans == "y":
        calc_ans = input("\nWould you like to do [1] OPT=(CalcFC,Tight), [2] OPT=(CalcAll,Tight) or [3] keep just OPT: ")
        if calc_ans == "1":
            calc_fc = True
        if calc_ans == "2":
            calc_all = True
    else:
        print("\nYou are good to go with just the OPT keyword :D")
    
#### END OF METHOD AND BASIS SET

#### PROPERTIES

    print("...............................................................................")
    print("\n---------------------------- ~List of Keywords~ ----------------------------\n")
    print("0. All of them!\n")
    print("1. Population Analysis [NBO, Hirshfeld, ChelpG] - Compute charges and occupancies.")
    print("2. NMR - Compute NMR shieldings.")
    print("3. Prop - Compute electrostactic properties.")
    print("4. Volume - Compute molecular volume.")
    print("5. Polar - Compute dipole electric field polarizabilities.")
    print("\n100. None\n")
    print("\n200. Add your own [NOT RECOMMENDED!]\n")
    print("...............................................................................")

    prop_ans = input("\nType the keyword number you would like to compute [e.g.: '1' or '1,2' ...]: ")
    if prop_ans == "100":
        prop = False
    else:
        prop = True

    if prop:
        SP_1 = "#N Guess=Read Geom=Check Integral(Ultrafine) Density "
        SP_2 = "#N Guess=Read Geom=Check Integral(Ultrafine) Density "
        
        if "200" in prop_ans:
            prop_list = "200"
            SP_1 += input("\nEnter the keywords for the FIRST Single Point: ")
            SP_2 += input("\nEnter the keywords for the SECOND Single Point: ")
        elif "0" in prop_ans or not prop_ans:
            prop_list = "0"
            SP_1 += NBO + Hirshfeld + ChelpG + Polar + Prop + Volume
            SP_2 += NMR
        else:
            prop_list = prop_ans.split(",")
            if "1" in prop_list:
                SP_1 += NBO + Hirshfeld + ChelpG
            if "2" in prop_list:
                SP_2 += NMR
            if "3" in prop_list:
                SP_1 += Prop
            if "4" in prop_list:
                SP_1 += Volume
            if "5" in prop_list:
                SP_1 += Polar

        method_post_ans = input("\nInput the method for single point jobs [default = wB97XD]: ")
        if method_post_ans == "":
            method_post = "wB97XD"
        elif method_post_ans.lower() in [key for key in wrong_dic]:
            method_post = wrong_dic[method_post_ans.lower()]
            print(f"\n\033[1;31mWARNING! You spelled the method incorrectly! It was corrected to: {wrong_dic[method_post_ans.lower()]}\033[0m")
        else:
            method_post = method_post_ans

        if method_post.lower() in D3_methods:
            dispersion_ans = input("\nWould you like to add dispersion [y/n]? ")
            if dispersion_ans.lower() == "no" or dispersion_ans.lower() == "n":
                method_post += ""
            else:
                method_post += " EmpiricalDispersion=GD3"

        if method_post.lower() in D3BJ_methods:
            dispersion_ans = input("\nWould you like to add dispersion [y/n]? ")
            if dispersion_ans.lower() == "no" or dispersion_ans.lower() == "n":
                method_post += ""
            else:
                method_post += " EmpiricalDispersion=GD3BJ"

        basis_set_post_ans = input("\nInput basis set for single point jobs [default = def2TZVP]: ")
        if basis_set_post_ans == "":
            basis_set_post = "def2TZVP"
        else:
            basis_set_post = basis_set_post_ans

#SOLVENT
        SCRF = False
        SCRF_ans = input("\nWould you like to compute properties with implicit solvent [default=no]? ")
        if SCRF_ans.lower() == "yes" or SCRF_ans.lower() == "y":
            SCRF = True
            SCRF_model_ans = input("\nWhat solvent model would you like to use [1] PCM or [2] SMD]? ")
#            if SCRF_model_ans == "1" or SCRF_model_ans == "PCM":
            if "2" not in SCRF_model_ans or "SMD" not in SCRF_model_ans:
                solvent_ans = input("\nInput the solvent you would like to use [e.g., Water, Dichloromethane...]: ")
                if solvent_ans == "":
                    solvent = "SCRF(IEFPCM,solvent="+"water"+")"
                else:
                    solvent = "SCRF(IEFPCM,solvent="+solvent_ans+")"
            elif SCRF_model_ans == "2" or SCRF_model_ans == "SMD":
                solvent_ans = input("\nInput the solvent you would like to use [e.g., Water, Dichloromethane...]: ")
                if solvent+ans == "":
                    solvent = "SCRF(IEFPCM,solvent=dichloromethane)"
                else:
                    solvent = "SCRF(IEFPCM,solvent="+solvent_ans+")"
            else:
                solvent = "SCRF(IEFPCM,solvet=dichloromethane)"

#### END OF PROPERTIES

#--------------------------------------------------
#### CLEANING INPUT: 
radius_count = 0
# Get the directory containing the text files
dir_path = os.getcwd()
# Number of files:
file_count = 0
# Loop through all the files in the directory
for filename in os.listdir(dir_path):
    if filename.endswith(".com"):
        file_count +=1 
        name_without_ext, ext = os.path.splitext(filename)
        file_path = os.path.join(dir_path, filename)

        with open(file_path, "r") as f:
            lines = f.readlines()

# Find the index of the first line containing the search string
        start_index = 0
        for i, line in enumerate(lines):
            pattern = r'^[a-zA-Z ].*\s\s\s.*\d$'
            match = re.match(pattern, line)
            if match:
                start_index = i-1
                break
        charge_spin = lines[start_index]
        end_index = 0
        for i, line in reversed(list(enumerate(lines))):
            pattern_end = r'^[a-zA-Z ].*\s\s\s.*\d$'
            match = re.match(pattern_end, line)
            if match:
                end_index = i+1
                break

# Remove all lines before the start_index and after the end_index
        lines = lines[start_index:end_index]

# Checking for atoms without defined radii:
        need_radius = []
        for line in lines:
            for key in atoms_radius_dic:
                if key in line and key not in need_radius:
                    radius_count += 1
                    need_radius.append(key)

# Checking for heavy atoms:
        for line in lines:
            for i in heavy_atoms:
                if i in line:
                    if basis_set not in heavy_basis or basis_set_post not in heavy_basis:
                        print("\033[1;31m..............................................................................................................")
                        print("\nWARNING!!! Your basis set may not be suitable for heavy atoms, consider changing it to def2SVP and def2TZVP\n")
                        print("..............................................................................................................\033[0m")
                        heavy_ans = input("Would you like to change the basis sets? ")
                        if heavy_ans == "" or heavy_ans == "yes" or heavy_ans.lower() == "y":
                            basis_set_ans = input("\nInput basis set for OPT [default = def2SVP]: ")
                            if basis_set_ans == "":
                                basis_set = "def2SVP"
                            else:
                                basis_set = basis_set_ans
                            basis_set_post_ans = input("\nInput basis set for single point jobs [default = def2TZVP]: ")
                            if basis_set_post_ans == "":
                                basis_set_post = "def2TZVP"
                            else:
                                basis_set_post = basis_set_post_ans
#--------------------------------------------------
#### WRITING INPUT HEAD:            
        with open(file_path, "w") as f:
            f.write(f"%NProcShared=24\n%Mem=64GB\n")
            f.write(f"%chk={name_without_ext}.chk\n")
            if calc_fc:
                f.write(f"#N OPT=(CalcFC,Tight) FREQ=NORAMAN Integral(Ultrafine) {method} {basis_set}")
            elif calc_all:
                f.write(f"#N OPT=(CalcAll,Tight) FREQ=NORAMAN Integral(Ultrafine) {method} {basis_set}")
            else:
                f.write(f"#N OPT FREQ=NORAMAN Integral(Ultrafine) {method} {basis_set}")
            f.write(f"\n\n{name_without_ext}\n\n")
#             f.write(charge_spin + "\n")

#### WRITING XYZ
            f.writelines(lines)
            f.write(f"\n")

#### WRITING INPUT BOTTOM
            if default:
                f.write(f"--Link1--\n%NProcShared=24\n%Mem=64GB\n")
                f.write(f"%chk={name_without_ext}.chk\n")
                if SCRF_def:
                    f.write(f"{SP_1} {method_post} {basis_set_post} {solvent_def}")
                else:
                    f.write(f"{SP_1} {method_post} {basis_set_post}")
                f.write(f"\n\n{name_without_ext}\n\n")
                f.write(f"{charge_spin}")
                f.write(f"\n")
#                if need_radius:
#                    for atom in need_radius:
#                        if atom in [key for key in atoms_radius_dic]:
#                            f.write(f"{atom} {atoms_radius_dic[atom]} \n")
#                    f.write("\n")
                f.write(f"--Link1--\n%NProcShared=24\n%Mem=64GB\n")
                f.write(f"%chk={name_without_ext}.chk\n")
                if SCRF_def:
                    f.write(f"{SP_2} {method_post} {basis_set_post} {solvent_def}")
                else:
                    f.write(f"{SP_2} {method_post} {basis_set_post}")
                f.write(f"\n\n{name_without_ext}\n\n")
                f.write(f"{charge_spin}")
                f.write(f"\n")
                if need_radius:
                    for atom in need_radius:
                        if atom in [key for key in atoms_radius_dic]:
                            f.write(f"{atom} {atoms_radius_dic[atom]} \n")
                    f.write("\n")

            else:
                if prop:
                    f.write(f"--Link1--\n%NProcShared=24\n%Mem=64GB\n")
                    f.write(f"%chk={name_without_ext}.chk\n")
                    if SCRF:
                        f.write(f"{SP_1} {method_post} {basis_set_post} {solvent}")
                    else:
                        f.write(f"{SP_1} {method_post} {basis_set_post}")
                    f.write(f"\n\n{name_without_ext}\n\n")
                    f.write(f"{charge_spin}")
                    f.write(f"\n")
#                    if need_radius:
#                        for atom in need_radius:
#                            if atom in [key for key in atoms_radius_dic]:
#                                f.write(f"{atom} {atoms_radius_dic[atom]} \n")
#                        f.write("\n")
                    if "0" in prop_list or "2" in prop_list:
                        f.write(f"--Link1--\n%NProcShared=24\n%Mem=64GB\n")
                        f.write(f"%chk={name_without_ext}.chk\n")
                        if SCRF:
                            f.write(f"{SP_2} {method_post} {basis_set_post} {solvent}")
                        else:
                            f.write(f"{SP_2} {method_post} {basis_set_post}")
                        f.write(f"\n\n{name_without_ext}\n\n")
                        f.write(f"{charge_spin}")
                        f.write(f"\n") 
                        if need_radius:
                            for atom in need_radius:
                                if atom in [key for key in atoms_radius_dic]:
                                    f.write(f"{atom} {atoms_radius_dic[atom]} \n")
                            f.write("\n")


if radius_count != 0:
    print(f"\n{vdw_rad}")
print(f"\nDone! {file_count} .com files were converted! :D")
