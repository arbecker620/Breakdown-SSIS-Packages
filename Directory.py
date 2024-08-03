import os
from os import listdir




class Directory():


    def __init__(self, file_dir):
        self.dir = file_dir
        self.ssis_files = []

    def parse_directory_files(self)->list:
        #return list of all files in assigned directory/folder
        return listdir(self.dir) 

    def confirm_ssis(self,file_name:str)->bool:
        return file_name.endswith('.dtsx') #return true false if a file is a dtsx file/ssis package

    def parse_files(self):
        files = self.parse_directory_files()
        for file in files:
            if self.confirm_ssis(file):
                self.ssis_files.append(file) 
