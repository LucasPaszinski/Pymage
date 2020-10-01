import re

'''
TODO:

If in future the list this module list on gets too big 
a refactor will be needed to change the .txt to one that guards only one path and a value with the number of hits
for that image. For the time being this will serve. And most of this code will be reused anyway.
'''


def AddHitFor(image):
    ''' Summary:
-------
    Add an entry for the file on the image frequency list. 
    The more an image is found inside a module the faster it will be called the next time (in PyMage Img ordering)
-------
Parameters:
--------
    image : str 
        String that contain the path of find image
        EX: "Img.Devices.NX5001"
--------'''
    if not (str.isspace(image) or image == None):
        image_freq_list = open('codegenerator\image_frequency_list.txt', "a")
        image_freq_list.write(image+"\n")
        image_freq_list.close()


def orderByFrequency(need_ordering):
    '''Summary:
-------
    This is called only by pymage.
    When writing the python code of pymage codegenerator will call this.
    Given an array of pymage entries that go inside a pymage method, 
    this method will try to order by the most find image to the least find image
-------
Parameters:
--------
    need-ordering: list
        list of variables that will be added to pymage to be order by most find to least find
--------
Return:
------
    The result of the search if everithing goes well.
    Might throw an exception of regex failed, must be inside a try/except
------'''
    imgs_to_order_path = {}

    try:
        for var_path in need_ordering:
            path = _searchForStringValueInModule(var_path)
            number_of_hits = _findNumberOfHits(path)
            imgs_to_order_path[var_path] = number_of_hits
        
        ordered = _MostToLeastFoundImage(imgs_to_order_path)
        return ordered


    except:
        return need_ordering


def _searchForStringValueInModule(variable, module_path="Images.py"):
    '''Summary:
-------
    Search for variable inside the module. But both as strings.
    This is for meta-programming only
-------
Parameters:
--------
    variable : str 
        String that contain how the variable is address outside the module
        EX: "Img.Devices.NX5001"
    module-path : str 
        The path to the module the variable is on
        EX: "Images.py" (is already the default path anyway)
--------
Return:
------
    The number of hits of the path find in the file
------'''
    # load text on images py
    images_py = open(module_path, "r")
    all_text_images = images_py.read()
    images_py.close()

    # generate regex for search
    regex = ""

    # Ex: "Img.Devices.NX5001" -> ["Img", "Device", "NX5100"]
    regex = ".*{}".format(variable.split(".")[-1])

    regex += "='(?P<result>.*)'"

    search = re.findall(regex, all_text_images, re.MULTILINE)

    return search[0]


def _findNumberOfHits(of_this_path, on_this_file='codegenerator\image_frequency_list.txt'):
    '''Summary:
-------
    Search for path inside the image frequency file. 
    This is for meta-programming only
-------
Parameters:
--------
    of-this-path : str 
        string containing a path
    on-this-file : str 
        The path to the file that the path will be searched
--------
Return:
------
    The result of the search if everithing goes well.
    Might throw an exception of regex failed, must be inside a try/except
------'''
    # load all text of file images frequency
    image_freq_list = open(on_this_file, "r")
    all_text_freq = image_freq_list.read()
    image_freq_list.close()

    # create regex for path (using this method to avoid caution for errors of special escape sequences)
    path_regex = str(of_this_path).replace("\\\\", ".*")
    number_of_hits = re.findall(
        path_regex,
        all_text_freq,
        re.MULTILINE
    ).__len__()

    return number_of_hits

def _MostToLeastFoundImage(var__number_of_hits):
    '''Summary:
-------
    Order the dict by higher to lower value. than return a list of the keys in that order
-------
'''
    if not any(i > 0 for i in list(var__number_of_hits.values())):
        return list(var__number_of_hits.keys())
    
    reversed_ordered_dict = {k: v for k, v in sorted(var__number_of_hits.items(), key=lambda item: item[1])}
    reverse_ordered_list = list(reversed_ordered_dict.keys())
    reverse_ordered_list.reverse()
    return reverse_ordered_list


    