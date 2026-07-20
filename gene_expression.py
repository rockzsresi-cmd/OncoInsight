import pandas as pd


def analyze_expression(uploaded_file):

    df = pd.read_csv(uploaded_file)

    if "Gene" not in df.columns or "Expression" not in df.columns:
        raise ValueError(
            "CSV file must contain 'Gene' and 'Expression' columns."
        )

    highest = df.loc[df["Expression"].idxmax()]
    lowest = df.loc[df["Expression"].idxmin()]

    average = round(df["Expression"].mean(), 2)

    return {

        "Data": df,

        "Highest Gene": highest["Gene"],
        "Highest Expression": highest["Expression"],

        "Lowest Gene": lowest["Gene"],
        "Lowest Expression": lowest["Expression"],

        "Average Expression": average

    }