#  webbrowser_helper.py
#  Created by Kiro Shin <mulgom@gmail.com> on 2023.

import sys
import webbrowser


def webbrowser_open_new_tab(url: str):
    """윈/맥에서 브라우저에서 특정 주소를 새 탭으로 연다"""
    if sys.platform == 'win32':
        webbrowser.get('windows-default').open_new_tab(url)
    elif sys.platform == 'darwin':
        webbrowser.get('safari').open_new_tab(url)


