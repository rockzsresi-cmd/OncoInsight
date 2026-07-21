import pandas as pd


def search_variant(gene, variant):

    df = pd.read_csv("clinical_variants.csv")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Clean values
    df["Gene"] = df["Gene"].astype(str).str.strip().str.upper()
    df["Variant"] = df["Variant"].astype(str).str.strip().str.upper()

    # Clean user input
    gene = gene.strip().upper()
    variant = variant.strip().upper()

    result = df[
        (df["Gene"] == gene) &
        (df["Variant"] == variant)
    ]

    return result
    
