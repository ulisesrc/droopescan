from cement.core import handler, controller
from plugins import BasePlugin
import requests
import common

class SilverStripe(BasePlugin):

    plugins_file = "plugins/silverstripe/wordlists/plugins"
    plugins_base_url = '%s/'

    themes_file = "plugins/silverstripe/wordlists/themes"
    themes_base_url = 'themes/%s/'

    folder_url = "framework/"
    regular_file_url = ["cms/css/layout.css", "framework/css/UploadField.css"]
    module_readme_file = "README.txt"

    class Meta:
        label = 'silverstripe'

    @controller.expose(help='silverstripe related scanning tools')
    def silverstripe(self):
        self.enumerate_route()


def load():
    handler.register(SilverStripe)
