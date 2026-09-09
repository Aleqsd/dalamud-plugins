# Codex Monitor — review notes

Current submission: [PR #9330](https://github.com/goatcorp/DalamudPluginsD17/pull/9330), based on 0.11.1. [Exact source and setup](https://github.com/Aleqsd/codex-monitor/blob/1ae42019dabf84dd3ad33ab0179f893cb26685a4/docs/SUBMISSION-20260909.md).

The plugin observes local tasks. Its included relay reads the local task database and internal Codex IPC, then exposes read-only loopback endpoints. Optional question previews are limited to 240 characters and removed from saved history. Answers and tool output are not sent to the game. The full internal stream exists before projection.

Start the relay from Settings → Connection. Automatic startup is optional and off by default. Node.js 22.22.2+ and Codex are external prerequisites; usage limits also need a signed-in Codex CLI. An external relay remains independent. The plugin cannot send prompts, answer questions or approve actions.

Aleqsd tested release 0.11.1 with the latest FFXIV update and confirmed it works. The metadata/build-only preparation compiled successfully; its separate in-game loading and the official Plogon build are not yet attested.
