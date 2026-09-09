# Sources et préparation technique

État du 9 septembre 2026 après accord de publication et confirmation des essais par Aleqsd.

| Plugin | Release de départ | Source de préparation publique |
| --- | --- | --- |
| Codex Monitor 0.11.1 | [8636098](https://github.com/Aleqsd/codex-monitor/commit/8636098bb42abfc817935bcd75144cb463aea8e7) | [1ae4201](https://github.com/Aleqsd/codex-monitor/commit/1ae42019dabf84dd3ad33ab0179f893cb26685a4) |
| Minimap Zoom 0.5.1 | [df96f63](https://github.com/Aleqsd/minimap-zoom/commit/df96f63db7423248f8a6d506fccb8c2eef6a379b) | [9212649](https://github.com/Aleqsd/minimap-zoom/commit/921264966a7f0936172826fd1a17633f9b18f94d) |

Les deux sources sont sur leur branche `prepare-dalamud-20260909`. Aucun changement du code C# de fonctionnement ; les cinq scripts du relais Codex Monitor sont également identiques à la release.

## Ajustements

**Codex Monitor** : déclaration de l'icône et des sons créés avec Codex dans la description, rétablissement de RepoUrl/IconUrl, résolution de TerraFX par DalamudLibPath. SDK 15 et lockfile conservés. [Note de préparation](https://github.com/Aleqsd/codex-monitor/blob/1ae42019dabf84dd3ad33ab0179f893cb26685a4/docs/SUBMISSION-20260909.md).

Le relais inclus se lance depuis les réglages ; démarrage automatique facultatif, désactivé par défaut. Node.js 22.22.2+ et Codex sont externes ; le quota nécessite aussi un CLI authentifié. Les extraits facultatifs de questions sont bornés à 240 caractères et absents de l'historique sauvegardé. Le flux IPC complet existe avant projection. Les réponses et sorties d'outils ne sont pas transmises au jeu.

**Minimap Zoom** : migration vers Dalamud.NET.Sdk 15.0.0, Packager et dépendances verrouillées, chemins SDK et symboles portables. Le contrôle du client `2026.09.01.0000.0000` et les fonctions natives sont inchangés. [Note de préparation](https://github.com/Aleqsd/minimap-zoom/blob/921264966a7f0936172826fd1a17633f9b18f94d/docs/SUBMISSION-20260909.md).

Le zoom 0.25–2 étend la collecte sous 0.5 jusqu'à deux fois sa portée native, avec la limite de 100 marqueurs. Aucune garde PvP ni liste de catégories autorisées ne protège cette extension. Les filtres d'apparence ne sont pas une telle garde. Des données déjà disponibles côté client peuvent néanmoins procurer un avantage ; l'admissibilité reste à discuter.

## Validation

Aleqsd confirme avoir testé personnellement les releases 0.11.1 et 0.5.1 avec la dernière mise à jour de FFXIV : les deux fonctionnent. Cela n'atteste ni l'acceptabilité du dézoom ni un chargement séparé des nouveaux builds de préparation.

Les deux copies isolées ont passé la restauration verrouillée et le build Release avec .NET 10.0.400 et Dalamud 15.0.3.3, sans avertissement ni erreur. Codex Monitor a été recompilé au commit 1ae4201 et Minimap Zoom au commit 50f1ff3. Le commit Minimap final 9212649 change uniquement la note de soumission ; code et build sont identiques. Les manifestes, versions et archives Packager sont vérifiés ; aucune dépendance hôte n'est embarquée. Les binaires installés et releases existantes sont préservés.

| Fichier | SHA-256 local |
| --- | --- |
| CodexMonitor.dll 0.11.1.0 | `33d558a7a9f986547a1ef9a2f8b163eb6a341c6f2e275fa7fea0055920abcaf6` |
| MinimapZoom.dll 0.5.1.0 | `e6bd522add6dd5ce3e8eb41aac9661a453afa6e537c365d3389cd92fda376d61` |

Ces empreintes décrivent les builds locaux, pas ceux que produira Plogon.

## Envois

La [PR Codex Monitor #9330](https://github.com/goatcorp/DalamudPluginsD17/pull/9330), ouverte par Aleqsd, ajoute cinq fichiers dans testing/live/CodexMonitor/ : manifeste, icône et trois aperçus. Branche `submit-codex-monitor-20260909`, commit D17 `95cfd8c95befbe1277bebe28fa7d0bdfd3862075`, base relue `0b906dfe65ddd5e866440a7344dcb918edb4df1c`. Le contrôle lint-manifest est réussi ; aucune compilation Plogon ou acceptation n'est encore attestée.

La [PR Minimap #9331](https://github.com/goatcorp/DalamudPluginsD17/pull/9331), ouverte par Aleqsd, ajoute cinq fichiers dans testing/live/MinimapZoom/. Branche `submit-minimap-zoom-20260909`, commit D17 `8ee89bb659da6fff1789e75cdb1016cf8877bdcc`. Son contrôle lint-manifest est réussi. Le périmètre du dézoom est présenté explicitement à la revue. Toute restriction fonctionnelle demandée nécessitera son propre changement et ses essais.

Les Actions du fork Aleqsd/DalamudPluginsD17 sont désactivées. Le catalogue personnalisé reste indépendant. Les assets viennent des sources publiques répertoriées dans [assets.json](../assets.json), avec versions et origine explicites.

Références relues : [soumission](https://dalamud.dev/plugin-publishing/submission/), [build D17](https://github.com/goatcorp/DalamudPluginsD17#preparing-your-repository), [restrictions](https://dalamud.dev/plugin-publishing/restrictions/), [politique IA](https://dalamud.dev/plugin-publishing/ai-policy/).
