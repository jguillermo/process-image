# -*- coding: utf-8 -*-
import importlib

import falcon
from bootstrap import File
from bootstrap.framework.middlewares.MultipartMiddleware import MultipartMiddleware
from bootstrap.framework.middlewares.basic import Basic
from bootstrap.framework.middlewares.cors_middleware import CORSMiddleware


class FalconApi:

    def __init__(self):
        self.api = falcon.API(middleware=[
            CORSMiddleware(),
            MultipartMiddleware()
        ])
        self.__load_routes('src/storage/infrastructure/framework/routes.yml')

    def __load_routes(self, path_route):
        file_config = File.read_yml(path_route)
        prefix = file_config[0]['prefix']
        routes = file_config[1]['routes']
        for route in routes:
            for resource, handler in route.items():
                module_parts = handler.split('.')
                module_name = '.'.join(module_parts[:-1])
                module = importlib.import_module(module_name)
                handler = getattr(module, module_parts[-1])
                handler_instance = handler()
                self.api.add_route(prefix + resource, handler_instance)
