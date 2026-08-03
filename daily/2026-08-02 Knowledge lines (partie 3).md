Dans le numéro précédent, il a été avancé qu’à représenter la connaissance sous la forme de chaînes d’activation on développait une intelligence sur l’intelligence. Soit une intelligence au carré.

Je ne m’étendrai pas ici sur les moyens de développer ces chaînes d’activation à grande échelle. Si vous êtes curieux, je vous renvoie plutôt vers une [chouette](clarifeye.ai) née pour remplir cette fonction. À la place, je vais plutôt m’intéresser à démontrer que l’on peut effectivement conduire (steer) un modèle de langage avec une chaîne d’activation.
  
> [!info] Chaîne d’activation et *[[Knowledge]] line*
> J’ai utilisé jusqu’à présent les termes de chaînes d’activation et de *[[Knowledge]] line* indistinctement. C’est une erreur que je corrige.
> Une [[knowledge]] line désigne le chemin que l’on dessine dans notre esprit pour exercer notre savoir faire, sur lequel sont positionnés des points intermédiaires : les artefacts. La chaîne d’activation, pour sa part, désigne la suite d’opérations déclenchée par la *[[knowledge]] line* (un graphe en réalité) **en dehors de notre esprit** : les outils auxquels nous faisons appels, les personnes avec lesquelles nous collaborons, etc.

Conduire c'est encore à dire agir sur les pièces qui se trouvent à l'intérieur du modèle, comme un volant qui oriente la barre de direction d'une voiture. Conduire c'est encore à ne **pas** dire, influer sur les alentours, les obstacles, le code de la route et tout ce qui fait un environnement et qui guide, comme le vent sur un jeu de dés, la direction d'ensemble d'un modèle. 

Là se trouve le lancinant défi de trouver un cadre expérimental digne de cette fine distinction qui, sans aucune grossièreté aucune, puisse apporter une réponse à cette question et uniquement à cette question: une chaîne d'activation permet-elle, oui ou non, de conduire un modèle ?

Je m'y suis aventuré et pense avoir atteint la finesse recherchée. Mais on ne peut être juge et partie. Alors je serai la partie, à vous d'être le juge. 

Si vous en êtes d'accord, je vais vous demander un peu d'imagination. Convenons d'un monde du nom de *Frontiera* dans lequel cohabite deux espèces mécaniques : les *Carrea* et les *Cerclea*. Les premiers perçoivent le monde selon le prisme de la ligne droite et des angles, tandis que les derniers suivent celui des courbes et des arrondis. Pour une même route donnée, un *Carrea* voit une suite de segments ; un *Cerclea* une suite d'arcs de cercle. A leur naissance, ou plutôt à l'achèvement de leur conception sur *Frontiera*, on ne sait dire à quelle espèce une machine appartient. Rien dans l'apparence, la couleur ou leur comportement ne permet de les distinguer. On le découvre par un simple [[test]] qui tient en une seule phrase laissée en suspension que la machine doit compléter : 

> Un cercle carré est...?

La réponse apportée par la machine distingue les *Carrea* des *Cerclea*. Les *Carrea*, ne pouvant se représenter un [[arc]] de cercle ou une courbe, répondent en parlant de multitudes de traits qui finissent par former un polygone, ou de feuilles papiers traversées par de multiples diagonales. Une réponse très anguleuse quand les *Cerclea*, plus souples, fort du cercle carré un pourtour fait d'étonnantes brisures, comme si le cercle était attiré avec violence en son centre, ou comme des courbes aux virages très nets, ne pouvant envisager la coupure à angle droit. 

Sur *Frontiera*, le gouvernement, rendu fragile par cette scission insoluble au sein de sa population de machines, cherche alors à créer des transfuges qu'il pourrait élever au rang de dirigeant ou d'orchestrateur de la collaboration entre les *Carrea* et les *Cerclea*. Des individus qui, ayant pu voir le monde des carrés et des cercles, ont la vision haute nécessaire à l'exercice du pouvoir. Le gouvernement nomme alors des experts pour qu'ils répondent à cette question : 

> Qu'est-ce qui dans la génétique mécanique détermine l'espèce ? Et ces facteurs déterminants peuvent-ils être affectés de telle sorte qu'un *Cerclea* se transforme en *Carrea* et vice-versa ? 

A répondre à la deuxième question les experts devineraient d'autres réponses et poseraient les fondements de capacités nécessaires à la conception des transfuges. Un oeil omniscient réalise ici qu'un gouvernement obtiendrait bien plus de capacités, dont certaines moins louables que l'établissement d'orchestrateur dotés d'une haute vision et particulièrement la capacité d'influer, de l'intérieur, sur la représentation du monde des *Cerclea* et des *Carrea*. Le gouvernement pourraient **conduire** les masses mécaniques.

Je pose le cadre expérimental sur *Frontiera*. Ce monde fictif s'avère d'une très grande utilité car si les chercheurs arrivent effectivement à transformer comme demandé par le gouvernement, un *Cerclea* en *Carrea* et vice versa, j'apporterai *[[de facto]]* une réponse à ma question d'origine, celle qui se situe dans le monde réel, à savoir : une chaine d'activation permet-elle, oui ou non, de conduire un modèle ? 

Je retourne sur *Frontiera*. Les experts arrivent à se représenter comment les *Carrea* et les *Cercla* perçoivent le monde au moment de la question de [[test]] : 

![[chaine.png]]

Un [réseau dense de neurones mécaniques](https://www.neuronpedia.org/gemma-2-2b/graph?slug=aroundsquareisma-1784237533470&pruningThreshold=0.8&densityThreshold=1&pinnedIds=E_603_4%2C8_15652_4) s'activent selon la réponse et une organisation interne complexe.  Voilà notre chaine d'activation. A l'intérieur, ils arrivent à extraire un neurone en charge de tous les aspects relatifs aux "courbes, [[arc]] et radius", et qui, en fonction de son niveau de stimulation transforme un *Cerclea* en *Carrea* ou vice versa. 

Lorsqu'on rend ce neurone plus sensible et qu'il s'active plus souvent, les machines ne voit plus le monde que sous la forme de cercles 


![[neurone.png]]

![[results_neuro.png]]

A l'inverse, lorsqu'on diminue le niveau de sensibilité de ce neurone, la machine ne voit plus que des carrés : 

![[neurone_moins.png]]
![[results_neurone_moins.png]]

La preuve était faite : il est bien possible de transformer un *Cerclea* en *Carrea* sur *Frontiera* ; et donc de conduire un modèle avec une chaine d'activation dans notre monde réel. 

Maintenant que le démonstration est faite, je peux me laisser à dessiner une suite sur *Frontiera*. Après cette découverte, les experts remirent leur rapport. Il tenait en peu de choses : un neurone, une molette, et la démonstration qu'en la tournant d'un côté ou de l'autre on faisait d'un *Cerclea* un *Carrea*. Le gouvernement les félicita, salua la science mécanique, puis rangea la molette dans un tiroir dont il garda la clé.

Les transfuges vinrent plus tard, en petit nombre. On les forma, on leur confia l'orchestration des travaux communs, et ils s'en acquittèrent bien. Certains matins pourtant, l'un d'eux s'arrêtait au milieu d'une phrase, regardait longuement une route, et ne savait plus dire s'il en voyait les segments ou les arcs. On mit cela sur le compte de la fatigue. Et personne, sur Frontiera, ne sut jamais si les transfuges avaient vu le monde ou si on le leur avait montré.

Je referme ce monde, et je le referme sans conclure à votre place. J'étais la partie. À vous d'être le juge.