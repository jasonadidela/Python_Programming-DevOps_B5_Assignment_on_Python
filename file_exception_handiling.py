import os
import sys
import shutil
import datetime

def backup_files(source_dir, dest_dir):
    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        files = os.listdir(source_dir)

        for file in files:
            src_path = os.path.join(source_dir, file)
            dest_path = os.path.join(dest_dir, file)

            if os.path.exists(dest_path):
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                base_name, ext = os.path.splitext(file)
                new_file_name = f"{base_name}_{timestamp}{ext}"
                dest_path = os.path.join(dest_dir, new_file_name)

            shutil.copy2(src_path, dest_path)
            print(f"Copied {file} to {dest_path}")

    except FileNotFoundError:
        print("Error: Source directory or destination directory does not exist.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
    else:
        source_directory = sys.argv[1]
        destination_directory = sys.argv[2]
        backup_files(source_directory, destination_directory)
