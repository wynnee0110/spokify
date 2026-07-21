from textual.containers import Vertical
from textual.widgets import Static


class Sidebar(Vertical):
    def compose(self):
        yield Static("🏠 Home")
        yield Static("🔍 Search")
        yield Static("❤️ Library")
        yield Static("📂 Playlists")
        yield Static("💻 Devices")
        yield Static("⚙ Settings")