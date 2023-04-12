# script_decision_by_criterion

Ce projet d'aide à la décision permet d'appliquer la méthode Electre I qui est une méthode multicritère d'aide à la décision. Cette méthode permet de classer des alternatives selon plusieurs critères. Les critères pris en compte sont Cr1, Cr2, Cr3, Cr4, Cr5, Cr6, Cr7 et les actions à évaluer sont P1, P2, P3, P4, P5, P6.

Le projet propose une matrice de concordance ainsi qu'une matrice de discordance permettant de calculer les concordances et discordances entre les différentes actions en fonction des critères choisis. Ces matrices permettent d'obtenir un classement des alternatives selon leurs performances.

Le projet propose également une valeur de seuil c qui permet de sélectionner les couples d'alternatives qui ont une concordance supérieure ou égale à cette valeur de seuil. Les couples d'alternatives ainsi sélectionnés sont stockés dans une liste nommée couples.

Le code Python proposé calcule également le delta qui est la plus grande différence entre les performances de deux actions pour un même critère. Ce delta permet d'obtenir une mesure de l'écart entre les différentes actions pour chaque critère.
