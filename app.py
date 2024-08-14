import os
from lxml import etree
from mdutils.mdutils import MdUtils
import xml.etree.ElementTree as ET
import typer
from tqdm import tqdm

from Directory import Directory
from Summary import Summary
from Package import Package,Package_Exectution, Package_MetaData

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
        #package = Package(ssis_package, file_dir)

    # now I remove duplicities - by convertion to set and back to list
        
        tree = etree.parse(ssis_package)
        root = tree.getroot()
 
        total_bytes = 0

        list_properties = []
        package_meta = Package_MetaData(ssis_package, file_dir)

        package_exec = Package_Exectution(ssis_package,file_dir)

        for cnt, ele in tqdm(enumerate(root.xpath(".//*"))):

            if ele.tag == "{www.microsoft.com/SqlServer/Dts}Executable": 
                for child0 in ele:
                    if child0.tag == "{www.microsoft.com/SqlServer/Dts}ObjectData":
                        for child1 in child0:
                            sql_comment = child1.tag
                            if child1.tag == "{www.microsoft.com/sqlserver/dts/tasks/sqltask}SqlTaskData":
                                dtsx_sql = child1.attrib["{www.microsoft.com/sqlserver/dts/tasks/sqltask}SqlStatementSource"]
                                dtsx_sql = "-- " + sql_comment + "\n" + dtsx_sql

                                package_exec.list_sql_statements.append(dtsx_sql)
                                
            elif ele.tag== 'path':
                dict_path = dict(ele.attrib)
                path_summary = []
                for k,v in dict_path.items():
                    line = str(k)+" : "+str(v)
                    path_summary.append(line)

                package_exec.list_path_info.append(path_summary)


            elif ele.tag == 'output' or ele.tag == 'outputColumn':  #finish getting data from here
                dict_path = dict(ele.attrib)
                output_summary = []
                for k,v in dict_path.items():
                    line = str(k)+" : "+str(v)
                    output_summary.append(line)

                package_exec.list_output_columns.append(output_summary)

            elif ele.tag == 'inputColumn' or ele.tag == 'input': #finish data from here
                dict_path = dict(ele.attrib)
                input_summary = []
                for k,v in dict_path.items():
                    line = str(k)+" : "+str(v)
                    input_summary.append(line)

                package_exec.list_input_columns.append(input_summary)

            elif ele.tag == 'property':
                print(ele.attrib)
            elif ele.tag == 'connection' or ele.tag == 'ConnectionManager':
                dict_path = dict(ele.attrib)
                connection_summary = []
                for k,v in dict_path.items():
                    line = str(k)+" : "+str(v)
                    connection_summary.append(line)

                package_exec.list_connection_info.append(connection_summary)

            elif ele.tag == "{www.microsoft.com/SqlServer/Dts}Property":
                
                dict_path = dict(ele.attrib)
                for i, v  in dict_path.items():
                    if i == '{www.microsoft.com/SqlServer/Dts}Name' and v == 'ConnectionString':
                        package_exec.list_connection_strings.append(ele.text)
                        
        
        mdFile.new_header(level=1, title=ssis_package)

        
        mdFile.new_header(level=1, title="Paths")
        mdFile.new_paragraph("The information below depicts the data flows or paths which is being used inside of the SSIS Package.")
        for path in package_exec.list_path_info:
            summary="\n".join(path)
            mdFile.new_paragraph(summary)

        mdFile.new_header(level=1, title="Connection Information")
        mdFile.new_paragraph("This is the identified Connection Types in inside of this SSIS Package. \nRefer to the Connection String section to see where the SSIS package is connected to. ")
        for connection in  package_exec.list_connection_info:
            summary="\n".join(connection)
            mdFile.new_paragraph(summary)


        mdFile.new_header(level=1, title="Connection Strings")
        mdFile.new_paragraph("This is the identified Connection Strings inside of this SSIS Package")
        for connection in  package_exec.list_connection_strings:
            summary="".join(connection)
            mdFile.new_paragraph(summary)


        mdFile.new_header(level=1, title="Input Columns")
        mdFile.new_paragraph("This is the identified Input Columns inside of this SSIS Package")
        for input_cols in  package_exec.list_input_columns:
            summary="\n".join(input_cols)
            mdFile.new_paragraph(summary)


        mdFile.new_header(level=1, title="Output Columns")
        mdFile.new_paragraph("This is the identified Output Columns inside of this SSIS Package")
        for connection in  package_exec.list_output_columns:
            summary="\n".join(connection)
            mdFile.new_paragraph(summary)

        mdFile.new_header(level=1, title="SQL Statements inside ExecutableFile")
        mdFile.new_paragraph("This is the SQL Statement inside of the Executable")
        for Statements in package_exec.list_sql_statements:
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
