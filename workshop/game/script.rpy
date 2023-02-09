

# --------------------------------------------------------------------------
# -------------------------------- IMAGES ----------------------------------

# ----- Scenes -----


# ----- Personnages -----




# --------------------------------------------------------------------------
# ----------------------------- PERSONNAGES --------------------------------


# Declarartions des personnages principaux / Love interests
define got = Character('Marie-Anne', color="#c8ffa8")
define punk = Character('Patrick', color="#ffa8a8")
define hippie = Character('Jeanne', color="#ffffa8")

# Declarations des personnages secondaires
define march = Character('Marchand', color="a8a8ff")
define skh = Character('Skinhead', color="ff8080")
define voisine = Character('Vieille Voisine', color="cc8888")




# --------------------------------------------------------------------------
# --------------------------------------------------------------------------


# Le jeu commence ici
label start:
    python:
        nom = renpy.input("Quel est ton nom ?")
        nom = nom.strip() or "Personne"

    # Declaration des amities
    $amitie_got = 0
    $amitie_hippie = 0
    $amitie_punk = 0

    # Declaration des flirts
    $flirt_got = False
    $flirt_hippie = False
    $flirt_punk = False

    $nbRejets_hippie = 0
    $jour = 0
    $nbBieres = 0
    $pasInterrompre = False


    # --------------------------------------------------------------------------
    # ----- JOURNEE 1 -----
    $jour += 1

    # afficher interieur studio
    "Tu t'appelles [nom]."

    "(Téléphone sonne)"
    "(Décroche le téléphone)"
    "Moi" "Allô? Oui maman! Oui je suis bien arrivé !"
    "Moi" "Oui je suis allé au studio tout à l’heure, le travail à l’air intéressant."
    "Moi" "On doit préparer un festival dans un mois et je dois aller rencontrer quatre groupes qui vont chacun faire une représentation si j’ai bien compris."
    "Moi" "Oui je te tiens au courant maman."
    "Moi" "Moi aussi je t’aime, je dois aller au studio je te rappelle plus tard. Bisous !"

    "Bon je dois me préparer maintenant, et me dépêcher d’y aller, je crois que je suis déjà en retard !"

    # afficher devanture studio
    "Le bus ne m’a pas aidé pour mon retard…"
    "Je crois que je me suis pas trompé de rue cette fois, pas comme ce matin haha !"
    "Par contre j’entends deux femmes qui ont l’air de se disputer, le quartier a l’air un peu dangereux..."

    # afficher interieur studio et got, hippie au premier plan, punk derriere en petit
    "Gothique" "Mais putain ! Tu m’as désaccordé ma guitare ! Pourquoi tu touches à mes instruments, reste avec ton djembé dans ton coin !"
    "Hippie" "C’est bon pas besoin de s’énerver, ça se réaccorde facilement."
    "Hippie" "Est-ce que tu peux éviter d’élever la voix maintenant ?"
    "Hippie" "J’aimerais que l’ambiance soit agréable pour accueillir notre nouvel ingé son..."

    "..."
    "Les voix de femmes proviennent en fait de mon studio..."
    "Il n’y a qu’elles ainsi qu’un homme posé dans un coin dans cette pièce, il a l’air d’observer comment se déroule la dispute depuis plusieurs minutes maintenant."
    "Elles ne m’ont visiblement pas vu, trop investies dans leur discussion"

    "Est-ce que je les interrompt pour les prévenir de mon arrivée ?"
    menu:
        "oui":
            jump choix1_oui

        "non":
            jump choix1_non


    label suite1:
        "Les membres des deux groupent partent ensuite se reposer après m'avoir demandé de les appeler rapidement pour reprendre les répetitions."
        "Bon, maintenant qu’elles sont parties, je vais pouvoir m’y mettre. "
        "Qui est-ce que j’enregistre aujourd’hui déjà ?"
        "Ah oui les \"Perruquiers noirs\"."
        "C’est à ce moment que l’homme qui semblait s’amuser de la dispute de tout à l'heure ouvre violemment la porte."
        "Il rentre dans la petite pièce puis me salue d’un mouvement de tête."
        "Moi" "Bonjour, enchanté de vous rencontrer, je suis le nouvel ingé-son, [nom]. J’..."
        "Punk" "Ouais ouais, super super. "
        punk "Moi c'est Patrick."
        punk "Contente-toi d'enregistrer et silence. Et t’as pas intérêt à foirer."

        "Oups, je crois qu'il vaudrait mieux éviter de trop lui parler..."
        #fondu noir
        "La séance se passe, puis arrive la fin de la journée."
        "Patrick sort du studio et me laisse ainsi seul."

        "J’aurais aimé avoir une première journée moins agitée..."
        "Les deux filles étaient intéressantes cependant, chacune à leur manière."
        "Vu que je ne suis pas encore fatigué, autant visiter un peu la ville, pour me familiariser avec."

        menu:
            "Visiter un parc":
                $amitie_got += 1
                jump choix2_got

            "Partir faire des courses":
                $amitie_hippie += 1
                jump choix2_hippie

            "Aller boire un verre au bar":
                $amitie_punk += 1
                jump choix2_punk

        jump suite1_done
    label suite1_done:

    label suite2:

        # rue la nuit
        "Il commence à se faire tard, la nuit est déjà tombée. "
        "Je travaille également demain, avec l'autre groupe que je n’ai pas encore rencontré."
        "Je vais essayer de ne pas faire de folies ce soir et avoir l’air frais pour donner une bonne première impression."
        # image devanture immeuble
        "En arrivant devant mon immeuble, je remarque quelques personnes en train de fumer devant l’entrée, discutant bruyamment sans faire attention aux autres personnes alentours."
        "D’ailleurs, ils semblent ignorer volontairement les personnes essayant d’entrer, présentement une vieille personne avec son caddie à courses, qui essaye de les interpeller sans succès."
        "Les trois personnes, chauves, vont jusqu’à pousser la vieille femme lorsqu’elle tente de passer à coté d’eux, la faisant chuter lourdement au sol. "
        "Je ne peux pas rester sans réagir."

        "Moi" "Eh ! Qu’est ce que vous pensez faire là ? Ça va pas ?"

        "Aidant la vieille femme à se relever, je fusille les trois voyous du regard. "
        "Ils portent des vestes militaires et me rendent mon regard. "
        "Je frisonne en remarquant le tatouage sur la nuque de l’un d’entre eux, rappelant les heures sombres du pays."
        "C’est bien ma veine, de tomber sur des skinheads si peu de temps après avoir emménagé."
        "S’ils traînent dans le voisinage, il faudra que je fasse attention."
        "Voyant qu’il ne réagissent cependant pas plus que ça, se contentant de ricaner, je les ignore et aide la vieille femme à rentrer dans l’immeuble. "
        "Par un fait du hasard, elle se trouve être ma voisine de palier."

        voisine "Merci beaucoup monsieur. Ces voyous rendent la vie ici impossible, ils se croient tout permis ! "
        voisine "Cela fait plaisir de voir qu’il y a encore des gens bien dans ce monde."
        "Moi" "Ils sont souvent par ici ?"
        voisine "Oh oui ! Mais ils traînent également dans d’autres quartiers, à faire chasse à tous ceux qu’ils jugent \" impures \". "
        voisine "Vous devriez faire attention à vous jeune homme, ils vous chercheront sûrement des noises après ce soir."
        "Moi" "Pas de soucis madame, je sais me défendre. Je vous souhaite une bonne soirée cependant, je dois me lever tôt demain."
        voisine "Il n’y a pas de soucis. Passez prendre une tasse de thé un de ces quatre. Bonne soirée."

        # image interieur appartement
        "Je rentre dans mon appartement, laissant la vieille femme rentrer chez elle."
        "Je ne m’attendais pas à passer une soirée si agitée. Il faudra que je fasse attention dans le voisinage désormais. "
        "Le coin n’est clairement pas aussi tranquille que le prétendais le promoteur immobilier."
        "La journée à été longue, autant aller se coucher directement."


        #METTRE FONDU NOIR

        # ------------------------- JOURNEE 2 (PAS JOUABLE) -------------------------------------
        $jour += 1
        "Allez, c’est parti pour une nouvelle journée de travail. "
        "Je me demande pourquoi le groupe d’aujourd’hui ne voulait pas faire la présentation en même temps que les autres."
        #scene studio
        "Enfin, ils ne devraient pas tarder."

        #afficher skinhead
        skh "Oy, c’est toi le nouveau ?"

        "Oh bon sang."

        skh "Mais quelle bonne surprise ! Si c’est pas le gringalet d'hier soir ! "
        skh "Je sens qu’on va bien s’amuser ensemble."
        "Moi" "Vous êtes le groupe Plus Plus Plan ? "
        skh "Et comment ! Tu trouveras pas meilleur que nous dans le coin. "
        skh "Les trois autres groupes minables de ce studio ne nous arrivent pas à la cheville ! "
        skh "Tu vas voir que lors de votre festival minable, c’est nous qui allons tout remporter. "
        "Moi" "Eh bien nous allons pouvoir voir ça. La séance d’enregistrement va commencer, vous pouvez y aller."

        #fondu noir pour faire comprendre qu'on est plus tard
        "Ça m'embête de le dire, mais ils sont effectivement très doués. "
        "C’est frustrant, mais en l’état, ce sont les favoris pour gagner le festival."

        skh "Alors minable, t’en as pensé quoi ? Ça envoie du lourd non ?"
        "Moi" "C’est pas mal en effet. Je ne pense pas que vous ayez besoin de plus de sessions avant le festival. "
        "Moi " "Je vais me concentrer sur les autres groupes d’ici là."
        skh "Ah ! Dis plutôt que t’as la trouille de nous revoir ! "
        skh "Mais ça nous va, moins on voit ta gueule de fouine, mieux on se porte. Et ça nous donne plus de temps pour… He he he…"

        "Je n’ai même pas envie d’imaginer ce qu’il laisse sous entendre. "
        "La journée à été suffisamment épuisante comme ça, juste par leur présence malsaine dans le studio."
        # image interieur appart
        "Je rentre chez moi sans incidents. "
        "Demain, il faudra que je choisisse quel groupe appeler pour une session d’enregistrement. "

        #fondu noir

        jump suite2_done
    label suite2_done:

    # --------------------------------------------------------------------------
    # ----- JOURNEE 3 -----
    $jour += 1

    "Le bruit de mon réveil insupportable me tire de mon sommeil."
    "Après la journée d'hier, j'ai une petite appréhension de comment celle d'aujourd'hui va tourner."
    "Un café et une tranche de pain puis direction le studio."
    #afficher image studio

    # Aller chez le marchand ou non ?
    "Est-ce que je passerais pas à la supérette du coin avant pour voir ce qu'ils proposent aujourd'hui ?"
    menu:
        "Pourquoi pas ?":
            jump magasin
        "Je suis déjà en retard...":
            "Une autre fois peut-être..."


    label suite02:
        "En arrivant je découvre cette fois le studio dans un silence assez effrayant. "
        "Aujoud'hui je vais devoir choisir un des trois groupes que j'ai rencontré hier pour commencer à enregistrer."
        "J'hésite..."
        jump suite02_done
    label suite02_done:

    # Decision session studio de la journée
    menu:
        "Je vais appeler le groupe \"Effervecence\".":
            $amitie_got += 1
            jump choix3_got

        "Le groupe \"Quatuor\" m'avait bien plus hier.":
            $amitie_hippie += 1
            jump choix3_hippie

        "J'ai envie de voir ce que peut donner le groupe de \"Perruquiers noirs\" aujourd'hui.":
            $amitie_punk += 1
            jump choix3_punk


    label suite3:
        # CHANGER DIALOGUES
        "Je suis enfin chez moi."
        "rompiche"


    # --------------------------------------------------------------------------
    # ----- JOURNEE 3 -----
    $jour += 1


    "Dans le noir, le studio a une allure terifiante."
    "Les ombres des instruments peuvent ressembler à des créatures tapies dans la pénombre."
    "Mais il me suffit d’un seul bouton pour les faire disparaître."
    "J'allume la lumière puis un reflet sur le côté attire mon œil vers le téléphone du studio."
    "Est-ce que je n'irai pas passer à coup d'oeil au magasin avant d'appeler un groupe ?"
    # Aller chez le marchand ou non ?
    menu:
        "Aller à l'Epicerie du Soleil":
            jump marchand_oui
        "Rester au studio d'enregistrement":
            "Je vais me concentrer sur les groupes..."

    label suite03:
        "Je suis content de mes achats."
        jump suite03_done
    label suite03_done:

    # Decision session studio de la journée
    menu:
        "\"Effervecence\" me fait de l'oeil.":
            $amitie_got += 1

            jump choix4_got



        "Je vais appeler \"Quatuor\" aujourd’hui.":
            $amitie_hippie += 1

            if flirt_hippie:
                "Dans un but purement professionnel, bien sûr."
            "La session se passe extrêmement bien, le groupe à bien progressé en quelques semaines."
            "Après la session, Jeanne vient me voir."

            hippie "Hey beau gosse, comment tu vas ? "
            hippie "Merci pour la session d'enregistrement, on a vraiment progressé aujourd'hui. "
            "Moi" "C'est vrai, vous étiez incroyables. "
            "Moi" "Vous êtes clairement devenus les favoris pour le festival."
            hippie "Hihi, disons qu'en plus de vouloir plaire au public, il y a une personne de plus à qui j'aimerais bien plaire."

            "Je sens le fard me monter aux joues. "
            "Je ne suis pas d'un naturel prude, mais cette fille fait ressortir de moi des aspects dont j'ignorais l'existence. "
            "Et ce n'est pas pour me déplaire."

            hippie "Sinon, cet aprem il y a une manif pour le bien être animal, mais si tu es libre ce soir, ça te dirait de me rejoindre dans le parc du Thabor ?"
            "Moi" "C'est un rencard que tu me proposes ?"
            hippie "Hihi, peut-être bien."

            menu:
                "Je serais là !":
                    jump date2_hippie


                "Je suis désolé, je ne pense pas que ça soit une bonne idée.":
                    "Moi" "Je t'apprécie énormément, mais je pense que nos relations doivent rester professionnelles."
                    hippie "Oh… Je… Je croyais que... "
                    hippie "Je suis désolée."

                    "Jeanne part en courant avant que je puisse l'arrêter."
                    #CHANGER ICI
                    if (nbRejets_hippie >= 4):
                        hippie "jai fait une overdose bg"
                        #changer dialogues ici
                        jump badEnding_2


        "Je préfererai enregistrer avec les \"Perruquiers noirs\".":
            $amitie_punk += 1

            if (amitie_punk >= 4):
                jump choix4_punk
            else:
                jump choix3_punk




    # --------------------------------------------------------------------------
    # ----- JOURNEE 4 -----
    $jour += 1

    "Le studio commence vraiment à m'être familier."
    "Les ombres des instruments ne me font plus croire à des monstres ou autres."
    "Le reflet des lumières en allumant continue par contre à attirer mon oeil vers le téléphone."
    "Est-ce que je vais chez les marchand pour voir s'il a des nouveautés ?"
    # Aller chez le marchand ou non ?
    menu:
        "Pourquoi pas ?":
            jump marchand_oui
        "Je crois que j'en ai assez vu.":
            "Je vais me concentrer sur mon travail."
            "Le festival arrive à grands pas."

    label suite04:
        "Courses productives"
        jump suite04_done
    label suite04_done:


    "C’est la dernière session d’enregistrement avant le festival."
    # Decision studio
    menu:
        "Le groupe \"Effervecence\" me plait bien.":
            $amitie_got += 1

            if flirt_got:
                got "Allo ? [nom] ?"
                "Moi" "Oui, j’ai une surprise qui je pense va te plaire. "
                "Moi" "Tu peux venir faire une session de suite ?"
                got "J’ARRIVE !"
                jump date3_got
            else:
                jump choix4_got

        "Je vais appeler \"Quatuor\".":
            $amitie_hippie += 1

            "Moi" "Hey ! Super session comme d’habitude. "
            "Moi" "Vous vous sentez prêt pour le festival ?"
            hippie "Plus que jamais, on va tout déchirer. "
            "Moi" "Haha, super, je sens que vous êtes motivés. On se revoit là-bas ?"
            hippie "Attends ! ça te dirait de venir à ma roulotte ce soir ?"
            hippie "Je t’aurais bien dit de venir avant, mais il y a encore une autre manif auquel je dois participer."

            menu:
                "J'ai vraiment envie de me rapprocher d'elle.":
                    jump date3_hippie

                    "Je préfère que l'on se concentre sur le festival."
                    jump neutralEnding_2




    # TOUS LES CHOIX

    # --------------------------------------------------------------------------
    # Aller chez le marchand ou non ?

    label magasin:
        hide screen inventory
        show astride with dissolve
        march "Bienvenue dans mon humble boutique ! Que désirez vous acheter ?"

        show screen bracelet
        show screen canette
        show screen pendentif
        $ renpy.pause()

        jump magasin_done
    label magasin_done:


    label achat_bracelet:
        hide screen bracelet
        hide screen canette
        hide screen pendentif

        if thune<200:
            march "Vous n'avez pas assez d'argent !"
            jump magasin
        else:
            $ thune = thune-200
            $inventaire.append(braceletOS)
            #ligne de commande pour afficher inventaire
            #ajouter un hide screen inventory quand on veut le cacher
            show screen inventory

            march "Merci pour votre achat !"
            jump magasin
        jump achat_done

    label achat_canette:
        hide screen bracelet
        hide screen canette
        hide screen pendentif

        if thune<200:
            march "Vous n'avez pas assez d'argent !"
            jump magasin
        else:
            $ thune = thune-200

            $inventaire.append(canetteP)
            #ligne de commande pour afficher inventaire
            #ajouter un hide screen inventory quand on veut le cacher
            show screen inventory

            march "Merci pour votre achat !"
            jump magasin
        jump achat_done

    label achat_pendentif:
        hide screen bracelet
        hide screen canette
        hide screen pendentif

        if thune<200:
            march "Vous n'avez pas assez d'argent !"
            jump magasin
        else:
            $ thune = thune-200

            $inventaire.append(pendentifH)
            #ligne de commande pour afficher inventaire
            #ajouter un hide screen inventory quand on veut le cacher
            show screen inventory

            march "Merci pour votre achat !"
            jump magasin
        jump achat_done
    label achat_done:



    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # Choix 1 : Interrompre les deux femmes ou non
    label choix1_oui:
        if pasInterrompre:
            $interrompre = False
        else:
            $interrompre = True

        "Moi" "Bonjour, est-ce que je pourrais savoir qui vous êtes ?"
        "Gothique" "Excusez-moi mais que faites vous ici ? Comment avez vous fait pour rentrer ?"
        "Moi" "Je suis [nom] . J'ai été embauché en tant qu'ingé son dans ce studio. Et pour répondre à votre question, la porte était ouverte."
        "Hippie" "Hahahaha !"
        "Moi" "Pourriez vous me dire qui vous êtes ?"

        hippie "Excusez moi hahaha ! Je suis Jeanne, membre du groupe \"Quatuor\", on m'a dit de venir aujourd'hui concernant un festival donc me voici !"
        hippie "C'est un plaisir de vous rencontrer"
        got "Ouais, désolée. Je m'appelle Marie-Anne et suis la guitariste de mon groupe \"Effervecence\"."

        "L'homme qui observait la dispute se lève sort par la porte qui mène à l'arrière du studio."

        "Nous continuons à discuter jusqu'à ce que, en effet, les autres membres de chaque groupe arrivent."
        "J'ai également appris que le quatrième groupe qui devait venir ne viendrait en fait que demain, seul."
        "Un peu déçu de ne pas les voir, je me concentre tout de même sur les trois qui se trouvent en face de moi."
        "\"Quatuor\" et \"Effervecence\" passent l'un après l'autre pour me montrer quelques titres qu'ils produisent chaque semaine dans des bars."
        "Les deux groupes sont uniques et ont leur patte qui les diffèrent de l'autre."


        jump choix1_done

    label choix1_non:
        $pasInterrompre = True

        # ECRIRE ICI
        "Gothique" "Il est déjà en retard, je ne pars pas sur de bonnes bases avec lui personnellement."
        "Gothique" "Qu'il aille se faire voir s'il ose se plaindre parce qu'on accueille mal."
        "Hippie" "Marie-Anne du calme."
        "Gothique" "Je me calmerai quand je le verrai pointer le bout de son nez !"
        "Gothique" "C'est pas une hippie comme toi qui va me dire quoi faire !"

        "Je crois qu'elles vont bientot en passer aux mains, je ferais mieux de les arrêter maintenant..."
        jump choix1_oui
        jump choix1_done

    label choix1_done:
        jump suite1


    # --------------------------------------------------------------------------
    # Choix 2 : Premiere balade du soir
    label choix2_got:
        $choix2_balade = True

        # ECRIRE ICI
        jump choix2_done

    label choix2_hippie:
        $choix2_magasin = True

        "Après avoir un petit peu tourné dans les rues autour de chez moi, j’ai trouvé une supérette, mais il semble y avoir un attroupement devant."
        "Mais… C’est pas la fille de tout à l’heure avec une pancarte au milieu de la foule ?"

        hippie "Non ! Non ! Non à l’exploitation !"

        "On dirait une manifestation..."
        "Je n’ai pas vraiment envie de me mêler de tout ça, autant chercher un autre magasin."

        hippie "Oh ! Mais tu es l’ingénieur de tout à l’heure ! Tu es venu te joindre à nous ? Comme c’est gentil !"

        "Trop tard, la fille aux vêtements colorés m’a vu."
        "Elle fend la foule et m’attrape par la manche et me regarde avec un sourire béat."

        "Moi" "Euuuh..."

        if interrompre:
            hippie "Ah, je suis contente de voir que tu t’intéresse au bien être animal ! "
            hippie "Je ne savais pas trop quoi penser de toi au studio..."
            hippie "Vu que tu ne m’avais pas laissé finir d’expliquer à cette fille que porter des crânes d’animaux n’était pas très respectueux pour ces pauvres petits écureuils."
            hippie "Mais tu as l’air sympa au final !"
        else:
            hippie "Ah, je suis contente de voir que tu t’intéresse au bien être animal ! "
            hippie "Ce magasin vend des produits qui abîment environnement."
            hippie "On essaye donc de les faire arrêter en protestant devant leur façade, mais ça ne fonctionne pas beaucoup pour l’instant..."

        "Moi" "Je suis sensible à la cause animale, bien sûr, mais ce genre d’attroupement n’est pas du goût de tout le monde..."

        "Je fais un signe en direction d’une patrouille de policiers observant la scène d’un air mauvais. "
        "Ils semblent attendre le moindre débordement pour sauter sur les protestants mal habillés."
        "D’ailleurs, en les observant de plus près, ils sont tous vêtus de la même façon, des habits larges, mais sales."
        "Certains maculés de boue dissimulant des motifs bigarrés multicolores qui couvrent leurs pantalons pattes d’eph."

        hippie "Bah, c’est pas grave, on à l’habitude. Au pire, on se prend quelques coups, mais la cause en vaut la peine."
        "Moi" "Oui alors non. "
        "Moi" "Je comprend que cette cause vous tient à cœur, mais je ne peux permettre à une de mes artistes de se mettre en danger comme ça. "
        "Moi" "Vous voulez bien rentrer chez vous ce soir ? Je vous promet de ne pas acheter de produits à ce magasin."
        hippie "Oh ! Tu cherchais un magasin en fait ? Ne t’inquiète pas, je connais un super magasin si tu veux ! Viens, je te le montre !"

        "Sans regarder si je la suit, la jeune femme rousse part en trombe dans une ruelle adjacente, laissant tomber sa pancarte au sol. "
        "Au moins elle ne se fera pas arrêter avant le festival..."
        "Je décide de la suivre cependant, intrigué par sa fougue et son esprit libre. "
        "Elle me mène au travers de plusieurs ruelles en riant, ses sandales de lin claquant sur les pavés de la ville."
        "Elle s’arrête finalement devant la petite devanture d’une épicerie asiatique, nommée « L’épicerie du Soleil ». "
        "Ironiquement, cette boutique est plus près de chez moi que l’autre magasin, mais je ne l’avais pas remarquée auparavant."

        hippie "Ici tu trouvera tout ce dont tu as besoin ! Et les vendeurs sont super sympas !"
        "Moi" "Je vois. Eh bien merci je suppose."
        hippie "Pas de soucis ! Ça fait plaisir de s’entraider non ? "
        hippie "Oh, c’est presque l’heure de mon cour de yoga ! Il faut que j’y aille, on se revoit bientôt au studio j’espère !"

        "Elle part encore une fois comme une fusée, sans que je la suive cette fois. "
        "Si elle a l’air tête en l’air, elle a également l’air de ne jamais s’arrêter. Une chic fille en vrai."
        "..."
        "Après quelques emplettes, je décide de rentrer chez moi"

        jump choix2_done

    label choix2_punk:
        $choix2_bar = True

        "J’irais bien faire un tour au bar ce soir, ça pourrait m’aider à rencontrer du monde et à me familiariser avec la ville."
        "J'entre dans un bar et m‘approche du comptoir pour commander une bière"

        punk "Hey! Le nouveau! Ramène toi!"
        "Est-ce que je vais le rejoindre ?"
        menu:
            "Oui pourquoi pas.":
                punk "Je savais pas que trainais dans ce genre de trous miteux."
                "Moi" "Il est pas si miteux ce bar."
                punk "(a voix basse) C’est surtout le moins cher oui."

            "(Je n'ai pas trop envie d'aller lui parler...)":
                "Je le vois se lever et se diriger vers moi. J'aurais peut être du accepter..."
                punk "Alors t’es timide ?"
                "Moi" "J’avais cru comprendre que vous préfériez que je me taise."
                punk "Alors déjà, TU, ensuite quand  on bosse tu te tais, mais là on bosse pas."

        if interrompre:
            punk "Par contre, t’as merdé, fallait les laisser s’arracher les cheveux aux deux autres."
            "Moi" "C’était mon premier jour, je ne voulais pas avoir d’ennuis."
            punk "Ouais bah la prochaine fois laisse les en venir au mains, j’ai un billet sur la gothique."

        else:
            punk "D’ailleurs, merci de pas les avoir interrompues direct au studio. "
            punk "Tu m’as fait gagner un billet. "
            "Moi" "Un billet ?"
            punk "Ouais avec les gars on parie sur laquelle aura le dessus a chaque fois qu’elles s’engueulent."

        "Moi " "C’est pas vraiment moral."
        punk "Rien à carrer. "
        punk "Écoute, c’est pas que j’apprécie pas cette discussion, mais c’est bientôt l’heure ou ces tocards de droitards sortent de la fac."
        punk "J’ai bien envie de leur mettre un coup de pression."

        "Patrick se lève et s'en va, me laissant seul face à ma bière."
        "..."
        "Bon, je vais finir ma bière et je vais rentrer."

        jump choix2_done

    label choix2_done:
        jump suite2


    # --------------------------------------------------------------------------
    # Choix 3 : Choix session studio
    label choix3_got:
        $choix3_cimetiere = True

        "Allez, je compose le numéro du groupe de gothique."
        "Le téléphone sonne, chaque bip fais monter en moi une pression étrange."
        "Chaque tonalité sonne en harmonie avec mon cœur."

        got "Hmmmm ! Allo ?"
        "Ca a décroché !"
        "Moi" "Bonjour c'est [nom] l'ingé son d'hier, j'ai décidé de commencer à enregistrer avec votre groupe, il m'avait bien plu."
        got "Oh merde !"
        got "En voyant ta petite gueule on pensait pas que tu nous choisirais en premier."
        got "T'es plus sympa que je pensais ! Bah attends nous, on arrive."

        "Je n'ai même pas eu le temps de répondre qu'elle a déjà raccroché."
        "Au moins ils ont l'air motivés."

        "La séance se passe sans réel problème."
        "Le temps de m'accommoder à mes nouveaux outils, on a perdu un peu de temps, ce qui n'a pas eu l'air de gêner le groupe."
        "Quelques heures ont passé et je crois qu'on arrive à la fin de notre première session d'enregistrement."

        got "Hé le bleu bite ! Ca te dirait de venir à notre petite soirée ?"
        menu:
            "Ouais pourquoi pas.":
                got "Allez suis nous on y va !"
                jump date1_got

            "Je comptais rentrer, je n'ai toujours pas fini de m'installer.":
                "Moi" "C'est gentil d'avoir proposé ceci dit"
                got "Boh pas grave ! Une prochaine fois."

        jump choix3_done




    label choix3_hippie:
        $choix3_diabolo = True


        "Je vais appeler \"Quatuor\" aujourd’hui."
        "Je prends mon téléphone et compose le numéro de leur meneuse, Jeanne."
        "Moi" "Bonjour, c’est à votre tour de passer pour la session d’enregistrement."
        hippie "Super ! On arrive, merci beaucoup !"
        "Moi" "Hey, merci à toi ! A tout de suite !"
        hippie "Hihi, tu veux tant que ça me revoir ? "

        "Le groupe \"Quatuor\" passe la journée au studio et s’améliore beaucoup !"

        "Moi" "La séance est terminée, merci beaucoup."
        hippie "Beau travail aujourd’hui !"
        "Moi" "Merci pour l’occasion, on en avait vraiment besoin…"
        hippie "Merci à toi, c’était sympa !"
        "Moi" "Hey, merci ! Ça fait toujours plaisir de venir ici."
        hippie "On joue de mieux en mieux, le festival n’a qu’à bien se tenir !"
        hippie "D’ailleurs, ce soir on organise un petit atelier de découverte des arts du cirque, ça te tente de venir ? "
        hippie "Je pourrais t’apprendre à jongler."

        menu:
            "Oui, pourquoi pas !":
                $amitie_hippie += 1
                jump date1_hippie

            "Non, désolé...":
                "Moi" "J’ai déjà quelque chose de prévu ce soir… Mais ça aurait été avec plaisir !"
                hippie "Pas de soucis, ça sera pour une prochaine fois !"

        jump choix3_done



    label choix3_punk:
        $choix3_bagarre = True

        "J'appelle un des membres du groupe et leur demande de venir."
        "blablabla"
        #ne pas oublier d'ecrire ici"

        if amitie_punk >= 2:
            punk "Hey [nom], tu trouvais l’autre trou pas trop mal, j’t’attends à la sortie, j’vais te montrer un vrai bar."
            "C’est presque menaçant comme invitation, je me demande si je devrais avoir peur."

            menu:
                "Je pense que je vais sortir par derrière, j’ai un peu peur de Patrick":
                    "..."
                "Je vais sortir par devant, je ne pense pas qu’il soit dangereux.":
                    "..."

            # Dans tous les cas, Patrick se trouve devant la porte
            punk "C’est pas trop tôt, tu traines la patte dis donc !"
            "Moi" "Désolé, je devais fermer le studio."
            punk "Ouais ouais, dépêche toi."
            "Moi" "J’arrive."

            punk "Voilà ça c’est un super bar tu vas voir."
            punk "Allez viens on va se prendre quelques bières."

            "Patrick m'emmène dans des petites ruelles avant de se poser à une terrasse."
            punk "Je te commande un truc ?"

            menu:
                "Je vais prendre comme toi":
                    $nbBieres += 1
                    $amitie_punk +=1

                "Je vais prendre une limonade.":
                    punk "Ah ouais."
                    $amitie_punk -= 1

            punk "Voilà, on est mieux ici. Moins de monde qu’à l’intérieur."
            punk "Tiens, ton verre."
            "Moi" "Je suis surpris, je croyais qu’en tant que musicien tu apprécierait plus les foules."
            punk "C’est pas les foules le problème, c’est les gens."
            punk "J’sais pas si t’as remarqué mais j’ai pas la dégaine classique par ici. "
            "Moi" "Si j’ai bien vu, mais tu ne m’as frappé comme quelqu’un de très préoccupé par ce que les gens pensent de lui."
            punk "C’est pas faux."
            punk "Bon, j’vais m’en reprendre une, tu veux quoi ?"

            "Oups je crois que j’ai touché un sujet sensible."

            menu:
                "Je prends la même bière que toi":
                    $nbBieres += 1
                    $amitie_punk +=1

                "Je vais prendre un cocktail sans alcool":
                    punk "Vraiment ?"
                    $amitie_punk -= 1

            punk "Voilà ton verre."
            "Moi" "Merci. "
            "Moi" "Alors, sinon à part la musique et effrayer des étudiants en droit, tu as d’autres loisirs?"
            punk "A part mon boulot, pas vraiment. "
            punk "Avant on allait chercher les fachos pour les tabasser, mais tout seul c’est moins marrant."
            "Moi" "Les autres ne te suivent plus ?"
            punk "Plus depuis..."
            punk "..."
            punk "Qu’un des nôtres s’est fait salement amocher."

            "Merde j’ai encore appuyé ou il fallait pas."

            "Moi" "Désolé d’avoir..."
            punk "T’excuses pas tu pouvais pas savoir."
            "Moi" "Oui... Mais du coup c’est quoi ton travail ?"
            punk "Je vends des glaces."
            "Moi" " Des glaces ?"
            punk "Tu trouves ça drôle ?"

            "Et de trois. Je les enchaîne ce soir."

            "Moi" "Non non pas du tout."
            punk "Détends toi, j’vais pas t’allumer, c’est bon, c’est vrai que c’est un peu marrant. "
            punk "J’ai juste besoin de payer mes factures. Et vu que ma musique fait pas l’unanimité j’ai besoin d’un job à la con. "
            punk "C’est pour ça que j’participe au festival, même si je gagne pas, j’espère faire passer mon message."
            "Moi" "Ton message ?"
            punk "Tu m’as écouté chanter ou tu te bouche les oreilles quand on enregistre ? "
            "Moi" "Oui, j’ai écouté, tu parles des pourris au pouvoir, ..."
            "Moi" "... des pauvres gens qui se butent au boulot pour rien et de ces salopards de racistes qui se baladent dans nos rues..."
            "Moi" "... et qui seront jamais arrêtés parce que les flics sont de leur côté."

            #punk rougit

            punk "Ouais... C’est l’idée. Je vais retourner en prendre une dernière, tu veux quelque chose ?"

            menu:
                "Encore une bière s'il te plait":
                    $boitBiere = True
                    $nbBieres += 1
                    $amitie_punk +=1

                "Je vais boir de l'eau pour cette fois":
                    punk "T'es nul."

            punk "Tiens."
            "Moi" "Merci."

            "Je regarde Patrick enfiler son verre cul-sec"
            if boitBiere:
                punk "Alors ? Je t’attends là en fait."

                "Je crois qu'il veut que je cul-sec aussi..."
                menu:
                    "Je le suis.":
                        punk "Voilà ! Ça me plaît ! "
                        punk "Allez viens avec moi on va faire un tour et j’te raccompagne chez toi."

                    "Je préfere en rester la...":
                        punk "Je t'imaginais un peu plus dévergondé."


            "En passant à côté d’une ruelle sombre, deux skinhead nous alpaguent."

            skh "Hey mais ce serait pas ce merdeux de Patrick ?"
            "Autre Skinhead" "Je crois bien que si, hey le raté, viens par là !"
            punk "Je crois qu’on va bien s’amuser."

            "OULA ! Patrick frappe un des deux skinhead."

            if nbBieres == 3:
                jump bagarre

            else:
                "Je ne sais pas quoi faire..."
                "Est-ce que je devrait aller l'aider ? Ca a tout de même l'air dangereux..."
                menu:
                    "Je n'ai pas à me poser de questions, je fonce.":
                        jump bagarre

                    "Je préfère partir discrètement.":
                        "..."
                        "J’ai réussi à leur échapper."
                        "J’espère que Patrick aussi... "

        else:
            punk "Beau travail aujourd'hui."
            punk "A demain peut-être."

        jump choix3_done


    label choix3_done:
        jump suite3

    label bagarre:
        #MINI JEU BAGARRE

        #si defaite
        $victoire_bagarre = False
        "Après nous avoir mis tous les deux à terre et nous avoir pris nos portefeuille les skinheads sont partis."
        punk "Putain, on s’est pris une grosse raclée."
        punk "Je pensais que tu aurait été plus utile que ça."
        "Moi" "Désolé, je ne suis pas un grand bagarreur moi."
        punk "J’ai remarqué."

        "--- Votre amitié avec Patrick diminue ---"
        $amitie_punk -= 1

        # si victoire
        $victoire_bagarre = True
        "Après quelques coups reçus, les skinheads ont pris la fuite."
        punk "Bien joué ! Tu lui as bien montré au tien."
        "Je pourrais en dire autant de toi."
        punk "Oh quel plaisir de les voir prendre leur jambes à leur cou."
        "Moi" "Ouais, c’est vrai que c’est grisant, je peux comprendre que tu apprécies autant."
        punk "Tu l’as dit bouffi. Allez, à la prochaine [nom]."

        "--- Votre amitié avec Patrick augmente ---"
        $amitie_punk += 2

        "Tandis que je regarde Patrick s'éloigner, je décide qu'il est temps pour moi de rentrer également."

        jump bagarre_done

    label bagarre_done:
        jump suite3




    # --------------------------------------------------------------------------
    # Choix 4 : Choix session studio
    label choix4_got:
        if amitie_got >= 5:
            got "Allô ?"
            "Moi" "Bonjour c’est [nom], je t’appelle pour savoir si tu avais envie de refaire une session aujourd’hui ?"
            if $choix3_cimetiere:
                # si choix got la veille
                got "Oh oui bien sûr ! ça été hier après que je sois parti ?"
                "Moi" "Nan tu m'as quand même laissé comme un imbécile au milieu d’un cimetière !"
                got "Mais je suis sûre que tu t'es bien amusé nan ?"
                "Moi" "Je peux pas dire le contraire mais je ne te ferai pas ce plaisir !"
                got "Ah ah ! Parfait alors on arrive, à tout à l’heure !"
            else:
                got "OUI ! On arrive !"

            "Sans que je puisse répondre elle raccroche."
            "Je n’ai plus qu' à attendre qu’ils arrivent."
            "Après une session plutôt mouvementée par leur entrain, nous finissons assez tard."
            "Il doit bientôt être 1h du matin maintenant."

            got "Hey ! [nom] t'as faim ? Ca te dirait de venir manger dehors ?"
            menu:
                "Ouais je mangerais bien un truc la.":
                    jump date2_got
                "Je me suis déjà préparé un repas à me réchauffer désolé...":
                    "fin de journee"
                    "tu apprends que la goth est en prison"
                    "----- BAD ENDING 1 -----"
                    jump badEnding_1
                    # coder la fin
        else:
            jump choix3_got

        jump choix4_done


    label choix4_punk:
        # ecrire dialogue de merde passe temps

        punk "Hey, champion, viens par là deux secondes."
        "Moi" "Qu'est-ce qu’il y a, tu as besoin de quelque chose ?"
        punk "Ça te dirait de remettre ça avec les fachos ? "
        punk "J’ai entendu dire qu’ils avaient un rassemblement ce soir."
        menu:
            "(Je vais le suivre, j’ai peur qu'il lui arrive quelque chose de grave.)":
                "Je crois qu'ils n'ont pas compris la dernière fois en effet."
                $amitie_punk += 1
                "--- Votre amitié avec Patrick augmente ---"
                punk "Parfait ! Viens avec moi on va chercher des baramines et on va leur montrer à ces sales fachos!"
                "Moi" "Je te suis."

                "Il attrape un sac au sol que je n’avais pas vu et me met un pied de biche dans les mains après en avoir attrapé un pour lui."
                punk "C’est parti, on va les démolir."

                "Est-ce que j'essaie de le convaincre de se calmer et de ne pas y aller ?"
                # MINI JEU CONVAINCRE LE PUNK DE NE PAS Y ALLER

                # si echec
                "je l'accompagne ou pas ?"
                menu:
                    "oui":
                        jump badEnding_3
                    "non":
                        jump badEnding_4

                # si reussite
                jump date1_punk



            "(J’ai trop peur de me faire démolir. Je n’y vais pas.)":
                $amitie_punk -= 3
                "Moi" "Ce sera sans moi haha..."
                punk "Mauviette ! "
                punk "Allez dégage, j’y vais moi !"
                jump badEnding_4



    label choix4_done:
        jump suite4



    # --------------------------------------------------------------------------
    # --------------------------------- DATES  ---------------------------------
    # Date 1 :
    label date1_got:

        $amitie_got += 2
        $flirt_got = True

        "Après un bon moment à les suivre, nous arrivons devant une grande grille."
        "\"Cimetière de ...\""
        #scene bg cimetiere5

        "Moi" "Mais qu'est-ce qu'on fait la !?"
        got "Bah notre soirée pourquoi ?"

        "Je commence légèrement à regretter d'être venu."
        "Qui fait une soirée dans un cimetière sérieux."

        "Le groupe reprend leur marche après avoir poussé dans un long grincement le portail."
        #scene bg cimetiere2
        "Après quelques instants, ils s'asseoient sur des tombes en ruine et allument leur enceinte."
        "Complètement ahuri, je contemple cette scène."
        "Trois personnes dansent sur du rock gothique dans un cimetière."
        "Mais où est-ce que je suis tombé ???"

        got "Tu comptes rester debout comme un poteau ?"
        "Moi" "Nan, je suis juste un peu surpris du déroulement de la soirée."

        "M'aggripant le bras, Marie-Anne commence à danser avec moi."
        "Plusieurs faisceau lumineux cassent le ciel et l'ambiance sombre du cimetière."
        "Marie-Anne écarquille les yeux et attrape l'enceinte."
        "Sans me lâcher le bras, elle et ses amis commencent à courir."

        got "Les flics ! Cours !"

        # ----- Mini jeu course poursuite -----
        # SI REUSSITE
        $amitie_got += 1

        #scene bg cimetiere3
        "J'ai perdu les membres du groupe et j'ai l'impression que je suis le seul à être poursuivi."
        "En passant un angle entre plusieurs tombes, une main sort d'entre deux plaques marbrées et m'attire."
        "Marie-Anne me tient fermement et me plaque contre elle"

        "Moi" "Qu'est-ce que-"
        got "Ferme la putain !"
        "..."
        "..."
        "Après plusieurs minutes Marie-Anne me lâche."

        got "Ah Ah Ah ! Si tu avais pu voir ta gueule pendant que les flics te courraient après ! C'était à mourir de rire !"
        "Moi" "Moi ça me fais pas rire. J'aurais fait quoi si j avais été arrêté ?"
        got "T'aurais passé la nuit dans une cellule, rien de grave c'est bon."
        got "Allez il faut que je retrouve les autres. C'etait sympa à plus."

        "Marie-Anne se remet à courir et disparaît dans le fond du cimetière me laissant seul dans cet endroit lugubre."
        "Je n'ai plus qu'à rentrer maintenant j'imagine..."

        # SI ECHEC
        "J'ai perdu les membres du groupe et j'ai l'impression que je suis le seul à être poursuivi."
        "Après avoir courru à en perdre haleine pendant plusieurs minutes, je me retrouve devant la grille du cimetière."
        "J'ai du mal à passer au dessus mais finit par y arriver."
        "Je n'aime pas être seul, en pleine nuit, dans cet endroit lugubre."
        "Je n'ai plus qu'à rentrer maintenant j'imagine..."

        jump suite3
        jump date1_done



    label date1_hippie:
        $amitie_hippie += 1

        hippie "Oh super ! Tu vas voir, je suis une super prof !"

        "Avant même que je puisse rajouter un mot, Jeanne m’attrape par la main et me tire hors du studio. "
        "Les membres de son groupe doivent avoir l’habitude, car ils attrapent prestement leurs instruments et nous suivent en courant."
        "L’ambiance est bonne enfant, aussi je finis par me joindre à l’hilarité générale du groupe pendant que nous dévalons les rues en direction du parc le plus proche."
        "Je me rends compte que la main de Jeanne est incroyablement douces. "
        "Ses vêtements sales auraient pu laisser penser le contraire, mais une agréable odeur de fleur émane de ses cheveux."
        "Ceux-ci viennent me chatouiller les narines pendant qu’elle me guide dans les rues de Rennes, hilare devant la beauté simple du monde."

        hippie "Et voilà, nous sommes arrivés !"

        "Avant même que je m’en rende compte, nous étions entourés de verdure."
        "Au beau milieu d’un parc dans lequel plusieurs personnes habillées de la même manière que Jeanne sont en train de s’amuser à se lancer divers objets."

        hippie "Tu vas voir, c’est super facile, faut juste prendre le coup. "
        hippie "Tu veux commencer par quoi ? Les balles de jonglage ou le diabolo ?"

        menu:
            "Je préfererai essayer le diabolo.":
                hippie "Super ! Le principe, c’est de tirer sur tes bâtons, et de faire retomber le diabolo entre elles, sur la ficelle. "
                hippie "Ça à l’air impressionnant, mais c’est assez simple. "
                hippie "Forcément, tu ne fera pas tout de suite des figures, mais avec un peu d’entrainement tu pourras sûrement y arriver !"

                "L’enthousiasme de Jeanne était communicatif, aussi j’attrapa les bâtons qu’elle me tendait avec empressement."

                # MINI JEU DIABOLO :
                #(rester appuyé sur le clic pour le lancer le plus haut possible, puis décaler de droite à gauche pour bien le rattraper)
                $reussite_diabolo = True

                if reussite_diabolo:
                    hippie "Ouah, t’as pris le coup super vite, c’était incroyable !"

                    "Portée par l’ambiance chaleureuse de la foule, et par sa joie de me voir réussir, Jeanne me prend dans ses bras et me serre contre elle."

                    hippie "Tu es incroyable comme gars, c’est vraiment super de t’avoir comme ami ! D’ailleurs je..."

                    "Jeanne réalise finalement la position dans laquelle nous sommes, et se recule précipitamment, les joues rouges comme des pivoines."
                    "Elle se dandine d’un pied sur l’autre, gênée. "
                    "Plusieurs fois elle semble vouloir dire quelque chose, avant de se raviser. "

                    if (amitie_hippie > 4):
                        "..."
                        menu:
                            "J'aimerai bien me rapprocher d'elle.":
                                $amitie_hippie += 1
                                $flirt_hippie = True
                                "Suivant mon instinct, je fais un pas en avant vers elle avant qu’elle ne puisse reprendre la parole."
                                "Moi" "Ça ne me dérangeais pas tu sais. Un câlin par une aussi jolie fille, ça ne se refuse pas..."

                                "Aaaaaah, mais qu’est ce que je raconte ? Non mais ça va pas ? "
                                "Elle va me coller une baffe et je vais me faire virer pour avoir fait des avances malpolies à une de mes artistes !"

                                hippie "Vraiment ?"

                                "Un sourire malicieux pointe le bout de son nez sur le visage de Jeanne. "
                                "Elle semble avoir retrouvé cette assurance optimiste qui la définissait si bien."

                                hippie "Et donc si je fais ça, cela ne te gêne pas non plus ?"

                                "Jeanne passe son doigt sous mon menton..."
                                "... avant de s’enfuir en riant."
                                "C’est à mon tour de me retrouver à rougir, regardant Jeanne partir danser avec des enfants en sautillant. "
                                "Cette fille a vraiment le cœur sur la main. "
                                "Je la rejoins, et nous finissons ainsi la journée, à s’amuser avec toutes les autres personnes ici, tout en s’échangeant des regards complices."

                                hippie "On se revoit bientôt au studio !"

                                "Je rentre seul chez moi, en ayant cependant promis de se revoir bientôt."

                            "Je préfere garder mes distances.":
                                "Un moment de silence un peu gênant s'installa entre nous, avant que nous reprenions les exercices, essayant de faire comme si rien ne s’était passé. "
                                "J’aurais peut-être dû dire quelque chose ?"
                                "La journée arriva à sa fin sans autre incident notable, et je fini par rentrer chez moi, seul."


                else:
                    hippie "Ne t’inquiète pas, tout le monde ne réussit pas du premier coup, c’est normal. "
                    hippie "On pourra recommencer une prochaine fois si tu veux."
                    '...'
                    hippie "Mais pour l’instant il commence à se faire tard, on devrait rentrer. A une prochaine fois !"

                    "Déçu, je rentre chez moi, pour me préparer à une nouvelle journée de travail le lendemain."

                    jump date1_done

            "Les balles de jonglage me tentent un peu plus !":
                "choix jonglage"
                # coder ici le choix diabolo
        jump date1_done


    label date1_punk:

        punk "T’as raison on ferait mieux de pas faire ça."
        punk "J’suis désolé de t’avoir embarqué là-dedans."
        "Moi" "C’est pas grave."
        punk "Si, c’est plutôt grave. "
        punk "J’ai été aveuglé par ma haine envers eux, et on aurait pu se faire tuer si tu m’avais pas convaincu. "
        "Moi" "Je sais, mais c’est mieux de s’en rendre compte maintenant que trop tard. "
        "Moi" "Mais j’aimerai bien comprendre d'où te vient cette rancœur. "
        punk "Tu veux dire au-delà de leur racisme ouvert et de leur haine de tous ceux qui sont différents?"
        "Moi" "Je sais que ce ne sont pas les personnes les plus recommandables."
        "Moi" "Bon nombre de personnes les ont en horreur, et pourtant personne ne les passe à tabac dans la rue."
        punk "J’sais bien, mais j’ai mes raisons."
        "Moi" "J'aimerais bien connaître les raisons qui te poussent à ce genre d'extrémités."

        "A peine ces mots ont quitté ma bouche que sa posture se referme."

        punk "C’pas tes oignons !"
        "Moi" "Écoute, je ne suis pas là pour fouiller ton passé, mais j’ai pas envie que tu te fasses du mal."

        "Il semble rougir brièvement."

        "Moi" "Je n’ai pas envie d’être lourd et d’insister, mais je m'inquiète. C’est...."
        punk "Je suis homosexuel !"

        "Je le vois jeter son pied de biche par terre et commencer à s’en aller puis faire brusquement demi-tour."

        punk "C’est pour ça que j’ai la rage contre tout et tout le monde! "
        punk "J’ai pas le droit d’être moi-même! Jamais! Nulle part! "
        punk "J’ai jamais pu vivre ma vie! Alors que j’y suis pour rien!"

        "Il commence à fondre en larmes."

        #cut sur fond noir
        "Je l’ai raccompagné chez lui, et sur le chemin nous avons longuement échangé sur le sujet. "
        "J’ai pu lui dire que moi même je n’étais pas sûr d’être à cent pour cent hétérosexuel, et je lui ai promis de garder le secret."

        #cut sur ruelle avec skinhead
        skh "Et bien dis donc, Patrick est un pd, voilà qui change tout…"


        # DIALOGUE A CHANGER ICI
        "Journée suivante"

        "Je vais appeler Patrick aujourd’hui."
        "..."
        "..."
        "Tiens, aucune réponse. C’est étrange."
        "..."
        "..."
        "J'espère qu’il ne lui est rien arrivé de grave."

        "Je devrais peut-être contacter les autres groupes pour voir s'ils arrivent à le contacter..."
        menu:
            "Non. Je vais aller directement chez lui.":
                jump goodEnding_3



            "Allez je les appelle.":
                "J’ai appelé les autres groupes et leur ai expliqué que Patrick ne répondait pas et que je m’inquiétais pour lui. "
                "Jeanne et Marie-Anne ont accepté de m’aider à le chercher."
                "Après s’être séparés et avoir cherché dans les coins de la ville où je savais qu’il avait l’habitude d’aller, nous nous sommes retrouvés devant chez lui."
                #toc toc
                "Faites qu’il ouvre."
                # il ouvre la porte
                "Dieu soit loué il va bien, même s’il n’a pas l’air dans son assiette."

                "Moi" "Dieu merci tu vas bien, je m’inquiétais pour toi on t’a cherché partout."
                punk "Ouais... Désolé..."
                got "Ça va pas de disparaître comme ça ?"
                punk "J’ai dit, désolé. "
                punk "Et pis qu’est-ce que vous faites là ?"
                hippie "On est venu prêter main forte à [nom]."
                hippie "Il se faisait un sang d’encre pour toi et par extension nous aussi."
                "Moi" "Qu’est-ce qu’il t’arrive ?"
                punk "Restez pas plantés là, entrez. "

                "Après être entrés, nous nous sommes installés dans son salon."
                "Nous sommes restés silencieux un bon moment, la tension dans l’air presque palpable."
                "Après un moment, j'ose enfin briser l’assourdissant silence qui était tombé sur la pièce."

                "Moi" "Dis nous tout. Qu’est-ce qu’il se passe ?"
                punk "Bah c’est vraiment très simple, tu te souviens de l’autre soir, quand je t’ai parlé de mon secret ?"
                "Moi" "Oui, comme si c’était hier."
                got "Comment ça ?"
                hippie "Quel secret ?"
                "Moi" "Ce n'est pas…"
                punk "Pas vos oignons."
                hippie "Si on savait de quoi tu parles on pourrait plus facilement t’aider."
                got "Pour un fois elle n'a pas tort."
                "Moi" "Laissez le, s'il n’a pas envie d’en parler, c’est son droit."
                punk "C’est bon, c’est pas grave, elles finiront pas l’apprendre dans tous les cas."
                punk "Je préfère les hommes..."
                punk "... et les skinheads de l’autre fois nous ont entendus en parler dans la rue l’autre soir."
                punk "Ils ont répandu la nouvelle en ville."
                punk "Plus personne veut me parler, même pas les autres membres de mon groupe."
                punk "Les seuls coups de fil que j’ai reçus aujourd’hui ça à été pour m’insulter."
                punk "Alors ouais, j’ai pas décroché."

                "Le silence s'abat de nouveau sur la pièce."
                "Alors que Jeanne et Marie-Anne sont bouche bée, je sens mon cœur se serrer dans ma poitrine."
                "Je n’avais jamais envisagé avoir des sentiments envers un autre homme et pourtant à cet instant rien ne m’importe plus que lui."

                if $flirt_got and $flirt_hippie:
                    jump goodEnding_4
                else:
                    jump goodEnding_5




        jump date1_done
    label date1_done:


    # DATE 2 :
    label date2_got:
        got "Parfait tiens. "
        got "On se dit rendez-vous dans 30 min ? Je dois aller récuperer des choses chez moi."

        "A peine le temps d’acquiescer que je la vois disparaître derrière la porte du studio."
        "En regardant ce qu'elle m'a donné, je comprends qu’il s’agit d’une adresse."
        "J’imagine que c’est là où je dois aller."
        "Ça me laisse le temps de ranger et fermer le studio au moins."
        "En arrivant à l’adresse du bout de papier j'aperçois un cimetière, mais Marie-Anne n’est pas là. "
        "En regardant au loin dans le cimetière j’aperçois de la lumière, surement Marie-Anne..."
        "En arrivnt au niveau de la lumière je peux voir avec une certaine appréhension Marie-Anne en train de dresser une nappe sur deux tombes collées côte à côte."
        "Elle y place plusieurs boites et quelques boissons."

        got "Oh ! t'es deja la !"
        got "Viens j’ai préparé quelques trucs."

        "Pour pouvoir m’asseoir en face d’elle je dois enjamber quelques caveaux et urnes sur mon passage. "
        "L’ambiance tout autour est un peu morbide, je ne peux pas voir à plus de dix mètres autour de moi et une brume commence à se former au loin."
        "Pendant que je me perds en regardant tout autour de moi, j'aperçois Marie-Anne me regarder avec excitation."

        got "Alors ! J’ai ramené plein de trucs différents et tu vas nous faire quelque chose !"

        "Son excitation me laisse perplexe."
        "Pourquoi est-elle si enjouée à l’idée de me laisser choisir des ingrédients dans des boîtes ?"

        "Moi" "Tu veux que je fasse le repas ?"
        got "Pas vraiment le faire."
        got "J’ai plein de trucs dans mes boites, et je veux que tu fasses un bon mélange."
        "Moi" "Heu... ok je peux essayer."
        # MINI JEU NOURRITURE

        #--- si minijzu perdu ---

        "Après quelques bouchées son regard vient croiser le mien."

        got "C’est original on va dire."

        "Je goûte ma création et je me rends bien compte que tout cela n’est pas spécialement fameux."

        "Moi" "Désolé ce n’est pas vraiment ce qu’on peut appeler un repas."
        got "Ne t’excuse pas tant qu’on ne devient pas malade, ce ne sera pas l’un des pires repas de ma vie."

        "Notre soirée continue dans une ambiance sympathique et un peu morbide du au lieu."
        "Moi" "Pourquoi aimes-tu ce genre d’endroit ? "
        "Moi" "Je dois avouer que je passe très peu de soirées dans ce genre d’endroit."
        got "J’aime beaucoup l’ambiance calme des endroit peu fréquenter, je n’aime pas spécialement les cimetières."
        got "Mais non loin du studio c’est le seul endroit ou je peux aller tard et être sur de ne croiser personne. "
        got "Les seules personnes ici ne sont plus en mesure de me juger."

        "Je sens une lègere pointe de tristesse sur sa dernière phrase."

        "Moi" "Les gens te…"

        "Je n’ai pas le temps de finir ma phrase que je vois le visage crispé de Marie-Anne. "
        "Elle me regarde avec un regard de haine, s’avance vers moi et m’attrape par le col."

        got "T'as mis quoi dans le repas du con ?"

        "Elle a perdu le côté innocente et triste d’il y a 20 secondes."

        "Moi" "Heu, je ne sais plus. Il y avait des cacahuètes, des concombres, du poulet..."

        "Avant que je ne finnissent ma phrase elle me jete au sol violemment."
        "Je me retrouve assis par terre et Marie-Anne avance vers moi."
        "Elle me frape le visage et commence à partir du cimetière. "
        "Je dois la rattraper"

        "Moi" "Qu’est-ce qu'il se passe !?"
        got "Je suis allergique tête de..."

        "Son visage me montre une vive douleur coupant sa phrase."
        "Elle lève de nouveau sa main vers moi et par réflexe je ferme les yeux."
        "Sans surprise elle me frappe."
        "En rouvrant les yeux je la vois au loin, j’imagine que cela ne sert a rien de la rattraper."
        "Je devrais rentrer et lui reparler une prochaine fois."


        #---si minijeu reussi---
        $flirt_got = True

        "J’essaye tant bien que mal à préparer quelque chose en faisant abstraction de l’environnement qui m’entoure."
        "Une fois fini je tend l’assiette composée des différents élements des boites à Marie-Anne."
        "J’attend une réaction de sa part et je commence à fixer son visage, intrigué."
        "Après quelques bouchées je vois un sourire commencer à s’afficher sur son visage."

        got "C’est trop bon !"

        "Elle me regarde avec de grands yeux comme une enfant qui découvre quelque chose de nouveau."

        got "Hey je me demandais... "
        got "Pourquoi tu as accepté de venir ce soir avec moi ?"
        "Moi" "Je suis nouveau dans le coin et tu es l’une des premières personnes que je connais à me proposer de faire des choses en dehors de travail."
        "Moi" "Je trouve ça cool en plus je découvre des endroits où je ne serais jamais venu sans toi."
        got "T'as pas peur ?"
        "Moi" "Peur de quoi ?"
        got "Je sais pas... "
        got "La plupart des personnes me fuient un peu... "
        got "Dans les magasins les parents avec des enfants leurs font des réflexion sur ce qu’il ne faut pas faire après m’avoir vu ou ce genre de choses. "
        got "J’ai plus l’habitude que les gens me fuient plutôt qu’il me suivent."
        "Moi" "Je ne vois pas de raison de te fuir, t'es gentille avec moi et j’aime bien sortir avec toi."

        "Après ma phrase je la vois rougir et comme chercher quelque chose dans le vide avec son regard."
        "Comme pour briser le silence qui commence à s'installer, elle recommence à manger."

        got "Hmmmm, j’aurais jamais imaginé que tu puisses faire quelque chose d’aussi bon !"
        "Moi" "Merci, j’ai essayé de me creuser la tête pour faire quelque chose qui pourrait te plaire."
        got "Juste pour me plaire ?"
        #rougit
        got "..."
        got "Et toi tu aimes ?"

        "Apres ces mots j’attrape une fourchette et prend une petite part dans son assiette."
        "J’approche mon visage de ma fourchette et met ma main en dessous puis goûte ma création."
        "Et bah on peut dire que j’ai réussi quelque chose de vraiment bon..."
        "En ouvrant les yeux pour donner ma réponse à Marie-Anne, je m’aperçois que je me trouve à quelque centimètres de son visage."
        "J’aperçois mieux que jamais son maquillage noir entourant ses yeux marrons."
        "Malgré la couleur sombre j’aperçois quelque chose de plutôt lumineux dedans."
        "Quelques secondes après avoir ouvert les yeux, Marie-Anne me repousse doucement et recule."
        "Elle semble gênée et tourne la tête."

        "Moi" "C’est vachement bon ! Je suis content de moi sur ce coup."
        got "..."
        "Moi" "C’est quoi les boissons que tu as apporté ?"
        got "..."
        "Moi" "Tu vas bien ?"
        got "Ferme la !"
        "Moi" "Hein ? Qu'est ce qu'il se passe ?"
        got "T'étais obligé de t'approcher autant ?"

        "J’ai l’impression de voir son visage rougir."
        "Elle continue de cacher son visage avec ses mains et bras comme si elle voulait disparaître."
        "Je me rapproche et met ma main sur son bras pour le baisser."

        "Moi" "Hey, désolé j’ai pas fait exprès, ça va aller ?"
        got "Oui, oui..."

        "En lâchant son bras elle laisse tomber les mains de son visage et se retourne vers moi, laissant face à moi son visage rougi pas une gêne. "
        "Elle à les yeux un peu humides les rendant brillants."

        "Moi" "Wha…, tu es vraiment belle."
        got "QUOIIIII ? JE..JE.. "

        "Marie-Anne commence à devenir bien plus rouge que tout à l’heure."
        "Son visage commence à me montrer un certaine gène et elle na pas l’air contente de ce que j’ai dit, merde."
        "Elle se lève, essaye de marcher mais tape dans les boîtes posées au sol et pars vers la sortie du cimetière."
        "Je la rattrape et lui attrape la main, mais elle enlève la sienne immédiatement, se retournant vers moi le visage encore plus rouge et les yeux humides. "
        "Elle lève sa main vers le ciel."

        got "T'es vraiment un connard !"

        "Je sens le contact de sa main sur ma joue, je crois qu’elle a voulu me gifler."
        "Je la regarde un peu perdu et constate qu’elle semble encore bien plus gênée."
        "Elle repart vers la sortie puis s'arrête quelque mètres avant, et se retourne vers moi."

        got "Mer… Merci pour la soirée, heu, heu... Bonne nuit."

        "Je la regarde sans bouger partir au loin, repensant à ce qu’il vient de se passer et rigolant."
        "Je me retourne vers notre table de fortune et range tout ce qui se trouve au sol avant de rentrer chez moi dans une certaine joie."


        jump date2_done

    label date2_hippie:
        hippie "Super ! Je t'attendrai avec impatience !"

        "Le soir venu..."
        "Je suis bien à l'adresse que m'a donnée Jeanne, mais je ne la vois nulle part..."
        "Je comprends pourquoi elle voulait qu'on se retrouve ici cependant, avec le coucher du soleil sur les arbres et la multitude de fleurs dans les hautes herbes, l'ambiance est presque féerique."

        hippie "Coucou, je t’ai fait attendre ?"

        "Jeanne arrive par derrière moi et me fait sursauter. "

        hippie "C’est beau ici non ? "
        hippie "Je n’ai jamais vu personne pourtant, donc je considère un peu cet endroit comme mon coin de paradis secret, là où la nature est laissée libre et heureuse..."
        "Moi" "C’est vrai que c’est superbe. "
        "Moi" "Mais il fait quasiment nuit, on devrait peut-être aller se mettre à l’abri non ?"
        hippie "Non attends, tu vas voir, le meilleur est à venir. "
        hippie "Tiens, allonge- toi dans l’herbe à côté de moi."

        "Surpris par sa demande, je m'exécute, curieux de voir où celà allait mener."
        "Nous restons ainsi quelques instants à profiter du coucher de soleil. "
        "Juste au moment où je tourne la tête vers Jeanne pour lui demander ce que nous allons faire ensuite, elle pousse un cri."

        hippie "Regarde, ça commence !"

        "Relevant les yeux vers le ciel, je vois les étoiles de la voûte céleste s’allumer les unes après les autres. "
        "Loin des lumières de la ville, elles sont indénombrables. C’est magnifique."

        hippie "Je ne me lasse jamais de ce spectacle. "
        hippie "Voir toutes ces lumières, toutes de tailles et d'intensité différentes danser dans la nuit, ça me donne espoir pour les humains."
        "Moi" "Comment ça ?"
        hippie "Tu sais que je fais partie du mouvement hippie non ? "
        hippie "Eh bien ça n’a pas toujours été le cas. "
        hippie "Au début, j'étais une fille totalement normale, perdue dans la masse..."
        hippie "Mais un jour mes parents ont gagné au loto. "
        hippie "J’étais encore innocente et crédule à l’époque, donc je me disais qu’on allait pouvoir rendre tout le monde heureux avec tout cet argent."
        hippie "Quelle n’a pas été ma déception quand j’ai vu mes parents s’isoler peu à peu du monde, devenir aigris et proches de leurs sous. "
        hippie "Quand ils ont refusé de donner de l’argent à un proche malade, j’en ai eu assez et je me suis enfui. "
        hippie "J’ai rejoint le camp hippie le plus proche et je ne suis jamais revenue. "
        hippie "Depuis, je me bat pour le bonheur, pour que tout le monde puisse être heureux. "
        hippie "Et je me dis qu’un jour, peut-être qu’on sera aussi unis et brillants que les étoiles dans le ciel."

        "C’était la première fois qu’elle s’ouvrait autant. "
        "Elle qui est d’habitude si rayonnante, si enjouée, je la trouvais à présent mélancolique, presque triste même."
        "Avant que je ne puisse l'interpeller, la rassurer, elle reprit la parole, tendant la main vers le ciel."

        hippie "Je sais bien que c’est impossible, mais j’aimerais bien changer le monde, faire comprendre à tous que les autres sont importants, du plus grand au plus petit..."
        "Moi" "C’est un beau rêve..."
        hippie "Merci."

        "Nous sommes restés longtemps comme ça, allongés dans l’herbe, à regarder le ciel, la main dans la main. "
        "Le moment est trop éthéré, trop beau pour que je le brise en disant quoi que ce soit d’autre."
        "Je ne sais pas combien de temps s’est écoulé avant que Jeanne se relève, et me tende la main pour m’aider à me relever à mon tour. "
        "La lumière de la lune, derrière sa tête, lui fait un halo d’albâtre, entouré d’une couronne de diamants d’étoiles. "
        "Elle est magnifique..."
        "Mon coeur manque un battement."
        "Je n’ai aucun souvenir de comment je suis rentré ensuite, mais quand je reprends mes esprits je suis déjà devant mon immeuble. "
        "J’ai vraiment l’impression de sortir d’un rêve."

        jump date2_done
    label date2_done:


    label date3_got:
        "Comme d'habitude, elle ne me laisse pas de temps avant de raccrocher."
        "Il lui aura fallu seulement une dizaine de minutes pour arriver au studio."

        "Moi" "Tu as fais vite."
        got "J’étais juste à côté."

        "Vu comment elle est essoufflée, j’ai un peu de mal à y croire."

        "Moi" "Maintenant que tu es la, je peux te présenter quelqu’un que, je pense, tu aimes."

        "J’ouvre la porte du studio d’enregistrement et tend le bras vers le guitariste de \"The cure\" ."

        got "Qui t'as dit que j’aimais \"The cure\" ?"
        "Moi" "Heu, personne... "
        "Moi" "Mais vu ton style de musique je me suis dit que c’était ce que tu aimais."
        "Moi" "Avec le festival il passait dans le coin et j’ai déjà travaillé avec lui."
        "Moi" "J’ai envie de te proposer de fare une collab avec lui pendant le festival !"

        # CONTINUER ICI
        if amitie_got >= 4:
            jump goodEnding_1
        else:
            jump neutralEnding_1

        jump date3_done


    label date3_hippie:
        "Moi" "ça commence à faire beaucoup de manifestations non ?"
        "Moi" " M’enfin, ça reste une invitation à laquelle je répondrais avec plaisir oui. A ce soir alors !"

        "Le soir venu..."
        "Après quelques minutes à attendre, je vois enfin Jeanne qui arrive. "
        "Mais quelque chose ne va pas. Est ce qu'elle est...  Oh bon sang !"

        "Moi" "Mais tu es blessée ! Est-ce que ça va ? Qu’est ce qui s’est passé ?"
        hippie "Ne t’inquiète pas, c’est juste une petite coupure au front, c’est impressionnant parce que ça saigne beaucoup, mais ce n’est vraiment pas grave."
        "Moi" "Mais comment tu t’es fait ça ? "
        "Moi" "C’est la manifestation de cet après-midi ? Je pensais que c’était un truc tranquille !"
        hippie "Ca aurait du oui, mais des chauves ont commencé à nous lancer des pavés, et j’en ai pris un sur la tête."
        hippie "Mais ce n’est pas grave, cela en valait la peine, je sais bien que tout le monde ne nous aime pas."
        "Moi" "Ecoute, je sais que ta cause te tient à cœur, mais tu es importante toi aussi. "
        "Moi" "Tu ne peux pas promouvoir le bien-être animal si tu ne prends pas soin de toi !"
        hippie "C’est gentil de ta part de t’inquiéter pour moi. Vraiment. "
        hippie "Mais je t’assure que ça va. "
        hippie "Ce n’est pas comme si j’allais manquer à grand monde tu sais..."
        "Moi" "Hey ! Et moi alors ? Et ton groupe ? Et les enfants à qui tu apprends le diabolo ? "
        "Moi" "Tu es importante toi aussi, ce n’est pas parce que la majorité pensent d’une manière différente qu’ils ont forcément raison. "
        "Moi" "Tu le sais d’ailleurs, sinon tu ne manifesterais pas non ?"
        "Moi" "Alors je t’en supplie, fais attention à toi d’accord ? Au moins pour moi. "
        "Moi" "Je tiens trop à toi pour supporter de te voir te blesser."
        hippie "Ah ce point hein ? "
        "Moi" "J’en doutais peut-être encore un petit peu avant de te voir arriver, mais te voir dans cet état m’a fait réaliser à quel point tu comptais pour moi. "
        "Moi" "Ce n’est pas grave si on n'est pas pareil, si on ne pense pas la même chose. "
        "Moi" "L’important c’est qu’on fasse un effort pour se comprendre l’un l’autre, que chacun fasse un pas vers les autres pour essayer de les comprendre."
        hippie "Sauf les nazis."
        "Moi" "Ouais, sauf les nazis."

        "Le silence s’installe un moment."

        menu:
            "On va dans ta roulotte ?":
                hippie "... Oui."

                "Il se passe ce qu’il se passe."

                jump goodEnding_2

            "On va faire du repérage pour le festival ?":
                hippie "... Oui."

                jump neutralEnding_2
    label date3_done:





    # --------------------------------------------------------------------------
    # ------------------------------- ENDINGS  ---------------------------------

    label badEnding_1:
        got "prisooooon"
        jump badEnding_done

    label badEnding_2:
        hippie "overdooooose"
        jump badEnding_done

    label badEnding_3:
        "aha les deux meurent"
        jump badEnding_done

    label badEnding_4:
        punk "je meurs"
        jump badEnding_done
    label badEnding_done:
        jump end



    label goodEnding_1:
        got "Tu te fous de ma gueule ?"
        got "C’est le vrai ?"
        # changer ici la phrase est bizarre ptdr
        "Guitariste" "Je suis le guitariste de \"The cure\"."
        "Moi" "Nan c’est une statue."
        got "Comment t'as fait pour le faire venir ?"
        "Moi" "J’ai déjà travaillé avec lui, et je lui ai demandé si il pouvait venir jouer pour\"Effervecence\" lors du festival de ce soir."
        got "Attend, attend..."
        got "Je vais jouer avec LUI ?!"
        "Moi" "Ouais c’est pas une blague."
        "Moi" "Vas-y, vous n’avez pas tant de temps que ca pour répéter."
        "Moi" "Profites-en !"

        "Son regard brille de mille feu."
        "Elle me lance un regard enivrant avant de disparaître dans la salle de répétition."
        "Après plusieurs heures de répétition intensive, je les arrête avant qu’ils ne s’écroulent de fatigue."

        "Moi" "Hey ! Allez vous reposer pour ce soir !"

        "Le guitariste et le reste du groupe rangent leurs affaires avant de partir se reposer."
        "J’entre dans la salle de répétition pour ranger ce qu’ils ont laissé derrière eux."
        "Après quelques pas dans la salle, j’entends la porte se claquer derrière moi."
        "Marie-Anne, adossée à la porte me regarde."
        "Son visage est empourpré, mais je ne crois pas que ce soit de la gêne."

        got "Tu sais que ça fait un moment que j’attend ça ? "
        got "Et là aujourd’hui tu m'as fait comprendre que je ne voulais plus attendre plus longtemps."
        "Moi" "Je crois que je sais ce dont tu vas parler."
        "Moi" "Est-cce que je peux te demander quelque chose avant ?"

        "Marie-Anne s’approche de moi doucement sans rien dire."
        "Elle met sa main sur mon torse, me pousse sur les fauteuils de la salle et s’assoie sur moi, puis approche sa bouche de mon oreille."
        "Je n'arrive plus à sortir ne serait-ce qu'un seul mot..."

        got "Tu devrais te dépêcher de parler."

        "A l’entente de cette phrase je reprends mes esprits."
        "J'attrape ses épaules, puis fais reculer son buste avant d’attraper son visage d’une main."
        "De mon bras libre j'entoure ses hanches et l’embrasse."
        "En me reculant pour la regarder je vois son visage complètement rouge."

        "Moi" "Ce n’est pas ce que tu voulais ?"
        got "Ta gueule ! "
        got "Je ne pensais pas que tu le ferais, j'y suis allée pour te taquiner. "
        got "Je ne suis quand même pas déçue..."

        "Marie-Anne se lève et attrape mon bras pour me relever, mais m'embrasse puis me repousse sur les fauteuils."

        got "Je vais aller me reposer. T'as intérêt à être là ce soir !"

        #fondu noir vers festival
        "Le festival se déroule agréablement..."
        "Quelques minutes avant que Marie-Anne ne passe sur scène, je me dirige en backstage pour la voir."
        "Je la trouve et lui fais un signe de la main qu’elle me rend."
        "Sa musique sonne incroyablement bien ce soir, je ne peux que en profiter."


        jump goodEnding_done

    label goodEnding_2:
        "Le festival bat son plein. "
        "C’est un succès retentissant, réunissant un public de tous horizons venu découvrir la culture hippie. "
        "Le groupe \"Quatuor\" est clairement la plus grande réussite, faisant déborder la prairie dans laquelle se déroule l'événement."

        "Cet événement de grande ampleur va démystifier la culture hippie à de nombreuses personnes, qui adopterons l’état d’esprit de paix et de tolérance que la culture prône. "
        "Un nouvel âge d’or des hippies allait commencer."

        "Jeanne et moi nous sommes mis en couple officiellement lors de ce festival. "
        "Elle continue de jouer de la musique et moi de gérer différents groupes. "
        "J’accorde cependant désormais plus de temps à ma famille, et aux causes sociales qui me semblaient juste. "
        "Quant à Jeanne, elle continue d’aller en manifestation, mais elle ne se met plus en danger comme avant, surtout qu’un petit grumeau lui fait désormais location sous le nombril."
        jump goodEnding_done


    label goodEnding_3:

        "Faites qu’il ouvre."
        # Patrick ouvre la porte
        "Dieu soit loué il va bien."
        "Il n’as pas tout de même pas l’air dans son assiette."

        "Moi" "Dieu merci tu vas bien. J’étais inquiet quand tu ne m’as pas répondu au téléphone."
        punk "(soupir)  Ouais... Désolé."
        "Moi" "Ca n’a pas l’air d’aller."
        punk "Ouais, pas terrible."
        "Moi" "Tu veux en parler ?"
        punk "Pas sur que ça arrange la situation, mais si t’y tiens. Entre."

        "Il me fait entrer dans son petit appartement, me mène jusqu’au salon et s’affale dans un fauteuil."
        "Il me pointe du doigt le fauteuil en face du sien."

        punk "Reste pas planté là assieds toi."

        "Je m'exécute et m’assieds."

        "Moi" "Dis moi tout, je t’écoute."
        punk "Bah c’est vraiment très simple, tu te souviens de l’autre soir, quand je t’ai parlé de mon secret ?"
        "Moi" "Oui, comme si c’était hier."
        punk "Ben les skinheads de l’autre fois nous ont entendus et ils ont répandu la nouvelle en ville. "
        punk "Plus personne veut me parler, et les seuls coups de fil que j’ai reçu aujourd’hui ça a été pour m’insulter. "
        punk "Alors ouais, j’ai pas décroché."
        "Moi" "Oh non, je suis terriblement désolé. Si j’avais su, je n'aurais pas insisté."
        punk "C’pas ta faute, c’est même plutôt l’inverse."
        punk "Sans cette discussion qu’on a eu, je l’aurai sûrement bien plus mal pris. "
        punk "J’aurai peut-être pas tenu le coup."
        "Moi" "Non, ne dis pas ça. Ce sont juste des abrutis."
        punk "C’est vrai, mais avant c’était des abrutis qui m’adressaient la parole, maintenant c’est juste des abrutis et j’suis tout seul."
        "Moi" "C’est pas totalement vrai, je suis la moi."
        punk "Ouais, pour combien de temps, après le festival le groupe va surement me virer, et on s’verra plus jamais."

        "Quand il prononce ces mots mon cœur se serre."
        "C’est fou je n’avais pas réalisé que je tenais autant à lui. "
        "Ce pourrait-il que je ne sois pas seulement attiré par les femmes ?"
        "C’est ça, je n’avais jamais considéré que je pourrais être attiré par un homme, mais l’idée de ne plus le voir m’amène au bord des larmes."

        "Moi" "Non, on se reverra. Je te le promets. Je ne te laisserai pas tomber. "
        "Moi" "Il est hors de question qu'on les laisse gagner."

        "Il me regarde puis et baisse les yeux vers la table."
        "A ce moment je réalise que j’ai instinctivement attrapé sa main sans même m’en rendre compte."

        punk "Ha... Heu... Ouais."

        "Il rougit et détourne le regard."

        "Moi" "Je suis on ne peut plus sérieux."
        punk "Je sais bien, mais c’est compliqué."
        "Moi" "Comment ça ?"
        punk "J’ai pas envie de t’exposer aux risques qui viennent avec cette vie. "
        punk "J’vais être honnête, j’ai déformé la vérité... "
        punk "Le membre du groupe qui à été passé à tabac dont je t’avais parlé. "
        punk "Bah c’était pas un membre du groupe, c’était mon mec... "
        punk "Et il à pas juste été salement amoché, il a été battu à mort."

        "Je reste silencieux à cette annonce, je ne sais trop que dire."

        punk "Alors comprends-moi bien, tu m’plais bien et je suis sûr que t’es un type super. "
        punk "Mais j’ai pas envie de te mettre en danger."
        "Moi" "Peut-être, mais ce n’est pas à toi de prendre cette décision pour moi."

        "Je me lève et l’attrapant par le col, l’embrasse passionnément. "
        "Il me rend mon baiser. "

        # fondu noir

        "Patrick et moi avons continué à nous voir, discrètement, presque en secret."
        "Malgré tout, il à continué à faire de la musique, et les membres de son groupe ont fini par venir lui présenter leurs excuses."
        "Quant à moi, j’ai continué de travailler dans le studio."
        # CONTINUER ICI

        jump goodEnding_done


    label goodEnding_4:

        "En fait rien ne m’importe plus qu’eux. Tous les trois."
        "Est-ce que je suis tombé amoureux de trois personnes d’un coup ?"
        "Mon introspection se retrouve soudainement interrompue."

        got "On les emmerde ces fachos, moi j’en ai rien a faire. "
        hippie "Entièrement d’accord avec elle."
        "Moi" "Je suis avec elles la dessus."
        "Moi" "Si ça leur suffit pour couper les ponts avec toi, ce sont des abrutis qui ne méritaient pas de rester dans ta vie."
        punk "Peut-être, mais avant c’était des abrutis qui m’adressaient la parole."
        punk "Maintenant c’est juste des abrutis et j’suis tout seul."
        got "Comment ça tout seul ? Il est vide ton salon là ?"
        hippie "On compte pour du beurre nous ?"
        "Moi" "Elles ont raison, nous on est là !"
        punk "Ouais, pour combien de temps."
        punk "Après le festival le groupe va surement me virer, et on s’verra plus jamais."

        "Quand il prononce ces mots mon cœur se serre, c’est fou je n’avais pas réalisé que je tenais autant à lui."
        "Et d’un simple coup d'œil autour de moi je remarque que les autres semblent peinées elles aussi."

        "Moi" "Non. On se reverra, c’est une promesse."
        "Moi" "Je ferai tout ce que je peux pour continuer à te voir."
        got "Bah dis donc, tu n’y vas pas de main morte toi."
        hippie "Shhhh, je crois que ça ressemble à une déclaration ça. "

        "Mes joues prennent instantanément une teinte pourpre."

        "Moi" "Je... Heu... Non..."

        "Apparemment je ne suis pas le seul à être devenu complètement rouge."

        punk "Ha... Heu... Ouais... Non..."
        got "Hahaha! Regardez vous rougir comme des gamins, vous êtes au collège ou quoi ?"
        "Moi" "Tu ne manques pas d’air, tu n’en menais pas large non plus l’autre soir au cimetière."

        "Oups, la boulette je crois que je l’ai mise en rogne."
        "Enfin, au moins elle est tout aussi embarrassée que moi."

        hippie "Qu’est-ce que ça veut dire ça ?"
        got "RIEN!"
        punk "Attends, vous êtes en train de me dire que tu sortais avec nous trois en même temps [nom] ?"
        "Moi" "Alors, je peux tout expliquer."
        got "Ouais."
        hippie "Hmmmm."
        punk "On aimerait bien."
        "Moi" "Pour faire court, au début je voulais juste rencontrer des gens, dans une nouvelle ville. "
        "Moi" "Mais en apprenant à vous connaître, je suis tombé amoureux de vous trois, indépendamment."
        "Moi" "J’aurai surement dû vous en parler plus tôt pour éviter cette situation, mais je n’ai pas pu m’y résoudre."
        punk "J’avoue que t’as plutôt merdé."
        got "Ouais grave."

        "Je suis écarlate à ce moment, quel idiot j’ai été."
        "Aucun d’entre eux ne va plus jamais m’adresser la parole."

        hippie "Calmez vous un peu, le cœur à ses raisons que la raison ignore, moi je comprends."
        hippie "Et si vous y êtes ouverts, on pourrait tous être avec lui, rien ne nous empêche de le voir tous en parallèle."
        punk "De toute façon c’est pas comme si on pouvait être ensemble en public. J’suis pas contre."
        got "Après tout pourquoi pas, après tout les gens nous regardent déjà tous bizarrement, on est pas à ça près."

        "Pour que Patrick puisse participer au festival, Jeanne et Marie-Anne ont proposé de l’accompagner sur scène à la place de son groupe."
        "Au final même si leurs méthodes étaient différentes leurs messages restaient très similaires."
        "Il s’agissait principalement de vivre sa vie et de laisser les autres vivre la leur."
        "Après le festival, j’ai continué à les voir, tous, je ne réalise toujours pas à quel point je suis chanceux d’être tombé sur ces gens."
        "Ils me rendent vraiment heureux."

        jump goodEnding_done

    label goodEnding_5:

        got "On les emmerde ces fachos, moi j’en ai rien a faire. "
        hippie "Entièrement d’accord avec elle."
        "Moi" "Je suis avec elles la dessus."
        "Moi" "Si ça leur suffit pour couper les ponts avec toi, ce sont des abrutis qui ne méritaient pas de rester dans ta vie."
        punk "Peut-être, mais avant c’était des abrutis qui m’adressaient la parole."
        punk "Maintenant c’est juste des abrutis et j’suis tout seul."
        got "Comment ça tout seul ? Il est vide ton salon là ?"
        hippie "On compte pour du beurre nous ?"
        "Moi" "Elles ont raison, nous on est là !"
        punk "Ouais, pour combien de temps."
        punk "Après le festival le groupe va surement me virer, et on s’verra plus jamais."

        "Quand il prononce ces mots mon cœur se serre, c’est fou je n’avais pas réalisé que je tenais autant à lui."

        "Moi" "Non. On se reverra, c’est une promesse."
        "Moi" "Je ferai tout ce que je peux pour continuer à te voir."
        got "Bah dis donc, tu n’y vas pas de main morte toi."
        hippie "Shhhh, je crois que ça ressemble à une déclaration ça. "

        "Mes joues prennent instantanément une teinte pourpre."

        "Moi" "Je... Heu... Ouais... Peut-être."

        "Patrick est tout aussi rouge que moi."

        punk "Ha... Ha... Ouais... Hahaha..."
        "Moi" "Je suis on ne peut plus sérieux."
        punk "Je sais bien, mais c’est compliqué."
        "Moi" "Comment ça ?"
        punk "J’ai pas envie de t’exposer aux risques qui viennent avec cette vie."
        punk "J’vais être honnête, j’ai déformé la vérité."
        punk "Le membre du groupe qui à été passé à tabac dont je t’avais parlé. Bah c’était pas un membre du groupe, c’était mon mec."
        punk "Et il à pas juste été salement amoché, il a été battu à mort."

        "Je reste silencieux à cette annonce, je ne sais trop que dire."

        punk "Alors comprends-moi bien, tu m’plais bien et je suis sûr que t’es un type super."
        punk "Mais j’ai pas envie de te mettre en danger."
        "Moi" "Peut-être, mais ce n’est pas à toi de prendre cette décision pour moi."

        "Je me lève et l’attrapant par le col, l’embrasse passionnément."
        "Il me rend mon baiser."
        "Les filles restent silencieuses et détournent le regard pour ne pas nous gêner mais je m’en fous."
        "Rien n'entachera ce moment."

        "Pour que Patrick puisse participer au festival, Jeanne et Marie-Anne ont proposé de l’accompagner sur scène à la place de son groupe."
        "Au final même si leurs méthodes étaient différentes leurs messages restaient très similaires."
        "Il s’agissait principalement de vivre sa vie et de laisser les autres vivre la leur."
        "Après le festival, Patrick et moi avons continué à vivre notre relation discrètement pour éviter les attaques et l’homophobie."
        "Mais nous avons milité dès que possible pour la libération des orientations sexuelles."

        jump goodEnding_done


    label goodEnding_done:
        jump end



    label neutralEnding_1:

        got "Dommage pour toi alors, je déteste ce groupe. "
        got "J’adore le style de musique ca s’arrête là, il peut repartir."
        "Moi" "Désolé j’aurais dû te prévenir avant tout ca."

        "J’explique honteusement au guitariste que Marie-Anne ne peut pas faire la collab avec lui. "
        "Il a l’air de le prendre assez mal et part sans plus tarder."

        got "Vraiment réfléchis avant de faire ce genre de choses. "
        got "Bon on la fait cette session ?"

        "La session se termine, je laisse les membres du groupe partir et retient Marie-Anne."

        "Moi" "Marie-Anne j’ai quelque chose à te dire."
        got "..."
        "Moi" "Depuis nos petites aventures, les rendez vous dans le cimetière,..."
        "Moi" "... j’ai l’impression que l'on s’entend vraiment bien et j'aimerais savoir si tu voulais sortir avec moi ?"
        got "[nom], t'es mignon et gentil, tu ne me juge pas, tu me rabaisse pas et je te suis reconnaissante pour tout ça."
        got "Mais je ne veux pas que notre relation change."
        "Moi" "Je comprends..."
        "Moi" "On se retrouve au festival du coup..."
        "Moi" "Salut..."

        "Sans attendre une réponse je pars du studio laissant Marie-Anne derrière moi."

        # fondu noir annoncant un changement de jour ?

        "Le festival se déroule devant moi, me laissant seul devant les différentes scènes."
        "Au loin j’entend Marie-Anne commencer à jouer avec son groupe."
        "J’aime sa musique mais je ne me sens pas d’aller la voir, je préfère l’écouter d’ici..."
        "Une fois son passage fini je retourne sur mes pas et rentre chez moi."


        jump neutralEnding_done

    label neutralEnding_2:
        # scene festivale
        "Nous arrivons ensemble sur la plaine où va se dérouler le festival."
        "Quelques régisseurs sont en train de monter la scène sur laquelle \"Quatuor\" va se produire dans maintenant quelques heures."
        hippie "festival trop bieeeennn"
        jump neutralEnding_done
    label neutralEnding_done:
        jump end

label end:
    "MERCI D'AVOIR JOUE A \"DE L'AMOUR ENTRE LES NOTES\" !"



    $renpy.pause()


    return
