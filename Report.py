from mdutils import MdUtils
import os


def CreateReportMarkdown(name, path):
    """
    Summary:
    -------
    Create a unified Report of the execution of the code
-------
Parameters:
--------
    name : str
        file name (no need for ext) Ex:. 'Report'
    path : str
        path to project Ex:. 'C:\\Users\\joker\\Documents\\CreatedByPythonAutomation\\NX3003\\TestProject'
    """
    mdFile = MdUtils(file_name=f'{path}\\Report-{name}', title='Relatório do Python Auto Teste')

    files = []

    for r, d, f in os.walk(f'{path}\\reports'):
        for file in f:
            file_name = os.path.basename(file)
            file_name_splited = file_name.split('.')
            if file_name_splited[-1] == 'png':
                files.append((int(file_name_splited[0]), file_name_splited[1], file.replace('.\\', '')))

    files.sort()  # sort by order

    for file in files:
        img_title = file[1].replace('_', ' ')
        mdFile.new_header(level=1, title=f'{file[0]}. {img_title}')
        mdFile.write(f'![{img_title}](.\\reports\\{file[2]})\n')

    mdFile.create_md_file()

if __name__ == "__main__":
    CreateReportMarkdown('BIrhKF','.\\to_delete\\BIrhKF')
    CreateReportMarkdown('CXZPBk','.\\to_delete\\CXZPBk')
    CreateReportMarkdown('IqoANd','.\\to_delete\\IqoANd')
    CreateReportMarkdown('miRTsU','.\\to_delete\\miRTsU')
    CreateReportMarkdown('VUjsyr','.\\to_delete\\VUjsyr')