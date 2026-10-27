
import os
import shutil

source_folder = input("Enter the source folder path: ").strip()
destination_folder = input("Enter the destination folder path: ").strip()

if not os.path.isdir(source_folder):
    print("Error: Source folder does not exist.")
else:
    os.makedirs(destination_folder, exist_ok=True)
    moved_count = 0

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(
                destination_folder, filename
            )

            if os.path.isfile(source_path):
                if os.path.exists(destination_path):
                    print(f"Skipped (already exists): {filename}")
                    continue

                shutil.move(source_path, destination_path)
                print(f"Moved: {filename}")
                moved_count += 1

    print(f"\nAutomation completed! Files moved: {moved_count}")
