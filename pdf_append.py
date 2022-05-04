import zipfile
import os,sys
import glob
import numpy as np
from PyPDF3 import PdfFileMerger

zip_path=sys.argv[1]
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall("./temp/")
pdfs=np.sort(glob.glob("./temp/*"))
#pdfs =["join_letters_result.pdf","join_words.pdf","joint_sentences_result.pdf","joint_passage_result.pdf"]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write(f"{zip_path}"[:-4]+".pdf")
merger.close()

for f in pdfs:
    os.remove(f"{f}")

