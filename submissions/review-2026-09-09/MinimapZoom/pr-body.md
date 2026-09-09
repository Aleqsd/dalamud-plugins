Hi! I'd like to share **Minimap Zoom**, a plugin for adjusting the native minimap's zoom, shape, frame and markers. It also offers saved profiles, optional zone switching and a hold-to-zoom-out shortcut. `/minizoom` opens settings; `/minizoom off` restores the minimap without deleting profiles.

The zoom range is 0.25–2, below the native minimum of 0.5. It also extends native marker collection using data already available to the client, keeping the 100-marker limit. There is currently no PvP disable or safe-category allowlist for this extension. It changes the minimap, not the world camera. These limits need explicit review; I don't want to assume the wider view is acceptable.

I've tested **0.5.1 in game with the latest FFXIV update**, and it works. The D17 build preparation leaves runtime code unchanged.

**AI usage: Auto (OpenAI Codex).** Codex wrote most of the code, including autonomous implementation and testing passes, and helped draft this submission. I chose the features, tested the plugin in game, and refined it through my own ideas and feedback.

The installer icon, square mask and procedural frames were created with Codex. The in-game screenshot comes from version 0.4.1; the map settings preview shows 0.5.0 outside the game. If the AI-made icon is an issue, I'm happy to make one by hand 🙂

Thanks for taking a look! I'm happy to discuss a narrower scope if needed.
