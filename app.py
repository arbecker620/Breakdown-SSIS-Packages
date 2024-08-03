import os
from lxml import etree
from mdutils.mdutils import MdUtils
import xml.etree.ElementTree as ET
import typer

from Directory import Directory

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
        for elem in xmlTree.iter():
            elemList.append(elem.tag)
    # now I remove duplicities - by convertion to set and back to list

        elemList = list(set(elemList))
    # Just printing out the result
        #print(elemList)
        print(elemList)
        print("List1")
        tree = etree.parse(ssis_package)
        root = tree.getroot()
        #print(root.tag) 
        #print(tree)
        #print(root.xpath)
        total_bytes = 0
        for tag in elemList:
            term = f".//{tag}"
            #print(term)
            print("Monroe")
            links = tree.findall(term)
            for i in links:
                #print(i.tag)
                print(i.attrib)
                print(i.iter)
                print(i.text)
        list_properties = []
        list_path_info = []

        for cnt, ele in enumerate(root.xpath(".//*")):

            print(ele.tag)
            ###Get SQL COde
            if ele.tag == "{www.microsoft.com/SqlServer/Dts}Executable":
                #attr = ele.attrib
                for child0 in ele:
                    #print(child0.tag)
                    if child0.tag == "{www.microsoft.com/SqlServer/Dts}ObjectData":
                        #print("Andrew Check this One")
                        for child1 in child0:
                            #print(child1.tag)
                            sql_comment = child1.tag
                            if child1.tag == "{www.microsoft.com/sqlserver/dts/tasks/sqltask}SqlTaskData":
                                mdFile.new_header(title=ssis_package, level=1)
                                dtsx_sql = child1.attrib["{www.microsoft.com/sqlserver/dts/tasks/sqltask}SqlStatementSource"]
                                dtsx_sql = "-- " + sql_comment + "\n" + dtsx_sql
                                #print(dtsx_sql)
                                mdFile.new_paragraph(dtsx_sql)
            elif ele.tag== 'path':
                #print(ele.tag)
                dict_path = dict(ele.attrib)
                for i in dict_path:
                    list_path_info.extend([i, dict_path[i]])
                #print(ele.attrib[0][0])
            elif ele.tag == 'output' or ele.tag == 'outputColumn':
                print("output1")
                #print(ele.attrib)
                print(ele.attrib)
            elif ele.tag == 'inputColumn' or ele.tag == 'input':
                print("inputcolumn")
                #print(ele.text)
                #print(ele.attrib)
            elif ele.tag == 'property':
                print("propoerty1")
                #print(ele.attrib)
                #print(ele.text)
            elif ele.tag == 'connection' or ele.tag == 'ConnectionManager':
                print("Connection1")
                #print(ele.attrib)
                #print(ele.text)
            elif ele.tag == "{www.microsoft.com/SqlServer/Dts}Property":

                list_properties.append(ele.attrib)
                list_properties.append(ele.text)

                #print(ele.attrib)

                    #for child1 in child0:
                    #    print(child1)
                    #for child1 in child0:
                    #    print(child1.tag)
        mdFile.new_header(level=1, title="Paths")
        mdFile.new_paragraph("This is pths listed")
        summary = '\n'.join(list_path_info)
        mdFile.new_paragraph(summary)

    #print(list_properties)
    print(list_path_info)
    mdFile.create_md_file()
    #print(values)

if __name__ == "__main__":
    app()
