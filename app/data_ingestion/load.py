import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)

    summary = []
    summary.append("DATASET OVERVIEW")
    summary.append(f"Total rows: {df.shape[0]}")
    summary.append(f"Total columns: {df.shape[1]}")
    summary.append("Column Names:")
    summary.append(", ".join(df.columns))

    summary.append("\nSAMPLE ROWS")
    summary.append(df.head(20).to_csv(index=False))

    summary.append("\nNUMERICAL COLUMN STATISTICS:")
    summary.append(df.describe(include="number").to_string())

    summary.append("\nCATEGORICAL COLUMN DISTRIBUTION:")
    summary.append(df.describe(include="object").to_string())

    return "\n\n".join(summary)
    