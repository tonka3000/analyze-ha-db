import platform
import subprocess
import os
import shutil
from argparse import ArgumentParser
from pathlib import Path

def main():
    parser = ArgumentParser()
    parser.add_argument("inputfile", help="The encrypted Home Assistant backup tar filename")
    args = parser.parse_args()
    backup_tar_filename = args.inputfile.replace("\\", "/")

    extract_output_folder = os.path.join(os.path.dirname(backup_tar_filename), Path(backup_tar_filename).stem).replace("\\", "/")

    env = {**os.environ, "HA_BACKUP_TAR_FILENAME" : backup_tar_filename}
    if platform.system() == "Windows":
        print("Starting docker because unpack of secure tar files does not work stable on Windows")
        current_directory = os.path.dirname(os.path.abspath(__file__))
        subprocess.check_call([
                "docker", "run",
                "-v", f"{current_directory}:/workspace",
                "--rm",
                "-it",
                "-e", f"HA_BACKUP_TAR_FILENAME={backup_tar_filename}",
                "python:3.11",
                "bin/bash", "/workspace/extract_from_backup.sh"
            ],
            env=env
        )
    else:
        subprocess.check_call([
                "python", "/workspace/extract_from_backup.sh"
            ],
            env=env
        )

    print(f"Search for Home Assistant database in extracted backup in '{extract_output_folder}'")
    ha_db_extracted = os.path.join(extract_output_folder, "homeassistant", "data", "home-assistant_v2.db")
    if not os.path.exists(ha_db_extracted):
        raise ValueError(f"Home Assistant database does not exist at '{ha_db_extracted}'")

    current_directory = os.path.dirname(os.path.abspath(__file__))
    target_db_filename = os.path.join(current_directory, "home-assistant_v2.db")
    print(f"Copy extracted database file to '{target_db_filename}'")
    shutil.copy2(
        src=ha_db_extracted,
        dst=target_db_filename
    )
    print("Copy done")
    print("Remove extracted backup folder")
    shutil.rmtree(extract_output_folder)
    print("Extracted data removed")

if __name__ == "__main__":
    main()
