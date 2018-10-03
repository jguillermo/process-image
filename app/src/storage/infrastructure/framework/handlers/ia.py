# -*- coding: utf-8 -*-
import os

import falcon
from bootstrap import File
from bootstrap.framework.decorators.service import handler_except
from sdk.process_image import ProcessImage
from sdk.types import TypeUuid
from src.storage.application.services.image_app_service import ImageAppService


class IaImageHandler:

    @handler_except
    def on_post(self, req: falcon.Request, resp: falcon.Response):
        id = TypeUuid.random().value()

        fileitem = req.get_param('image')

        if not fileitem.filename:
            raise Exception("No existe el parámetro : image")

        service = ImageAppService(fileitem.file, id)
        name_large = service.image_resize(1200)

        img = ProcessImage(name_large)
        rs = img.process()

        os.remove(name_large)

        return rs


    def on_get(self, req: falcon.Request, resp: falcon.Response):
        file = File.read('/app/doc/form.html')
        resp.body = file.read()
        resp.content_type = falcon.MEDIA_HTML
        resp.status = falcon.HTTP_200
