


class Summary():

    def __init__(self, list_variables):
        self.list_values = list_variables
        self.combined_summary = ''
        
    def create_summary(self):
        if len(self.list_values)==1:
            sep = ""
        else:
            sep = '\n'
        for values in self.list_values:
            summary=sep.join(values)
        self.combined_summary = summary

    def return_summary(self)->str:

        return self.combined_summary
