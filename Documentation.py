



class Documentation():


    def __init__(self, file_dir):
        self.dir = file_dir
        self.ssis_files = []


    def generate_summaries(self, list_info:list)->str:
        summaries = ""
        if len(list_info)== 1:
            sep = ""
        else:
            sep = "\n"
        for information in list_info :
            summaries=sep.join(information)
        
        return summaries
