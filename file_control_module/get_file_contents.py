import os
import re

def get_file_contents(dir_path:str,include_sub=False,exception=[],reg_ex=False) -> dict:
    """
        This fuction return dictionary which have each file name as a key and content as a value encoded utf-8.
        value is only string. So, this function can't read file as any other form.
        key names don't include extensions.
        if "all" option is True, returned dictionary include all files in sub directories.
        "exception" attribute must list which all members is string. this specify the files you don't want to read.
        if "reg_ex" option is True, the all members of "exception" list is interpreted as regular expression.
        if there is file which have same name, this function raise error.
    """
    def search_sub(dir_path:str,path_ls:list):
        for path in os.listdir(dir_path):
            joined_path = os.path.join(dir_path,path)
            if os.path.isfile(joined_path):
                path_ls.append(joined_path)
            elif os.path.isdir(joined_path):
                search_sub(joined_path,path_ls)
    if not type(dir_path) is str:
        raise Exception(f"dir_path must be str class, but {str(type(dir_path))} class is given")
    if not type(exception) is list:
        raise Exception(f"exception must be list class, but {str(type(exception))} class is given")    
    if include_sub:
        folder_path = []
        search_sub(dir_path,folder_path)
    else:
        folder_path = [os.path.join(dir_path,path) for path in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path,path))]
    file_dict = {}
    for path in folder_path:
        with open(path,"r",encoding="utf-8") as f:
            name = "".join(os.path.basename(path).split(".")[:-1])
            if not name:
                name = os.path.basename(path)
            if name in file_dict:
                raise Exception("overlapping error: There are files which have same name")
            elif name in exception or (reg_ex and re.match(exception,name)):
                continue
            file_dict[name] = f.read().strip()
    return file_dict