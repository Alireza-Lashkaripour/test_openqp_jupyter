import os
import subprocess

# Define input file and content
input_file = "example_input.inp"
input_content = """
[input]
system=
   8   0.000000000   0.000000000  -0.041061554
   1  -0.533194329   0.533194329  -0.614469223
   1   0.533194329  -0.533194329  -0.614469223
charge=0
runtype=energy
functional=bhhlyp
basis=6-31g(d)
method=hf

[guess]
type=huckel

[scf]
multiplicity=1
type=rhf

[dftgrid]
rad_type=becke
"""

with open(input_file, "w") as f:
    f.write(input_content)

# Run OpenQP and capture output
result = subprocess.run(["/usr/local/bin/openqp", input_file], capture_output=True, text=True)

if result.returncode != 0:
    print("Errors during execution:")
    print(result.stderr)
else:
    log_file = "example_input.log"  
    if os.path.exists(log_file):
        print("Output from log file:")
        with open(log_file, "r") as log:
            print(log.read())
    else:
        print("Log file not found. OpenQP execution might have failed.")
