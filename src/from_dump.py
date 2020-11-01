import pickle

with open('/Users/astepanenko/projects/ln/hw11/dump/faces.pickle', 'rb') as fl:
    data_new = pickle.load(fl)

print(data_new)
