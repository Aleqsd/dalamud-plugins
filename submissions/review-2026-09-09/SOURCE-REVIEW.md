# Sources et préparation technique

Vérification du 9 septembre 2026, en lecture seule sur les dépôts des plugins. Cette passe n'a compilé, chargé ni publié de nouvelle DLL. Les validations ci-dessous sont celles documentées par les tâches propriétaires, pas de nouveaux essais.

| Plugin | Dernière release et source publique | Ancien commit du dossier D17 |
| --- | --- | --- |
| Codex Monitor | 0.11.1 — [8636098](https://github.com/Aleqsd/codex-monitor/commit/8636098bb42abfc817935bcd75144cb463aea8e7) | 0.6.1 — `7958d1930ae9dbd4200d7c26a5ecd889643c8a8f` |
| Minimap Zoom | 0.5.1 — [df96f63](https://github.com/Aleqsd/minimap-zoom/commit/df96f63db7423248f8a6d506fccb8c2eef6a379b) | 0.4.1 — `4c26d7f5edd7cec4505559ef151a9ad21681cf90` |

Les tags et les branches publiques `main` résolvent vers les commits de la colonne centrale. Les deux noms sont absents de `stable/` et `testing/live/` au commit D17 [0b906df](https://github.com/goatcorp/DalamudPluginsD17/commit/0b906dfe65ddd5e866440a7344dcb918edb4df1c), arbre complet vérifié. Aucune PR d'Aleqsd n'a été trouvée dans D17. Ces états sont à relire au moment de l'envoi.

## Codex Monitor

- Le [projet actuel](https://github.com/Aleqsd/codex-monitor/blob/8636098bb42abfc817935bcd75144cb463aea8e7/src/CodexMonitor.csproj) utilise déjà `Dalamud.NET.Sdk/15.0.0`, un lockfile committé et `Version.props`. Les cinq scripts du relais sont embarqués ; TerraFX est une dépendance de l'hôte, sans copie dans le paquet.
- La description du projet ne mentionne plus l'icône et les sons créés avec Codex. Reporter cette déclaration de l'ancienne préparation, ainsi que `RepoUrl` et `IconUrl`, dans une nouvelle préparation issue de 0.11.1. La déclaration dans la PR ne remplace pas celle des assets dans la description visible du plugin.
- Le relais écoute sur loopback et accepte les lectures `/health` et `/api/threads`, avec contrôles Host/Origin. Le plugin peut le lancer manuellement ; l'automatisme reste désactivé par défaut. Un relais externe existant reste indépendant. Node.js et le CLI ne sont pas distribués par Dalamud.
- Les questions structurées peuvent fournir un extrait borné à 240 caractères. Le texte facultatif reste local et est retiré de l'historique sauvegardé. Ne plus écrire que tout texte de conversation est absent du jeu : décrire précisément cette exception. Le flux IPC interne complet existe avant projection.
- Les [validations de la release](https://github.com/Aleqsd/codex-monitor/blob/8636098bb42abfc817935bcd75144cb463aea8e7/docs/VALIDATION.md) rapportent un build et 796 contrôles ImGui / 127 rendus. Elles n'attestent pas le chargement de cette DLL dans FFXIV. La nouvelle préparation devra vérifier les métadonnées générées, puis être essayée personnellement avec les HUD, les notifications et le relais.
- Une consultation préalable sur le relais peut aider les reviewers ; aucune obligation spécifique de consultation pour ce type de moniteur n'a été identifiée dans les règles relues.

## Minimap Zoom

- Le [projet actuel](https://github.com/Aleqsd/minimap-zoom/blob/df96f63db7423248f8a6d506fccb8c2eef6a379b/src/MinimapZoom.csproj) utilise `Microsoft.NET.Sdk` et des références locales via `DalamudHome`, sans DalamudPackager. Le lockfile existe mais ne suffit pas à adapter le build à Plogon. Reporter la migration D17 de l'ancienne préparation sur la 0.5.1, avec restauration verrouillée et vérification du paquet, sans utiliser le script local qui remplace la DLL surveillée par le jeu.
- La [description du manifeste](https://github.com/Aleqsd/minimap-zoom/blob/df96f63db7423248f8a6d506fccb8c2eef6a379b/src/MinimapZoom.json) déclare déjà l'icône, le masque et les cadres créés avec Codex. Conserver cette déclaration.
- [ZoomPolicy](https://github.com/Aleqsd/minimap-zoom/blob/df96f63db7423248f8a6d506fccb8c2eef6a379b/src/ZoomPolicy.cs) permet 0.25–2 contre 0.5–2 en natif. [NativeMarkerRange](https://github.com/Aleqsd/minimap-zoom/blob/df96f63db7423248f8a6d506fccb8c2eef6a379b/src/NativeMarkerRange.cs) étend la collecte pendant la mise à jour de la mini-carte et restaure le scope. Il n'existe pas de garde PvP ou de liste blanche pour cette collecte. Les filtres d'apparence ne constituent pas une telle garde. Ne pas prétendre que les données déjà présentes côté client excluent un avantage en combat.
- La 0.5.1 adapte la compatibilité au client `2026.09.01.0000.0000`. Les [validations publiées](https://github.com/Aleqsd/minimap-zoom/blob/df96f63db7423248f8a6d506fccb8c2eef6a379b/docs/validation.md) rapportent 70 contrôles hors jeu et 36 scénarios ImGui ; elles réservent explicitement l'essai en jeu. La capture native disponible est celle de la 0.4.1. L'image publique `settings-map.png` conserve le titre 0.5.0 : c'est un aperçu de cette interface, pas une preuve du chargement de 0.5.1.
- Demander l'avis sur le périmètre avant de soumettre. Si les mainteneurs demandent une garde PvP ou un zoom limité, ce sera un changement fonctionnel à décider et tester, pas une simple retouche du texte de PR.

## Fichiers de la future PR

Chaque PR sera dans sa propre branche du fork D17 et contiendra `testing/live/<InternalName>/manifest.toml`, `images/icon.png`, puis les aperçus retenus. Le manifeste utilisera `owners = ["Aleqsd"]`, `project_path = "src"` et le **nouveau commit public final** après les ajustements ci-dessus. Les commits de release relus ici identifient le périmètre ; ils ne sont pas présentés comme des candidats déjà prêts à compiler dans D17.

Les icônes actuelles sont des SVG originaux écrits avec Codex puis rasterisés en PNG 256 × 256, sous MIT. Elles ne sont pas faites à la main. Aleqsd propose de les remplacer manuellement si demandé. Pour les aperçus, privilégier les vues actuelles ; une capture plus ancienne garde sa version en légende.

Références relues : [soumission](https://dalamud.dev/plugin-publishing/submission/), [préparation du build](https://github.com/goatcorp/DalamudPluginsD17#preparing-your-repository), [restrictions](https://dalamud.dev/plugin-publishing/restrictions/), [politique IA](https://dalamud.dev/plugin-publishing/ai-policy/).
