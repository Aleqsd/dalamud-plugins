# Maintenance

Ce dépôt distribue des archives adaptées à l'installateur Dalamud. Les DLL restent identiques aux releases des trois dépôts sources. Les licences des plugins sont conservées ; le catalogue, ses scripts et ses icônes originales sont sous MIT.

## Préparer une version

Prérequis : Python 3.10+, Git et `gh` connecté à Aleqsd. Aucun workflow GitHub Actions.

1. Partir d'une release publiée et vérifiée du plugin. Relever son commit, son nom d'archive et son SHA256 via `gh api`. Épingler aussi le SHA256 de la DLL transmis par la tâche propriétaire et le vérifier dans l'archive téléchargée. Si une DLL est publiée comme asset séparé, son empreinte GitHub doit également correspondre ; cet asset est facultatif.
2. Actualiser son entrée dans `sources.json` : tag, commit, hashes, fichiers nécessaires, aperçu et changelog court. `installationNote`, si présente, complète la description du catalogue avec les prérequis de cette version. Ne pas retirer une dépendance de runtime requise. Garder les mêmes `InternalName`.
3. Choisir un nouveau `packageRelease` unique (par exemple `catalogue-2026-09-08-1`). Ne pas écraser les archives déjà publiées.
4. Exécuter :

```powershell
python -m unittest discover -s tests
python tools/build_repo.py
```

Le script contrôle le tag/commit, les empreintes GitHub, le contenu des archives, les versions et la palette d'icônes. Il ne compile ni ne charge les DLL. Les fichiers candidats sont dans `.artifacts/<packageRelease>/`. Le `repo.json` public n'est pas modifié à ce stade.

Examiner aussi la version d'assembly de chaque DLL avec `System.Reflection.AssemblyName.GetAssemblyName` et la comparer au manifeste. Vérifier les besoins externes, notamment le relais Codex Monitor. Un changement de DLL doit avoir une version supérieure : un autre fichier sous le même numéro n'est pas une mise à jour détectable.

## Publier dans le bon ordre

1. Vérifier l'identité `gh api user --jq .login`, la branche `main`, le remote et les seuls fichiers à committer.
2. Committer/pousser les sources, scripts, docs et icônes validés. Conserver le catalogue précédent jusqu'à ce que les nouvelles archives existent.
3. Créer le tag de catalogue sur ce commit exact et une release contenant les ZIP préparés, `SHA256SUMS.txt` et `catalogue.lock.json`. Préparer les notes dans un fichier, puis utiliser `gh release create ... --notes-file ...`. Marquer les versions expérimentales comme prérelease. Aucune pièce jointe venant des caches ou du poste.
4. Lancer `python tools/build_repo.py --verify-public`. Ce contrôle télécharge les ZIP, vérifie les hashes, identités, versions, icônes et aperçus publics.
5. Copier les candidats `repo.json` et `catalogue.lock.json` à la racine. Les relire, committer et pousser uniquement ces changements.
6. Lancer `python tools/build_repo.py --verify-index` pour comparer l'URL publique à la version validée.

Le client Dalamud utilise l'URL JSON, les versions et les liens d'archives. La distinction prérelease GitHub est indépendante du canal de ce dépôt personnalisé : les entrées restent installables normalement ici et sont décrites comme expérimentales. Ne pas activer le mode développeur ou forcer une compatibilité pour contourner une erreur.

## Coordination

Chaque tâche de plugin garde son dépôt et transmet sa nouvelle release à la tâche de publication du catalogue. Une seule tâche met à jour ce dépôt à la fois. Publier une release de plugin n'actualise pas automatiquement ce JSON.

Hotbar Atelier et Codex Monitor livrent actuellement leur DLL sous `plugin/` ; le script la place à la racine du ZIP d'installation. Codex Monitor embarque son relais dans sa DLL : la 0.10.0 contient cinq scripts (`bridge.mjs`, `observer.mjs`, `questions.mjs`, `usage.mjs`, `files.mjs`), sans fichier de relais supplémentaire dans le ZIP installateur. Vérifier que chaque ressource correspond aux sources de la release, y compris les nouveaux modules.

Le plugin extrait les scripts et crée les données d'exécution sous son dossier de configuration lors du lancement manuel depuis **Connexion**, ou du lancement automatique après connexion au personnage si l'utilisateur a activé cette option. Elle est désactivée par défaut. Node.js 22.22.2 minimum et le CLI Codex restent externes. Le plugin ne gère l'arrêt que du relais qu'il a créé ; un relais externe préexistant est conservé et se met à jour séparément si nécessaire. Une mise à jour apporte les nouveaux scripts pour le prochain lancement du relais intégré. Pour un autre schéma d'archive, adapter explicitement les fichiers autorisés.

La 0.10.0 nécessite aussi son nouveau relais pour le modèle, l'effort et l'indicateur de réponse non lue. Mentionner sa relance dans le catalogue et les notes de release : depuis **Connexion** pour le relais intégré, depuis son dossier après mise à jour pour un relais externe. Le packaging ne doit pas arrêter ni remplacer une instance active.

## Vérifications de référence

Le format est fondé sur les [métadonnées Dalamud](https://dalamud.dev/plugin-development/plugin-metadata/), [PluginRepository](https://github.com/goatcorp/Dalamud/blob/master/Dalamud/Plugin/Internal/Types/PluginRepository.cs), [PluginManager](https://github.com/goatcorp/Dalamud/blob/master/Dalamud/Plugin/Internal/PluginManager.cs) et [LocalPluginManifest](https://github.com/goatcorp/Dalamud/blob/master/Dalamud/Plugin/Internal/Types/Manifest/LocalPluginManifest.cs).

Le contrôle hors jeu reproduit les invariants de packaging utiles : DLL et JSON à la racine, identité/version cohérentes, manifestes sans état local, licences et icônes disponibles. Une lecture HTTP et une archive valide ne prouvent pas le chargement en jeu.

## Icônes

Les trois SVG de `icons/` sont les sources des PNG 256 × 256. Pour les régénérer avec ImageMagick :

```powershell
magick -background none icons/HotbarAtelier.svg -strip -depth 8 -define png:color-type=6 icons/HotbarAtelier.png
```

Conserver une silhouette lisible à petite taille, une palette commune et un dessin original. Les captures LMeter et les assets du jeu ne sont pas redistribués.
