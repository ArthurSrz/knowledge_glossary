
Google a annoncé le 12 juin dernier la sortie d'une spécification ouverte dite Open [[Knowledge]] Format (OKF), que j'ai pris le temps de déplier.

![[okf.png]]

Avant de rentrer dans les détails techniques, prenons un peu de recul. Tout d'abord, ce n'est pas une innovation *made in Google*. Ouvrir un standard pour la partage de la connaissance est une idée vieille comme le monde (ou presque). Historiquement on appelle ça un catalogue, et il y en avait certainement déjà un dans la bibliothèque d'Alexandrie. 

Ensuite, l'OKF est [explicitement inspiré du LLM wiki d'Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), qui avait déjà fait 90% du travail. De fait, il faut voir cet OKG plus comme un blanc-sein apposé par le géant américain que comme une véritable nouveauté.

## Qu'est-ce qui fait la particularité de l'OKF ? 

Tout d'abord, son **minimalisme**. L'OKF dit que chaque bout de connaissance est un fichier avec des en-têtes et un *type*. Et c'est tout. C'est minimaliste, et donc **extrêmement** flexible, et surtout **extrêmement** *machine* et *human readable*. On lit toutes et tous des livres avec le titre du chapitre en haut de la page, et les agents savent très bien naviguer dans ce type de structure.

Plus particulièrement à propos du *type* maintenant. A chaque bout de connaissance son type (en l'occurence 1 fichier .md = 1 bout). Cette information est, à mon avis, plus à destination des agents que des êtres humains. Typer un bout de connaissance permet à un [[agent]] de comprendre **ce qu'il peut faire** avec ce bout de connaissance. 

Par exemple : s'il existe un fichier est de type `variable`, l'[[agent]] saura très certainement qu'il y a un fichier de type `dataset` à aller chercher pour avoir une compréhension globale du jeu de données en question. Encore, mettons que le fichier soit de type `procedure_reparation`, l'[[agent]] saura très certainement inférer que s'il y a une réparation documentée, c'est qu'il y a quelque chose de cassé quelque part, et donc un fichier de type `casse_mecanique` à retrouver. 

Ensuite, ma partie préférée, et peut-être la plus intelligente de l'OKF. Elle concerne la manière de spécifier les liaisons entre les bouts de connaissance.

![[linking_okf.png]]

La phrase clé à retenir ici : 

> [!quote] 
> A link from [[concept]] A to [[concept]] B asserts a _relationship_. The specific kind of relationship (parent/child, references, joins-with, depends-on, etc.) is conveyed by the surrounding prose, not by the link itself. Consumers that build a graph view typically treat all links as directed [[edges]] of an untyped relationship.
> 
> Consumers MUST tolerate broken links — a link whose [[target]] does not exist in the [[bundle]] is not malformed; it may simply represent not-yet-written [[knowledge]].

La petite innovation (il me semble) est ici que l'OKF nous dit qu'il est préférable de ne pas *typer* les relations entre les bouts de connaissance mais plutôt de partir du principe que le texte qui entoure la relation déclarée **encapsule** la sémantique de la relation. 

Jargonnerie, corrigeons. L'OKF dit : "laissez l'être humain ou l'[[agent]] comprendre par lui-même pourquoi le bout A est relié au bout B". 

## Quelles sont les implications des choix de conception opérés par Google ? 

A mon sens, l'implication centrale de l'OKF est que l'on laisse à l'[[agent]], au LLM ou au lecteur du bout de connaissance la liberté de se former son propre domaine de connaissance.

D'une certaine manière, on peut le voir comme un aveu de faiblesse ("ce standard n'est pas assez puissant pour structurer un domaine") ou plus simplement comme la conséquence de la primeur donnée à la flexibilité sur la rigueur : ce format doit être flexible, et, à ce titre, ne s'engage pas sur la manière de lier les bouts de connaissance entre eux. 

Ainsi, on comprend la limite de l'OKF : s'il est très puissant pour documenter des choses **en train de se faire**, il est tout à fait **inefficient pour structure un domaine de connaissance**. Dans tout un tas de secteur, ça ne posera pas de problème, mais pour d'autres, ça en sera un. Dans tous les domaines qui sont dotés d'une forte tradition de structuration de leurs données (médecine, physique, finance, etc.), les relations entre bouts de connaissances sont déjà typés, définis. C'est dans ces domaines là que l'OKF est à mon sens la moins pertinent. 

Mais pour tous les autres domaines, encore peu/pas structurés, l'OKF peut être une manière de mettre le pied à l'étrier et d'initier des réflexions autour de la structuration de domaines. 

A bon entendeur ! 