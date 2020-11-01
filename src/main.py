import logging
from path_reader import PathReader
from face_detector import FaceDetector
from serializer import Serializer

logging.basicConfig(level=logging.DEBUG, filename='./log/quadratic_equation_roots.log', filemode='w')


def run():
    logging.info('Program starts.')

    files_path = PathReader(logging).read()
    frames = FaceDetector(logging).detect_all(files_path)
    Serializer(logging).serialize(frames)

    logging.info('Program ends.')


if __name__ == '__main__':
    run()

