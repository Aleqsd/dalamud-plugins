# État de la préparation — 7 septembre 2026

Les sources sont publiques sur une branche `prepare-dalamud-submission` dans chaque dépôt. Les manifestes pointent vers des commits exacts. Les versions sont conservées pour ces builds de préparation : ils ne remplacent pas les binaires déjà distribués sous les mêmes numéros.

| Plugin | Version | Commit proposé | Vérification locale |
| --- | --- | --- | --- |
| Hotbar Atelier | 0.5.2.0 | [5a662db](https://github.com/Aleqsd/hotbar-atelier/commit/5a662db413320e5e0e327f3823c937ed08c2f54a) | Nouveau clone public, caches NuGet neufs, Release, 74 tests réussis |
| Codex Monitor | 0.6.1.0 | [7958d19](https://github.com/Aleqsd/codex-monitor/commit/7958d1930ae9dbd4200d7c26a5ecd889643c8a8f) | Copie isolée, Release, métadonnées générées vérifiées |
| Minimap Zoom | 0.4.1.0 | [4c26d7f](https://github.com/Aleqsd/minimap-zoom/commit/4c26d7f5edd7cec4505559ef151a9ad21681cf90) | Copie isolée, Release, ZIP Packager, 54 contrôles hors jeu réussis |

Les tâches propriétaires ont compilé avec .NET 10.0.400, Dalamud.NET.Sdk 15.0.0 et les bibliothèques locales API 15, avec restauration verrouillée. Les trois compilations sont sans avertissement ni erreur. Hotbar Atelier et Codex Monitor ont un `global.json` ; Minimap Zoom choisit le SDK .NET installé, sans ce fichier. Son SDK Dalamud et ses dépendances sont verrouillés dans le projet et le lockfile.

La tâche de publication a relu les rapports de build, recomputé les empreintes des trois DLL et vérifié les sources publiques, les déclarations d'assets, les TOML et les 12 PNG. Les icônes sont carrées, en 256 × 256. `assets.json` trace les images. Les trois noms étaient absents de `testing/live` et `stable` au contrôle du dépôt D17 ; revérifier avant l'envoi.

Les branches ajoutent la documentation, les métadonnées et, pour Minimap Zoom, le build adapté. Hotbar Atelier inclut aussi le correctif 0.5.2 : sa fenêtre de configuration reste fermée au chargement. Le catalogue personnalisé distribue séparément la release 0.5.2 issue du commit `b18e70f`, tandis que le dossier officiel utilise le commit `5a662db` avec ses déclarations d'assets. Les anciens assets de release et les DLL en cours d'utilisation n'ont pas été remplacés. Aucun workflow GitHub Actions n'a été ajouté ni activé par cette préparation. Aucun message aux approbateurs ni PR officielle n'a été envoyé ; le service Plogon n'a donc pas encore compilé ces sources.

## À terminer avant la soumission

Les essais personnels déclarés par Aleqsd concernent le développement des plugins. Aucun essai en jeu de ces trois nouveaux commits n'est attesté. Vérifier le build retenu avec une seule copie du plugin chargée, en conservant la configuration :

- **Hotbar Atelier** : apparence et clics des barres, visuels de recharge, restauration, éditeur HUD et changements de zone/job. [Notes de revue](HotbarAtelier/reviewer-notes.md).
- **Codex Monitor** : connexion au relais, tâches et questions, notifications/HUD, sons et état hors ligne. Le relais reste installé séparément. [Notes de revue](CodexMonitor/reviewer-notes.md).
- **Minimap Zoom** : zoom, marqueurs, forme/cadre, restauration et cycle de vie de la mini-carte. Faire préciser l'acceptabilité de la portée accrue et l'absence de restriction PvP avant de soumettre. [Notes de revue](MinimapZoom/reviewer-notes.md).

Les messages d'avis préalable sont prêts dans chaque dossier. Les notes de code aident à comprendre les choix et à répondre aux reviewers ; elles ne constituent pas une attestation de compréhension ou de revue humaine. Après une modification fonctionnelle demandée par les approbateurs, mettre à jour le commit, le build et l'essai correspondant.

## Empreintes des builds locaux de préparation

Ces empreintes identifient les fichiers vérifiés ici. Elles ne prédisent pas les DLL que produira Plogon dans son propre environnement.

```text
HotbarAtelier.dll  B02B7F2829196D74DEE64F17691E89F35277CD65AD749EC15C6C679A5AF8041D
CodexMonitor.dll   51158010A79572BA3569F680BC883B32260EE4CB5FA430538D245CD4704F9F72
MinimapZoom.dll    9ED0678F2FFB904DA960D57A58C1A43D9116AD2EDD94B6B42333DA1B363868D7
```
