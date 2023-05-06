import os

def get_file_path(filename, extension):
    cwd = os.getcwd()
    filepath = os.path.join(cwd, f"{filename}.{extension}")
    return filepath