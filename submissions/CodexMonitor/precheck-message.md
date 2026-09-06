Hi! I'm preparing Codex Monitor for the testing repository and wanted to check the separate relay setup with you first.

It shows the status of my local Codex tasks in game. A user-started Node.js relay reads local task metadata and exposes it on `127.0.0.1:43187`. It doesn't send conversation text to the game or accept task actions. Codex itself and its signed-in CLI are separate prerequisites; the relay uses an internal Codex protocol that may change. Dalamud would install only the plugin.

I tested it in game and guided its features and improvements. Codex wrote most of the code, including autonomous coding and testing passes (AI usage: Auto). The icon and optional procedural sounds were also made with Codex. If the AI-made icon is an issue, I'm happy to make one by hand 🙂

[Source and relay setup](https://github.com/Aleqsd/codex-monitor/tree/prepare-dalamud-submission). Does this setup fit the repository's expectations?
