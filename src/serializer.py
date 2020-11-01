import pickle


class Serializer:
    def __init__(self, log):
        self.log = log

    def serialize(self, frames):
        self.log.info('Serialization.')

        with open('./dump/faces.pickle', 'wb') as fl:
            pickle.dump(frames, fl)
