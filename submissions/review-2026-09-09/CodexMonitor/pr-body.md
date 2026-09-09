Hi! I'd like to share **Codex Monitor**, a small HUD for keeping an eye on local Codex tasks while playing. It shows task status, unread replies, questions, model and effort, with optional notifications and usage limits. Clicking the HUD opens settings; its bell pauses notifications.

The plugin includes a local Node.js relay, started from settings. Automatic startup is optional and off by default. Node.js 22.22.2+ and Codex are required; usage limits also need a signed-in Codex CLI. It doesn't run tasks, answer questions or approve requests. Optional question previews are limited to 240 characters and aren't saved in history; answers and tool output aren't sent to the game. The internal Codex protocol may change.

**AI usage: Auto (OpenAI Codex).** Codex wrote most of the code, including autonomous implementation and testing passes, and helped draft this submission. I chose the features, tested the plugin in game during development, and refined it through my own ideas and feedback.

The installer icon and built-in procedural sounds were created with Codex. Sounds can be disabled or replaced with a local WAV. The screenshots show the actual ImGui components with fictional data, outside the game. If the AI-made icon is an issue, I'm happy to make one by hand 🙂

Thanks for taking a look! I'm happy to discuss the relay and work through feedback.
