Hi! I'd like to share **Minimap Zoom**, a plugin for zooming the native minimap out further and customising its shape, frame and existing markers.

The zoom range is 0.25–2, compared with the native minimum of 0.5. It extends native marker collection using data already available to the client and keeps the native marker limit. This extension has no safe-category allowlist or PvP disable. It changes the minimap, not the world camera. `/minizoom` opens the settings and `/minizoom off` restores it. I'd like the extended range and marker behaviour to be reviewed explicitly.

**AI usage: Auto (OpenAI Codex).** Codex wrote most of the code and ran autonomous implementation and testing passes. I chose the features, tested the plugin in game and guided improvements with my own ideas and feedback. Codex also helped prepare this submission.

The installer icon, square mask and procedural frame textures were created with Codex and are disclosed in the plugin description. The minimap preview is an in-game screenshot; the settings previews were rendered outside the game. If the AI-made icon is an issue, I'm happy to make one by hand 🙂

This is an initial testing submission. Thanks for taking a look — I'm happy to discuss changes to the scope!

[Build and review notes](https://github.com/Aleqsd/dalamud-plugins/blob/prepare-official-submissions/submissions/MinimapZoom/reviewer-notes.md).
