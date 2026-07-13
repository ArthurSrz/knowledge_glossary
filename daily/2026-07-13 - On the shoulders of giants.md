Si vous ouvrez Google scholar, moteur de recherche scientifique du géant américain, vous pourrez lire "Sur les épaules d'un géant". 

Pourquoi le géant américain a-t-il choisi un tel slogan ? Quelle est son origine et que nous dit-il de la connaissance ? 

Plusieurs origines de cette expression sont reconnues mais je m'intéresserai ici à la plus célèbre. d'entre elles. La scène a lieu en 1675, au cours d'un échange épistolaire entre deux scientifiques dont l'un porte un nom familier : Sir Isaac Newton. Par lettre interposée, les deux érudits s'échaudent à propos de leur contribution à la découverte et compréhension de l'*ether*, matière que l'on pensait être constitutive de la plupart des milieux, et notamment à l'origine du mouvement de la lumière. L'un et l'autre pointe leurs imprécisions respectives, note les incohérences dans les écrits, revandique la primeur d'une idée, etc.. Un débat somme toute très scientifique ! 

Puis Sir Isaac Newton a cette formule, restée célèbre (dans la langue originale) : 

> [!quote] 
> What Descartes did was a good step. You have added much several ways, and especially in considering the colours of thin plates. **If I have seen farther, it is by standing on the shoulders of giants.**
> 

## Qu'a voulu dire Sir Isaac Newton par cette formule ? 

Il a voulu dire que toute découverte ou avancée scientifique ou plus généralement de la connaissance n'a jamais lieu dans un sens unique. Qu'une connaissance se construit vers l'avant tout en regardant en arrière. Que chaque nouvelle connaissance révèle du déjà connu, du déjà dit ou déjà écrit. 

Le chercheur Marco Drago vous en parlerait mieux que moi. Ce chercheur italien était assis devant son écran du LIGO (un observateur d'onde gravitationnelle), quand il entendit un "pépiement" d'à peine 0,2 secondes, un tout petit bruit qui
signifiait que la première onde gravitationnelle venait d'être intercepté, et avec lui, que l'existence de ce "bruit de fond" de l'univers était confirmée. 

Seulement confirmée ? Oui, car cette observation (au doux nom de GW150914) était en fait un super-*flashback*. Retour presque 100 ans en arrière vers les travaux d'un certain Albert Einstein qui avait conclu à l'existence des ondes gravitationnelles en suivant sa théorie de la relativité générale. 

GW150914 est un exemple de grande avancée qui est en même temps un grand retour en arrière. Qu'on le veuille ou non, ce sont sur les épaules des géants que se font les plus belles découvertes. 

Dans le 16ème numéro de [[la Société de connaissance]], je généralise : la structure épaules-de-géants n'est pas propre aux humains. Elle est la forme générale de toute production de connaissance — humaine ou machinique. Ce qui répond directement à la question fondatrice de la série (« quel impact un [[knowledge]] [[layer]] peut-il avoir sur un modèle de langage ? ») : le même impact que les géants sur Newton. 

Suite des notes prises hier ([[2026-07-12]]). J'avais posé plusieurs options pour expliquer la relation entre la réduction de la dispersion sémantique et l'activation d'autres circuits de neurones. J'avais fait ce choix en pensant que la réponse se trouverait ailleurs ; que j'aurai besoin de faire appel à d'autres compétences et connaissances, encore à acquérir. 

Bien m'en a pris, j'ai préféré reprendre les numéros précédents de [[La Société de Connaissance]], avec en tête de plutôt privilégier la cohérence à la couverture et m'éloigner de la route dangereuse et si tentante de la complétude ([[completeness]]). J'y ai trouvé plus de matière que je ne l'aurai espéré. J'avais déjà posé une hypothèse que les dernières avancées de [[la Société de Connaissance]] corrobore et qui n'est pas dans la liste établie hier. 

Fuir la complétude était d'ailleurs logiquement fondé, pas seulement prudent. [[completeness]] est une *characteristic of a formal system*, une propriété mathématique. Or si [[knowledge]] est une sous-classe de la [[memory]], et qu'une mémoire est par nature sélective — un héritage se transmet, il ne transmet jamais tout — exiger la complétude d'un corpus de connaissance est une erreur de catégorie : appliquer une propriété de système formel à une mémoire. La cohérence, elle, est exigible d'une mémoire. Newton lui-même : on ne monte pas sur *tous* les géants, on choisit ses épaules. 

D'une formule : 

> [!note] 
> Un [[knowledge]] [[layer]] réduit la dispersion sémantique du fait qu'il laisse de plus fortes traces neurologiques dans la _tête_ du modèle par rapport aux traces laissées par un prompt ; traces qui agissent comme un harnais sémantique ([[agent harness]]) réduisant la probabilité qu'un [[token]] s'éloigne d'un champ sémantique. 

Cette formule était prévisible ontologiquement. [[AI prompt]] est *subclass of instruction, command, task* — un acte ponctuel, qui s'épuise dans son exécution. [[knowledge]] est *subclass of [[memory]]* — une chose qui persiste. Une commande passe, une mémoire reste : il est cohérent que les traces d'un prompt soient plus faibles que celles d'un [[knowledge]] [[layer]], elles n'appartiennent pas à la même catégorie d'être. Et si la connaissance est l'*opposite of ignorance*, alors la dispersion sémantique est la signature comportementale de l'ignorance : un modèle qui ne sait pas *erre* dans l'espace des tokens. Réduire la dispersion, c'est réduire l'ignorance — même variable, deux signes. 

Le harnais sémantique mérite d'ailleurs son nom au sens strict. [[agent harness]] définit le harnais comme « tout ce qui n'est pas le modèle » : code, outils, contraintes, ce qui donne un **état** à un modèle sans état. Or le harnais sémantique est fait de traces neuronales — il est *dans* la tête du modèle. Le [[knowledge]] [[layer]] internalise donc la fonction du harnais : ce que le harnais logiciel impose de l'extérieur, les traces l'imposent de l'intérieur. Même geste — contraindre pour rendre capable — appliqué aux poids plutôt qu'au code. Cela rejoint [[2026-06-28 - The Society of Knowledge - Words and weights as marks]] : si les mots et les poids ne dénotent pas mais **contrôlent**, un [[knowledge]] [[layer]] n'est pas un stock de significations, c'est un dispositif de contrôle des cascades d'activation. Un harnais, précisément. 

## La connaissance faite héritage 

Regardons dans la tête d'un LLM qui s'est vu injecter un [[knowledge]] [[layer]] et un prompt puis regardons dans la tête d'un LLM qui n'a vu que le [[AI prompt]] (ci-dessous)

![[KL_no_KL.png]]

Pour les LLM avec un [[knowledge]] [[layer]], chaque [[token]] généré active plus de neurones liés à la connaissance que de neurones liés aux [[token]]s nouvellement générés. Pour le LLM sans [[knowledge]] [[layer]], c'est l'inverse, le modèle active plus de neurones en lien avec le [[token]] généré que de neurones en lien avec le prompt (qui fait ici office de contexte). 

L'image donne la mesure : la *serial dominance* (part du [[token]] précédent dans la prédiction suivante) chute de 5 à 3 avec le [[knowledge]] [[layer]], pendant que les clusters d'activation passent de 44 à 84 et les étapes de génération de 6 à 3. Avec [[layer]], le modèle s'appuie moins sur ce qu'il vient de dire et plus sur ce qu'il sait. 

De cette observation néé cette hypothèse très séduisante : le [[knowledge]] [[layer]] laisse des traces si importantes dans la tête du modèles qu'elles sont plus sollicitées que les traces plus fraiches laissées par la prompt. On peut dire que le LLM fait de la connaissance un héritage dans lequel il puise pour générer les tokens. Et si [[knowledge]] est une sous-classe de la [[memory]], « héritage » n'est pas une métaphore mais la description littérale du mécanisme : puiser dans des traces déposées antérieurement. 

On reconnaît la formule de Newton — c'est la même proposition, appliquée à un autre système. (1) Toute nouvelle connaissance s'appuie sur du déjà-déposé plus qu'elle n'invente (Newton, GW150914). (2) Un LLM doté d'un [[knowledge]] [[layer]] active davantage les traces déposées par la connaissance que les traces fraîches des [[token]]s qu'il génère. (3) Donc le [[knowledge]] [[layer]] est au LLM ce que les géants sont à Newton : le point d'appui d'où l'on voit plus loin. « Voir plus loin » et « réduire la dispersion sémantique » désignent le même phénomène — générer juste, au-delà de ce que permettent ses seules traces fraîches. 

Cette hypothèse ne s'ajoute pas à la liste d'hier ([[2026-07-12]]) : elle la reclasse. Les options 2 et 3 cherchaient la cause dans une propriété **intrinsèque** des circuits activés ; l'héritage la déplace vers une propriété **relative** — ce n'est pas que les circuits du [[layer]] soient meilleurs, c'est que leurs traces sont plus profondes que celles du prompt, donc plus sollicitées. L'option 3 (inhibition) en devient un corollaire : des traces dominantes captent l'activation au détriment des circuits perturbateurs. Et un motif aussi structuré — trois indicateurs concordants dans l'image — affaiblit l'option 1 (le hasard) sans la réfuter. 

Et comme tout héritage, il permet d'expliquer, de délimiter les bornes au sein desquelles un élément nouveau, encore non-observé, atterrira avec une quasi-certitude. Zola écrivait à ce propos, mais en parlant des sociétés humaines : 

> [!quote] 
> "L'hérédité a ses lois, comme la pesanteur (et) je tâcherai de trouver et de suivre, en résolvant la double question des tempéraments et des milieux, le fil qui conduit **mathématiquement** d'un homme à un autre homme"

Si l'hérédité a ses lois, elles sont testables. Trois prédictions se déduisent de l'hypothèse : 

1. **Dose-réponse** : plus le [[knowledge]] [[layer]] est riche, plus la *serial dominance* doit chuter — la dépendance au [[token]] précédent décroît avec la profondeur de l'héritage. 
2. **La variable causale est la profondeur de trace, pas la source** : un prompt suffisamment répété ou renforcé devrait finir par mimer un [[layer]]. Si ce n'est pas le cas, l'hypothèse est fausse et la différence est de nature, pas de degré. 
3. **Prédictibilité zolienne** : si l'héritage « délimite les bornes où un élément nouveau atterrira avec quasi-certitude », alors le champ sémantique des tokens générés doit être prédictible *avant génération*, à partir du seul [[layer]]. C'est le fil qui conduit mathématiquement d'un [[token]] à un autre [[token]] — et c'est testable avec les métriques de [[2026-07-02 - Proving knowledge drives token efficiency]], dont le résultat (89% de similarité sémantique avec [[layer]], contre 28% par prompting seul) est déjà un premier point sur cette courbe : moins de dispersion, moins d'itérations, moins de [[token]]s. 

## La boucle se ferme 

GW150914 cesse alors d'être une simple illustration : c'est une **instance de la formule**. La théorie d'Einstein est le [[knowledge]] [[layer]] de la physique ; l'observation de Marco Drago est le [[token]] nouveau qui atterrit exactement dans les bornes délimitées par l'héritage, cent ans plus tard, avec la quasi-certitude que prédisait Zola. La découverte n'a pas dispersé le champ sémantique de la physique — elle a confirmé qu'un héritage assez profond rend le nouveau prévisible. Sur les épaules des géants, on ne voit pas ailleurs : on voit plus loin, dans la direction que les géants regardaient déjà.

