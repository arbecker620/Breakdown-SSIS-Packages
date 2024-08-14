


class Package():

    def __init__(self,package_name,file_loc):
        self.package_name = package_name
        self.file_loc = file_loc

    def __str__(self):
        return f"{self.file_loc + self.package_name}"

    def package_info(self):

        return {'package name': self.package_name, "File Location": self.file_loc, "Path":self.file_loc+self.package_name} 
    
    def package_combined(self):
        dict_info = {'package name': self.package_name, "File Location": self.file_loc, "Path":self.file_loc+self.package_name} 
        summary = ''
        for k,v in dict_info.items():
                    line = str(k)+" : "+str(v)
                    path_summary.append(line)
        
        return "".join(path_summary)




class Package_MetaData(Package):
    def __init__(self, name,file_loc):
        super().__init__(name, file_loc)
        self.file_size = ''
        self.creation_date = ''



class Package_Exectution(Package):
    def __init__(self, name,file_loc):
        super().__init__(name, file_loc)
        self.list_properties = []
        self.list_path_info = []
        self.list_connection_strings = []
        self.list_sql_statements = []
        self.list_connection_info =[]
        self.list_output_columns = []
        self.list_input_columns = []

    
