Hi! I'd like to share **Codex Monitor**, a small way to keep an eye on Codex tasks while playing: task status, questions waiting for attention, notifications and an optional mini HUD.

It needs a separate local Node.js relay, started by the user. The plugin reads it through loopback; it doesn't start tasks or approve requests. Conversation text isn't sent to the game. Dalamud updates the plugin; the relay is installed and updated separately. `/codex` opens the task list.

**AI usage: Auto (OpenAI Codex).** Codex wrote most of the code and ran autonomous implementation and testing passes. I chose the features, tested the plugin in game and guided improvements with my own ideas and feedback. Codex also helped prepare this submission.

The installer icon and built-in procedural notification sounds were created with Codex and are disclosed in the plugin description. Sounds can be disabled or replaced with a local WAV. The previews use the real ImGui components with fictional data, outside the game. If the AI-made icon is an issue, I'm happy to make one by hand 🙂

This is an initial testing submission. The relay's Codex protocol is internal and may change. Thanks for taking a look!

[Build and review notes](https://github.com/Aleqsd/dalamud-plugins/blob/prepare-official-submissions/submissions/CodexMonitor/reviewer-notes.md).
