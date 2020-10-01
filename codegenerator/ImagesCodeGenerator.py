import os
from codegenerator.ImageFrequencyOptimization import orderByFrequency

def Run():
    '''
    This code generate the Images.py code, it goes through the folder images
    and the first level of subfolders generating the path of each image and binding
    it to a variable named like the image.

    So this code generate the class Img and Pymage, be careful when changind this code to 
    not alter the behaviour or how the images will be access.

    Below you can see the examples of how thing should be

     Ex: 

     gvl/gvlbutton_2.png ->  GVLBUTTON_2 = "./gvl/gvlbutton_2.png"

    also for each folder it's created a class. So another example

    The image on the folder ./pou/pouicon_1.png will generate

        class Pou:
            POUICON_1 = "./pou/pouicon_1.png" 

    and can be access like :

        from Images import Img

        Img.Pou.POUICON_1


    This will also generate the pymage the more modern aprouch that uses the code of the older aprouch to improve development

    so if we have a folder  like ./PID/ and multiple images on it like
    pidicon.png, pidicon_2.png, pidicon_3.png, pidbutton_1.png and pidbutton_2.png

    will generate the Pymage with

        class Pymage:
            class PID:
                def PIDICON():
                    return [Img.PID.PIDICON, Img.PID.PIDICON_2, Img.PID.PIDICON_3]

                def PIDBUTTON():
                    return [Img.PID.PIDBUTTON, Img.PID.PIDBUTTON_2, Img.PID.PIDBUTTON_3]
    and can be acess like:

        from Images import Pymage

        Pymage.PID.PIDICON()
        
    '''
    img_file = open('.\Images.py', 'w')
    img_file.write('if __name__ == "__main__":\n')
    img_file.write('    import codegenerator.ImagesCodeGenerator as Gen\n')
    img_file.write('    Gen.Run()\n\n')
    img_file.write('class Img:\n')
    
    adder = []

    for r, d, f in os.walk('.\\'):
        if(str(r).__contains__('.\\images')):
            if(r == '.\\images'):
                for file in f:
                    dir_name = os.path.basename(r)
                    path_to = dir_name +"\\\\"+ str(file) #can't use os.path.join because files with n become special cases
                    filename = os.path.splitext(str(file))[0]
                    img_file.write('    {}'.format(filename.upper())+'='+'\'{}\' \n'.format(path_to))
                    adder.append(('',filename.split('_')[0].upper(),f'Img.{filename.upper()}'))                    
            else:
                class_name = str(r).replace('.\\images\\', '')
                img_file.write(f'    class {class_name}:\n')
                for file in f:
                    dir_name = os.path.basename(r)
                    path_to = 'images'+"\\\\"+dir_name +"\\\\"+ str(file)
                    filename = os.path.splitext(file)[0]
                    img_file.write('        {}'.format(filename.upper())+'='+'\'{}\' \n'.format(path_to))
                    adder.append((class_name,filename.split('_')[0].upper(),f'Img.{class_name}.{filename.upper()}'))
    
    img_file.write('class Pymage:\n')
    intern_classes = []
    for add in adder:
        i_class = add[0]
        if not intern_classes.__contains__(i_class):
            intern_classes.append(i_class)

    for icls in intern_classes:
        of_class = list(filter(lambda x: icls==x[0], adder))
        if icls != '':
            img_file.write(f'\tclass {icls}:\n')
        methods = []
        for mtds in of_class:
            mtd = mtds[1]
            if not methods.__contains__(mtd):
                methods.append(mtd)
        for m in methods: 
            of_method = list(filter(lambda x: m==x[1], of_class))
            if icls != '':
                img_file.write(f'\t\tdef {m}():\n')
                of_img = list(map(lambda x: x[2], of_method))
                sort_by_hits = orderByFrequency(of_img)
                list_imgs = ', '.join(sort_by_hits)
                img_file.write(f'\t\t\treturn [{list_imgs}]\n\n')
            else:
                img_file.write(f'\tdef {m}():\n')
                of_img = list(map(lambda x: x[2], of_method))
                list_imgs = ', '.join(of_img)
                img_file.write(f'\t\treturn [{list_imgs}]\n\n')
                pass
                


            pass

    img_file.close()
    with open("Images.py", 'r') as r_file:
        fixed_text = r_file.read().replace(chr(0), '')
    with open("Images.py", "w") as w_file:
        w_file.write(fixed_text)