# NDEMBO KIN CRM — Notes de build

## Brief
MVP web mobile-first pour **Ndembo Kin Connect SARL** (agence de management sportif, Kinshasa, RDC).
Outil quotidien équipe métier, inspiré Odoo mais plus léger/élégant/sportif.
FR uniquement · USD · dates jj/mm/aaaa · TVA 25% optionnelle · paiements Orange Money, M-Pesa, Airtel Money, banque, espèces.

## Choix utilisateur (questions_v2, m0003)
- **Palette : 100% logo Ndembo Kin** (ardoise #44707F, cyan #45C0E8, rouge #E8262C, jaune #FFCE2B) — choix EXPLICITE qui prime sur le DS "La Victoire" (or/navy) pourtant bound sous _ds/. Ne pas utiliser La Victoire pour les couleurs/typo.
- Logo PNG fourni → recadré : `assets/logo-lockup.png|-t.png` (lockup), `assets/logo-mark.png|-t.png` (emblème seul, -t = fond transparent).
- Tout le reste « Decide for me ». Données démo congolaises fictives réalistes (AS Vita, TP Mazembe…).
- Services / avantages VIP : tirés de ndembokin.com (management carrière, événementiel/tournois élite/hospitalité VIP/stages, conseil juridique FIFA-CAS, Kinshasa Héritage, Elite Club VIP).

## Mes décisions
- 1 version solide. Fond clair + sidebar ardoise sombre. Desktop sidebar / mobile bottom-tabs (Accueil, Projets, Sportifs, Docs, Plus→sheet).
- Projets : kanban (Brouillon→En cours→En attente→Validé→Terminé) + switch liste.
- Police : Archivo (Google Fonts). Pas d'emoji.
- Fichier : `Ndembo Kin Connect.dc.html` — app complète avec écrans :
  dashboard, projets(+drawer détail), sportifs(+fiche), partenaires, devis&factures(+éditeur+aperçu A4), membres VIP(carte NFC visuelle+avantages), précontrat (assistant 5 étapes+aperçu A4), rapports, paramètres, espaces Partenaire & Sportif (switch de rôle dans le header).
- Carte VIP NFC = 100 USD. Statuts carte : actif/attente/expiré/préinscrit.
- Statuts docs : brouillon/envoyé/accepté/payé/annulé ; devis→facture en 1 clic.
- Admin démo : Christelle Makiese. Date du jour : 11/06/2026.

## Prochaines étapes possibles (post-MVP)
- Vrais PDF imprimables, export PPTX/CSV réels, intégration NFC/QR, backend Laravel (specs dans uploads/gemini-code-…txt).
