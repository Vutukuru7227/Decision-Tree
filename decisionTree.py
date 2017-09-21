from math import log
import csv
import operator


def get_data_set_and_feature_labels():
    '''
    dataSet = [[0, 1, 1, 'yes'],
               [0, 1, 0, 'no'],
               [1, 0, 1, 'no'],
               [1, 1, 1, 'no'],
               [0, 1, 0, 'no'],
               [0, 0, 1, 'no'],
               [1, 0, 1, 'no'],
               [1, 1, 0, 'no']]
    labels = ['cartoon', 'winter', 'more than 1 person']
    # change to discrete values
    return dataSet, labels
    :return:
    '''
    # TODO: Instantiate the data set and the labels
    feature_labels = ['XB', 'XC', 'XD', 'XE', 'XF', 'XG', 'XH', 'XI', 'XJ', 'XK', 'XL', 'XM', 'XN', 'XO', 'XP', 'XQ', 'XR', 'XS', 'XT', 'XU']

    #feature_labels = ['Hair Length', 'Weight', 'Age']
    with open('./data_sets1/training_set.csv', 'rt') as csv_file:
        next(csv_file)
        reader = csv.reader(csv_file)
        data_set = list(reader)

    return data_set, feature_labels


def calculate_entropy(data_set):
    # TODO: Fetch the total number of instances
    total_instances = len(data_set)

    # TODO: Create an empty dictionary to get the number of instances in each class
    count_splitter = {}

    # TODO: Parse through the list and identify the Class of each instance
    for each_instance in data_set:
        if each_instance[-1] not in count_splitter.keys():
            count_splitter[each_instance[-1]] = 0
        count_splitter[each_instance[-1]] += 1
    #print count_splitter
    # TODO: Calculate entropy using the formula
    entropy = 0.0
    for each_class in count_splitter:
        entropy -= float(count_splitter[each_class])/total_instances * log(float(count_splitter[each_class])/total_instances, 2)

    return entropy


def check_for_entropy(label_list):

    # TODO: Stop building the tree id entropy is 0
    if label_list.count(label_list[0]) == len(label_list):
        return True
    return False


# TODO: NEED to be Completed
def if_any_features():
    # TODO: Stop building the tree if there are no more feature values(attributes left)
    if len(data_set) == 1:
        pass
    else:
        return False


def divide_data_set(data_set, attribute_value, set_value):
    divided_data_set = []
    for attribute_vector in data_set:
        if attribute_vector[attribute_value] == set_value:
            reduced_attribute_list = attribute_vector[:attribute_value]
            reduced_attribute_list.extend(attribute_vector[attribute_value+1:])
            divided_data_set.append(reduced_attribute_list)

    return divided_data_set


def check_best_attribute_to_split(data_set):

    no_of_remaining_attributes = len(data_set[0])-1
    entropy_of_parent = calculate_entropy(data_set)

    highest_information_gain = 0.0
    best_feature = -1

    for i in range(no_of_remaining_attributes):
        attr = [value[i] for value in data_set]
        unique_attribute_value = set(attr)
        split_entropy = 0.0
        for value in unique_attribute_value:
            split_data_set = divide_data_set(data_set, i, value)
            probability = len(split_data_set) / float(len(data_set))
            split_entropy += probability * calculate_entropy(split_data_set)

        information_gain = entropy_of_parent - split_entropy

        if information_gain > highest_information_gain:
            highest_information_gain = information_gain
            best_feature = i

    return best_feature


def build_tree(data_set, feature_labels):

    label_list = [each_instance[-1] for each_instance in data_set]
    if label_list.count(label_list[0]) == len(label_list):
        return label_list[0]

    # TODO: NEED to check for the number of feature values remaining =================NEEDS ATTENTION
    if len(data_set[0]) == 0:
        pass

    # TODO: Check for the best attribute to split on
    best_attribute = check_best_attribute_to_split(data_set)
    best_feature = feature_labels[best_attribute]

    decision_tree = {best_feature: {}}
    del feature_labels[best_attribute]

    feature = [each_feature[best_attribute] for each_feature in data_set]

    unique_values = set(feature)
    for value in unique_values:
        remaining_labels = feature_labels[:]
        decision_tree[best_feature][value] = build_tree(divide_data_set(data_set, best_attribute, value), remaining_labels)

    return decision_tree

if __name__ == '__main__':

    # TODO: Function call to fetch the data and feature labels
    data_set, feature_labels = get_data_set_and_feature_labels()

    # TODO: Function call to build the Tree
    tree = build_tree(data_set, feature_labels)
    print("Started")
    print(tree)
    print("Finished")