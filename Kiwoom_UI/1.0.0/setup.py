import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "ATH",
    version = "0.1",
    description = "Auto Trading System",
    author = "Zero Kim",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
# python setup.py bdist_msi
