import os
import subprocess

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

result = subprocess.run(["/usr/local/bin/openqp", input_file], capture_output=True, text=True)

print("Output:")
print(result.stdout)
print("Errors:")
print(result.stderr)

