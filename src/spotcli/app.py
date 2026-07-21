from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header

from spotcli.widgets.sidebar import Sidebar
from spotcli.widgets.content import Content
from spotcli.widgets.player import PlayerBar


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
            yield Sidebar()
            yield Content()

        yield PlayerBar()