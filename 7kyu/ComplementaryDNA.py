def DNA_strand(dna):
    arr = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(arr[i] for i in dna)