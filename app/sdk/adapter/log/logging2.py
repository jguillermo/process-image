# -*- coding: utf-8 -*-

import sys
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s'
)


def main():
    try:
        logger.error('Procesando main.py...')
    except exceptions.ExceptionHandler as error:
        logger.error(str(error), exc_info=True)


if __name__ == "__main__":
    main()
