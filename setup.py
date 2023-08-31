from cx_Freeze import setup, Executable

executables = [Executable('main.py', base='Win32GUI',icon='images\\icon.ico')]

setup(
    name='Cryptographic-Coding-Toolbox',
    version='1.0.0',
    description='You can choose a common cryptographic encoding to convert to each other.',
    executables=executables
)
