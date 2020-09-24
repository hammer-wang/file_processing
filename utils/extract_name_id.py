"""
This script renamed the .ipynb files with the format [uniquename]_[umid].ipynb and put them in to a new dir.

Author: Haozhu Wang (hzwang@umich.edu)
Date: 2020-02-21

Dependency:
-- tqdm
-- jupyter nbconvert 5.6.0 (this should come with jupyter lab)

Example:
    python extract_name_id.py --source ~/Documents/EECS504_files/psets/pset1/submissions --target ~/Documents/EECS504_files/psets/pset1/submissions_renamed
    python extract_name_id.py --source ~/Documents/EECS504_files/psets/pset5/submissions --target ~/Documents/EECS504_files/psets/pset5/submissions_renamed
    python extract_name_id.py --source ~/Documents/EECS504_files/psets/pset6/submissions --target ~/Documents/EECS504_files/psets/pset6/submissions_renamed
"""

# python extract_name_id.py --source ~/Documents/EECS504_files/psets/pset6/submissions --target ~/Documents/EECS504_files/psets/pset6/submissions_renamed
# python extract_name_id.py --source ~/Documents/EECS504_files/psets/pset7/submissions --target ~/Documents/EECS504_files/psets/pset7/submissions_renamed
# python extract_name_id.py --source ~/Documents/EECS504_files/psets/pset8/submissions --target ~/Documents/EECS504_files/psets/pset8/submissions_renamed
# python extract_name_id.py --source ~/Documents/EECS504_files/psets/pset9/submissions --target ~/Documents/EECS504_files/psets/pset9/submissions_renamed
# python extract_name_id.py --source ~/Documents/EECS504_files/psets/pset10/submissions --target ~/Documents/EECS504_files/psets/pset10/submissions_renamed

import os
import tqdm
import subprocess
import re

if __name__ == "__main__":
    import argparse

    argparser = argparse.ArgumentParser()
    argparser.add_argument('--source', type=str, help='where to extrac the ipynbs', default=None)
    argparser.add_argument('--target', type=str, help='where to store the converted pdfs', default=None)
    argparser.add_argument('--smoke_test', action='store_true')

    args = argparser.parse_args()

    source = args.source
    target = args.target
    files = os.listdir(source)
    if ".DS_Store" in files:
        files.remove(".DS_Store")
    print('Total number of ipynb files {}'.format(len(files)))

    if not os.path.exists(target):
        os.mkdir(target)

    if args.smoke_test:
        files = files[:3]

    for file in tqdm.tqdm(files):

        if "LATE" in file:
            file_ = '_'.join(file.split('_')[4:6])
        elif "EECS" in file:
            file_ = file
        elif len(file.split('_')) <= 4:
            file_ = file
        else:
            file_ = '_'.join(file.split('_')[3:5])

        # print edge case
        if ".ipynb" == file_:
            print(file)

        if '.ipynb' not in file_:
            file_ += '.ipynb'

        # remove version
        if '-' in file_:
            file_ = re.sub(r"-\d", "", file_)

        cmd = 'cp {} {}'.format(os.path.join(source, file), os.path.join(target, file_)).split(' ')
        # print(cmd)
        command_run = subprocess.call(cmd)

        if command_run:
            print(cmd)