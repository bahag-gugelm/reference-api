from io import BytesIO
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
import zipfile
import os

from app.utils.pdf_gen.pdf_generator import PDF
from app.utils.dependencies import verify_token


#to test fastapi ui
## [https://images.icecat.biz/img/gallery_mediums/79787991_5105415178.jpg,https://images.icecat.biz/img/gallery_mediums/79787991_2812868271.jpg]


router = APIRouter()


@router.get("/utils/copyright")
async def docs_pack(
    pics_urls: str,
    dependencies=Depends(verify_token),
    response_model=None,
    status_code=200
    ):
    pics_urls = pics_urls.split(',')
    pdf = PDF()
    out_filename = 'media_usage_agreement.zip'
    pdf.generate_document(pics_urls, "Vereinbarung Bildrechte Hersteller.pdf")
    out_file = BytesIO()
    zipfile_path = pdf.compress_docs()
    with zipfile.ZipFile(out_file, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in os.listdir(zipfile_path):
            fpath = os.path.join(zipfile_path, file)
            zf.write(fpath, file)
    out_file.seek(0)
    response = StreamingResponse(
        out_file,
        media_type="application/x-zip-compressed",
        headers = { "Content-Disposition": f"attachment; filename={out_filename}"}
    )

    pdf.cleanup_export()
    return response
