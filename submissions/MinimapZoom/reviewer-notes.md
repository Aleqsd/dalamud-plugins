# Minimap Zoom — review notes

Current preparation is based on 0.5.1. [Exact source and build notes](https://github.com/Aleqsd/minimap-zoom/blob/921264966a7f0936172826fd1a17633f9b18f94d/docs/SUBMISSION-20260909.md). [PR #9331](https://github.com/goatcorp/DalamudPluginsD17/pull/9331) presents the extended zoom scope for explicit review.

The native zoom range is 0.5–2; the plugin permits 0.25–2. Below 0.5, native marker collection expands up to twice the normal range, retaining the 100-marker limit and client data. There is no safe-category allowlist or PvP disable. Enemy markers are not guaranteed to be excluded; client-side data does not establish the absence of a combat advantage.

Compatibility checks require the supported client, executable hash, signatures and expected structures. Range changes are scoped and restored; the addon lifecycle restores native fields owned by the plugin. World camera and server queries are unchanged.

The source also includes minimap profiles, an optional hold-to-zoom-out shortcut and marker appearance controls. The submission adaptation changes only SDK, dependency locking and packaging.

Aleqsd tested release 0.5.1 with the latest FFXIV update and confirmed it works. The isolated preparation build passed; it was not separately loaded in game. Functional testing does not establish catalogue eligibility.
