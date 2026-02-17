from pathlib import Path

def scan_files(source_dir):
    return [file for file in Path(source_dir).rglob("*") if file.is_file()]
