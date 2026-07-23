from textual.widgets import ContentSwitcher

from spotcli.pages.home import HomePage
from spotcli.pages.search import SearchPage


class Content(ContentSwitcher):

    def compose(self):
        yield HomePage(id="home")
        yield SearchPage(id="search")

    def on_mount(self):
        self.current = "home"

    def show_page(self, page: str):
        self.current = page