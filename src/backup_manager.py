import shutil
from pathlib import Path

def get_category(file_path, file_types):
    for category, extensions in file_types.items():
        if file_path.suffix.lower() in extensions:
            return category
    return "others"

def backup_files(files, backup_dir, file_types, logger):
    for file in files:
        category = get_category(file, file_types)
        target_dir = Path(backup_dir) / category
        target_dir.mkdir(parents=True, exist_ok=True)

        target_file = target_dir / file.name
        shutil.copy2(file, target_file)

        logger.info(f"Backed up {file} to {target_file}")
