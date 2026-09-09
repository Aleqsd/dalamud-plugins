# PR envisagées — 9 septembre 2026

Deux brouillons en anglais, actualisés avec les dernières versions publiques. **Aucune PR ni demande d'avis n'a été envoyée.** Cette passe prépare les textes ; elle ne modifie ni les plugins ni le catalogue installé.

| Plugin | Version relue | Texte proposé | Avant l'envoi |
| --- | --- | --- | --- |
| Codex Monitor | [0.11.1](https://github.com/Aleqsd/codex-monitor/releases/tag/v0.11.1) | [Lire la PR](CodexMonitor/pr-body.md) | Déclaration des assets dans les métadonnées, build du commit retenu et essai personnel ciblé. |
| Minimap Zoom | [0.5.1](https://github.com/Aleqsd/minimap-zoom/releases/tag/v0.5.1) | [Lire la PR](MinimapZoom/pr-body.md) | [Avis préalable sur la portée et le PvP](MinimapZoom/precheck-message.md), adaptation D17 du build et essai sur le client pris en charge. |

Les titres seront **[Testing] Add Codex Monitor** et **[Testing] Add Minimap Zoom**. Ce sont des premières soumissions officielles, même si les plugins sont déjà distribués dans notre dépôt personnalisé.

Chaque PR ajoutera uniquement `testing/live/CodexMonitor/` ou `testing/live/MinimapZoom/` dans [goatcorp/DalamudPluginsD17](https://github.com/goatcorp/DalamudPluginsD17), sur une branche distincte. Le dossier contiendra le manifeste pointant vers le commit public final, une icône et les aperçus retenus. [Procédure officielle](https://dalamud.dev/plugin-publishing/submission/).

Les textes déclarent simplement le rôle de Codex, les passes autonomes et les assets concernés. Ils reprennent les essais en jeu rapportés pendant le développement, sans affirmer que les derniers builds ont déjà été validés. La proposition de refaire les icônes à la main est conservée 🙂

## Codex Monitor

La PR présente maintenant le relais inclus et son lancement facultatif, les neuf HUD, la cloche intégrée, les réponses non lues, le modèle/effort et les notifications. Elle précise la portée des extraits de questions et les prérequis externes. L'ancien texte « relais à installer séparément » ne décrit plus cette version.

![HUD actuels de Codex Monitor](https://raw.githubusercontent.com/Aleqsd/codex-monitor/8636098bb42abfc817935bcd75144cb463aea8e7/docs/images/new-huds.png)

*Composants ImGui réels, données fictives, hors jeu — source 0.11.1.*

## Minimap Zoom

La PR couvre les profils, le raccourci temporaire et la compatibilité 0.5.1. Le point à discuter reste la portée élargie des marqueurs et l'absence de garde PvP. Mon conseil est d'envoyer d'abord le court message d'avis : les [restrictions officielles](https://dalamud.dev/plugin-publishing/restrictions/) demandent un échange préalable pour les fonctions pouvant affecter le combat. Il s'agit d'une question d'acceptabilité à faire trancher, pas d'une certitude de refus.

![Réglages actuels de Minimap Zoom](https://raw.githubusercontent.com/Aleqsd/minimap-zoom/df96f63db7423248f8a6d506fccb8c2eef6a379b/docs/images/settings-map.png)

*Réglages ImGui hors jeu, rendus en 0.5.0 et conservés dans le dépôt 0.5.1. La capture en jeu disponible montre encore la 0.4.1. Ces versions resteront explicites dans les légendes si les images sont jointes.*

Les [points techniques vérifiés](SOURCE-REVIEW.md) expliquent les ajustements restants. Les anciens manifestes et images du 7 septembre, dans les dossiers voisins, restent un historique de préparation : **ne pas les copier pour ces deux nouvelles soumissions**. Le dossier Hotbar Atelier reste hors de cette relecture.

La [politique IA de Dalamud](https://dalamud.dev/plugin-publishing/ai-policy/) demande de déclarer l'aide reçue, de tester personnellement le plugin et de pouvoir expliquer les choix de code. La rédaction du brouillon ne suffit pas à attester cette compréhension.
