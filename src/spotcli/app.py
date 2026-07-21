from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header

from spotcli.widgets.sidebar import Sidebar
from spotcli.widgets.content import Content
from spotcli.widgets.player import PlayerBar
from textual import on
from textual.widgets import ListView, ListItem, Label


class SpotCLI(App):

    CSS = """
    Screen {
        layout: vertical;
    }

    #body {
        layout: horizontal;
        height: 1fr;
    }

    Sidebar {
        width: 24;
        border: solid green;
    }

    Content {
        width: 1fr;
        border: solid blue;
    }

    PlayerBar {
        height: 3;
        border: solid white;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        with Horizontal(id="body"):
            yield Sidebar(id="sidebar")
            yield Content(id="content")
            yield PlayerBar(id="player")

    def on_mount(self):
        self.query_one("#sidebar").focus()

    @on(ListView.Selected)
    def sidebar_selected(self, event: ListView.Selected):

        page = event.item.query_one(Label).renderable

        self.query_one(Content).show_page(str(page))