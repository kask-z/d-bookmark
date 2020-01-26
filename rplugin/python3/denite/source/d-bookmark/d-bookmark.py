# ============================================================================
# FILE: defx/drive.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# License: MIT license
# ============================================================================

import typing
import os
from denite.source.base import Base
# from defx.util import Nvim, UserContext, Candidates
from denite.util import globruntime, Nvim, UserContext, Candidates
# from denite.source.file import Source as File
# from denite.base.source import Base
# from .base import Base

class Source(Base):

    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)

        self.name = 'book/bookmark'
        self.kind = 'command'
        self._bookmark: typing.List[str] = []

    def on_init(self, context: UserContext) -> None:

        path_text = self.vim.vars['denite#bookmark_info']
        with open(path_text) as f:
            self._bookmark= f.read().splitlines()

    def gather_candidates(self, context: UserContext) -> Candidates:

        result_list = list()
        
        for x in self._bookmark:
            if os.path.isdir(x):
                result_list.append({
                    'word': x,
                    'abbr': x + '/',
                    'action__command': f"Defx " + x,
                    'action__path': x
                })
            elif os.path.isfile(x):
                result_list.append({
                    'word': x,
                    'abbr': x,
                    'action__command': f"e " + x,
                    'action__path': x,
                })

        return result_list



