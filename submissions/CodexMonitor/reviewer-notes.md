# Codex Monitor — review notes

The plugin is a display client. Its separate relay opens the local Codex task database read-only and observes the local `codex-ipc` named pipe. It publishes task metadata and status, not conversation bodies, to the game. The internal IPC stream itself can contain conversation data before projection.

The HTTP server binds to `127.0.0.1:43187` and serves `GET /health` and `GET /api/threads`. It checks Host and Origin and accepts no task actions. There is no local authentication token: another local process can read the exposed task metadata. The plugin polls every two seconds with response size and time limits, without proxying or redirects.

The optional usage display calls `account/rateLimits/read` through a separately authenticated Codex CLI over stdio. Its account can differ from the desktop app's account. Internal protocols can change, and stale or unavailable states are displayed as unknown.

For a review, use Windows, Node.js 22.22.2 and an open Codex desktop app. In a separate durable copy of the pinned source, run `bridge/Start-Bridge.ps1`. The signed-in CLI is needed for usage limits. Dalamud installs only the plugin and will not install or update the relay. Keep one relay instance.

[Detailed source map and setup](https://github.com/Aleqsd/codex-monitor/blob/7958d1930ae9dbd4200d7c26a5ecd889643c8a8f/docs/SUBMISSION-REVIEW.md).

Local Release compilation passed. Personal in-game testing was reported during development; the new submission build and the official Plogon pipeline have not been exercised in this preparation.
