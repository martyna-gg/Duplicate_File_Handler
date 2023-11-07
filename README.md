# Duplicate_File_Handler

A program for detecting and removing duplicate files with usage of os, sys and hashlib modules, lists, dicts, if/else statements, while and for loops and processing user input.

## Installation

Os, sys and hashlib modules are python built-in modules. No installation is required.

## Requirements

Code was developed and tested using: 

Ubuntu 18.04.6 LTS 

Python 3.6.9

## Usage

While running a program from the terminal, please pass the directory you want to check for duplicates as an argument.
```
$ python3 file_handler.py /home/martyna/Downloads

```
Then program will ask you to define the format of files you want to check (if you want to check all the formats just press Enter). Next you need to decide if you want the files to be listed in ascending or descending order. Afterwards a list of all files of the same size will be printed.
```
$ python3 file_handler.py /home/martyna/Downloads
Enter file format: >jpg
Size sorting options:
1. Descending
2. Ascending
> 1
607681 bytes
/home/martyna/Downloads/hdimged38f3776e673701a9341887dee1cb (copy).jpg
/home/martyna/Downloads/hdimged38f3776e673701a9341887dee1cb.jpg

413270 bytes
/home/martyna/Downloads/hdimg27036eb627db468c3e11ff29badaa8 (another copy).jpg
/home/martyna/Downloads/hdimg27036eb627db468c3e11ff29badaa8 (copy).jpg
/home/martyna/Downloads/hdimg27036eb627db468c3e11ff29badaa8.jpg

```
In the next step the program will ask you if you want to check the files of the same size for duplicates among them. If you insert yes the list of duplicates will be printed. Otherwise the program will stop running.

```
Check for duplicates? >yes
607681 bytes
Hash: 7dec62fe10fc80569034b6ee6c7e6e19
1. /home/martyna/Downloads/hdimged38f3776e673701a9341887dee1cb (copy).jpg
2. /home/martyna/Downloads/hdimged38f3776e673701a9341887dee1cb.jpg

413270 bytes
Hash: 95931ba28bd7873997f5a68dfc60bbe2
3. /home/martyna/Downloads/hdimg27036eb627db468c3e11ff29badaa8  (copy).jpg
4. /home/martyna/Downloads/hdimg27036eb627db468c3e11ff29badaa8  (another copy).jpg
5. /home/martyna/Downloads/hdimg27036eb627db468c3e11ff29badaa8 .jpg

```

After that you need to decide if you want to delete the duplicates. If you do, you need to specify which files should be deleted by inserting numbers of the files in the list (separated by white space). When you do so, the files will be deleted and the information about freed up space will be printed. If you won't decide to delete any files the program will stop running.

```
Delete files? >yes
Enter file numbers to delete: >1 3 4
Total freed up space:1434221 bytes

```

## Support

If you face any problem let me know by Issue.



