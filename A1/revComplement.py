import re

def revComplement (dna_string):
    # type: (dna_string) -> string

    dna_string = dna_string.upper()
    pattern = "[^ACTG]+"

    if re.findall(pattern, dna_string):
        print("Sequence is not a DNA string")

    else:

        sequence = list(dna_string)
        compl = sequence
        for i in range(0, len(sequence)):
            if sequence[i] == 'A' :
                compl[i] = 'T'
            elif sequence[i] == 'T' :
                compl[i] = 'A'
            elif sequence[i] == 'C':
                compl[i] = 'G'
            elif sequence[i] == 'G':
                compl[i] = 'C'
        compl = ''.join(compl)
        reversed = compl[::-1]

        return reversed