from textual.containers import Vertical
from textual.widgets import ListView, ListItem, Static, Label


class Sidebar(ListView):
    def compose(self):
        yield ListItem(Label("🏠 Home"), id="home")
        yield ListItem(Label("🔍 Search"), id="search")
        yield ListItem(Label("❤️ Library"), id="library")
        yield ListItem(Label("📂 Playlists"), id="playlists")
        yield ListItem(Label("💻 Devices"), id="devices")
        yield ListItem(Label("⚙ Settings"), id="settings")