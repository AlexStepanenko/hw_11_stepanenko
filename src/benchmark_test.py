import os
from logger import Logger
from face_detector import FaceDetector
from serializer import Serializer

logger = Logger().setup_logger('test', '/Users/astepanenko/projects/ln/hw11/log/test.log')


def benchmark(iterations):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iterations):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            logger.info(f'[*] Execution time of {func.__name__} is: {total / iterations} sec.')
            return return_value

        return wrapper

    return actual_decorator


null_logger = Logger().setup_logger('null', os.devnull)
files_path = '/Users/astepanenko/projects/ln/hw11/data'


@benchmark(iterations=5)
def detect_images(detector):
    return detector.detect_all(files_path)


@benchmark(iterations=5)
def serialize_images(serializer, data):
    return serializer.serialize(data)


detect_images(FaceDetector(null_logger))

frames = FaceDetector(null_logger).detect_all(files_path)
serialize_images(Serializer(null_logger), frames)
