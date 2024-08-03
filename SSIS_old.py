

import os
from lxml import etree

#Output Results directory
#assign Direcotry to Output Results
sql_out = r"C:\temp\dtsxsql"
#if output directory does not exist
if not os.path.isdir(sql_out):
#create output directory at the assigned location
    os.makedirs(sql_out)


#input SSIS Package
#assign the SSIS Package to Parse
ssis_dtsx = r'C:\temp\dtsx\ParseXML.dtsx'
#if package is not in this assigned location
if not os.path.isfile(ssis_dtsx):
#print no SSIS Package in the directory
    print("no package file")



# read and parse ssis package
tree = etree.parse(ssis_dtsx)

root = tree.getroot()
root.tag 


pfx = '{www.microsoft.com/'
exe_tag = pfx + 'SqlServer/Dts}Executable'
obj_tag = pfx + 'SqlServer/Dts}ObjectName'
dat_tag = pfx + 'SqlServer/Dts}ObjectData'
tsk_tag = pfx + 'sqlserver/dts/tasks/sqltask}SqlTaskData'
src_tag = pfx + \
  'sqlserver/dts/tasks/sqltask}SqlStatementSource'
print(exe_tag)
print(obj_tag)
print(tsk_tag)
print(src_tag)




# extract sql source statements and write to *.sql files 
total_bytes = 0
package_name = root.attrib[obj_tag].replace(" ","")
for cnt, ele in enumerate(root.xpath(".//*")):
    if ele.tag == exe_tag:
        attr = ele.attrib
        for child0 in ele:
            if child0.tag == dat_tag:
                for child1 in child0:
                    sql_comment = attr[obj_tag].strip()
                    if child1.tag == tsk_tag:
                        dtsx_sql = child1.attrib[src_tag]
                        dtsx_sql = "-- " + \
                            sql_comment + "\n" + dtsx_sql
                        sql_file = sql_out + "\\" \
                             + package_name + str(cnt) + ".sql"
                        total_bytes += len(dtsx_sql)
                        print((len(dtsx_sql), 
                             sql_comment, sql_file))
                        with open(sql_file, "w") as file:
                              file.write(dtsx_sql)
print(('total bytes',total_bytes))