from io import BytesIO
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
import zipfile
import os

from app.utils.media_copyright.package import MediaRightsRequestPack
from app.utils.dependencies import verify_token



router = APIRouter()


@router.get("/utils/copyright")
async def docs_pack(
    pics_urls: str,
    force: bool = False,
    dependencies=Depends(verify_token),
    response_model=None,
    status_code=200
    ):
    pics_urls = pics_urls.split(',')
    with MediaRightsRequestPack(pics_urls) as doc_pack:
        success, result = doc_pack.make_package(force=force)
        if not success and not force:
            return result
        zipfile_path = result['output_path']
        out_filename = 'media_usage_agreement.zip'
        out_file = BytesIO()
        with zipfile.ZipFile(out_file, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
            for file in os.listdir(zipfile_path):
                fpath = os.path.join(zipfile_path, file)
                zf.write(fpath, file)
        out_file.seek(0)
        response = StreamingResponse(
            out_file,
            media_type='application/x-zip-compressed',
            headers = {
                "Content-Disposition": f'attachment; filename={out_filename}'
                }
            )
        return response
