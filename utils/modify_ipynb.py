import nbformat
import os
import glob

'''
This script modifies the first cell of the notebook.
'''

# change this folder path to your path
folder = '/Users/wanghaozhu/Documents/EECS504_files/psets/pset9/submissions_renamed'
for file in glob.glob(folder+'/*.ipynb'):
    print(file)
    with open(os.path.join(folder, file)) as f:

        try:
            nb = nbformat.read(f, nbformat.NO_CONVERT)
        except:
            print('File cannot be opened! {}'.format())
        filename = file.split('/')[-1]

        # modify title
        name, umid = filename.split('_')[0], filename.split('_')[1].rstrip('.ipynb')

        try:
            fullname = nb['cells'][0]['source'].split('\n\n')[2].split(',')[0]
        except:
            fullname = name

        # for i, cell in enumerate(nb['cells']):
        #     if 'outputs' in cell and len(cell['outputs']) > 20:
        #         nb['cells'][i]['outputs'] = nb['cells'][i]['outputs'][-2:]

        nb['cells'][0]['source'] = '# UNIQUENAME and UMID  \n ## Fullname: {}  \n ## Unique Name: {}  \n ## UMID: {}'.format(fullname, name, umid)

        # remove goolge dirve links
        for c in nb['cells']:
            if 'https' in c['source']:
                c['source'] = ' '
        nbformat.write(nb, os.path.join(folder, file))