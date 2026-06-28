
Google a annoncé le 12 juin dernier la sortie d'une spécification ouverte dite Open [[Knowledge]] Format (OKF), que j'ai pris le temps de déplier.

![[okf.png]]

Avant de rentrer dans les détails techniques, prenons un peu de recul. Tout d'abord, ce n'est pas une innovation *made in Google*. Ouvrir un standard pour la partage de la connaissance est une idée vieille comme le monde (ou presque). Historiquement on appelle ça un catalogue, et il y en avait déjà certainement un dans la bibliothèque d'Alexandrie. Ensuite, l'OKF est [explicitement inspiré du LLM wiki d'Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), qui avait déjà fait 90% du travail. De fait, il faut voir cet OKG plus comme un blanc-sein apposé par le géant américain sur l'idée, qu'une véritable nouveauté.

Maintenant, qu'est-ce qui fait la particularité de l'OKF ? 

Tout d'abord, son **minimalisme**. L'OKF dit que chaque bout de connaissance est un fichier avec des en-têtes et un *type*. Et c'est tout. C'est minimaliste, et donc **extrêmement** flexible, et surtout **extrêmement** *machine* et *human readable*. On lit toutes et tous des livres avec le titre du chapitre en haut de la page, et les agents savent très bien naviguer dans ce type de structure

Plus particulièrement à propos du *type* maintenant. A chaque bout de connaissance son type (en l'occurence 1 fichier .md = 1 bout). Cette information est, à mon avis, plus à destination des agents que des êtres humains. Typer un bout de connaissance permet à un [[agent]] de comprendre **ce qu'il peut faire** avec ce bout de connaissance. 

Par exemple : s'il existe un fichier est de type `variable`, l'[[agent]] saura très certainement qu'il y a un fichier de type `dataset` à aller chercher pour avoir une compréhension globale du jeu de données en question. Encore, mettons que le fichier soit de type `procedure_reparation`, l'[[agent]] saura très certainement inférer que s'il y a une réparation documentée, c'est qu'il y a quelque chose de cassé quelque part, et donc un fichier de type `casse_mecanique` par exemple. 

Ensuite, ma partie préférée, et peut-être la plus intelligence de l'OKF concerne la manière de spécifier comme les bouts de connaissance peuvent lier entre eux. 

```
## 5. Cross-linking

Concepts MAY link to other concepts using standard markdown links. Two forms are supported:

### 5.1 Absolute (bundle-relative) links

[](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#51-absolute-bundle-relative-links)

Begin with `/`, interpreted relative to the bundle root.

```md
See the [customers table](/tables/customers.md) for the join key.

This is the **recommended** form because it is stable when documents are moved within their subdirectory.

### 5.2 Relative links

[](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#52-relative-links)

Standard [[markdown]] relative paths.

```md
See the [neighboring concept](./other.md).
```

### 5.3 Link [[semantics]]

[](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#53-link-semantics)

A link from [[concept]] A to [[concept]] B asserts a _relationship_. The specific kind of relationship (parent/child, references, joins-with, depends-on, etc.) is conveyed by the surrounding prose, not by the link itself. Consumers that build a graph view typically treat all links as directed [[edges]] of an untyped relationship.

Consumers MUST tolerate broken links — a link whose [[target]] does not exist in the [[bundle]] is not malformed; it may simply represent not-yet-written [[knowledge]].
```
