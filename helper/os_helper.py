#  os_helper.py
#  Created by Kiro Shin <mulgom@gmail.com> on 2024.

import os


def os_open_finder(path: str):
    """윈/맥에서 특정 경로 파인더를 연다(리눅스X)"""
    if os.name == "nt":
        os.startfile(path)
    else:
        os.system(f"""open -R '{path}'""")

