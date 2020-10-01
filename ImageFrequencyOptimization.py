def AddHitFor(image):
    '''Write on a image frequency file onde a image is found'''
    if not (str.isspace(image) or image == None):
        image_freq_list = open('codegenerator/image_frequency_list.txt',"a")
        image_freq_list.write(image+"\n")
        image_freq_list.close()
