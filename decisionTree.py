from math import log
import numpy as np


def main():

    # TODO: Instansiate the data set and the labels
    labels = ['Person', 'HairLength', 'Weight', 'Age']
    dataSet = np.loadtxt("./data_sets1/my_data.csv", delimiter=',', dtype='string', skiprows=1)

    return dataSet


def calculate_entropy():
    # TODO: Fetch the total number of instances
    total_instances = len(dataSet)

    # TODO: Create an empty dictionary to get the number of instances in each class
    count_splitter = {}

    # TODO: Parse through the list and identify the Class of each instance
    for each_instance in dataSet:
        if each_instance[-1] in count_splitter.keys():
            count_splitter[each_instance[-1]] += 1
        else:
            count_splitter[each_instance[-1]] = 1

    # TODO: Calculate entropy using the formula
    entropy = 0.0
    for each_class in count_splitter.keys():
        num_of_instances = count_splitter[each_class]
        fraction_value = float (num_of_instances)/total_instances
        entropy -= fraction_value * log(fraction_value, 2)

    return entropy


def build_tree():
    pass


if __name__ == '__main__':

    dataSet = main()
    calculate_entropy()