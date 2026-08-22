import os
import shutil

folder = input("Enter folder path: ").strip()

# Remove automatically pasted quotes
folder = folder.strip('"').strip("'")

if not os.path.isdir(folder):
    print("❌ Folder does not exist!")
    print("You entered:", folder)
    exit()

print("✅ Folder found!")
print("Starting organization...\n")
print("\n📁 Organizing files...\n")

file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Excel": [".xls", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"]
}

files_found = False

for filename in os.listdir(folder):

    file_path = os.path.join(folder, filename)

    # Skip existing folders
    if os.path.isdir(file_path):
        continue

    files_found = True

    extension = os.path.splitext(filename)[1].lower()

    category_found = False

    for category, extensions in file_categories.items():

        if extension in extensions:

            category_path = os.path.join(folder, category)
            os.makedirs(category_path, exist_ok=True)

            shutil.move(
                file_path,
                os.path.join(category_path, filename)
            )

            print(f"✅ {filename} → {category}")
            category_found = True
            break

    if not category_found:

        other_folder = os.path.join(folder, "Others")
        os.makedirs(other_folder, exist_ok=True)

        shutil.move(
            file_path,
            os.path.join(other_folder, filename)
        )

        print(f"✅ {filename} → Others")


if not files_found:
    print("ℹ️ No files to organize.")
else:
    print("\n🎉 File organization completed!")