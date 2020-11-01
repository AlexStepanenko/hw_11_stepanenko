import pickle
import os
from logger import Logger
from face_detector import FaceDetector

logger = Logger().setup_logger('test', '/Users/astepanenko/projects/ln/hw11/log/test.log')


def faces_count(expected_count):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            frames = func(*args, **kwargs)
            count = 0



            for _image, faces in frames.items():
                for _face in faces:
                    count += 1

            logger.info(f'[*] Expected count {expected_count}, real count {count}')
            return count

        return wrapper

    return actual_decorator


null_logger = Logger().setup_logger('null', os.devnull)


@faces_count(4)
def image_detection():
    return FaceDetector(null_logger).detect_all('/Users/astepanenko/projects/ln/hw11/data')


image_detection()

