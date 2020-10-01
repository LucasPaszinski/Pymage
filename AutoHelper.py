import pyautogui as auto
import pAutoHelper as p_auto
from pAutoHelper import parallel_findall as findall
import codegenerator.ImageFrequencyOptimization as ImgFreqOptimize
import time
from Screenshot import screenshot

def GetWindowBox(name):
    '''
-----
Summary:
--------
    Given a windows name return windows box. 
    Can be used as region for image searches

------
Parameters:
----------
    name : str 
        Name of the windows to get box
------
Return:
------
    Box  : when window is found 
    None : no window with name is found
    '''
    try:
        w_box = auto.getWindowsWithTitle(name)[0].box
        return w_box
    except:
        return None


def finder(images, region=None):
    """
    Summary:
    -------
    Try to find images on screen, then return the first image found.
-------

Parameters:
--------
    images : tuple/array of string
        enumerable with the path of the images to be found on screen.
--------

Return:
------
    return the obj box containing information of the found image on screen

    """

    def SearchImage(img, region):
        find = auto.locateOnScreen(img, region=region, grayscale=True)
        if find is not None:
            ImgFreqOptimize.AddHitFor(img)
            print(f'*** The Image {img} was Found ***\t\t\t\t')
        return find

    isMultipleImages = isinstance(images, (list, tuple))
    if isMultipleImages:
        find = p_auto.parallel_finder(images, region, max_cores_threads=4)
        if find == [True, None]:
            for image in images:
                find = SearchImage(image, region)
                if find is not None:
                    break
    else:
        find = SearchImage(images, region)

    if find is not None:
        return find
    else:
        screenshot(name="ERROR on finding Images")
        print('None of {} were found'.format(', '.join(images)))
        raise Exception('None of {} were found'.format(', '.join(images)))


def AwaitImages(imagesToFind, timeoutSeconds=10, do_while_looping=None, region=None):
    '''
    Summary:
    -------
    Search for images until times outs (if time out happen on mid search cycle, will end cycle).
-------

Parameters:
--------
    images : tuple/array of string
        enumerable with the path of the images to be found on screen.
    timeoutSeconds: int (seconds)
        seconds until time out
    do_while_looping: lambda
        Execute this function in between search cycles.
    region : box
        region os the screen that the search will be made.
--------

Return:
------
    the path of the img that was found (is the img path not the position)
    '''
    time_now = time.time()
    timeout = time_now + timeoutSeconds
    imageFound = None

    while time_now < timeout:
        if do_while_looping is not None:
            do_while_looping()

        try:
            imageFound = finder(imagesToFind, region)
        except:
            pass

        if imageFound is not None:
            return imageFound

        time_now = time.time()

    print('*** ERROR: Time out {}s and {} were not found ***'
          .format(timeoutSeconds, ', '.join(imagesToFind)))


def GetImageVersionFoundOnScreen(images, region=None):
    '''
    Summary:
    -------
    Try to find the image on screen, the first matching is returned.
-------

Parameters:
--------
    images : tuple/array of string
        enumerable with the path of the images to be found on screen.
    region : box
        region os the screen that the search will be made.
--------

Return:
------
    the path of the img that was found (is the img path not the position)

    '''
    for img in images:
        find = auto.locateOnScreen(img, region=region, grayscale=True)
        if find is not None:
            return img
    raise Exception('None of the following images were found:\n {}'
                    .format(images))


    
if __name__ == "__main__":
    auto.sleep(3)
    from Images import Pymage
    var = finder(Pymage.ProductLibrary.SELECTEDBLUE())
    print(var)
