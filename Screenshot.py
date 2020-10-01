import pyautogui as auto
import os

_path = ''

def screenshot(path='', name='', specificWindow="MasterTool IEC XE"):
    '''
        Summary:
        ---------
        Create a screen shot on the screen.
        The first time using it you need to pass a path to it.

        It will create a report folder inside that path and put the images there.

        Parameters:
        -----------
        path: the path where the images need to be saved
        
        name: the name of the image, preferable test related
        
        specificWindow: the name of the window you want to screenshot. 
        In case of not foundind the specific name a full screenshot will be made
    '''
    _set_path(path)
    
    if _path == '': # path can't be undefined
        return

    if path == '': 
        path = _path

    try:
        window = auto.getWindowsWithTitle(specificWindow)
        if not window:
            im1 = auto.screenshot()
        else:
            im1 = auto.screenshot(region=(window[0].left, window[0].top, window[0].width, window[0].height))

        if not os.path.exists(path):
            print("Creating folder")
            os.makedirs(path)

        num = _lastImage(path)

        print(f"Saving image {num} - {name}")
        if name == '':
            pathToSave = f'{path}\\{num}.png'
        else:
            pathToSave = f'{path}\\{num}.{name}.png'
        im1.save(pathToSave, 'PNG')
    except:
        print("Error creating folder or file")
        pass


def _set_path(path):
    global _path
    if path != '':
        _path = path + '\\reports'

def _lastImage(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.png' in file:
                file = file.split('.')[0]
                if file.isnumeric():
                    try:
                        files.append(int(os.path.join(file).split('.')[0]))
                    except:
                        pass
                else:
                    pass
    try:
        if files == []:
            return 1
        files.sort()
        return files.pop() + 1
    except:
        print("error")
        pass
