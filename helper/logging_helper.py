#  logging_helper.py
#  Created by Kiro Shin <mulgom@gmail.com> on 2024.

import logging

def logging_set_root(stream_level=logging.INFO, filename: str = None, file_level=logging.WARNING):
    _sfmt = '[%(asctime)s|%(levelname)s|%(module)s] %(message)s'
    _dfmt = '%y%m%d:%H%M%S'
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(fmt=_sfmt, datefmt=_dfmt)
    # 화면에만 출력
    console_handler = logging.StreamHandler()
    console_handler.setLevel(stream_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    # 파일까지 저장
    if filename is not None:
        file_handler = logging.FileHandler(filename=filename)
        file_handler.setLevel(file_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

