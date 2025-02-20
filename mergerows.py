import pandas as pd

# Specify the correct CSV file path
file_path = "your_file.csv"  # Ensure this is the correct path

# Read the CSV file with proper encoding
df = pd.read_csv(file_path, encoding="utf-8")

# Ensure correct column names (update if needed)
id_col = "H"  # Change this to the actual column name for Deal ID
text_col = "B"  # Change this to the actual column name for text/comments

# Fill NaN values in the text column to avoid issues when merging
df[text_col] = df[text_col].fillna("")

# Convert Deal ID to integer (handling NaN values properly)
df[id_col] = pd.to_numeric(df[id_col], errors="coerce").fillna(0).astype(int)

# Group by ID and merge text, ensuring all related comments are combined
df_grouped = df.groupby(id_col, as_index=False)[text_col].agg(lambda x: ', '.join(x.astype(str)))

# Get the full range of Deal IDs to ensure all numbers are represented
full_range = pd.DataFrame({id_col: range(df[id_col].min(), df[id_col].max() + 1)})

# Merge with grouped data to ensure all Deal IDs are present, filling missing text with blanks
df_final = full_range.merge(df_grouped, on=id_col, how="left").fillna("")

# Save to a new CSV file with correct encoding
output_file = "merged_output.csv"
df_final.to_csv(output_file, index=False, encoding="utf-8-sig")

print(f"Processed file saved as {output_file}")
