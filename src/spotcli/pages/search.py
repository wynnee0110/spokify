from textual.containers import Center
from textual.widgets import Label
from textual.widgets import Input


class SearchPage(Center):
    def compose(self):
        yield Label("🔍 Search")
        yield Input(placeholder="Search for songs, artists, albums...")