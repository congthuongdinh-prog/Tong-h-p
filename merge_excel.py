import io
from pathlib import Path
from typing import Iterable

import pandas as pd


def merge_excel_files(input_files: Iterable[str], output_file: str) -> None:
    frames = []
    for file in input_files:
        df = pd.read_excel(file)
        df["Source_File"] = Path(file).name
        frames.append(df)

    if not frames:
        raise ValueError("Khong co file de tong hop.")

    merged_df = pd.concat(frames, ignore_index=True)
    merged_df.to_excel(output_file, index=False)


def merge_uploaded_excel(uploaded_files) -> pd.DataFrame:
    """Tong hop cac file Excel upload tu Streamlit."""
    frames = []
    for uploaded_file in uploaded_files:
        df = pd.read_excel(io.BytesIO(uploaded_file.getvalue()))
        df["Source_File"] = uploaded_file.name
        frames.append(df)

    if not frames:
        raise ValueError("Khong co file de tong hop.")

    return pd.concat(frames, ignore_index=True)


if __name__ == "__main__":
    files_to_merge = [
        "demo_file_1.xlsx",
        "demo_file_2.xlsx",
        "demo_file_3.xlsx",
    ]
    output_path = "tong_hop_du_lieu.xlsx"

    merge_excel_files(files_to_merge, output_path)
    print(f"Da tong hop xong! File ket qua: {output_path}")
