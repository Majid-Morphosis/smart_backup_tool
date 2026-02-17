import yaml
from src.logger import setup_logger
from src.file_scanner import scan_files
from src.backup_manager import backup_files

def load_config():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)

def main():
    config = load_config()

    logger = setup_logger(config["log_file"])
    logger.info("Backup process started")

    files = scan_files(config["source_directory"])
    backup_files(
        files,
        config["backup_directory"],
        config["file_types"],
        logger
    )

    logger.info("Backup process completed")
    print("✅ Backup completed successfully.")

if __name__ == "__main__":
    main()
