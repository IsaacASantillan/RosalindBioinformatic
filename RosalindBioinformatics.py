_warningregistry__ = {'version': 0}
amino = {'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T', 'AGA': 'R', 'AGC': 'S'}

"""These are my functions for assignment 2 Isaac Santillan"""
import re
amino = {line.split()[0].replace("T", "U"): line.split()[2] for line in open("/srv/datasets/amino")}


def prot(rna):
    if len(rna) < 36 or rna[:3] != "AUG":
        return None
    protiens = []
    for i in range(0, len(rna), 3):
        if (i < 30 or i != len(rna) - 3) \
            and (rna[i:i + 3] == "UAA" or rna[i:i + 3] == "UGA" or rna[i:i + 3] == "UAG"):
            return None
        if rna[i:i + 3] == "UAA" or rna[i:i + 3] == "UGA" or rna[i:i + 3] == "UAG":
            return "".join(protiens)
        else:
            protiens += amino[rna[i:i + 3]]
    return None

def potential_proteins(rna):
    empty_list = []
    for triplet in re.finditer("AUG", rna):
        for x in range(triplet.start(), len(rna), 3):
            codon = rna[x:x + 3]
            if codon in ("UGA", "UAA", "UAG"):
                acids = prot(rna[triplet.start():x + 3])
                if acids is not None:
                    empty_list += [acids]
                else:
                    empty_list += []
    return empty_list




