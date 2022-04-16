## Translating RNA Into Protein

Calculates and returns the protein string encoded by an RNA string, or None if the encoding is invalid. 
A valid encoding consists of 12 or more codons, where the first is start codon 'AUG', followed by at least 
10 more non-stop codons, and then a stop codon. One interesting way of using this code is to search a genome 
(or part of one) for possible proteins and see if they correspond to the products of any actual genes that 
have been identified by scientists in the relevant genome.
