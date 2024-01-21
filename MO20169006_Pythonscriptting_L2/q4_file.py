import re


try:
     file1 = open('q4_file_doc.txt', 'r')
     Lines = file1.readlines()
     
     for line in Lines:
            word = re.search(r"([AEIOUaeiou][AEIOUaeiou])", line)
            if word is not None:
                    print(line)
           
except FileNotFoundError:
    print(f"File '{filename}' not found.")
