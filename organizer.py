from datetime import datetime
from pathlib import Path
import os

my_files = Path(r'C:\Users\dell\Desktop\fileorganizer')

# is the path a file?
print(my_files.is_file())  # return fale

# is the path a dir?
print(my_files.is_dir())  # return true


# What is the parent of the file?
print(my_files.parent)


# What is the base of the filename?
print(my_files.stem)


# What are the extensions of the file?
print(my_files.suffix)

# for file in my_files.iterdir():
#     directory = file.parent
#     extension = file.suffix
#     old_name = file.stem
#     new_name = old_name.replace('text', 'text.txt')
#     file.rename(Path(directory, new_name+extension))

for file in my_files.iterdir():

    # 1) Check if the file is a file
    if file.is_file() and file.stem != ".DS_Store":
        # 2) Create helpful variables
        directory = file.parent
        extension = file.suffix

        old_name = file.stem
        region, report_type, old_date = old_name.split('-')

        # 3) Change date format and label the new file
        old_date = datetime.strptime(old_date, "%Y%b%d")
        date = datetime.strftime(old_date, '%Y-%m-%d')
        new_file = f'{date} - {region} - {report_type}{extension}'

        # 4) Calculate the month and create a new path with it
        month = datetime.strftime(old_date, "%B")
        new_path = my_files.joinpath(month)

        # 5) Check if the folder exists. If not, create it
        if not new_path.exists():
            new_path.mkdir()

        # 6) Create a new path in the new directory
        new_file_path = new_path.joinpath(new_file)

        # 7) Move the files
        file.replace(new_file_path)
