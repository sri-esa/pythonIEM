from rdkit import Chem
from rdkit.Chem import Draw

# Define structures using SMILES strings for the diagrams
# 4.14: Val-Ser and Ser-Val
val_ser = "N[C@@H](C(C)C)C(=O)N[C@@H](CO)C(=O)O"  # Val-Ser
ser_val = "N[C@@H](CO)C(=O)N[C@@H](C(C)C)C(=O)O"  # Ser-Val

# 4.9: Fully protonated Ala-Asp (Ala: CH3 side chain, Asp: CH2COOH side chain)
ala_asp = "N[C@@H](C)C(=O)N[C@@H](CC(=O)O)C(=O)O"

# 4.25: Asp-Phe (Asp: CH2COOH, Phe: Benzene ring side chain)
asp_phe = "N[C@@H](CC(=O)O)C(=O)N[C@@H](Cc1ccccc1)C(=O)O"

# Oxidized protein structure: Cys-S-S-Cys
oxidized_protein = "N[C@@H](CS)C(=O)N[C@@H](CS)C(=O)O"

# Generate the structures
mol_val_ser = Chem.MolFromSmiles(val_ser)
mol_ser_val = Chem.MolFromSmiles(ser_val)
mol_ala_asp = Chem.MolFromSmiles(ala_asp)
mol_asp_phe = Chem.MolFromSmiles(asp_phe)
mol_oxidized_protein = Chem.MolFromSmiles(oxidized_protein)

# Draw the structures into one grid image
mols = [mol_val_ser, mol_ser_val, mol_ala_asp, mol_asp_phe, mol_oxidized_protein]
labels = ["Val-Ser", "Ser-Val", "Ala-Asp (Protonated)", "Asp-Phe", "Oxidized Protein"]
img = Draw.MolsToGridImage(mols, legends=labels, molsPerRow=2, subImgSize=(300, 300))

# Save and display the image
output_path = "/mnt/data/protein_diagrams.png"
img.save(output_path)
output_path
