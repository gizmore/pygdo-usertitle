from gdo.base.GDO_Module import GDO_Module
from gdo.base.GDO import GDO
from gdo.base.GDT import GDT

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.ui.GDT_Page import GDT_Page


class module_usertitle(GDO_Module):

    def gdo_load_scripts(self, page: 'GDT_Page'):
        pass

    def gdo_init_sidebar(self, page: 'GDT_Page'):
        pass

    def gdo_module_config(self) -> list[GDT]:
        return [
        ]

    def gdo_user_config(self) -> list[GDT]:
        return [
        ]

    def gdo_user_settings(self) -> list[GDT]:
        return [
        ]

    def gdo_classes(self) -> list[type[GDO]]:
        return [
        ]
