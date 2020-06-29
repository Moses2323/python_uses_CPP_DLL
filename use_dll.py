# -*- coding: utf-8 -*-

import ctypes
import os
import math
import numpy as np
import numpy.ctypeslib as ctl
import matplotlib.pyplot as plt
import sys

class EvalLib:
    def __init__(self):
        self._libname = 'simple_dll.dll'

        thispath = os.path.dirname(os.path.abspath(__file__))

        if ctypes.sizeof(ctypes.c_voidp) == 4:
            raise RuntimeError(f"The {self._libname} library can only be used "
                               f"with 64-bit python.")

        dllpath = f"/{self._libname}"

        abs_dllpath = os.path.abspath(thispath + dllpath)

        currentDir = os.getcwd()
        os.chdir(os.path.dirname(abs_dllpath))
        evallib = ctypes.CDLL(abs_dllpath)
        os.chdir(currentDir)

        self.lib_path = abs_dllpath
        self.lib = evallib

        # add function to the lib
        self._printSmth = evallib.printSmth


    def Close(self):
        if self.lib is not None:
            # Free DLL so we can overwrite the file when we recompile
            ctypes.windll.kernel32.FreeLibrary.argtypes \
                = [ctypes.wintypes.HMODULE]
            ctypes.windll.kernel32.FreeLibrary(self.lib._handle)
            self.lib = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.Close()

    def printSmth(self):
        self._printSmth()


if __name__ == '__main__':
    with EvalLib() as elib:
        elib.printSmth()
        print( 'DONE!' )