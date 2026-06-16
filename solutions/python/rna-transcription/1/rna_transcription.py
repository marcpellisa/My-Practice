def to_rna(dna_strand):
    RNA = ''
    if dna_strand == '':
        return ''
    for letter in dna_strand:
        if letter == 'A':
            RNA += 'U'
        elif letter == 'C':
            RNA += 'G'
        elif letter == 'G':
            RNA += 'C'
        elif letter == 'T':
            RNA += 'A'
    return RNA