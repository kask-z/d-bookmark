import typing 
from defx.base.kind import Base
from defx.action import ActionAttr
from defx.action import ActionTable
from defx.action import do_action
from defx.context import Context
from defx.defx import Defx
from defx.session import Session
from defx.util import Nvim
from defx.view import View
from defx.base.kind import action

_action_table: typing.Dict[str, ActionTable] = {}

ACTION_FUNC = typing.Callable[[View, Defx, Context], None]


def action(name: str, attr: ActionAttr = ActionAttr.NONE
           ) -> typing.Callable[[ACTION_FUNC], ACTION_FUNC]:
    def wrapper(func: ACTION_FUNC) -> ACTION_FUNC:
        _action_table[name] = ActionTable(func=func, attr=attr)

        def inner_wrapper(view: View, defx: Defx, context: Context) -> None:
            return func(view, defx, context)
        return inner_wrapper
    return wrapper


class Base(Base):

    def __init__(self, vim: Nvim) -> None:
        self.vim = vim
        self.name = 'base'

    def get_actions(self) -> typing.Dict[str, ActionTable]:
        return _action_table

@action(name='echotest')
def _echotest(view: View, defx: Defx, context: Context) -> None:
    yank = '\n'.join([str(x['action__path']) for x in context.targets])
    view.print_msg('testecho:\n' + yank)
