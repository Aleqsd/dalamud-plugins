# Soumissions — 9 septembre 2026

- **Codex Monitor 0.11.1** : [PR #9330 ouverte](https://github.com/goatcorp/DalamudPluginsD17/pull/9330) pour le canal testing. Contrôle du manifeste réussi ; compilation officielle et revue à confirmer.
- **Minimap Zoom 0.5.1** : [PR #9331 ouverte](https://github.com/goatcorp/DalamudPluginsD17/pull/9331) pour le canal testing. Manifeste validé ; le périmètre du dézoom étendu reste à discuter pendant la revue.

## Fonctionnalités en bref

**Codex Monitor** : HUD des tâches locales, réponses non lues et questions, modèle/effort, notifications avec pause et quota facultatif. Relais inclus, lancé depuis les réglages ; Node.js et Codex restent nécessaires.

**Minimap Zoom** : dézoom, forme et cadre de la mini-carte, réglages des marqueurs, profils et raccourci temporaire. La collecte élargie des marqueurs n'a actuellement ni garde PvP ni liste de catégories autorisées.

Aleqsd a confirmé le 9 septembre avoir testé ces deux versions en jeu avec la dernière mise à jour de FFXIV : elles fonctionnent. Les adaptations de soumission portent seulement sur les métadonnées et le build. Les nouveaux binaires isolés ont été compilés et leurs paquets vérifiés ; leur chargement séparé en jeu n'est pas attesté.

## Textes et sources

- [PR Codex Monitor envoyée](CodexMonitor/pr-body.md)
- [PR Minimap envoyée](MinimapZoom/pr-body.md)
- [Sources, builds et limites de validation](SOURCE-REVIEW.md)

Les textes déclarent le niveau IA **Auto (OpenAI Codex)**, les passes autonomes, le rôle d'Aleqsd dans les idées, essais et améliorations, ainsi que l'origine des assets. La proposition de refaire les icônes à la main est conservée 🙂

![HUD de Codex Monitor](https://raw.githubusercontent.com/Aleqsd/codex-monitor/1ae42019dabf84dd3ad33ab0179f893cb26685a4/docs/images/new-huds.png)

*Composants ImGui réels, données fictives, hors jeu — source 0.11.1.*

![Réglages de Minimap Zoom](https://raw.githubusercontent.com/Aleqsd/minimap-zoom/921264966a7f0936172826fd1a17633f9b18f94d/docs/images/settings-map.png)

*Réglages ImGui hors jeu, rendus en 0.5.0 et conservés en 0.5.1. La capture en jeu du dossier montre la 0.4.1.*

Les dossiers techniques voisins ont été actualisés avec les commits exacts. Hotbar Atelier reste hors de cet envoi.
