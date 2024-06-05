import sys

if sys.version_info < (3, 5):
    raise RuntimeError("最低支持 Python3.7 版本，请升级！")

from .WebBot import WebBotMain
from .WindowsBot import WinBotMain
from .AndroidBot import AndroidBotMain


__all__ = ["WebBotMain", "WinBotMain","AndroidBotMain"]
