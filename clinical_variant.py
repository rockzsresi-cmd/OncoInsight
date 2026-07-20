import pandas as pd


def search_variant(gene, variant):

    df = pd.read_csv("data/clinical_variants.csv")

    result = df[
        (df["Gene"].str.upper() == gene.upper())
        &
        (df["Variant"].str.upper() == variant.upper())
    ]

    return result