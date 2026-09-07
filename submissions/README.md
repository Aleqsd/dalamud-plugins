# Préparer les soumissions Dalamud

Les trois dossiers sont préparés pour le catalogue officiel. Ils contiennent les textes des PR, les icônes et les fichiers à ajouter à `testing/live`. Rien n'a encore été envoyé à l'équipe Dalamud.

| Plugin | Texte de la PR | Avis préalable |
| --- | --- | --- |
| Hotbar Atelier | [Lire le brouillon](HotbarAtelier/pr-body.md) | [Présenter les changements des barres](HotbarAtelier/precheck-message.md) |
| Codex Monitor | [Lire le brouillon](CodexMonitor/pr-body.md) | [Expliquer le relais séparé](CodexMonitor/precheck-message.md) |
| Minimap Zoom | [Lire le brouillon](MinimapZoom/pr-body.md) | [Vérifier l'acceptabilité du dézoom](MinimapZoom/precheck-message.md) |

Les messages sont en anglais pour les reviewers. Ils expliquent simplement que Codex a écrit une grande partie du code, et que j'ai choisi les fonctionnalités, testé les plugins en jeu et guidé les améliorations. Le niveau **Auto** décrit les passes autonomes de programmation, accompagnées de ma direction produit et de mes essais. Les icônes pourront être refaites à la main si nécessaire 🙂

Les essais en jeu déclarés par Aleqsd concernent le développement des plugins. La préparation ajoute des métadonnées, ajuste la compilation et inclut le démarrage discret des réglages de Hotbar Atelier 0.5.2 ; elle ne prouve pas que ces nouveaux builds ont déjà été essayés en jeu. Les [notes de vérification](VERIFICATION.md) séparent ces étapes.

Le dossier **Codex Monitor reste basé sur la 0.6.1**, avec son relais séparé. Les versions suivantes du catalogue personnalisé ajoutent notamment le lancement du relais depuis le plugin, les emojis colorés et l'ouverture des tâches dans Codex ; ces fonctions ne sont pas couvertes par le brouillon officiel actuel.

Le dossier **Minimap Zoom reste basé sur la 0.4.1**, avec sa préparation du build D17. Les profils, raccourcis et autres nouveautés des versions suivantes du catalogue personnalisé ne sont pas inclus dans ce brouillon.

Pour soumettre, utiliser un fork de [DalamudPluginsD17](https://github.com/goatcorp/DalamudPluginsD17), puis **une branche et une PR par plugin**. Copier uniquement le sous-dossier `testing/` du dossier concerné, utiliser son titre et son texte de PR, puis laisser Plogon compiler le commit public indiqué dans le manifeste. Les brouillons et notes de ce dossier n'ont pas à être copiés dans D17. [Procédure officielle](https://dalamud.dev/plugin-publishing/submission/).

Avant l'envoi : obtenir l'avis utile sur les fonctions natives et le relais, terminer l'essai ciblé du build retenu et pouvoir expliquer les choix de code. Le message Codex est une consultation utile, pas une formalité imposée identifiée. Le ciblage Tab reste exclu. L'acceptation dépend de l'équipe Dalamud ; le dépôt personnalisé continue de fonctionner séparément.

Les [notes de vérification](VERIFICATION.md) donnent les commits et les points à terminer. La [provenance des images](ASSETS.md) distingue captures en jeu, rendus ImGui et ressources créées avec Codex. `python submissions/prepare.py --check`, depuis la racine du catalogue, revérifie les fichiers contre leurs sources publiques ; cette commande ne publie rien.

Références consultées le 7 septembre 2026 : [compilation D17](https://github.com/goatcorp/DalamudPluginsD17#preparing-your-repository), [restrictions](https://dalamud.dev/plugin-publishing/restrictions/), [politique IA et assets](https://dalamud.dev/plugin-publishing/ai-policy/).
