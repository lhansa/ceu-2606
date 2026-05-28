"""
Extracts media channel sheets from the Excel macro file and saves each as a CSV in processed/data-monitor/.

Usage:
    python src/extract_media_channels.py

Requirements:
    - pandas
    - openpyxl

The script will extract all sheets from 'TV' through 'AnyOtherMedia' (inclusive) as separate CSV files.
"""
import os
import pandas as pd

RAW_XLSM = os.path.join('data', 'raw', 'Media Database Template V1.2.3.xlsm')
OUT_DIR = os.path.join('data', 'processed', 'data-monitor')

# List of media channel sheet names (adjust as needed)
MEDIA_CHANNELS = [
    'TV',
    'TV Sponsorship',
    'Youtube',
    'VOD',
    'Radio',
    'Social',
    'PPC',
    'Press',
    'OOH',
    'Display',
    'Affiliates',
    'CRM',
    'AnyOtherMedia'
]

def main():
    # Load all sheet names
    xls = pd.ExcelFile(RAW_XLSM, engine='openpyxl')
    available_sheets = xls.sheet_names
    print(f"Available sheets: {available_sheets}")

    os.makedirs(OUT_DIR, exist_ok=True)
    for sheet in MEDIA_CHANNELS:
        if sheet in available_sheets:
            print(f"Extracting {sheet}...")
            df = pd.read_excel(RAW_XLSM, sheet_name=sheet, engine='openpyxl')
            # Replace 'Dreams' with 'ClientBrand' in the first column if it is 'Brand'
            if not df.empty and df.columns[0] == 'Brand':
                df[df.columns[0]] = df[df.columns[0]].replace('Dreams', 'ClientBrand')
            out_path = os.path.join(OUT_DIR, f"{sheet}.csv")
            df.to_csv(out_path, index=False)
        else:
            print(f"Warning: Sheet '{sheet}' not found in workbook.")
    print("Extraction complete.")

if __name__ == "__main__":
    main()
