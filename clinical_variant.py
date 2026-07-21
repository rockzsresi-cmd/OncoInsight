import pandas as pd

def search_variant(gene, variant):

    df = pd.read_csv("clinical_variants.csv")

    print(df)

    df.columns = df.columns.str.strip()

    df["Gene"] = df["Gene"].astype(str).str.strip().str.upper()
    df["Variant"] = df["Variant"].astype(str).str.strip().str.upper()

    gene = gene.strip().upper()
    variant = variant.strip().upper()

    print("Input:", gene, variant)

    result = df[
        (df["Gene"] == gene) &
        (df["Variant"] == variant)
    ]

    print(result)

    return result
    
