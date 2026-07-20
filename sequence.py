from Bio import SeqIO
from Bio.Seq import Seq
from io import StringIO


def analyze_sequence(uploaded_file):

    text = uploaded_file.getvalue().decode("utf-8")
    record = SeqIO.read(StringIO(text), "fasta")

    sequence = str(record.seq).upper()

    length = len(sequence)

    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")

    gc_content = round(((g + c) / length) * 100, 2)

    reverse_complement = str(Seq(sequence).reverse_complement())

    protein = str(Seq(sequence).translate())

    return {
        "Sequence": sequence,
        "Length": length,
        "A": a,
        "T": t,
        "G": g,
        "C": c,
        "GC": gc_content,
        "Reverse Complement": reverse_complement,
        "Protein": protein,
    }