# Define the pathway for different elements' POTCAR in your systerm
POTCAR_PATH = ""

# Get Elements from POSCAR
def find_elements_from_POSCAR(file):
    with open(file,"r") as POSCAR:
        content = POSCAR.readlines()
        return content[5][:-1].split()

# Read the elements and zip all the POTCAR you need.
def write_POTCAR(element_list,POTCAR_Dir):
    return_file = ""
    for element in element_list:
        with open(POTCAR_Dir + "/POTCAR_" + element) as file:
            return_file = return_file + file.read()
    with open("POTCAR","a") as file:
        file.write(return_file)

# Start
elements = find_elements_from_POSCAR("POSCAR")
write_POTCAR(elements,POTCAR_PATH)
