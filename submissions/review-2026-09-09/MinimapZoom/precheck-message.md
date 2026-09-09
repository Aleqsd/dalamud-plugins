Hi! Before opening a PR, could I ask whether **Minimap Zoom** would fit the official repository?

It adjusts the native minimap's shape, frame and markers, with profiles and an optional hold-to-zoom-out shortcut. Its zoom range is 0.25–2 instead of the native 0.5–2. Below 0.5, it expands native marker collection up to twice the normal range, keeping the native 100-marker limit and using client data. It doesn't change the world camera.

The current version has no PvP disable or safe-category allowlist for the wider collection. I can't claim enemy markers are excluded or that this provides no combat advantage. Would a restricted scope be acceptable, and what limits would you require before submission?

AI usage is **Auto (OpenAI Codex)**: Codex wrote most of the code and ran autonomous passes; I chose the features, tested in game during development and guided improvements. The icon, mask and frames were also made with Codex. If the icon is a problem, I'm happy to make one by hand 🙂

Current source: https://github.com/Aleqsd/minimap-zoom/tree/df96f63db7423248f8a6d506fccb8c2eef6a379b

Thanks for your advice!
