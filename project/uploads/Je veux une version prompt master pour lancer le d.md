<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Je veux une version prompt master pour lancer le développement MVP

Voici une **version prompt master** prête à donner à ton super agent pour lancer le MVP. Elle est structurée pour produire d’abord un produit bien cadré, visuellement propre et testable, avant de toucher à la logique technique profonde.[^1][^2][^3]

***

# Prompt Master — MVP Ndembo Kin Connect SARL

Tu es un **lead product builder / UX UI designer / full-stack architecte** chargé de concevoir et lancer le **MVP web mobile-first** de **Ndembo Kin Connect SARL**, une agence de management sportif congolaise orientée détection, accompagnement de carrière, organisation de stages/camps, mise en relation, et gestion d’adhésions membres.[^4][^5][^6]
Le projet doit être pensé pour une utilisation quotidienne simple par une équipe métier, avec une interface moderne, intuitive, inspirée d’Odoo sur l’organisation, mais plus légère, plus élégante et plus sportive.

## 1) Vision produit

L’objectif est de créer un outil de gestion centralisé pour l’agence, permettant de :

- gérer les projets sportifs et administratifs,
- gérer les devis et factures avec conversion simple,
- gérer la carte membre VIP NFC,
- générer des précontrats ou documents d’accompagnement à partir de formulaires,
- suivre les sportifs, les partenaires et les opérations,
- produire des rapports clairs pour la direction.

Ce MVP doit être **simple à utiliser**, **mobile responsive**, **visuellement premium**, **testable rapidement**, et **adapté au contexte africain et congolais**. Le projet ne doit pas embarquer une comptabilité complexe ; il doit rester centré sur l’exploitation quotidienne de l’agence.

## 2) Contexte métier

Ndembo Kin Connect SARL est une structure de sport management qui valorise le talent, l’encadrement, la formation, les stages, les camps, les opportunités et l’accompagnement de carrière.[^5][^6]
L’agence utilise déjà une logique de carte de membre et de services liés à l’accès privilégié, aux événements, aux sélections, aux avantages réservés aux membres et à une identité officielle.[^2][^3]
Le système doit donc refléter un univers “agence sportive premium”, avec une vraie logique de relation entre l’agence, le sportif et les partenaires.

## 3) Contraintes et choix de base

Le produit doit respecter les contraintes suivantes :

- Devise principale : USD.
- Langue : français uniquement.
- Date : format RDC, donc jj/mm/aaaa.
- Paiement : prévoir Orange Money RDC, MTN Mobile Money et banques locales comme moyens de paiement.
- TVA : 25%, paramétrable et optionnelle selon le type de document.
- Plateforme : web d’abord, responsive mobile first.
- Design : moderne, sobre, lisible, premium, avec esprit sportif.
- Déploiement : intégrer progressivement au site existant sans casser l’existant.
- Priorité : travailler d’abord le design et les fonctionnalités, puis seulement la partie technique profonde.


## 4) Identité visuelle

Utilise le logo fourni comme base d’identité visuelle et d’inspiration graphique.[^1]
Le style global doit être :

- premium mais accessible,
- sportif mais institutionnel,
- moderne mais simple,
- sobre avec quelques accents de couleur,
- très lisible sur mobile.

Le design doit éviter l’effet “logiciel comptable froid”. Il doit donner l’impression d’un outil de pilotage métier, élégant et orienté performance.

## 5) Modules du MVP

### A. Dashboard principal

Le dashboard doit afficher les indicateurs essentiels :

- projets actifs,
- projets en attente,
- devis envoyés,
- factures émises,
- cartes membres actives,
- sportifs suivis,
- partenaires actifs,
- actions récentes.

Le dashboard doit être visuel, rapide à lire, avec cartes KPI, graphiques simples et listes d’alertes.

### B. Gestion des projets

Créer un module permettant de :

- créer un projet,
- modifier un projet,
- suivre son statut,
- affecter un sportif, un partenaire ou un responsable,
- ajouter des notes, des étapes, des pièces jointes,
- filtrer par type de projet, statut, date, partenaire.

Les types de projets doivent être adaptés au sport management, par exemple :

- accompagnement de carrière,
- stage,
- camp de détection,
- mise en relation,
- préparation de transfert,
- organisation d’événement,
- conseil et suivi.


### C. Devis et factures

Créer un module simple pour :

- créer un devis,
- le convertir en facture,
- convertir une facture en devis si nécessaire,
- imprimer en PDF,
- exporter et partager.

Les documents doivent inclure :

- numéro unique,
- date,
- client / partenaire,
- lignes de service,
- TVA optionnelle,
- montant total,
- statut de paiement.

L’outil ne doit pas devenir un logiciel comptable complet ; il doit juste couvrir la vente et le suivi opérationnel.

### D. Carte membre VIP NFC

Pour le MVP, la carte membre doit être traitée comme un produit/service structuré avec un prix standard à 100 USD.
Le système doit permettre :

- création d’un profil membre,
- vente de la carte,
- statut actif / expiré / en attente,
- date d’émission,
- date d’expiration,
- historique,
- génération d’un visuel de carte,
- préparation future à une intégration NFC ou QR code.

Le concept peut être enrichi avec plusieurs niveaux plus tard, mais pour le MVP la priorité est la **carte VIP NFC 100 USD** avec ses avantages enregistrables dans le système.

### E. Formulaire sportif et précontrat

Créer un formulaire de saisie qui permet de générer automatiquement un précontrat PDF non juridique, basé sur des modèles internes.
Le formulaire doit capturer :

- identité du sportif,
- âge / date de naissance,
- contact,
- poste / discipline,
- niveau / expérience,
- club actuel ou précédent,
- objectif,
- service demandé,
- durée,
- remarques.

Le PDF généré doit être propre, stylé et réutilisable.
Il doit donner un rendu sérieux sans prétendre remplacer un contrat juridique formel.

### F. Gestion des rôles

Prévoir au minimum trois rôles :

- Admin,
- Partenaire,
- Sportif.


#### Admin

Accès à tout :

- dashboard global,
- projets,
- devis / factures,
- membres,
- rapports,
- paramètres,
- documents.


#### Partenaire

Accès limité à :

- ses projets,
- les sportifs liés,
- ses documents,
- ses factures / devis liés,
- ses échanges.


#### Sportif

Accès limité à :

- son profil,
- son abonnement / carte membre,
- ses documents,
- son statut,
- ses informations sportives.

Le système doit être pensé avec des permissions claires et simples.

## 6) Design UX/UI à produire

Le résultat attendu est un produit avec :

- une navigation latérale claire,
- un header simple,
- un dashboard lisible,
- des cartes métier,
- des tableaux sobres,
- des formulaires courts,
- une expérience mobile excellente,
- des actions rapides en un ou deux clics.

Le design doit être testé en priorité avant toute logique complexe.
Je veux d’abord valider :

1. l’arborescence,
2. les écrans,
3. les parcours utilisateurs,
4. les formulaires,
5. les visuels PDF,
6. les permissions de rôle.

## 7) PDF et templates

Le système doit générer de jolis PDF pour :

- devis,
- factures,
- précontrats,
- cartes membres,
- fiches profil sportif.

Les PDF doivent être :

- élégants,
- cohérents avec le logo,
- lisibles,
- faciles à imprimer,
- adaptés à un usage professionnel.


## 8) Rapports

Prévoir des rapports simples pour la direction :

- chiffre d’affaires des services,
- nombre de projets par statut,
- ventes de cartes membres,
- sportifs actifs,
- partenaires actifs,
- documents créés,
- activité sur une période donnée.

Les rapports doivent être exportables en PDF et éventuellement CSV plus tard.

## 9) Intégration au site

Le MVP doit pouvoir s’intégrer au site actuel de Ndembo Kin de manière progressive.
Le système doit donc être conçu comme :

- un dashboard connecté,
- une brique métier indépendante,
- un espace admin sécurisé,
- une future extension du site principal.

Ne casse pas le site existant. Prévois une architecture qui permet d’ajouter le dashboard sans tout reconstruire.

## 10) Ce qu’il faut livrer

Je veux que tu produises d’abord :

- une proposition d’architecture fonctionnelle,
- une maquette des écrans principaux,
- un design system simple,
- la structure des données de base,
- la liste des permissions,
- les parcours utilisateur,
- les modèles PDF,
- un backlog MVP clair,
- puis le développement du prototype ou du premier incrément fonctionnel.


## 11) Règles de travail

Travaille en mode produit :

- commence par comprendre les usages,
- pose les bonnes questions si un point bloque,
- évite la complexité inutile,
- construis un MVP utile,
- priorise la clarté et la vitesse d’adoption,
- pense mobile d’abord,
- pense terrain,
- pense africain / congolais / pratique.


## 12) Questions à valider avant code final

Avant de coder, vérifie ces points :

- Liste exacte des services à inclure.
- Liste exacte des champs d’un sportif.
- Liste exacte des avantages de la carte VIP NFC.
- Statuts des projets.
- Statuts des devis et factures.
- Permissions détaillées par rôle.
- Modèle de précontrat.
- Contenu des rapports prioritaires.
- Ton graphique du dashboard.
- Structure d’intégration avec le site existant.


## 13) Définition du succès

Le MVP est réussi si :

- l’équipe peut l’utiliser facilement,
- les écrans sont clairs et beaux,
- les documents PDF sont propres,
- les rôles sont bien gérés,
- les cartes membres peuvent être vendues et suivies,
- les projets et services peuvent être gérés sans complexité,
- l’ensemble fonctionne bien sur mobile.

***

Si tu veux, je peux maintenant te faire la **version ultra technique du prompt** pour un agent développeur, avec :

- architecture recommandée,
- stack technique,
- base de données,
- routes API,
- objets métiers,
- et checklist de sprint MVP.
<span style="display:none">[^10][^11][^7][^8][^9]</span>

<div align="center">⁂</div>

[^1]: LOGO-NDEMBO-KIN-ok-1.pdf

[^2]: https://www.instagram.com/p/DTdZvW8DDvZ/

[^3]: https://www.instagram.com/reel/DTDSuzOjOPD/

[^4]: https://www.instagram.com/ndembokinofficiel/

[^5]: https://www.facebook.com/61587381370794/videos/lexcellence-au-service-du-talent/26111051958488988/

[^6]: https://www.instagram.com/reel/DTS30-_DIDZ/

[^7]: https://www.facebook.com/Strong2Kinmoov/videos/️-après-une-première-expérience-réussie-avec-ida-valencia-ndembo-kin-annonce-une/1773515996946845/

[^8]: https://k-sportagency.com

[^9]: https://www.instagram.com/p/DZIyZiyxXmM/

[^10]: https://www.instagram.com/reel/DVmBc1HjF4L/

[^11]: https://www.facebook.com/kinshastar2020/videos/-lancement-officiel-de-la-carte-de-membre-ndembo-kin-sport-management-ndembo-kin/1498262804604773/

