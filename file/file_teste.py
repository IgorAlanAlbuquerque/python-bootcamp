# %% [markdown]
# # Module: File Handling Assignments
# ## Lesson: File Handling and Operations
# ### Assignment 1: Reading a File
# 
# Write a function that reads the contents of a file named `sample.txt` and prints each line.

# %%
def read_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

#read_file('sample.txt')

# %% [markdown]
# ### Assignment 2: Writing to a File
# 
# Write a function that writes a list of strings to a file named `output.txt`, with each string on a new line.

# %%
def write_file(lines, filename):
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + '\n')


#write_file(['Hello', 'World'], 'output.txt')

# %% [markdown]
# ### Assignment 3: Copying a File
# 
# Write a function that copies the contents of a file named `source.txt` to a new file named `destination.txt`.

# %%
def copy_file(source, destination):
    with open(source, 'r') as src:
        with open(destination, 'w') as dest:
            dest.write(src.read())

#copy_file('source.txt', 'destination.txt')

# %% [markdown]
# ### Assignment 4: Appending to a File
# 
# Write a function that appends a given string to the end of a file named `log.txt`.

# %%
def append_to_file(text, filename):
    with open(filename, 'a') as file:
        file.write(text + '\n')

#append_to_file('This is a new log entry.', 'log.txt')

# %% [markdown]
# ### Assignment 5: Counting Words in a File
# 
# Write a function that reads the contents of a file named `document.txt` and returns the number of words in the file.

# %%
def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

#print(count_words('document.txt'))

# %% [markdown]
# ### Assignment 6: Finding and Replacing Text
# 
# Write a function that finds and replaces all occurrences of a given word in a file named `data.txt` with another word.

# %%
def find_and_replace(filename, old_word, new_word):
    with open(filename, 'r') as file:
        text = file.read()
    new_text = text.replace(old_word, new_word)
    with open(filename, 'w') as file:
        file.write(new_text)

#find_and_replace('output.txt', 'old', 'new')

# %% [markdown]
# ### Assignment 7: Reading a File in Reverse
# 
# Write a function that reads the contents of a file named `reverse.txt` and prints each line in reverse order.

# %%
def read_reverse(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in reversed(lines):
        print(line.strip())


#read_reverse('sample.txt')

# %% [markdown]
# ### Assignment 8: Counting Lines, Words, and Characters
# 
# Write a function that reads the contents of a file named `stats.txt` and returns the number of lines, words, and characters in the file.

# %%
def count_lwc(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        words = sum(len(line.split()) for line in lines)
        characters = sum(len(line) for line in lines)
    return len(lines), words, characters


#print(count_lwc('sample.txt'))

# %% [markdown]
# ### Assignment 9: Merging Multiple Files
# 
# Write a function that merges the contents of multiple files into a single file named `merged.txt`.

# %%
def merge_files(file_list, output_file):
    with open(output_file, 'w') as outfile:
        for fname in file_list:
            with open(fname, 'r') as infile:
                outfile.write(infile.read() + '\n')

#merge_files(['sample.txt', 'output.txt'], 'merged.txt')

# %% [markdown]
# ### Assignment 10: Splitting a Large File
# 
# Write a function that splits a large file named `large.txt` into smaller files of 100 lines each.

# %%
def split_file(filename, lines_per_file):
    with open(filename, 'r') as file:
        lines = file.readlines()
    for i in range(0, len(lines), lines_per_file):
        with open(f'{filename}_part{i//lines_per_file + 1}.txt', 'w') as part_file:
            part_file.writelines(lines[i:i + lines_per_file])


#split_file('sample.txt', 100)

# %% [markdown]
# ### Assignment 11: Creating a Log File
# 
# Write a function that creates a log file named `activity.log` and writes log messages with timestamps.

# %%
import datetime

def log_message(message, filename='activity.log'):
    timestamp = datetime.datetime.now().isoformat()
    with open(filename, 'a') as file:
        file.write(f'[{timestamp}] {message}\n')


#log_message('This is a log message.')

# %% [markdown]
# ### Assignment 12: Binary File Operations
# 
# Write a function that reads a binary file named `image.bin` and writes its contents to another binary file named `copy_image.bin`.

# %%
def copy_binary_file(source, destination):
    with open(source, 'rb') as src:
        with open(destination, 'wb') as dest:
            dest.write(src.read())

# copy_binary_file('image.bin', 'copy_image.bin')

# %% [markdown]
# ### Assignment 13: CSV File Operations
# 
# Write a function that reads a CSV file named `data.csv` and prints its contents as a list of dictionaries.

# %%
import csv

def read_csv_as_dicts(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

# print(read_csv_as_dicts('data.csv'))

# %% [markdown]
# ### Assignment 14: JSON File Operations
# 
# Write a function that reads a JSON file named `data.json` and prints its contents as a Python dictionary.

# %%
import json

def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data

# print(read_json('data.json'))

# %% [markdown]
# ### Assignment 15: File Permission Handling
# 
# Write a function that attempts to read a file named `protected.txt` and handles any permission errors gracefully by printing an error message.

# %%
def read_protected_file(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except PermissionError as e:
        print(f"Permission error: {e}")

# read_protected_file('protected.txt')


