import pytest
from Directory import Directory



class Test_Directory:


    def test_Directory(self):
        directory = Directory('/app/')
        assert directory.dir == '/app/'

    def test_Directory_data_type(self):
        directory = Directory('/app/')
        assert type(directory.dir) == str

    def test_Directory_not_data_type():
        directory = Directory(1)
        assert type(directory.dir) != str


    def test_dt_parse_directory_files(self):
        directory = Directory('/app/')
        list_dir_files = directory.parse_directory_files()
        assert type(list_dir_files) == list
        assert len(list_dir_files) > 0
        

    def test_parse_SSIS_Files(self):
        directory = Directory('/app/')
        list_dir_files = directory.parse_directory_files()
        list_ssis_files = directory.parse_files()
        assert len(directory.ssis_files) == 2

    def test_confirm_ssis(self):
        directory = Directory('/app/')
        file_name = 'hi.dtsx'
        assert directory.confirm_ssis(file_name) == True

