#!/usr/bin/env python3
import re, os, subprocess, sys,time

home_dir = os.path.expanduser('~')

media_dir = '/media/EXTRA/Movies'

downloads_directory = os.path.join(home_dir,'Downloads')

# Joining command-line arguments into a single string
dir_name = ' '.join(sys.argv[1:])

def dir_name_cleanup(dir_name):
    # Define a regular expression pattern to match unwanted text and resolution information
    unwanted_pattern = r'(.*)(\(\d{4}\))(.*)'
    # Use the re.match() function to match the pattern to the dir_name
    match = re.match(unwanted_pattern, dir_name)
    # If the pattern matches, remove the unwanted text and resolution information
    new_name = match.group(1)+ match.group(2)
    # Return the cleaned-up dir_name
    return new_name



def rename_dir(dir_name,new_name):
    path = media_dir
    
    os.rename(os.path.join(path, dir_name), os.path.join(path, new_name))
    
    # print('Done')
    
    
    

def rename_files(directory):
    pattern = r"^(.*?)\.\d{4}\..*(\.(mp4|mkv|srt))$"

    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):  # Check if it's a file, not a directory
            match = re.match(pattern, file)
            if match:
                
                # print(f"'{file}' matches the pattern")
                
                title = match.group(1).replace('.', ' ')
                extension = match.group(2)
                old_path = os.path.join(directory, file)
                new_path = os.path.join(directory, title + extension)
                os.rename(old_path, new_path)
                
                # print(f"'{file}' renamed to '{title + extension}'")


def move():
    rename_files(os.path.join(downloads_directory, dir_name))
    
    if os.name != 'nt':
        print(f"{os.path.join(downloads_directory, dir_name)} and '/media/EXTRA/Movies/'")
        subprocess.run(f"mv '{os.path.join(downloads_directory, dir_name)}' '/media/EXTRA/Movies/'", shell=True)
        
    
   

if __name__ == "__main__":
    move()
    new_name = dir_name_cleanup(dir_name)
    rename_dir(dir_name,new_name)
