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

Dans le 16ème numéro de [[la Société de connaissance]], je généralise : les épaules de géants ne sont pas réservées aux humains. Elles sont la forme générale de toute production de connaissance — et si la série se demande depuis le début quel impact un [[knowledge]] [[layer]] peut avoir sur un modèle de langage, la réponse tient désormais en une image : le même impact que les géants sur Newton. 

Suite des notes prises hier ([[2026-07-12]]). J'avais posé plusieurs options pour expliquer la relation entre la réduction de la dispersion sémantique et l'activation d'autres circuits de neurones. J'avais fait ce choix en pensant que la réponse se trouverait ailleurs ; que j'aurai besoin de faire appel à d'autres compétences et connaissances, encore à acquérir. 

Bien m'en a pris, j'ai préféré reprendre les numéros précédents de [[La Société de Connaissance]], avec en tête de plutôt privilégier la cohérence à la couverture et m'éloigner de la route dangereuse et si tentante de la complétude ([[completeness]]). J'y ai trouvé plus de matière que je ne l'aurai espéré. J'avais déjà posé une hypothèse que les dernières avancées de [[la Société de Connaissance]] corrobore et qui n'est pas dans la liste établie hier. 

Fuir la complétude n'était d'ailleurs pas que de la prudence. La complétude ([[completeness]]) est une vertu de systèmes formels, une affaire de mathématiciens. La connaissance, elle, est de la famille de la [[memory]] — et une mémoire est sélective par nature : un héritage se transmet, il ne transmet jamais tout. Exiger d'un corpus de connaissance qu'il soit complet, c'est se tromper d'objet. Lui demander d'être cohérent, en revanche, c'est lui demander ce qu'une mémoire sait faire. Newton lui-même n'est pas monté sur *tous* les géants : il a choisi ses épaules. 

D'une formule : 

> [!note] 
> Un [[knowledge]] [[layer]] réduit la dispersion sémantique du fait qu'il laisse de plus fortes traces neurologiques dans la _tête_ du modèle par rapport aux traces laissées par un prompt ; traces qui agissent comme un harnais sémantique ([[agent harness]]) réduisant la probabilité qu'un [[token]] s'éloigne d'un champ sémantique. 

Il fallait s'y attendre. Un [[AI prompt]] est un ordre, une consigne — un acte qui s'épuise dans son exécution. La [[knowledge]] est une [[memory]] — une chose qui persiste. Une commande passe, une mémoire reste ; rien d'étonnant à ce que la première laisse des traces plus légères que la seconde. La dispersion sémantique se lit alors pour ce qu'elle est : le visage que prend l'ignorance chez un modèle. Un modèle qui ne sait pas *erre* dans l'espace des tokens ; un modèle qui sait s'en tient à son champ. 

Et le harnais sémantique mérite son nom. Un [[agent harness]], c'est tout ce qui n'est pas le modèle : le code, les outils, les contraintes qui donnent un **état** à un modèle qui n'en a pas. Le harnais sémantique, lui, est fait de traces neuronales : il travaille *dans* la tête du modèle. Ce que le logiciel impose de l'extérieur, l'héritage l'impose de l'intérieur — même geste, contraindre pour rendre capable, appliqué aux poids plutôt qu'au code. On retrouve [[2026-06-28 - The Society of Knowledge - Words and weights as marks]] : les mots et les poids ne dénotent pas, ils **contrôlent**. Un [[knowledge]] [[layer]] n'est pas un stock de significations ; c'est un dispositif de contrôle des cascades d'activation. Un harnais, précisément. 

## La connaissance faite héritage 

Regardons dans la tête d'un LLM qui s'est vu injecter un [[knowledge]] [[layer]] et un prompt puis regardons dans la tête d'un LLM qui n'a vu que le [[AI prompt]] (ci-dessous)

![[KL_no_KL.png]]

Pour les LLM avec un [[knowledge]] [[layer]], chaque [[token]] généré active plus de neurones liés à la connaissance que de neurones liés aux [[token]]s nouvellement générés. Pour le LLM sans [[knowledge]] [[layer]], c'est l'inverse, le modèle active plus de neurones en lien avec le [[token]] généré que de neurones en lien avec le prompt (qui fait ici office de contexte). 

L'image donne la mesure : la *serial dominance* (part du [[token]] précédent dans la prédiction suivante) chute de 5 à 3 avec le [[knowledge]] [[layer]], pendant que les clusters d'activation passent de 44 à 84 et les étapes de génération de 6 à 3. Avec [[layer]], le modèle s'appuie moins sur ce qu'il vient de dire et plus sur ce qu'il sait. 

De cette observation néé cette hypothèse très séduisante : le [[knowledge]] [[layer]] laisse des traces si importantes dans la tête du modèles qu'elles sont plus sollicitées que les traces plus fraiches laissées par la prompt. On peut dire que le LLM fait de la connaissance un héritage dans lequel il puise pour générer les tokens. « Héritage » n'est d'ailleurs pas une métaphore : la [[knowledge]] est de la [[memory]], et puiser dans des traces déposées antérieurement, c'est très exactement ce que fait une mémoire. 

On reconnaît Newton. Toute nouvelle connaissance s'appuie sur du déjà-déposé plus qu'elle n'invente ; un LLM doté d'un [[knowledge]] [[layer]] sollicite davantage les traces de la connaissance que celles de ses propres [[token]]s ; le [[knowledge]] [[layer]] est au modèle ce que les géants furent à Newton — le point d'appui d'où l'on voit plus loin. Voir plus loin, réduire la dispersion sémantique : c'est le même phénomène, générer juste au-delà de ce que permettent ses seules traces fraîches. 

Les options d'hier ([[2026-07-12]]) en sortent réordonnées. Je cherchais la cause dans les circuits eux-mêmes — mieux organisés, plus inhibiteurs. Elle se tient peut-être ailleurs : non dans ce que valent les circuits, mais dans la profondeur relative des traces qu'ils portent. Des traces dominantes captent l'activation au détriment des circuits perturbateurs — l'inhibition n'est plus une cause, c'est un effet de l'héritage. Quant au hasard expérimental, trois indicateurs concordants dans une même image commencent à faire beaucoup pour lui. 

Et comme tout héritage, il permet d'expliquer, de délimiter les bornes au sein desquelles un élément nouveau, encore non-observé, atterrira avec une quasi-certitude. Zola écrivait à ce propos, mais en parlant des sociétés humaines : 

> [!quote] 
> "L'hérédité a ses lois, comme la pesanteur (et) je tâcherai de trouver et de suivre, en résolvant la double question des tempéraments et des milieux, le fil qui conduit **mathématiquement** d'un homme à un autre homme"

Si l'hérédité a ses lois, elles sont testables. Plus l'héritage est profond, moins le modèle devrait dépendre du [[token]] précédent : la *serial dominance* doit chuter à mesure que le [[knowledge]] [[layer]] s'enrichit. Si c'est bien la profondeur des traces qui compte, et non leur source, un prompt assez répété devrait finir par mimer un [[layer]] — et s'il n'y parvient jamais, c'est que la différence est de nature et non de degré, et l'hypothèse tombe. Enfin, si l'héritage délimite les bornes où atterrit le nouveau, le champ sémantique des tokens devrait pouvoir se lire *avant* génération, dans le seul [[layer]] : le fil qui conduit mathématiquement d'un [[token]] à un autre [[token]]. Les métriques de [[2026-07-02 - Proving knowledge drives token efficiency]] en donnent déjà un premier point — 89% de similarité sémantique avec [[layer]], 28% sans : moins de dispersion, moins d'itérations, moins de [[token]]s. 

## La boucle se ferme 

Relisons GW150914 avec ces lunettes. La théorie d'Einstein est le [[knowledge]] [[layer]] de la physique ; le pépiement entendu par Marco Drago est le [[token]] nouveau qui atterrit exactement dans les bornes délimitées par l'héritage, cent ans plus tard, avec la quasi-certitude que prédisait Zola. La découverte n'a pas dispersé le champ sémantique de la physique — elle a confirmé qu'un héritage assez profond rend le nouveau prévisible. Sur les épaules des géants, on ne voit pas ailleurs : on voit plus loin, dans la direction que les géants regardaient déjà.


***


