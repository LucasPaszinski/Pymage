import pyautogui as auto 
import AutoHelper as helper
import pyscreeze
from Images import Img, Pymage


def WaitImageThenClick(imgs):
    '''
    Receive a list of images and wait until it find it, then click it, and wait 5 seconds
    '''
    found = None

    while found == None:
        try:
            found = helper.finder(imgs)
            pass
        except:
            pass

    auto.click(found)
    auto.sleep(5)


if __name__ == "__main__":
    download_imgs = Pymage.LeLivros.DOWNLOAD()

    WaitImageThenClick(download_imgs)

    not_a_robot_imgs = Pymage.LeLivros.NOTROBOT()

    WaitImageThenClick(not_a_robot_imgs)

    continue_imgs = Pymage.LeLivros.CONTINUE()

    WaitImageThenClick(continue_imgs)

    save_imgs = Pymage.LeLivros.SAVE()

    WaitImageThenClick(save_imgs)

    print("🎉🎉🎉 Finished must be downloading right now!!! 🎉🎉🎉")


