import pickle

with open('../dump/faces.pickle', 'rb') as fl:
    data_new = pickle.load(fl)

print(data_new)
