import os
import csv
import random, string
import numpy as np

class CsvHanlder:

    def __init__(self):

        self.target_folderpath = "./ilovecoffee"
        if not os.path.exists(self.target_folderpath):
            os.mkdir(self.target_folderpath)

    def random_id(self, max_length):

        isSuccess = False
        result_id = ""
        while not isSuccess:
            result_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(max_length))
            if result_id[0].isdigit() == False:
                isSuccess = True

        return result_id

    def random_name(self, customer_id):

        namelist = ['Tom', 'Jack', 'Kitty', 'Kevin', 'Joe', 'Poe', 'Fred', 'Hank', 'Peter', 'Cho']
        return random.choice(namelist) + '.' +  customer_id

    def random_mobile(self):

        phone_number = ''.join(random.choice(string.digits) for _ in range(8))
        return '+8869'+ phone_number

    def random_frequency(self):

        random_num = [i for i in range(21)]
        return random.choice(random_num)

    def create_csv(self):

        csvfile_name = 'customers.csv'
        csvfile_path = os.path.join(self.target_folderpath, csvfile_name)

        with open(csvfile_path, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['customer_id', 'customer_name', 'customer_mobile', 'frequency'])

            id_maxlength = 8

            for i in range(500):
                customer_id = self.random_id(id_maxlength)
                customer_name = self.random_name(customer_id)
                customer_mobile = self.random_mobile()
                frequency = self.random_frequency()

                writer.writerow([customer_id, customer_name, customer_mobile, frequency])

    def caculate_csv(self):

        csvfile_name = 'customers.csv'
        csvfile_path = os.path.join(self.target_folderpath, csvfile_name)

        with open(csvfile_path, mode='r') as f:

            rows = csv.DictReader(f)
            frequency_list = [int(row['frequency']) for row in rows]

            np_frequency = np.array(frequency_list)
            Mean_val = np.around( np.mean(np_frequency), 5)
            Median_val = np.median(np_frequency)

            _count = np.bincount(np_frequency)
            Mode_val = np.argmax(_count)

            print("Median:{}, Mean:{}, Mode:{}".format(Median_val, Mean_val, Mode_val))

csvhanlder = CsvHanlder()
csvhanlder.create_csv()
csvhanlder.caculate_csv()

