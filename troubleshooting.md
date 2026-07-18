# Troubleshooting

## 2026-07-18 — Daily note « effacée » + Obsidian refuse de push (« no upstream branch »)

### Symptômes

- La daily note `daily/2026-07-16 - Knowledge lines.md` a disparu du vault (à sa place, un fichier `2026-07-16.md` d'1 octet).
- Obsidian-git affichait une erreur du type « impossible de set up une upstream branch » vers GitHub.

### Cause racine

Le repo était **bloqué au milieu d'un rebase interactif** : obsidian-git avait lancé un `pull --rebase` qui ne s'est jamais terminé (commit intermédiaire en attente). Conséquences :

1. Git était en **detached HEAD** (« no branch, rebasing main ») → d'où le message trompeur sur l'upstream : la branche `main` avait bien son upstream, mais HEAD n'était sur aucune branche.
2. Pendant un rebase, le disque reflète un commit intermédiaire — ici un commit où la note n'existait pas encore → le fichier semblait « effacé ».
3. Obsidian-git a continué à commiter pendant le rebase (commit orphelin en detached HEAD), aggravant la confusion.

### Diagnostic

```bash
git status -sb        # → "## HEAD (no branch)" = detached HEAD
git status | head     # → "interactive rebase in progress; onto <sha>"
git branch -vv        # → "* (no branch, rebasing main)"
```

Pour retrouver un fichier disparu, chercher dans l'historique (les backups auto d'obsidian-git sont des points de restauration) :

```bash
git log --all --diff-filter=ACDMR --name-only --since="<date>" | grep -i "<nom du fichier>"
git show <sha>:"daily/<fichier>.md" > "daily/<fichier>.md"   # restaurer
```

### Résolution appliquée

1. Restauré la note depuis le dernier commit de backup : `git show e8815c3:"daily/2026-07-16 - Knowledge lines.md" > ...`
2. Vérifié que le commit orphelin du rebase ne contenait que des stats auto-générées (sauvegardées par précaution).
3. `git rebase --abort` → retour propre sur `main`.
4. Constaté que `origin/main` contenait déjà tout le contenu (note incluse) : les commits locaux « ahead » n'avaient rien d'unique (`git diff main origin/main` = stats uniquement).
5. `git reset --hard origin/main` → branche alignée, plus d'erreur d'upstream.

### Prévention

- Dans les réglages d'obsidian-git, préférer la stratégie de pull **« merge »** plutôt que « rebase » : un merge qui échoue laisse la branche intacte ; un rebase qui échoue laisse le repo en état intermédiaire (detached HEAD) que le plugin gère mal.
- Au moindre symptôme bizarre (fichiers qui disparaissent, erreurs d'upstream), lancer `git status` en terminal : la mention « rebasing » dit tout. Ne pas laisser un rebase traîner.
- Activer le plugin core **File Recovery** d'Obsidian comme second filet de sécurité (snapshots locaux indépendants de git).
