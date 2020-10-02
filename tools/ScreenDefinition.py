import pyautogui as auto
import pyscreeze


# This is a module to help search faster certains regions of the screen
# Each function has a draw of it  and the regions marked as X are the searched ones

def GetLowerHalf():
    '''
    -------------
    |.....|.....|
    -------------
    |..x..|..x..|
    -------------
    '''
    box = GetScreenBox()
    left = box.left
    top = box.top+box.height/2
    width = box.width
    height = box.height/2
    return pyscreeze.Box(left, top, width, height)


def GetLowerLowerHalf():
    '''
    -------------
    |.....|.....|
    -------------
    |.....|.....|
    -------------
    |.....|.....|
    -------------
    |..x..|..x..|
    -------------
    '''
    box = GetLowerHalf()
    left = box.left
    top = box.top+box.height/2
    width = box.width
    height = box.height/2
    return pyscreeze.Box(left, top, width, height)


def GetUpperHalf():
    '''
    -------------
    |..x..|..x..|
    -------------
    |.....|.....|
    -------------
    '''
    box = GetScreenBox()
    left = box.left
    top = box.top
    width = box.width
    height = box.height/2
    return pyscreeze.Box(left, top, width, height)


def GetLeftHalf():
    '''
    -------------
    |..x..|.....|
    -------------
    |..x..|.....|
    -------------
    '''
    box = GetScreenBox()
    left = box.left
    top = box.top
    width = box.width/2
    height = box.height
    return pyscreeze.Box(left, top, width, height)


def GetRightHalf():
    '''
    -------------
    |.....|..x..|
    -------------
    |.....|..x..|
    -------------
    '''
    box = GetScreenBox()
    left = box.left + box.width/2
    top = box.top
    width = box.width/2
    height = box.height
    return pyscreeze.Box(left, top, width, height)


def GetScreenBox():
    '''
    -------------
    |..x..|..x..|
    -------------
    |..x..|..x..|
    -------------
    '''
    screen = auto.size()
    return pyscreeze.Box(0, 0, screen.width, screen.height)


if __name__ == "__main__":
    a = GetLeftHalf()
    print(a)
