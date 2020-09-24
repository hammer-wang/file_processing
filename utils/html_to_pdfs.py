'''
python html_to_pdfs.py --source ~/Documents/EECS504_files/psets/pset5/htmls --target ~/Documents/EECS504_files/psets/pset5/pdfs
'''
import pdfkit
import os
import argparse
import tqdm
import glob

if __name__=='__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--source', type=str, help='where to extract the html files', default=None)
    argparser.add_argument('--target', type=str, help='where to store the converted pdfs', default=None)
    argparser.add_argument('--smoke_test', action='store_true')
    args = argparser.parse_args()

    source = args.source
    target = args.target
    files = os.listdir(source)

    files = [item for item in files if '.html' in item]
    print('Total number of ipynb files {}'.format(len(files)))

    if not os.path.exists(target):
        os.mkdir(target)

    for file in tqdm.tqdm(files):
        pdfkit.from_file(os.path.join(source, file), os.path.join(target, file.replace('.html', '.pdf')))
