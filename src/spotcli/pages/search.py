from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Input, Label, ListItem, ListView

from spotcli.services.spotify import SpotifyService


class SearchPage(Vertical):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spotify = SpotifyService()

    def compose(self) -> ComposeResult:
        yield Label("🔍 Search")
        yield Input(
            placeholder="Search for songs...",
            id="search-input"
        )
        yield Label("Type a search term and press Enter.", id="search-status")
        yield ListView(id="search-results")

    def on_input_submitted(self, event: Input.Submitted):
        query = event.value.strip()
        status = self.query_one("#search-status", Label)
        results_list = self.query_one("#search-results", ListView)

        results_list.clear()

        if not query:
            status.update("Type a search term and press Enter.")
            return

        results = self.spotify.search(query)

        if not results:
            status.update(f"No results for {query!r}.")
            return

        status.update(f"{len(results)} result(s) for {query!r}.")
        for result in results:
            results_list.append(ListItem(Label(result)))
