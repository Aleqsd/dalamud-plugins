# Hotbar Atelier — review notes

The plugin changes the presentation of the ten native keyboard hotbars. It does not execute actions or change their costs or key bindings. Mouse click-through disables mouse interaction only; keyboard bindings remain available.

The native controller validates addon and node identities, applies presentation changes and coordinates restoration. Separate controllers manage layout, clipping masks, textures, text visibility and mouse flags. Original values and the plugin's latest writes are tracked so restoration can preserve later changes made by the game or another plugin.

Effects are removed when disabled, during HUD editing, and before relevant addon refresh/destruction events. Unknown structures suspend the affected effect. If safe detachment cannot be established, some resources are retained until game exit instead of freeing memory still referenced by native nodes.

[File-by-file code map](https://github.com/Aleqsd/hotbar-atelier/blob/5a662db413320e5e0e327f3823c937ed08c2f54a/docs/native-code-map.md).

The settings use Dalamud's Windowing API. The displayed shape/border samples and settings captures are rendered outside the game; they do not prove live GPU rendering, mouse hitboxes or pointer safety for every game hierarchy.

Personal in-game testing was reported during development. The submission build still needs its own targeted in-game pass, especially restoration, HUD editing, zone/job changes, clicks and cooldown visuals.
