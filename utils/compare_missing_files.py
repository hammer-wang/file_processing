import glob

pdfs = glob.glob('/Users/wanghaozhu/Documents/EECS504_files/psets/pset7/pdfs/*.pdf')
pdfs = [item.split('/')[-1].split('.')[0] for item in pdfs]

# pdfs = glob.glob('/Users/wanghaozhu/Documents/EECS504_files/psets/pset7/submissions/*.ipynb')
# pdfs = [item.split('/')[-1].split('.')[0] for item in pdfs]

notebooks = glob.glob('/Users/wanghaozhu/Documents/EECS504_files/psets/pset7/submissions_renamed_copy/*.ipynb')
notebooks = [item.split('/')[-1].split('.')[0] for item in notebooks]

print("Missing values in first list:", (set(notebooks).difference(pdfs)))

# print("Missing values in first list:", (set(pdfs).difference(notebooks)))