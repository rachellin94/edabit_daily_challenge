# Question_2

"""
File: complement.py
Name: Rachel
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""
def main():
    """
    Pre-condition/Post-condition: There are 4 different genes in the company, based on complementation genetics theory.
                    A's complementation gene is T , vice versa.
                    C's complementation gene is G , vice versa.
                    If DNA is empty string, print out "DNA strand is missing."
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    if dna == "":
        return "DNA strand is missing."
    new_definition = ""
    for i in range(len(dna)):
        ch = dna[i]
        if ch == "A":
            new_definition = new_definition + "T"
        elif ch == "T":
            new_definition = new_definition + "A"
        elif ch == "C":
            new_definition = new_definition + "G"
        elif ch == "G":
            new_definition = new_definition + "C"
    return new_definition

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

