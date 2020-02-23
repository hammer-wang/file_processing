'''
This scripts convert all .ipynb files in a folder to PDFs.

Author: Haozhu Wang (hzwang@umich.edu)
Date: 2020-01-22

Dependency:
-- tqdm
-- jupyter nbconvert 5.6.0 (this should come with jupyter lab)

Example:
    python ipynb_to_pdf.py --source ~/Documents/EECS504_files/psets/pset1/submissions --target ~/Documents/EECS504_files/psets/pset1/pdfs
'''

import os
import argparse
import tqdm

if __name__=='__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--source', type=str, help='where to extrac the ipynbs', default=None)
    argparser.add_argument('--target', type=str, help='where to store the converted pdfs', default=None)
    argparser.add_argument('--smoke_test', action='store_true')
    args = argparser.parse_args()

    source = args.source
    target = args.target
    files = os.listdir(source)

    # filter ipynb files
    files = [item for item in files if '.ipynb' == item[-6:]]
    print('Total number of ipynb files {}'.format(len(files)))

    if not os.path.exists(target):
        os.mkdir(target)

    if args.smoke_test:
        files = files[:3]

    for file in tqdm.tqdm(files):
        cmd = 'jupyter nbconvert --to pdf {} --output-dir {}'.format(os.path.join(source, file), target)
        os.system(cmd)
        print(cmd, os.getcwd())