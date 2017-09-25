class MetaData:
    def __init__(self):
        self.trainingInstances = 0
        self.trainingAttributes = 0
        self.nodes = 0
        self.leafNodes = 0
        self.trainingAccuracy = 0
        self.validationInstances = 0
        self.validationAttributes = 0
        self.validationAccuracy = 0
        self.testInstances = 0
        self.testAttributes = 0
        self.testAccuracy = 0

    def setTrainingInstances(self, value):
        self.trainingInstances = value
        return 

    def setTrainingAttributes(self, value):
        self.trainingAttributes = value
        return

    def setValidationInstances(self, value):
        self.validationInstances = value
        return 

    def setValidationAttributes(self, value):
        self.validationAttributes = value
        return

    def setTestInstances(self, value):
        self.testInstances = value
        return 

    def setTestAttributes(self, value):
        self.testAttributes = value
        return

    def addNode(self):
        self.nodes += 1
        return

    def addLeafNode(self):
        self.leafNodes += 1
        return

    def printMetaData(self):
        print("Number of training instances = " + str(self.trainingInstances))
        print("Number of training attributes = " + str(self.trainingAttributes))
        print("Total number of nodes in the tree = " + str(self.nodes))
        print("Number of leaf nodes in the tree = " + str(self.leafNodes))
        print("Accuracy of the model on the training dataset = " + str(self.trainingAccuracy))
        print("Number of validation instances = " + str(self.validationInstances))
        print("Number of validation attributes = " + str(self.validationAttributes))
        print("Accuracy of the model on the validation dataset after pruning = " + str(self.validationAccuracy))
        print("Number of testing instances = " + str(self.testInstances))
        print("Number of training attributes = " + str(self.testAttributes))
        print("Accuracy of the model on the training dataset = " + str(self.testAccuracy))
        return