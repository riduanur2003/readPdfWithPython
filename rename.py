import os
import sys

directory = sys.path[0]+r"\files"

# def rename_files(directory, new_name_template):
#     # Get a list of files in the directory

files = os.listdir(directory)

counter = 11
for file in files:
   counter= counter+1
   os.rename(os.path.join(directory, file), os.path.join(directory, 'xyz_' + str(counter) + '.pdf'))

    
#     for count, filename in enumerate(files):
#         # Construct the new file name
#         new_name = f"{new_name_template}_{count}{os.path.splitext(filename)[1]}"
        
#         # Create the full paths
#         old_file = os.path.join(directory, filename)
#         new_file = os.path.join(directory, new_name)
        
#         # Rename the file
#         os.rename(old_file, new_file)
#         print(f"Renamed '{old_file}' to '{new_file}'")

# # Example usage
# directory = '/path/to/your/directory'
# new_name_template = 'new_name'
# rename_files(directory, new_name_template)