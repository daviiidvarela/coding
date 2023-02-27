class DnaSeq:
    def __init__(self, accession, seq):
        if not accession or not seq:
            raise ValueError("Accession and sequence strings cannot be empty")
        self.accession = accession
        self.seq = seq
    
    def prefix(self, n):
        return self.seq[:n]

    def suffix(self, n):
        return self.seq[-n:]

    def __len__(self):
        return len(self.seq)

    def __str__(self):
        return f"<DnaSeq accession='{self.accession}'>"


def read_dna(filename):
    sequences = []
    with open(filename, 'r') as f:
        accession = None
        sequence = ''
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if accession is not None:
                    sequences.append(DnaSeq(accession, sequence))
                    sequence = ''
                accession = line[1:]
            elif line:
                sequence += line
        if accession is not None:
            sequences.append(DnaSeq(accession, sequence))
    return sequences


def check_exact_overlap(seq1, seq2, min_length=10):
    """
    Detects overlaps between two DNA sequences

    Parameters:
    seq1 (DnaSeq): the first DNA sequence to compare
    seq2 (DnaSeq): the second DNA sequence to compare
    min_length (int): the minimum length of an overlap to consider (default: 10)

    Returns:
    int: the length of the longest overlap detected, or 0 if no overlap is detected
    """
    seq1_length = len(seq1)
    seq2_length = len(seq2)

    max_overlap_length = 0

    for i in range(min_length, min(seq1_length, seq2_length) + 1):
        if seq1.suffix(i) == seq2.prefix(i):
            max_overlap_length = i

    return max_overlap_length


def overlaps(seq_list, overlap_func=check_exact_overlap, min_len=10):
    """
    Finds all detectable overlaps among pairs of sequences in the input list using the given overlap detection function

    Parameters:
    seq_list (list): A list of DnaSeq objects
    overlap_func (function): A function that takes two DnaSeq objects and a minimum length and returns the length of the longest overlap between them
    min_len (int): The minimum length of an overlap to be considered

    Returns:
    dict: A dictionary of dictionaries containing the lengths of overlaps between sequences. If d is the result of a call to overlaps, and the sequences with accessions s1 and s2 overlaps with length 10, then d['s1']['s2'] == 10 should be true

    """
    overlap_lengths = {}
    for i in range(len(seq_list)):
        for j in range(i+1, len(seq_list)):
            overlap_len = overlap_func(seq_list[i], seq_list[j], min_len)
            if overlap_len > 0:
                if seq_list[i].accession not in overlap_lengths:
                    overlap_lengths[seq_list[i].accession] = {}
                overlap_lengths[seq_list[i].accession][seq_list[j].accession] = overlap_len

                # Since the overlap is not commutative, we need to add the reverse overlap length as well
                if seq_list[j].accession not in overlap_lengths:
                    overlap_lengths[seq_list[j].accession] = {}
                overlap_lengths[seq_list[j].accession][seq_list[i].accession] = overlap_len

    return overlap_lengths


#
# Testing code. You should not change any code below here. To run the tests
# uncomment the last line in the file.
#
def test_class_DnaSeq():
    s1 = DnaSeq('s1', 'ACGT')
    s2 = DnaSeq('s2', 'ATGTTTGTTTTTCTTGTTTTATTGCCACTAGTCTCTAGTCAGTGTGTTAATCTTACAACCAGAACTCAAT')
    assert len(s1) == 4, 'Your length method (__len__) is not correct.'
    assert len(s2) == 70, 'Your length method (__len__) is not correct.'

    assert str(s1) == "<DnaSeq accession='s1'>", 'The __str__ method is not following the specification.'
    assert str(s2) == "<DnaSeq accession='s2'>", 'The __str__ method is not following the specification.'

    # The rest of this function is verifying that we are indeed raising an exception.
    status = 0
    try:
        s3 = DnaSeq('', 'ACGT')
    except ValueError:
        status += 1
    try:
        s3 = DnaSeq('s3', None)
    except ValueError:
        status += 1

    try:
        s3 = DnaSeq(None, '')
    except ValueError:
        status += 1
    if status != 3:
        raise Exception('class DnaSeq does not raise a ValueError '
                        'exception with initialised with empty '
                        'accession and sequence.')
    print('DnaSeq passed')


def test_reading():
    dna1 = read_dna('ex1.fa')
    assert len(dna1) == 6, 'The file "ex1.fa" has exactly 6 sequences, but your code does not return that.'
    assert list(map(lambda x: x.accession, dna1)) == [f's{i}' for i in range(6)], 'The accessions are not read correctly'

    dna2 = read_dna('ex2.fa')
    assert len(dna2) == 6, 'The file "ex2.fa" has exactly 6 sequences, but your code does not return that.'

    covid = read_dna('sars_cov_2.fa')
    assert len(covid[0].seq) == 29903, 'The length of the genome in "sars_cov_2.fa" is 29903, but your code does not return that.'

    print('read_dna passed')


def test_overlap():
   s0 = DnaSeq('s0', 'AAACCC')
   s1 = DnaSeq('s1', 'CCCGGG')
   s2 = DnaSeq('s2', 'TTATCC')
   s3 = DnaSeq('s3', 'CCAGGG')
   s4 = DnaSeq('s4', 'GGGGGGGGAAAGGGGG')
   s5 = DnaSeq('s5', 'AAATTTTTTTTTTTTTTTTTAT')

   data1 = [s0, s1, s2, s3]
   assert check_exact_overlap(s0, s1, 2) == 3
   assert check_exact_overlap(s0, s1) == 0
   assert check_exact_overlap(s0, s3, 2) == 2
   assert check_exact_overlap(s1, s2, 2) == 0
   assert check_exact_overlap(s2, s1, 2) == 2
   assert check_exact_overlap(s2, s3, 2) == 2
   assert check_exact_overlap(s4, s5, 1) == 0
   assert check_exact_overlap(s4, s5, 2) == 0
   assert check_exact_overlap(s4, s5, 3) == 0
   assert check_exact_overlap(s5, s2, 1) == 4

   res0 = overlaps(data1, lambda s1, s2: check_exact_overlap(s1, s2, 2))
   assert len(res0) == 2, 'You get the wrong number of overlaps'
   assert res0 == {'s0': {'s1': 3, 's3': 2}, 's2': {'s1': 2, 's3': 2}}

   dna_data = read_dna('ex1.fa')
   res1 = overlaps(dna_data, check_exact_overlap)
   assert len(res1) == 5
   for left, right in [('s0', 's1'), ('s1', 's2'), ('s2', 's3'), ('s3', 's4'),
                       ('s4', 's5')]:
       assert res1[left][right], f'Missing overlap of {left} and {right} (in that order)'
   print('overlap code passed')



def test_all():
    test_class_DnaSeq()
    test_reading()
    test_overlap()
    print('Yay, all good')

# Uncomment this to test everything:
#test_all()
test_class_DnaSeq()
test_reading()
test_overlap()

# create function that continues to ask a user a question until the user inputs q?