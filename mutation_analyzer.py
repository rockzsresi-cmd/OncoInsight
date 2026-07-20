from Bio import SeqIO
from Bio.Seq import Seq
from io import StringIO


def compare_sequences(normal_file, mutant_file):

    # Read uploaded FASTA files
    normal_text = normal_file.getvalue().decode("utf-8")
    mutant_text = mutant_file.getvalue().decode("utf-8")

    normal_record = SeqIO.read(StringIO(normal_text), "fasta")
    mutant_record = SeqIO.read(StringIO(mutant_text), "fasta")

    normal_seq = str(normal_record.seq).upper()
    mutant_seq = str(mutant_record.seq).upper()

    # Compare DNA sequences
    mutations = []

    minimum = min(len(normal_seq), len(mutant_seq))

    for i in range(minimum):

        if normal_seq[i] != mutant_seq[i]:

            mutations.append({
                "Position": i + 1,
                "Reference": normal_seq[i],
                "Mutant": mutant_seq[i]
            })

    # Protein Translation
    normal_protein = str(Seq(normal_seq).translate())

    mutant_protein = str(Seq(mutant_seq).translate())

    protein_changed = normal_protein != mutant_protein

    if protein_changed:
        mutation_type = "Protein Altering"
    else:
        mutation_type = "Silent Mutation"

    # Mutation Rate
    mutation_rate = round(
        (len(mutations) / len(normal_seq)) * 100,
        2
    )

    # Biological Interpretation
    if len(mutations) == 0:

        interpretation = (
            "No mutations were detected between the reference and mutant DNA "
            "sequences. The translated protein sequence remained unchanged."
        )

    elif protein_changed:

        interpretation = (
            "Mutation(s) were detected between the reference and mutant DNA "
            "sequences. The translated protein sequence differs from the "
            "reference, indicating that the mutation alters the encoded "
            "protein. Such variants may influence protein structure or "
            "function and require further biological or clinical validation."
        )

    else:

        interpretation = (
            "Mutation(s) were detected in the DNA sequence, but the translated "
            "protein sequence remained unchanged. This is consistent with a "
            "silent (synonymous) mutation."
        )

    return {

        "Normal Sequence": normal_seq,
        "Mutant Sequence": mutant_seq,

        "Normal Protein": normal_protein,
        "Mutant Protein": mutant_protein,

        "Mutations": mutations,

        "Total": len(mutations),

        "Mutation Rate": mutation_rate,

        "Mutation Type": mutation_type,

        "Interpretation": interpretation

    }