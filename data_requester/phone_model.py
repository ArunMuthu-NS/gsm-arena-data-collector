from utils import get_file_name


class Phone:
    def __init__(self, brand, data_path):
        self.brand = brand
        self.data_path = data_path

    def base_path(self):
        return f'{self.data_path}/{self.brand}'

    def processed_data_path(self):
        return f'{self.data_path}/{self.brand}/phones.txt'

    def current_file_path(self):
        return f'{self.data_path}/{self.brand}/{get_file_name(self.base_path())}.csv'
