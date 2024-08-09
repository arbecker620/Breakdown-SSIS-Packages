import os
from lxml import etree
from mdutils.mdutils import MdUtils
import xml.etree.ElementTree as ET
import typer
from tqdm import tqdm

from Directory import Directory
from Summary import Summary

#Output Results directory
#assign Direcotry to Output Results

app = typer.Typer()

@app.command()
def main(file_dir: str):
    mdFile = MdUtils(file_name='SSIS Packages Review', title='Results of SSIS')


    print("reading files.....")

    file_directory = Directory(file_dir)


    list_dir_files = file_directory.parse_directory_files()
    file_directory.parse_files()

    mdFile.new_header(level=1, title="Files Reviewed")
    mdFile.new_paragraph("This is the following items which are analyzed")
    summary = '\n'.join(file_directory.ssis_files)
    mdFile.new_paragraph(summary)



    for ssis_package in file_directory.ssis_files:

        xmlTree = ET.parse(ssis_package)
        elemList = []
    # now I remove duplicities - by convertion to set and back to list

        tree = etree.parse(ssis_package)
        root = tree.getroot()
 
        total_bytes = 0

        list_properties = []
        list_path_info = []
        list_connection_strings = []
        list_sql_statements = []

        for cnt, ele in tqdm(enumerate(root.xpath(".//*"))):

            ###Get SQL Code
            if ele.tag == "{www.microsoft.com/SqlServer/Dts}Executable": 
                for child0 in ele:
                    if child0.tag == "{www.microsoft.com/SqlServer/Dts}ObjectData":
                        for child1 in child0:
                            sql_comment = child1.tag
                            if child1.tag == "{www.microsoft.com/sqlserver/dts/tasks/sqltask}SqlTaskData":
                                dtsx_sql = child1.attrib["{www.microsoft.com/sqlserver/dts/tasks/sqltask}SqlStatementSource"]
                                dtsx_sql = "-- " + sql_comment + "\n" + dtsx_sql
                                #mdFile.new_paragraph(dtsx_sql)
                                list_sql_statements.append(dtsx_sql)
            elif ele.tag== 'path':
                #print(ele.tag)
                dict_path = dict(ele.attrib)
                path_summary = []
                for k,v in dict_path.items():
                    line = str(k)+" : "+str(v)
                    path_summary.append(line)
                #print(list_path_info)
                #take key and value, combin into a string, then add a new line to string then
                
                #print(ele.attrib[0][0])
                list_path_info.append(path_summary)
                #list_path_info= "\n".join(path_summary)

            elif ele.tag == 'output' or ele.tag == 'outputColumn':  #finish getting data from here
                print("")

                #print(ele.attrib)
            elif ele.tag == 'inputColumn' or ele.tag == 'input': #finish data from here
                print("")
                #print(ele.text)
                #print(ele.attrib)
            elif ele.tag == 'property':
                print("")
                #print(ele.attrib)
                #print(ele.text)
            elif ele.tag == 'connection' or ele.tag == 'ConnectionManager':
                print("Connection1")

                print(ele.attrib)
                #print(ele.text)
            elif ele.tag == "{www.microsoft.com/SqlServer/Dts}Property":
                #print("property")
                #print(ele.attrib)

                dict_path = dict(ele.attrib)
                #dict_text = dict(ele.text)
                for i, v  in dict_path.items():
                    if i == '{www.microsoft.com/SqlServer/Dts}Name' and v == 'ConnectionString':
                        list_connection_strings.append(ele.text)
                        


                    #print(dict_path,ele.text)
                #print(dict_text)

                #list_properties.append(ele.attrib)
                #list_properties.append(ele.text)

                #print(ele.attrib)

                    #for child1 in child0:
                    #    print(child1)
                    #for child1 in child0:
                    #    print(child1.tag)
        
        
        mdFile.new_header(level=1, title="Paths")
        mdFile.new_paragraph("The information below depicts the data flows or paths which is being used inside of the SSIS Package.")
        for path in list_path_info:
            summary="\n".join(path)
            mdFile.new_paragraph(summary)

        mdFile.new_header(level=1, title="Connection Strings")
        mdFile.new_paragraph("This is the identified Connection Strings inside of this SSIS Package")
        for connection in list_connection_strings:
            summary="".join(connection)
            mdFile.new_paragraph(summary)

        mdFile.new_header(level=1, title="SQL Statements inside ExecutableFile")
        mdFile.new_paragraph("This is the SQL Statement inside of the Executable")
        for Statements in list_sql_statements:
            summary="".join(Statements)
            mdFile.new_paragraph(summary)


        

    #print(list_properties)
    mdFile.create_md_file()
    #print(values)


@app.command()
def verify_folder(file_dir: str):
    file_directory = Directory(file_dir)


    list_dir_files = file_directory.parse_directory_files()
    file_directory.parse_files()
    print(file_directory.ssis_files)



if __name__ == "__main__":
    app()
