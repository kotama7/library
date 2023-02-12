from PIL import Image, ImageTk

def get_tk_images(path_list:list,size_list:list) -> list:
    """
        This function return list of ImageTk.PhotoImage objects.
        Each member of ImageTk.PhotoImage is composed by image file which is indicated by each member of path_list and have size of each member of size_list.
        The attribute of path_list must be list of string which is path of image file.
        The attribute of size_list must be list of list likes (width, height).
        Additionally, all members of size_list must be list which have two int elements.
        The length of path_list and size_list must be same.
    """
    if(len(path_list) != len(size_list)):
        raise Exception("The length of path_list and size_list must be same.")
    image_ls = []
    for path, size in zip(path_list, size_list):
        if type(path) is not str:
            raise Exception("All members of path_list must be string")
        if len(size) != 2 or not (type(size[0]) is int and type(size[1]) is int):
            raise Exception("All members of size_list must be (width, height) and both of that is integer")
        try:
            img = Image.open(path)
        except FileNotFoundError:
            raise FileNotFoundError(f"FileNotFoundError:\nThere is no file having name : {path}")
        img = img.resize((size[0],size[1]))
        tk_img = ImageTk.PhotoImage(img)
        image_ls.append(tk_img)
    return image_ls
