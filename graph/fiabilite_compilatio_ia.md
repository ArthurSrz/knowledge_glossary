---
toexplainWith: "[[Bayes' theorem]]"
uses:
  - "[[Recall]]"
  - "[[Precision]]"
  - "[[Accuracy]]"
---
Le **détecteur de contenu IA Compilatio** permet de **distinguer les textes humains des textes générés par les Intelligences Artificielles** pour ainsi vérifier l’authenticité des écrits.  

## **Comment bien mesurer la fiabilité du système Compilatio pour la détection de textes rédigés par IA ?**

L’efficacité de la détection de contenus d’IA s’appuie sur, à la fois :

- **la capacité du moteur de détection** à étiqueter "IA" ou "humain" chacun des extraits de **texte homogène** qui lui sont présentés (t_exte homogène = texte entièrement généré par IA ou texte entièrement rédigé par humain)_
- **la capacité de l’analyse Compilatio** à identifier dans un **document hétérogène** les passages attribuables à un auteur humain ou IA (_texte hétérogène = texte contenant un mélange de textes rédigé par un humain et de textes générés par IA)_

Note : les mesures de performance indiquées dans cet article sont valables pour le système Compilatio de détection de textes IA version 4.2.1, utilisé depuis le 15 octobre 2024.

## **La fiabilité du moteur de détection de texte IA**

### Le rôle du moteur de détection : étiqueter "IA" ou "humain" des courts extraits de textes

Le moteur de détection Compilatio utilise un **modèle de langue** (une intelligence artificielle spécialisée dans le traitement des langues) **spécifiquement entraîné à déterminer** si un texte s'apparente à une production provenant d'une IA ou d'un humain.

Ce « moteur de détection » reçoit les textes de sources inconnues et détermine, selon le **style d'écriture**, lesquels se rapprochent de textes rédigés par un humain et ceux rédigés par une intelligence artificielle.

**_![](https://support.compilatio.net/hc/article_attachments/24099623144593)_**

### Les mesures de fiabilité du moteur de détection

Pour avoir un **regard complet sur la fiabilité**, il convient de mesurer **plusieurs indicateurs** : la précision (precision), le rappel (recall) et l’exactitude (accuracy). Pour mieux comprendre comment sont calculés ces indicateurs, consultez les articles suivants : "_[Précision et rappel](https://fr.wikipedia.org/wiki/Pr%C3%A9cision_et_rappel)_" et "_[Exactitude et précision](https://fr.wikipedia.org/wiki/Exactitude_et_pr%C3%A9cision)_".

- **Précision du moteur de détection Compilatio : 98,5%**  
    La précision = la capacité du moteur à ne pas se tromper.  
    Cela signifie que sur 100 passages identifiés par le moteur comme “texte rédigé par une IA”, 99 ou 98 sont bien générés par une IA et seulement 1 ou 2 sont en réalité rédigés par un humain.
- **Rappel du moteur de détection Compilatio : 99%**  
    Le rappel = la capacité du moteur à ne rien oublier.  
    Cela signifie que sur 100 passages IA qu’il faut identifier, 99 sont correctement trouvés et 1 seul ne l'a pas été. 
- **L’exactitude du moteur de détection Compilatio : 99%  
    **L'exactitude = la capacité à étiqueter correctement (humain ou IA) les textes.  
    Cela signifie que sur 100 passages à étiqueter (humain ou IA), 99 ont été correctement étiquetés.

Le moteur de détection Compilatio affiche **un taux de faux positifs inférieur à 1,5%.**

Ces mesures ont été réalisées sur environ 7.000 textes en 24 langues. L’échantillon était constitué de 3.700 textes rédigés par des humains et 3.300 textes rédigés par Intelligence Artificielle.  
Les prompts ont formulé des questions simples sans demander d'adaptation du style à l'IA.

## **La fiabilité de l’analyse Compilatio**

La tâche effectuée par Compilatio lors de l’analyse d’un document n’est pas uniquement de juger si des textes sont attribuables à 100% à l’IA ou à 100% aux humains (comme le fait le moteur de détection d’IA).

**Le rôle de l’analyse est d’identifier et de quantifier les passages** susceptibles d’être rédigés par une IA ou par un humain **dans un texte contenant un mélange** des deux sources (document hétérogène).

**_![](https://support.compilatio.net/hc/article_attachments/24099623156753)_**

**La performance finale du système Compilatio pour détecter les textes rédigés par IA  
est de** **9/10**.

Cela signifie que dans un document contenant 10 passages à étiqueter (humain ou IA), 9 sont correctement étiquetés.

L’illustration ci-dessous est représentative du niveau d’efficacité mesuré, pour le système actuellement proposé par Compilatio :

![FR-Détecteur IA Compilatio-Fiabilité.png](https://support.compilatio.net/hc/article_attachments/19412602232337)

## **Précaution à prendre concernant les mesures d’efficacité**

Les statistiques communiquées décrivent la **performance globale** du service sur un grand nombre de documents représentatifs de travaux d’étudiants.  
Dans les faits, les sources (IA ou humain) de certains passages/documents peuvent être parfaitement identifiés, et d’autres moins bien. Gardez à l’esprit que la détection d’IA s’appuie sur la reconnaissance de caractéristiques stylistiques typiques des textes rédigés par une IA ; il peut arriver qu’un humain ait un style similaire à celui d’une intelligence artificielle.

**Aucun détecteur d'IA ne peut être fiable à 100%.** 

**Les taux de fiabilité communiqués par les détecteurs d'IA** **ne sont pas comparables !** Il est difficile de comparer objectivement la fiabilité des outils de détection d'IA si les environnements de test diffèrent.

Les mesures peuvent changer en fonction de plusieurs facteurs : source et langue du corpus, nombre de documents testés, modèle d'IA générative utilisé, origine des documents humains, engagement de l'entreprise à ne pas manipuler les résultats...

Il est primordial de se rappeler que les outils Compilatio fournissent des **indications** sur des passages suspects. **Il revient toujours au correcteur d'interpréter ces informations pour valider ou imputer les fraudes potentielles**. En cas de doute, procédez à un examen plus approfondi des connaissances de l’étudiant sur les passages suspects.

Pour déterminer si nos solutions sont adaptées à vos besoins, nous vous invitons à _[contacter nos conseillers](https://www.compilatio.net/magister-plus#form)_.

## **Est-ce que le détecteur d'IA Compilatio est multilingue ?**

**Oui, le détecteur d'IA Compilatio est multilingue.** Il permet d'identifier les contenus IA dans  
plusieurs langues : français, anglais, espagnol, italien, portugais, russe, arabe, hindi et autres langues du monde entier !

**Les mesures de fiabilité ont été réalisées sur des textes en 24 langues :** allemand, anglais, arabe, croate, danois, espagnol, finnois, français, grec moderne, hindi, hongrois, italien, néerlandais, norvégien, polonais, portugais, roumain, russe, serbe, slovaque, slovène, suédois, tchèque, ukrainien.

## **Le détecteur d'IA Compilatio s'adaptera-t-il aux avancées permanentes des IA ?**  

Consultez la réponse ici : _[https://support.compilatio.net/hc/fr/articles/17435773405329-Le-d%C3%A9tecteur-d-IA-Compilatio-s-adapte-t-il-aux-avanc%C3%A9es-permanentes-des-IA](https://support.compilatio.net/hc/fr/articles/17435773405329-Le-d%C3%A9tecteur-d-IA-Compilatio-s-adapte-t-il-aux-avanc%C3%A9es-permanentes-des-IA)_

   * Rappel :   
   Le détecteur d'IA Compilatio est accessible avec l'abonnement à l'offre Compilatio Magister+.   
   Pour en savoir plus, consultez notre site internet : [https://www.compilatio.net/magister-plus](https://www.compilatio.net/magister-plus)