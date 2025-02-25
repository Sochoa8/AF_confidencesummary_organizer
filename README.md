# AF_confidencesummary_organizer

## Overview
This Python script extracts key structural confidence metrics from **AlphaFold 3 JSON summary files** and compiles them into a CSV for further analysis.

## Features
- Parses multiple AlphaFold 3-generated JSON files.
- Extracts confidence scores such as **iPTM, pTM, ranking score, disorder fraction, and more**.
- Saves the results in a structured CSV file.

## Installation
Clone this repository:
```bash
git clone https://github.com/Sochoa8/AF_confidencesummary_organizer.git
cd AF_confidencesummary_organizer
```
This script only requires Python 3 and standard libraries (json, csv, tkinter), so no extra installation is needed.

## Usage
Run the script:
```
python extract_AFconfidence_summary.py
```
- You will be prompted to select JSON files.
- The extracted data will be saved in alphafold_confidence_summary2.csv.

Example Output:

| File Name     | iPTM | pTM  | Ranking Score | Recycles | Fraction Disordered |
|--------------|------|------|--------------|----------|------------------|
| model_1.json | 0.85 | 0.92 | 90.2         | 3        | 0.12             |
| model_2.json | 0.78 | 0.88 | 87.6         | 3        | 0.10             |
