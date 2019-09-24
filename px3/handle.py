"""

"""
import os
from pathlib import Path
import logging
import asyncio
from asyncio import StreamReader, StreamWriter

log = logging.getLogger(__name__)


class Proxy(object):
    """

    """

    def __init__(self, settings):
        """ """

        self.running = True

    async def handle_client(self, reader: StreamReader, writer: StreamWriter):
        """ handle incoming clent session

        """
        peername = writer.transport.get_extra_info("peername")
        log.info("handle_client : %s", peername)

        # loop = asyncio.get_running_loop()

        while self.running:

            try:
                req = reader.read_lines()
                log.debug("req: %s", req)

            except (
                asyncio.streams.IncompleteReadError,
                ConnectionResetError,
                BrokenPipeError,
                RuntimeError,
            ) as ex:
                log.info("lost client session [%s] due to [%s]", peername, ex)
                # end session
                return

    async def close(self):
        """ clean up """
        self.running = False
