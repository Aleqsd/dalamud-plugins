# Minimap Zoom — review notes

The native zoom range is 0.5–2; the plugin permits 0.25–2. Below 0.5, it increases the collection range by `0.5 / zoom`, capped at 2. This affects native marker collection within the minimap scope, including the fixed-marker radius. There is no allowlist limited to aetherytes, vendors or quests, and enemy markers are not guaranteed to be excluded from its effects.

The plugin uses the client's native marker vector and keeps the 100 regular-marker limit plus the player marker. It does not add server queries or scan a separate object table. This does not establish the absence of a combat or PvP advantage. There is currently no PvP-specific disable, and PvP behaviour was not tested during this preparation.

Compatibility checks require the supported client version and executable hash, native signatures and expected structures. Range changes are scoped and restored in `finally`. Other code owns and restores zoom, marker presentation, masks, frames and collision state through the addon lifecycle. Saved zoom is returned to native bounds while preserving the north-lock bits.

[Native code map, exact ranges and limitations](https://github.com/Aleqsd/minimap-zoom/blob/4c26d7f5edd7cec4505559ef151a9ad21681cf90/docs/submission-preparation.md).

The preparation migrates the build to Dalamud.NET.Sdk 15.0.0 and committed locked dependencies. It does not change native functionality. Acceptance of the wider view remains an open question for the approval team. Personal in-game testing was reported during development; the new preparation build still needs its own in-game pass.
