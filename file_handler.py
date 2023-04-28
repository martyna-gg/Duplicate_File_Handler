import os
import sys
import hashlib

args = sys.argv  # take directory as an argument
if len(args) == 1:
    print("Directory is not specified")
else:
    decision1 = input('Enter file format:')  # specify a file format
    decision2 = input('''Size sorting options:
1. Descending
2. Ascending''')  # specify type of sorting
    while decision2 not in ['1', '2']:
        print('Wrong option')
        decision2 = input('''Size sorting options:
1. Descending
2. Ascending''')
    files_sizes = {}
    for root, dirs, files in os.walk(args[1], topdown=True):  # create a dict with files and their sizes
        for name in files:
            if name.endswith(decision1) or decision1 == '':
                if os.path.getsize(os.path.join(root, name)) in files_sizes:
                    files_sizes[os.path.getsize(os.path.join(root, name))].append(os.path.join(root, name))
                else:
                    files_sizes[(os.path.getsize(os.path.join(root, name)))] = [os.path.join(root, name)]
    # create a dict with files od the same sizes with sizes as keys
    files_same_size = {key: value for (key, value) in files_sizes.items() if len(value) > 1}
    files_sizes =  list(files_same_size.keys())
    if decision2 == '1':
        files_sizes.sort(reverse=True)
    else:
        files_sizes.sort()
    files_same_size_sorted = {i: files_same_size[i] for i in files_sizes}  # sort the dict
    files_same_size = files_same_size_sorted

    for key in files_same_size:  # print the list of same size files
        print(str(key) + ' bytes')
        for x in files_same_size[key]:
            print(x)
        print()

    decision3 = input('Check for duplicates?')  # decision if checking for duplicates
    while decision3 not in ['yes', 'no']:
        print('Wrong option')
        decision3 = input('Check for duplicates?')
    if decision3 == 'yes':
        files_hash = {key: {} for key in files_same_size}  # create a dict with files of same sizes with hashes
        for key in files_same_size:
            for x in files_same_size[key]:
                with open(x, 'rb') as x_file:
                    hash_x = hashlib.md5((x_file.read())).hexdigest()
                    if hash_x in files_hash[key]:
                        files_hash[key][hash_x].append(x)
                    else:
                        files_hash[key][hash_x] = [x]

    files_same_hash = {key: {} for key in files_hash}  # creates a dict with files of same size and same hash
    for size in files_hash:
        for hash_v in files_hash[size]:
            if len(files_hash[size][hash_v]) > 1:
                files_same_hash[size].update({hash_v: files_hash[size][hash_v]})
                
    counter = 1  # prints list of files of same size and same hash
    for size in files_same_hash:
        print(str(size) + ' bytes')
        for hash_v in files_same_hash[size]:
            print('Hash: ' + str(hash_v))
            for x in files_same_hash[size][hash_v]:
                x = str(counter) + '. ' + x
                counter += 1
                print(x)
        print()

    decision4 = input('Delete files?') # decision of deleting duplicates
    while decision4 not in ['yes', 'no']:
        print('Wrong option')
        decision4 = input('Check for duplicates?')
    if decision4 == 'yes':

        decision5 = input('Enter file numbers to delete:')  # decision which files to delete
        try:
            while not (decision5 != '' and all([int(x) in range(1, counter+1) for x in decision5.split(' ')])):
                print("Wrong format")
                decision5 = input('Give me numbers')
        except:
            print("Wrong format")
            decision5 = input('Give me numbers')

        files_del = [int(x) for x in decision5.split(' ')]  # deleting files
        freed_space = 0
        counter = 0
        for size in files_same_hash:
            for hash_v in files_same_hash[size]:
                for x in files_same_hash[size][hash_v]:
                    counter += 1
                    if counter in files_del:
                        freed_space += int(size)
                        os.remove(x)

        print('Total freed up space:' + str(freed_space) + ' bytes')

