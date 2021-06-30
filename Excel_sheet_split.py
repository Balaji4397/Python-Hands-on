import os
import time
import shutil
import pandas as pd

def split():
    main_file = os.getcwd()
    split_files_lst, split_file_lst = [], []
    limit = 10000
    row_start = 0
    row_end = limit
    file_sequence = 0
    for file in os.listdir():
        if file.endswith(".xlsx"):
            file_name = file.split('.',1)
            file_path = f"{main_file}\{file}"
            new_folder = f"{main_file}\{file_name[0]}"
            df = pd.read_excel (file_path)
            number_of_splits = len(df)//limit
            rest_of_rows = len(df)
            if number_of_splits >0 and len(df)%limit > 0:
                number_of_splits = number_of_splits + 1
            if number_of_splits > 0:
                try:
                    os.mkdir(new_folder)
                except:
                    shutil.rmtree(new_folder)
                    time.sleep(5)
                    os.mkdir(new_folder)
                for y in range(1,number_of_splits+1):
                    split_files = file_name[0]+ "_" + str(y)
                    split_files_lst.append(split_files)
                    split_file_path = f"{new_folder}\{split_files}.xlsx"
                    split_file_lst.append(split_file_path)
                for y in range(1,number_of_splits+1):
                    if y < number_of_splits:
                        split_files_lst[file_sequence] = df[row_start:row_end]
                        row_start = row_end
                        row_end = row_end + limit  
                    else:
                        split_files_lst[file_sequence] = df[row_start:rest_of_rows]
                        file_sequence = file_sequence - 1
                    file_sequence = file_sequence + 1
                for x in range(0,len(split_files_lst)):
                    split_files_lst[x].to_excel(split_file_lst[x], index=False)     
            else:
                continue
        split_files_lst, split_file_lst = [], []
        row_start = 0
        row_end = limit
        file_sequence = 0       
split()
