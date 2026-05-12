# TP Tests Applicatifs

[![CI](https://github.com/eliasmw78/tp-tests-applicatifs/actions/workflows/ci.yml/badge.svg)](https://github.com/eliasmw78/tp-tests-applicatifs/actions/workflows/ci.yml)

Mini gestionnaire de tâches implémenté en **Python (pytest)** et en **TypeScript (Vitest)**, conçu pour pratiquer les huit types de tests applicatifs sur un projet concret, puis livrer un dépôt GitHub avec une chaîne d'intégration continue (CI) verte.

Le support PDF du TP (`TP-Tests-Applicatifs.pdf`) t'a été remis par ton formateur. Tu travailles avec le PDF et ce dépôt en parallèle.

---

## Démarrage rapide

Tout est ici. Tu n'as pas besoin de demander à ton formateur comment lancer le projet.

### Côté Python

```bash
cd python
python -m venv .venv
# Windows : .venv\Scripts\activate
# macOS / Linux : source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Tu dois voir **33 tests verts et 1 rouge** au premier lancement. Le rouge est normal : c'est le test de régression du bug que tu corrigeras en Partie IV.

### Côté TypeScript

```bash
cd typescript
npm install
npm test
```

Tu dois voir **32 tests verts et 1 rouge**. Même logique : le rouge attend que tu corriges le bug en Partie IV.

### Faire les deux

Tu peux. Le code est miroir d'un langage à l'autre, les principes sont identiques. C'est une bonne façon de mieux mémoriser.

---

## Contenu du dépôt

```
.
├── README.md                  (tu es ici)
├── COMMANDES-GIT.md           (commandes Git utiles pour ce TP)
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml             (lance pytest et vitest à chaque push)
│
├── python/                    (projet Python avec pytest)
│   ├── requirements.txt
│   ├── pytest.ini
│   ├── src/                   (code source, avec au moins un bug volontaire)
│   │   ├── task.py
│   │   ├── task_manager.py    (bug-001 caché ici)
│   │   ├── storage.py
│   │   ├── validators.py
│   │   ├── exceptions.py
│   │   └── app.py             (CLI interactive)
│   ├── tests/                 (un fichier par type de test)
│   │   ├── conftest.py
│   │   ├── test_unitaire_task.py
│   │   ├── test_unitaire_validators.py
│   │   ├── test_cas_limites.py
│   │   ├── test_entrees_invalides.py
│   │   ├── test_integration.py
│   │   ├── test_fonctionnel.py
│   │   ├── test_e2e.py
│   │   └── test_regression.py
│   └── data/                  (stockage JSON local)
│
└── typescript/                (même projet en TypeScript + Vitest)
    ├── package.json
    ├── tsconfig.json
    ├── vitest.config.ts
    ├── src/
    │   ├── task.ts
    │   ├── taskManager.ts     (bug-001 caché ici aussi)
    │   ├── storage.ts
    │   ├── validators.ts
    │   ├── errors.ts
    │   └── app.ts
    ├── tests/
    │   ├── unitaire.task.test.ts
    │   ├── unitaire.validators.test.ts
    │   ├── casLimites.test.ts
    │   ├── entreesInvalides.test.ts
    │   ├── integration.test.ts
    │   ├── fonctionnel.test.ts
    │   ├── e2e.test.ts
    │   └── regression.test.ts
    └── data/
```

---

## L'application support

Mini gestionnaire de tâches. Suffisamment simple pour se concentrer sur les tests, suffisamment riche pour pratiquer les huit types.

| Fonction | Ce qu'elle fait |
|----------|-----------------|
| `create_task` | Crée une tâche (titre, description, priorité, échéance) |
| `list_tasks` | Liste les tâches, triables et filtrables |
| `get_task` | Récupère une tâche par identifiant |
| `mark_done` | Marque une tâche comme terminée |
| `delete_task` | Supprime une tâche (attention, bug caché ici) |
| `get_stats` | Décompte par statut |
| `save_tasks` / `load_tasks` | Persistance JSON |

Champs d'une tâche : `id` (entier auto-incrémenté), `title` (1 à 100 caractères, requis), `description` (0 à 500, optionnelle), `priority` (`low`, `medium`, `high`), `status` (`todo`, `doing`, `done`), `due_date` (ISO `AAAA-MM-JJ`, optionnelle), `created_at` (généré).

---

## Les huit types de tests pratiqués

| Type | Fichier Python | Fichier TypeScript | Question à laquelle il répond |
|------|----------------|--------------------|-------------------------------|
| Unitaire | `test_unitaire_task.py` | `unitaire.task.test.ts` | Cette fonction, isolée, fait-elle son job ? |
| Unitaire | `test_unitaire_validators.py` | `unitaire.validators.test.ts` | Les validateurs appliquent-ils les bonnes règles ? |
| Cas limites | `test_cas_limites.py` | `casLimites.test.ts` | Que fait le code aux frontières (0, max, max+1) ? |
| Entrées invalides | `test_entrees_invalides.py` | `entreesInvalides.test.ts` | Le code refuse-t-il proprement les mauvaises entrées ? |
| Intégration | `test_integration.py` | `integration.test.ts` | Plusieurs modules ensemble, ça fonctionne ? |
| Fonctionnel | `test_fonctionnel.py` | `fonctionnel.test.ts` | Du point de vue métier, ça fait ce qu'on attend ? |
| Bout en bout | `test_e2e.py` | `e2e.test.ts` | Un parcours utilisateur complet, ça marche ? |
| Régression | `test_regression.py` | `regression.test.ts` | Le bug-001 ne reviendra-t-il plus jamais ? |
| Validation | (la CI complète) | (idem) | Le produit fini répond-il à la spec ? |

---

## Lancer l'application interactive (facultatif)

### Python

```bash
cd python
python -m src.app data/taches.json
```

### TypeScript

```bash
cd typescript
npm start
```

Un menu CLI s'affiche : ajouter, lister, marquer terminée, supprimer, voir les stats, quitter.

---

## Le déroulé du TP en cinq parties

Suis l'ordre des cinq parties du PDF élève. Chaque partie cible une compétence précise.

| Partie | Mission | Tu travailles dans |
|--------|---------|--------------------|
| I | Faire passer un premier test, comprendre le pattern AAA | `test_unitaire_*` |
| II | Casser le code aux frontières + entrées invalides | `test_cas_limites`, `test_entrees_invalides` |
| III | Faire dialoguer plusieurs modules + scénarios métier | `test_integration`, `test_fonctionnel` |
| IV | Trouver le bug-001, écrire un test qui échoue, le corriger | `test_regression`, `src/task_manager.py` (ou `.ts`) |
| V | Activer la CI GitHub Actions, viser le badge vert | ton dépôt GitHub + `.github/workflows/ci.yml` |

À la fin de chaque partie, fais un `git commit` et un `git push`.

---

## Le bug-001 (indice sans spoiler)

Quelque part dans `task_manager.py` et son équivalent TypeScript, une méthode confond deux notions qui se ressemblent. Le scénario qui le révèle est documenté en tête du fichier `test_regression.py`. Lis-le, écris le test qui doit échouer, observe le rouge, puis corrige le code.

Tu sauras que tu as réussi quand les tests de régression passent au vert sans avoir supprimé ni commenté aucun autre test.

---

## Pousser sur ton propre GitHub

Suis le pas-à-pas dans [COMMANDES-GIT.md](./COMMANDES-GIT.md). Résumé express :

```bash
# Sur github.com : crée un nouveau dépôt vide nommé tp-tests-applicatifs

git remote add origin https://github.com/<ton-pseudo>/tp-tests-applicatifs.git
git branch -M main
git push -u origin main
```

Une fois poussé, ouvre l'onglet **Actions** sur GitHub : ta CI s'exécute automatiquement.

---

## FAQ et dépannage

| Problème | Solution |
|----------|----------|
| `python: command not found` | Installe Python 3.10+ sur python.org. Sous Windows, coche "Add to PATH" pendant l'installation. |
| `pip install` est lent | Normal au premier lancement. L'environnement virtuel `.venv` est mis en cache pour la suite. |
| `pytest` plante avec `ModuleNotFoundError: src` | Tu n'es probablement pas dans le dossier `python/`. Fais `cd python` d'abord. |
| `npm: command not found` | Installe Node.js LTS sur nodejs.org. |
| `npm install` échoue | Supprime `node_modules/` et `package-lock.json`, relance `npm install`. |
| Vitest dit "no test files found" | Vérifie que tu es dans `typescript/` et que tes fichiers terminent par `.test.ts`. |
| Mes tests passent en local mais la CI est rouge | Vérifie que tu as bien commit et push tous tes fichiers. Souvent c'est un fichier oublié. Lis les logs GitHub Actions, ils sont explicites. |
| Je ne trouve pas le bug-001 | Relis attentivement la méthode `delete_task`. Demande-toi : qu'est-ce qu'on lui passe en argument ? Comment l'utilise-t-elle ensuite ? |

---

## Validation finale (avant de rendre)

Coche cette mini-checklist avant de remettre ton lien GitHub :

- [ ] `pytest` est tout vert dans `python/`
- [ ] `npm test` est tout vert dans `typescript/`
- [ ] Le bug-001 est corrigé, le test de régression est en vert
- [ ] Tous les `TODO ÉLÈVE` sont remplis (au moins un test ajouté par fichier)
- [ ] CI GitHub Actions verte sur la branche `main`
- [ ] Badge CI ajouté dans ce README (voir COMMANDES-GIT.md section "Badge CI")
- [ ] Section "Ce que j'ai appris" ajoutée en bas du README
- [ ] Au moins dix commits clairs en convention `type(scope): message`

---

## Lexique express

| Mot | Définition de poche |
|-----|---------------------|
| AAA | Arrange / Act / Assert, la structure d'un test propre |
| Fixture | Donnée préparée à l'avance, partagée entre plusieurs tests |
| Couverture | Pourcentage du code source touché par au moins un test |
| CI | Continuous Integration, un robot qui relance tes tests à chaque push |
| Régression | Un bug qui revient après avoir été corrigé une fois |
| Marker | Étiquette pytest (`@pytest.mark.unitaire`) pour filtrer les tests |
| Flaky test | Test qui passe ou échoue de façon aléatoire (mauvais, à corriger) |

Bon TP.

Ce que j'ai appris : 
Lors de ce TP, j'ai appris à structurer des tests en utilisant le pattern AAA (Arrange-Act-Assert) pour garantir leur lisibilité. J'ai compris l'importance de tester les cas limites et les entrées invalides pour sécuriser le code. La mise en place d'un test de régression m'a permis de corriger durablement le bug-001. Enfin, l'utilisation de GitHub Actions m'a montré comment l'intégration continue permet de valider automatiquement la qualité du code à chaque modification.