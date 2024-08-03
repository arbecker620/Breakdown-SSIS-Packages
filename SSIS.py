import os
from lxml import etree
from mdutils.mdutils import MdUtils

#Output Results directory
#assign Direcotry to Output Results

mdFile = MdUtils(file_name='SSIS Packages Review', title='Results of SSIS')

#if os.name == 'posix':
#    string_seperator ='//'
#else:
#    string_seperator = '\\'

#sql_out = f"C:{string_seperator}temp{string_seperator}dtsxsql"
sql_out = r'C:/temp/dtsxsql'
#if output directory does not exist
if not os.path.isdir(sql_out):
#create output directory at the assigned location
    os.makedirs(sql_out)


sql_out = os.getcwd()

#print(sql_out)
#input SSIS Package
#assign the SSIS Package to Parse
print("reading files.....")
ssis_dtsx = r'C:\temp\dtsx\ParseXML.dtsx'

print(os.path.isfile(ssis_dtsx))


#if package is not in this assigned location
if not os.path.isfile(ssis_dtsx):
#print no SSIS Package in the directory
    mdFile.create_md_file()
    print("no package file")