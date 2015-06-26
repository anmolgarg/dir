'''
Creates a folder directory consisting of a root folder named [date]_[project] 
(date optional), by copying a template folder. Also writes a README.md file.
Run this by typing '$python mkdir.py'.
'''

import os
import shutil
import datetime as dt


def make_project_dir(name, date = True, template = './template', root = './'):

    # create folder name w/optional date
    name = name.strip()
    datestr = dt.datetime.now().strftime('%m%d%y')

    if not date:
        folder_name = name.replace(' ', '_')
        ipy_name = datestr + '_' + name.replace(' ', '_')
    else:
        folder_name = ipy_name = datestr + '_' + name.replace(' ', '_')

    # if given a template full of scripts, dirs, requirements, etc., copy it over
    shutil.copytree(template, root + folder_name)
    
    # if providing a template with a nb located at ipynbs/eda.ipynb, renames to date + folder name
    try:
        os.rename(root + folder_name + "/ipynbs/eda.ipynb",
                  root + folder_name + "/ipynbs/" + ipy_name + ".ipynb")
    except: 
        pass

    # write README
    readthis = name.upper()+'\n\ncreated by: ' + os.getlogin() + '\ncreated at: ' + str(dt.datetime.now())
    readme = os.open(root + folder_name + "/README.md", os.O_RDWR | os.O_CREAT)
    os.write(readme, readthis)
    os.close(readme)
    print 'created', folder_name


def ask_master():

    #ask for user input on project details
    name = raw_input("Please enter name of project: ")
    date = raw_input("Do you want to date stamp the folder name?: ")

    if date.lower()[0] == 'y':
        date = True    
    else: 
        date = False
    return name, date


if __name__ == "__main__":

    name, date = ask_master()
    make_project_dir(name, date)

