from better_profanity import profanity
import numpy as np

def cleanData(dataset):
    for i in range(len(dataset)):
        if profanity.contains_profanity(dataset[i][1]):
            np.delete(dataset, i, axis=0)
            print("profanity found")
    return dataset
