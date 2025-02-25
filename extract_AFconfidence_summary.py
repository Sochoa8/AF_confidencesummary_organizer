import json
import csv
from tkinter import Tk, filedialog

def main():
    # Prompt user to select JSON files
    Tk().withdraw()  # Hide the root Tkinter window
    file_paths = filedialog.askopenfilenames(
        title="Select AlphaFold 3 Confidence Summary JSON Files",
        filetypes=[("JSON Files", "*.json")]
    )

    if not file_paths:
        print("No files selected. Exiting...")
        return

    # Collect data from each file
    data_list = []
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                file_name = file_path.split("/")[-1]  # Get the file name
                # Extract relevant data
                data_entry = {
                    "File Name": file_name,
                    "iPTM": data.get("iptm", None),
                    "pTM": data.get("ptm", None),
                    "Ranking Score": data.get("ranking_score", None),
                    "Number of Recycles": data.get("num_recycles", None),
                    "Fraction Disordered": data.get("fraction_disordered", None),
                    "Has Clash": data.get("has_clash", None),
                    "Chain Pair iPTM": data.get("chain_pair_iptm", None),
                    "Chain Pair PAE Min": data.get("chain_pair_pae_min", None),
                    "Chain PTM": data.get("chain_ptm",None),
                }
                data_list.append(data_entry)
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

    # Write collected data to a CSV file
    output_file = "alphafold_confidence_summary2.csv"
    try:
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = [
                "File Name", "iPTM", "pTM", "Ranking Score",
                "Number of Recycles", "Fraction Disordered",
                "Has Clash", "Chain Pair iPTM", "Chain Pair PAE Min", "Chain PTM"
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data_list:
                writer.writerow(row)
        print(f"Data successfully saved to {output_file}")
    except Exception as e:
        print(f"Error writing to CSV file: {e}")

if __name__ == "__main__":
    main()