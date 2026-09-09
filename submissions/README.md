# Soumissions Dalamud

État du 9 septembre 2026 :

| Plugin | État |
| --- | --- |
| Codex Monitor 0.11.1 | [PR #9330 ouverte en testing](https://github.com/goatcorp/DalamudPluginsD17/pull/9330). Manifeste validé ; compilation officielle et revue à confirmer. |
| Minimap Zoom 0.5.1 | [PR #9331 ouverte en testing](https://github.com/goatcorp/DalamudPluginsD17/pull/9331). Manifeste validé ; périmètre du dézoom et PvP à discuter pendant la revue. |
| Hotbar Atelier | [Ancien brouillon](HotbarAtelier/pr-body.md), hors de cet envoi. |

[Résumé et textes actuels](review-2026-09-09/README.md) · [Vérifications](VERIFICATION.md) · [Origine des images](ASSETS.md)

Aleqsd confirme avoir testé Codex Monitor 0.11.1 et Minimap Zoom 0.5.1 en jeu avec la dernière mise à jour de FFXIV : les deux fonctionnent. Les builds de préparation changent seulement les métadonnées et la compilation ; leur chargement séparé en jeu n'est pas attesté.

Les textes déclarent l'aide substantielle de Codex, ses passes autonomes, ainsi que les idées, essais et retours d'Aleqsd. Ils proposent de refaire les icônes à la main si nécessaire 🙂

Les manifestes et images de CodexMonitor et MinimapZoom correspondent désormais aux sources de préparation du 9 septembre. Chaque dossier testing/live a été envoyé dans sa propre PR pour Codex Monitor et Minimap Zoom. Une soumission ne vaut pas acceptation ; le dépôt personnalisé reste indépendant.

Pour vérifier les fichiers contre leurs sources publiques : `python submissions/prepare.py --check`. Cette commande ne publie rien.

Références : [soumission officielle](https://dalamud.dev/plugin-publishing/submission/), [restrictions](https://dalamud.dev/plugin-publishing/restrictions/), [politique IA](https://dalamud.dev/plugin-publishing/ai-policy/).
