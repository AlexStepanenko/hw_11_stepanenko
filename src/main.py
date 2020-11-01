from logger import Logger
from path_reader import PathReader
from face_detector import FaceDetector
from serializer import Serializer


def run():
    logger = Logger().setup_logger('main', '/Users/astepanenko/projects/ln/hw11/log/main.log')
    logger.info('Program starts.')

    files_path = PathReader(logger).read()
    frames = FaceDetector(logger).detect_all(files_path)
    Serializer(logger).serialize(frames)

    logger.info('Program ends.')


if __name__ == '__main__':
    run()

