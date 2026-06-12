<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Peux-tu me donner des exemples de wireframes pour ce dashboard

Oui. Je peux te proposer des **wireframes concrets** pour le dashboard Ndembo Kin, pensés pour un usage web mobile-first, avec une logique simple, sportive et premium. Je te donne ci-dessous plusieurs écrans types, organisés comme un vrai produit MVP, en tenant compte du logo et de l’identité visuelle fournie.[^1]

## 1) Écran d’accueil admin

C’est le cœur du système. Il doit permettre à l’admin de voir l’activité en un coup d’œil et d’aller vite vers les actions principales.

```text
┌──────────────────────────────────────────────────────┐
│ Ndembo Kin Connect SARL     🔍 Recherche   🔔   👤   │
├───────────────┬──────────────────────────────────────┤
│ Dashboard     │  Bonjour, Admin                      │
│ Projets       │  ┌──────┬──────┬──────┬──────┐        │
│ Sportifs      │  │ Proj │ Dev. │ Fact.│ Mbrs │        │
│ Partenaires   │  │  12  │  8   │  5   │  64  │        │
│ Devis         │  └──────┴──────┴──────┴──────┘        │
│ Factures      │  Actions rapides                      │
│ Membres VIP   │  [ + Projet ] [ + Devis ] [ + Carte ] │
│ Rapports      │                                        │
│ Paramètres    │  Projets récents                      │
│               │  ┌────────────────────────────────┐   │
│               │  │ Projet A   En cours   Voir →   │   │
│               │  │ Projet B   En attente Voir →   │   │
│               │  └────────────────────────────────┘   │
│               │  Statistiques / Graphique             │
└───────────────┴──────────────────────────────────────┘
```


### Ce que ce wireframe doit contenir

- Les KPI principaux.
- Des boutons d’action immédiats.
- Les projets récents.
- Les alertes prioritaires.
- Un mini graphique ou une vue activité.


## 2) Écran projets

Cet écran doit ressembler à un pipeline simple, pas à un tableau administratif lourd. L’idée est de suivre le projet de la création jusqu’à la clôture.

```text
┌──────────────────────────────────────────────────────┐
│ Projets                             + Nouveau projet │
├─────────────┬─────────────┬─────────────┬────────────┤
│ Brouillon   │ En cours    │ En attente  │ Terminé    │
│ ─────────   │ ─────────   │ ─────────   │ ─────────  │
│ Projet A    │ Projet B    │ Projet C    │ Projet D   │
│ Projet E    │ Projet F    │             │            │
└─────────────┴─────────────┴─────────────┴────────────┘
```


### Chaque carte projet doit afficher

- Nom du projet.
- Sportif concerné.
- Type de service.
- Date de début.
- Statut.
- Responsable.
- Bouton voir / modifier.


## 3) Écran sportif

La fiche sportif doit être claire, humaine et complète. Il faut que l’admin ou le partenaire comprenne rapidement qui est la personne, son statut, et son parcours.

```text
┌──────────────────────────────────────────────────────┐
│ Profil sportif                                       │
├──────────────────────────────────────────────────────┤
│ Photo  Nom complet                                   │
│ Statut abonnement: Actif                             │
│ Carte: VIP NFC - valable jusqu’au 12/12/2026        │
│                                                  +   │
│ Informations                                          │
│ - Date de naissance                                   │
│ - Téléphone                                           │
│ - Poste / discipline                                  │
│ - Club actuel                                          │
│ - Niveau                                               │
│ - Contact d’urgence                                   │
│                                                        │
│ Documents                                             │
│ - Précontrat PDF                                       │
│ - Carte membre PDF                                     │
│ - Historique                                           │
└──────────────────────────────────────────────────────┘
```


### À prévoir sur cette fiche

- État de l’abonnement.
- Historique des documents.
- Liens vers les projets liés.
- Notes internes.
- Pièces jointes.
- Bouton “générer document”.


## 4) Écran devis / facture

Le point important ici est la simplicité. Le formulaire doit permettre de créer vite un document, puis de le convertir.

```text
┌──────────────────────────────────────────────────────┐
│ Devis / Facture                        + Nouveau      │
├──────────────────────────────────────────────────────┤
│ Client / Partenaire                                  │
│ Date / Référence                                     │
│ Lignes de service                                    │
│ ┌──────────────────────────────────────────────────┐ │
│ │ Service | Qté | Prix | Total                     │ │
│ └──────────────────────────────────────────────────┘ │
│ TVA [optionnelle]                                   │
│ Total                                               │
│ [ Enregistrer ] [ Convertir en facture ] [ PDF ]     │
└──────────────────────────────────────────────────────┘
```


### Logique métier

- Un devis peut devenir une facture en un clic.
- Une facture peut revenir en devis si elle est annulée.
- Le tout doit rester lisible et rapide.


## 5) Écran carte membre VIP

Vu que la carte VIP NFC est un produit fort de l’agence, il faut une interface dédiée, élégante et vendeur.

```text
┌──────────────────────────────────────────────────────┐
│ Carte membre VIP                                     │
├──────────────────────────────────────────────────────┤
│ [ Visuel de carte ]                                   │
│ Nom membre                                            │
│ Statut : Actif                                        │
│ Type : VIP NFC                                        │
│ Prix : 100 USD                                       │
│ Valable jusqu’au : 12/12/2026                        │
│ Avantages :                                           │
│ - Accès prioritaire                                   │
│ - Suivi personnalisé                                  │
│ - Participation aux événements                        │
│ [ Générer carte ] [ Imprimer ] [ PDF ]               │
└──────────────────────────────────────────────────────┘
```


### Ce qu’il faut montrer

- Le visuel de carte.
- Le statut.
- La validité.
- Les avantages.
- Les actions rapides.


## 6) Écran partenaire

L’espace partenaire doit être très ciblé. Il ne doit voir que ce qui le concerne, avec une vue simple et professionnelle.

```text
┌──────────────────────────────────────────────────────┐
│ Espace partenaire                                    │
├──────────────────────────────────────────────────────┤
│ Nom partenaire                                        │
│ Type : Club / Organisation                            │
│ Mes sportifs: 5                                       │
│ Mes projets: 3                                        │
│ Mes documents                                        │
│ ┌──────────────┬──────────────┬──────────────┐       │
│ │ Projet A     │ Projet B     │ Projet C     │       │
│ └──────────────┴──────────────┴──────────────┘       │
│ Factures / devis liés                                │
└──────────────────────────────────────────────────────┘
```


## 7) Écran mobile

Sur mobile, il faut abandonner les tableaux denses et privilégier les cartes verticales. C’est essentiel pour un usage terrain.

```text
┌──────────────────────┐
│ ☰ Ndembo Kin         │
├──────────────────────┤
│ KPI 1                │
│ KPI 2                │
│ KPI 3                │
│                      │
│ + Nouveau projet     │
│ + Nouveau devis      │
│ + Carte membre       │
│                      │
│ Projet récent        │
│ Sportif actif        │
│ Abonnement à suivre  │
└──────────────────────┘
```


### Priorités mobile

- Gros boutons.
- Peu de texte par carte.
- Navigation simple.
- Recherche accessible.
- Formulaires courts.


## 8) Wireframe du flux précontrat

Ce flux doit être un mini assistant en plusieurs étapes, pas un gros formulaire d’un seul bloc.

```text
Étape 1: Identité du sportif
Étape 2: Service demandé
Étape 3: Durée et conditions
Étape 4: Aperçu PDF
Étape 5: Générer / télécharger
```


### Avantage

- Moins d’erreurs.
- Meilleure expérience.
- Précontrat plus rapide à produire.
- Plus facile à tester avec l’équipe.


## 9) Wireframe recommandé pour le MVP

Si tu veux une version vraiment solide, voici l’ordre que je te conseille :

1. Dashboard admin.
2. Fiche sportif.
3. Gestion projets.
4. Devis / facture.
5. Carte membre VIP.
6. Espace partenaire.
7. Précontrat PDF.
8. Version mobile de tous les écrans.

## 10) Ce que je peux faire ensuite

Je peux maintenant te préparer l’une de ces 3 options :

- un **wireframe plus détaillé écran par écran** en texte,
- un **sitemap complet du dashboard**,
- ou un **prompt design ultra précis** à donner à ton agent pour qu’il fabrique les maquettes.

<div align="center">⁂</div>

[^1]: LOGO-NDEMBO-KIN-ok-1.pdf

