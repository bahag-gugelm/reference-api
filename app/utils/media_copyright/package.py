import logging
import os
import shutil
from tempfile import TemporaryDirectory
from typing import Tuple, Dict 
import requests
from rfc6266 import parse_requests_response
import warnings


from jinja2 import Environment, PackageLoader, select_autoescape
from weasyprint import HTML


warnings.filterwarnings('ignore')
logger = logging.getLogger(__name__)


templates_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')


template_env = Environment(
    loader=PackageLoader("app.utils.media_copyright"),
    autoescape=select_autoescape(),
    # enable_async=True
    )


OUTPUT_PDF_FNAME = 'Vereinbarung Bildrechte Hersteller.pdf'


class MediaRightsRequestPack:
    def __init__(self, links) -> None:
        self.links = set(links)
        self.work_dir = TemporaryDirectory(prefix='_MRR_')
        self.images_dir = os.path.join(self.work_dir.name, 'images')
        os.makedirs(self.images_dir, exist_ok=True)
        self.html_dir = os.path.join(self.work_dir.name, 'html')        
        os.makedirs(self.html_dir, exist_ok=True)
        self.template = template_env.get_template('pic_rights.html')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.work_dir.cleanup()

    def _get_file(self, url):
        r = requests.get(url, verify=False)
        if r.ok:
            fname = parse_requests_response(r).filename_unsafe
            with open(os.path.join(self.images_dir, fname), 'wb') as f:
                f.write(r.content)
            return fname

    def _get_images(self):
        dead_links = list()
        for link in self.links:
            if not self._get_file(link):
                dead_links.append(link)
        return dead_links
    
    def _save_html(self, html):
        shutil.copytree(
            os.path.join(templates_path, 'assets'),
            os.path.join(self.html_dir, 'assets')
            )
        with open(os.path.join(self.html_dir, 'pics_rights.html'), 'w') as f:
            f.write(html)

    def _render_html(self, ctx = {}):
        html_doc = self.template.render(ctx)
        self._save_html(html_doc)
        return HTML(os.path.join(self.html_dir, 'pics_rights.html'))

    def _render_pdf(self):
        html = self._render_html({'links': self.links})
        num_pages = len(html.render().pages)
        html = self._render_html(
            {
                'pages_count': num_pages - 1,
                'assets_count': len(self.links),
                'links': self.links
            }
        )
        html.write_pdf(os.path.join(self.work_dir.name, OUTPUT_PDF_FNAME))
        shutil.rmtree(self.html_dir)

    def make_package(self, force=False) -> Tuple[bool, Dict]:
        dead_links = self._get_images()
        if dead_links:
            if not force:
                shutil.rmtree(self.images_dir)
                return False, {
                    'msg': 'Some files are not available',
                    'links': dead_links
                    }
            self.links = self.links - set(dead_links)
        shutil.make_archive(self.images_dir, 'zip', self.images_dir)
        shutil.rmtree(self.images_dir)
        self._render_pdf()
        return True, {'output_path': self.work_dir.name}

    def cleanup(self):
        self.work_dir.cleanup()
