#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Remove_extension.py: Changes all extension name on all sibling directories ."""

__author__      = "Pablo Pérez"
__license__ = "GPL"
__version__ = "1.0.1"

import os
import logging

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='output.log', encoding='utf-8', level=logging.DEBUG)


def make_log(old, new):
    n = len(old)
    i = 0
    
    changes_list = list()
    while(i < n ):
        if old[i] != new[i]:
            logging.info(f'INFO: Modified: {old[i]} -> {new[i]}')
         
            changes_list.append(f'.../{ "/".join( old[i].split("/")[-3::] )  } -> .../{ "/".join(new[i].split("/")[-3::] ) }')
        i += 1
    
    return changes_list

def change_extension(directories):
    for direc in directories:   
        
        current_dir = os.listdir(direc)
        
        # check if directory is not empty
        if any(os.scandir(direc)):
            name_files_older = [ direc + '/' + x for x in current_dir ]
            
            # List dir and get namefiles listdir(direc), if file ends with '.md' remove suffix '.md', if not dont do nothing
            file_name_list = [ x.removesuffix('.md') if x.endswith('.md') else x for x in current_dir ]
            
            # Change 
            name_files_newer = [ direc + '/' + name  for name in file_name_list ]
        else:
            continue
        

        try:
            n = len(file_name_list)
            
            for i in range(0,n):
                if name_files_older[i] != name_files_newer[i]:
                    os.rename(name_files_older[i], name_files_newer[i])
                    
            return name_files_older, name_files_newer
        
        except FileNotFoundError as err:
            logging.error(f'ERROR: {err}')
            return
            

def get_list_directories():
    current_dir = os.getcwd()
    all_directories = [ x[0] for x in os.walk(current_dir) if ".git" not in x[0] and not x[0].endswith('personal') ]
    return all_directories 


def main():
    try:
        logging.info('INFO: Started')

        directories = get_list_directories()
        old_dir, new_dir = change_extension(directories)
        
        changes = make_log(old_dir, new_dir)


        logging.info('INFO: Finished')
    
    except Exception as e:
        logging.error(f'ERROR: {e}')
        print('Error Ocurred! Review the output.log file')

    print("Changes")
    print( [mod for mod in changes][0] )

if __name__ == '__main__':   
    
    main()
    