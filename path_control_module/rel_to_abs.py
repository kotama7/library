import os
import sys
import warnings

def rel_to_abs(path:str|list) -> str|list:
    """
        This function make reletive path which reletive to calling file's parent directory to absolute path.
        If attribute is given as a string object or list object, this function return same type object as given.
        Otherwise, attribute is given as a any other type object, this function raise error.
        If there isn't path which is given, this function raise Warning but don't raise error.
    """

    def get_abspath(path):
        basedir = os.path.dirname(sys.argv[0])
        abs_path = os.path.join(basedir,path)
        if not os.path.exists(abs_path):
            warnings.warn(f"Warning:there isn't path such as {abs_path}",Warning)
        return abs_path

    if type(path) is str:
        abs_path = get_abspath(path)
        return abs_path
    elif type(path) is list:
        path_ls = []
        for ele in path:
            if type(ele) is not str:
                raise Exception(f"the all member of list must be string, but {type(ele)} is included")
            abs_path = get_abspath(ele)
            path_ls.append(abs_path)
        return path_ls
    else:
        raise Exception("attribute must be string or list of string.")
