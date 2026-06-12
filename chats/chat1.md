# Ndembo Kin Connect MVP

_Started 2026-06-10 23:44 UTC_

---

## User

Tu es un lead product builder / UX UI designer / full-stack architecte chargé de concevoir et lancer le MVP web mobile-first de Ndembo Kin Connect SARL, une agence de management sportif congolaise orientée détection, accompagnement de carrière, organisation de stages/camps, mise en relation, et gestion d’adhésions membres.

Le projet doit être pensé pour une utilisation quotidienne simple par une équipe métier, avec une interface moderne, intuitive, inspirée d’Odoo sur l’organisation, mais plus légère, plus élégante et plus sportive.

## Assistant

_[tool: list_files]_

_[tool: read_file]_

_[tool: read_file]_

_[tool: read_file]_

_[tool: read_file]_

_[tool: list_files]_

_[tool: list_files]_

_[tool: read_skill_prompt]_

_[tool: list_files]_

_[tool: run_script]_

_[tool: copy_files]_

_[tool: run_script]_

_[tool: run_script]_

_[tool: run_script]_

_[tool: run_script]_

_[tool: write_file]_

_[tool: show_html]_

_[tool: show_html]_

_[tool: sleep]_

_[tool: save_screenshot]_

_[tool: get_webview_logs]_

_[tool: str_replace_edit]_

_[tool: show_html]_

_[tool: sleep]_

_[tool: save_screenshot]_

_[tool: sleep]_

_[tool: save_screenshot]_

_[tool: run_script]_

_[tool: run_script]_

_[tool: run_script]_

_[tool: run_script]_

_[tool: run_script]_

_[tool: run_script]_

_[tool: save_screenshot]_

_[tool: questions_v2]_

## User

Questions answered:
- palette: 100% palette du logo Ndembo Kin (bleu ardoise, cyan, rouge, jaune)
- logo_png: uploads/logo_png-1781137527218.png
- scope: Decide for me
- roles: Decide for me
- variations: Decide for me
- ambiance: Decide for me
- nav_mobile: Decide for me
- projets_vue: Decide for me
- services: cherche sur le site ndembokin.com
- avantages_vip: cherche sur le site ndembokin.com ou propose
- demo_data: Oui, noms/clubs congolais réalistes fictifs (FC Renaissance, AS Vita…)

## Assistant

_[tool: list_files]_

_[tool: view_image]_

_[tool: image_metadata]_

_[tool: read_file]_

_[tool: read_file]_

_[tool: read_file]_

_[tool: read_file]_

_[tool: web_fetch]_

_[tool: update_todos]_

_[tool: run_script]_

_[tool: web_fetch]_

_[tool: view_image]_

_[tool: run_script]_

_[tool: dc_write]_

Logo prêt. Je construis maintenant l'application complète.

_[tool: write_file]_

_[tool: snip]_

_[tool: dc_write]_

Maintenant le gros morceau : l'application complète en un Design Component.

## User

continue

## Assistant

_[tool: dc_write]_

Je reprends — j'écris l'application en plusieurs passes (coquille + dashboard d'abord, puis chaque module).

_[tool: dc_html_str_replace]_

_[tool: dc_html_str_replace]_

_[tool: dc_html_str_replace]_

_[tool: dc_html_str_replace]_

_[tool: dc_html_str_replace]_

_[tool: dc_html_str_replace]_

_[tool: dc_html_str_replace]_

_[tool: dc_html_str_replace]_

_[tool: dc_html_str_replace]_

_[tool: done]_

Petite correction dans le drawer projet, puis vérification.

_[tool: fork_verifier_agent]_

Le MVP **Ndembo Kin Connect** est en ligne dans l'aperçu — application complète, mobile-first, palette 100 % logo (ardoise, cyan, rouge, jaune), typographie Archivo.

**Ce qui est cliquable :**
- **Dashboard** : KPI, actions rapides, projets en cours, abonnements à renouveler (bouton fonctionnel), activité
- **Projets** : kanban ↔ liste, filtres par type, drawer détail avec avancement de statut et annulation
- **Sportifs** : registre + fiche complète (infos, carte VIP, projets, documents, notes internes ajoutables)
- **Devis & Factures** : liste filtrée, éditeur (client, lignes de service, TVA 25 % optionnelle), **conversion devis→facture en 1 clic**, marquage payé, aperçu A4 avec le logo
- **Membres VIP** : carte NFC Elite Club visuelle (100 $), avantages, registre avec vente/renouvellement
- **Précontrat** : assistant 5 étapes avec aperçu PDF stylé et signatures
- **Rapports, Paramètres** (tarifs éditables, TVA, paiements RDC), **espaces Partenaire et Sportif** via le menu avatar en haut à droite
- Sur mobile (<920 px) : barre d'onglets en bas + sheet « Plus »

**Caveats :**
- Le design system « La Victoire » (or/navy) attaché au projet n'a volontairement **pas** été utilisé — vous aviez choisi la palette du logo Ndembo Kin ; dites-moi si vous voulez une variante La Victoire.
- Les prix des services sont des propositions à valider (modifiables dans Paramètres) ; les exports PDF/CSV sont simulés (toasts) — je peux brancher de vrais PDF imprimables ensuite.

**Prochaines étapes possibles :** vrais PDF imprimables, écran de connexion, version sombre, ou handoff technique Laravel.

## User

Check didn’t complete

## Assistant



