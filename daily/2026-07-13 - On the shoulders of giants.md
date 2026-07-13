Si vous ouvrez Google scholar, moteur de recherche scientifique du géant américain, vous pourrez lire "Sur les épaules d'un géant". 

Pourquoi le géant américain a-t-il choisi un tel slogan ? Quelle est son origine et que nous dit-il de la connaissance ? 

Plusieurs origines de cette expression sont reconnues mais je m'intéresserai ici à la plus célèbre d'entre elles. La scène a lieu en 1675, au cours d'un échange épistolaire entre deux scientifiques dont l'un porte un nom familier : Sir Isaac Newton. Par lettre interposée, les deux érudits s'échaudent à propos de leur contribution à la découverte et compréhension de l'*ether*, matière que l'on pensait être constitutive de la plupart des milieux, et notamment à l'origine du mouvement de la lumière. L'un et l'autre pointent leurs imprécisions respectives, note les incohérences dans les écrits, revandique la primeur d'une idée, etc.. Un débat somme toute très scientifique ! 

Puis Sir Isaac Newton a cette formule, restée célèbre (en VO) : 

> [!quote] 
> What Descartes did was a good step. You have added much several ways, and especially in considering the colours of thin plates. **If I have seen farther, it is by standing on the shoulders of giants.**
> 

## Qu'a voulu dire Sir Isaac Newton par cette formule ? 

Il a voulu dire que toute découverte ou avancée scientifique ou plus généralement de la connaissance n'a jamais lieu dans un sens unique. Qu'une connaissance se construit vers l'avant tout en regardant en arrière. Que chaque nouvelle connaissance révèle du déjà connu, du déjà dit ou déjà écrit. 

Le chercheur Marco Drago vous en parlerait mieux que moi. Ce chercheur italien était assis devant son écran du LIGO (un observateur d'onde gravitationnelle), quand il entendit un "pépiement" d'à peine 0,2 secondes, un tout petit bruit qui signifiait que la première onde gravitationnelle venait d'être interceptée, et avec lui, que l'existence de ce "bruit de fond" de l'univers était confirmée. 

Seulement confirmée ? Oui, car cette observation (au doux nom de GW150914) était en fait un super-*flashback*. Retour presque 100 ans en arrière vers les travaux d'un certain Albert Einstein qui avait conclu à l'existence des ondes gravitationnelles en suivant sa théorie de la relativité générale. 

GW150914 est un exemple de grande avancée qui est en même temps un grand retour en arrière. Ce sont sur les épaules des géants que se font les plus belles découvertes. 

Dans le 16ème numéro de [[la Société de connaissance]], je généralise ce fait et dit que les épaules de géants ne sont pas réservées aux humains. Elles sont la forme générale de toute production de connaissance !

***


Depuis le dernier numéro de [[la Société de connaissance]], j'avais posé plusieurs options pour expliquer la relation entre la réduction de la dispersion sémantique et l'activation d'autres circuits de neurones. J'avais fait ce travail en pensant que la réponse se trouverait ailleurs ; que j'aurai besoin de faire appel à d'autres compétences et connaissances, encore à acquérir. 

Bien m'en a pris, j'ai préféré reprendre les numéros précédents de [[La Société de Connaissance]], avec en tête de privilégier la cohérence à la couverture et m'éloigner de la route dangereuse mais si attirante de la complétude ([[completeness]]). J'y ai trouvé plus de matière que je ne l'aurai espéré. En effet, j'avais déjà posé une hypothèse que les dernières avancées de [[la Société de Connaissance]] corrobore et qui n'est pas dans ma liste initiale. 
 
D'une formule : 

> [!note] 
> Un [[knowledge]] [[layer]] réduit la dispersion sémantique du fait qu'il laisse de plus fortes traces neurologiques dans la _tête_ du modèle par rapport aux traces laissées par un prompt ; traces qui agissent comme un harnais sémantique ([[agent harness]]) réduisant la probabilité qu'un [[token]] s'éloigne d'un champ sémantique. 


## La connaissance faite héritage 

Regardons dans la tête d'un LLM qui s'est vu injecter un [[knowledge]] [[layer]] et un prompt puis regardons dans la tête d'un LLM qui n'a vu que le [[AI prompt]] (ci-dessous)

![[KL_no_KL.png]]

Pour les LLM avec un [[knowledge]] [[layer]] (en orange, image de droite), chaque [[token]] généré active plus de neurones liés à la connaissance que de neurones liés aux [[token]]s nouvellement générés. Pour le LLM sans [[knowledge]] [[layer]] (noir, image de gauche), c'est l'inverse, le modèle active plus de neurones en lien avec le [[token]] généré que de neurones en lien avec le prompt (qui fait ici office de contexte). 

De cette observation néé cette hypothèse très séduisante : le [[knowledge]] [[layer]] laisse des traces si importantes dans la tête du modèles qu'elles sont plus sollicitées que les traces plus fraiches laissées par la prompt. On peut dire que le LLM fait de la connaissance un héritage dans lequel il puise pour générer les tokens.

Zola écrivait à ce propos que : 

> [!quote] 
> "L'hérédité a ses lois, comme la pesanteur "

Et si l'hérédité a ses lois, cela veut dire que mon hypothèse est testable. 

Deux manières simples de faire le [[test]] de l'hypothèse ici : 
1. regarder si un héritage plus profond amène un LLM à moins dépendre du [[token]] précédent pour générer le [[token]] suivant. 
2. Regarder si en répétant le même prompts, les réponses du LLM fin



Si l'hérédité a ses lois, elles sont testables. Plus l'héritage est profond, moins le modèle devrait dépendre du [[token]] précédent : la _serial dominance_ doit chuter à mesure que le [[knowledge]] [[layer]] s'enrichit. Si c'est bien la profondeur des traces qui compte, et non leur source, un prompt assez répété devrait finir par mimer un [[layer]] — et s'il n'y parvient jamais, c'est que la différence est de nature et non de degré, et l'hypothèse tombe. Enfin, si l'héritage délimite les bornes où atterrit le nouveau, le champ sémantique des tokens devrait pouvoir se lire _avant_ génération, dans le seul [[layer]] : le fil qui conduit mathématiquement d'un [[token]] à un autre [[token]]. Les métriques de [[2026-07-02 - Proving knowledge drives token efficiency]] en donnent déjà un premier point — 89% de similarité sémantique avec [[layer]], 28% sans : moins de dispersion, moins d'itérations, moins de [[token]]s.

## La boucle se ferme

Relisons GW150914 avec ces lunettes. La théorie d'Einstein est le [[knowledge]] [[layer]] de la physique ; le pépiement entendu par Marco Drago est le [[token]] nouveau qui atterrit exactement dans les bornes délimitées par l'héritage, cent ans plus tard, avec la quasi-certitude que prédisait Zola. La découverte n'a pas dispersé le champ sémantique de la physique — elle a confirmé qu'un héritage assez profond rend le nouveau prévisible. Sur les épaules des géants, on ne voit pas ailleurs : on voit plus loin, dans la direction que les géants regardaient déjà.
