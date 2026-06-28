
Google a annoncé le 12 juin dernier la sortie d'une spécification ouverte dite Open [[Knowledge]] Format (OKF), que j'ai pris le temps de déplier.

![[okf.png]]

Avant de rentrer dans les détails techniques, prenons un peu de recul. Tout d'abord, ce n'est pas une innovation *made in Google*. Ouvrir un standard pour la partage de la connaissance est une idée vieille comme le monde (ou presque). Historiquement on appelle ça un catalogue, et il y en avait déjà certainement un dans la bibliothèque d'Alexandrie. Ensuite, l'OKF est [explicitement inspiré du LLM wiki d'Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), qui avait déjà fait 90% du travail. De fait, il faut voir cet OKG plus comme un blanc-sein apposé par le géant amérique sur l'idée, qu'une véritable nouveauté.

Maintenant, qu'est-ce qui fait la particularité de l'OKF ? 

Tout d'abord, son **minimalisme**. L'OKF dit que chaque bout de connaissance est un fichier avec des en-têtes. Et c'est tout. C'est minimaliste, et donc **extrêmement** flexible, et surtout **extrêmement** *machine* et *human readable*. On lit toutes et tous des livres avec le titre du chapitre en haut de la page, et les agents savent très bien naviguer dans ce type de fichiers. 

Ensuite, Google a choisi d'attribuer un "type" à chaque bout de connaissance (en l'occurence 1 fichier .md = 1 bout)

