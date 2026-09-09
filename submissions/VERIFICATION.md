# Vérifications — 9 septembre 2026

[Sources exactes, builds et empreintes actuels](review-2026-09-09/SOURCE-REVIEW.md).

| Plugin | État vérifié |
| --- | --- |
| Codex Monitor 0.11.1 | Build local et archive vérifiés ; PR #9330 ouverte, lint-manifest réussi. |
| Minimap Zoom 0.5.1 | Build local et archive vérifiés ; PR #9331 ouverte, lint-manifest réussi. |
| Hotbar Atelier 0.5.2 | Ancienne préparation du 7 septembre, hors de cet envoi. |

Aleqsd confirme avoir testé Codex Monitor 0.11.1 et Minimap Zoom 0.5.1 avec la dernière mise à jour de FFXIV : ils fonctionnent. Les adaptations de soumission ne changent pas leur code de fonctionnement. Le chargement séparé des builds de préparation et la compilation officielle Plogon ne sont pas encore attestés.

Les sources publiques, déclarations d'assets, manifestes TOML et 12 PNG ont été vérifiés. Les icônes sont carrées, 256 × 256. Les versions des captures Minimap restent explicites dans assets.json. Le catalogue personnalisé, les releases et les DLL installées sont indépendants de ces soumissions.

## Historique Hotbar Atelier

La préparation conserve le commit [5a662db](https://github.com/Aleqsd/hotbar-atelier/commit/5a662db413320e5e0e327f3823c937ed08c2f54a), version 0.5.2.0. Le rapport du 7 septembre documente clone public, caches neufs, restauration verrouillée, Release et 74 contrôles réussis. DLL locale : `B02B7F2829196D74DEE64F17691E89F35277CD65AD749EC15C6C679A5AF8041D`. Ces preuves ne sont pas de nouveaux essais en jeu et ce dossier n'a pas été soumis dans cette passe.
