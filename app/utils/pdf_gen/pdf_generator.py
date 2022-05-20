from urllib import request
from fpdf import FPDF
from math import ceil
import logging
from urllib.error import HTTPError
import os
import shutil
from tempfile import TemporaryDirectory

import requests

import warnings

warnings.filterwarnings('ignore')

from rfc6266 import parse_requests_response

from .templates.pic_rights import template


logger = logging.getLogger(__name__)


def get_file(url, storage_dir):
    r = requests.get(url, verify=False)
    fname = parse_requests_response(r).filename_unsafe
    with open(os.path.join(storage_dir, fname), 'wb') as f:
        f.write(r.text.encode())
    return fname


class PDF(FPDF):
    template = template

    def __init__(self, *args, **kwargs):
        ## Set temp work dir
        self.tempdir = TemporaryDirectory(prefix='PDFGEN_')
        self.work_dir = os.path.join(self.tempdir.name, 'package')
        self.image_dir = os.path.join(self.work_dir, "images")
        os.makedirs(self.image_dir, exist_ok=False)
        super().__init__(*args, **kwargs)

    def header(self):
        if self.page_no()==1:
            pass
        else:
            self.set_font('Times', 'B', 15)
            self.cell(0, 10, 'Image URLs', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Times', 'B', 9)
        self.cell(0, 10, str(self.page_no()), 0, 0, 'C')

    def generate_document(self, image_list: list, export_name: str):
        self.add_page()
        self.set_margins(20, 10, 20)
        self.set_font("Times", size=14, style="B")
        self.cell(200, 8, txt="Vereinbarung", ln=1, align='C')
        self.cell(175, 8, txt="über die Einräumung von Nutzungsrechten zu Vertriebszwecken", ln=2, align='C')
  
        num_img_file = len(image_list) 
        num_page = ceil(len(image_list)/46) # Calculate number of pages assuming 1 URL will not exceed one line
        self.set_font("Times", size = 8)
        for x in self.template.split("\n"):
            self.multi_cell(0, 5.5, txt=x.format(num_1=str(num_page), num_2=str(num_img_file)), align='J')
        
        self.add_page()
        self.set_font("Times", size=9)
        for idx, url in enumerate(image_list, 1):
            try:
                get_file(url, storage_dir=self.image_dir)
                item = "- " + url.split("?")[0]
                self.cell(200, 5.5, txt=item, ln=idx)
            except HTTPError as e:
                logger.info(f'Error getting {url} because of {e}')

        my_document = os.path.join(self.work_dir, export_name)
        self.output(my_document)
    
    def compress_docs(self):
        shutil.make_archive(self.image_dir, 'zip', self.image_dir)
        shutil.rmtree(self.image_dir)
        return self.work_dir

    def cleanup_export(self):
        self.tempdir.cleanup()
