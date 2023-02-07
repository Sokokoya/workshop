

# --------------------------------------------------------------------------
# -------------------------------- IMAGES ----------------------------------

# ----- Scenes -----

image bg cimetiere1 = bg_cimetiere_jour.jpg
image bg cimetiere2 = bg_cimetiere2_jour.jpg
image bg cimetiere3 = bg_cimetiere3_jour.jpg
image bg cimetiere4 = bg_cimetiere4_jour.jpg
image bg cimetiere5 = bg_cimetiere5_jour.jpg
image bg crypte = bg_crypte_jour.jpg

image bg plaine1 = bg_plaine_jour.jpg
image bg plaine2 = bg_plaine2_jour.jpg
image bg plaine3 = bg_plaine3_jour.jpg
image bg plaine4 = bg_plaine4_jour.jpg
image bg plaine5 = bg_plaine5_jour.jpg

# ----- Personnages -----




# --------------------------------------------------------------------------
# ----------------------------- PERSONNAGES --------------------------------


# Declarartions des personnages principaux / Love interests
define got = Character('Marie-Anne', color="#ffc8ff")
define punk = Character('Patrick', color="#ffc8a8")
define hippie = Character('Jeanne', color="#ffffc8")

# Declarations des personnages secondaires
define march = Character('Marchand', color="c8c8ff")
define skh = Character('Skinhead', color="ff3030")
define voisine = Character('Vieille Voisine', color="555555")




# --------------------------------------------------------------------------
# --------------------------------------------------------------------------


# Le jeu commence ici
label start:
    python:
        nom = renpy.input("Quel est ton nom ?")
        nom = name.strip() or "Personne"

        # Declaration des amities
        amitie_got = 0
        amitie_hippie = 0
        amitie_punk = 0

        # Declaration des flirts
        flirt_got = False
        flirt_hippie = False
        flirt_punk = False

        nbRejets_hippie = 0
        jour = 0
        nbBieres = 0


    # --------------------------------------------------------------------------
    # ----- JOURNEE 1 -----
    jour += 1

    # afficher interieur studio

    "(Téléphone sonne)"
    "(Décroche le téléphone)"
    "Moi" "Allô? Oui maman! Oui je suis bien arrivé !"
    "Moi" "Oui je suis allé au studio tout à l’heure, le travail à l’air intéressant."
    "Moi" "On doit préparer un festival dans un mois et je dois aller rencontrer trois groupes qui vont chacun faire une représentation si j’ai bien compris."
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
    "Il n’y a seulement qu’elles ainsi qu’un homme posé dans un coin dans cette pièce, il a l’air d’observer comment se déroule la dispute depuis plusieurs minutes maintenant."
    "Elles ne m’ont visiblement pas vu, trop investies dans leur discussion"

    "Est-ce que je les interrompt pour les prévenir de mon arrivée ?"
    menu:
        "oui":
            jump choix1_oui

        "non":
            jump choix1_non



    "Eh bien, j’aurais aimé avoir une première journée moins agitée..."
    "Ces filles étaient intéressantes cependant, chacune à leur manière."
    "Vu que je ne suis pas encore fatigué, autant visiter un peu la ville, pour me familiariser avec."

    menu:
        "Visiter un parc":
            nbRejets_hippie += 1
            jump choix2_got

        "Partir faire des courses":
            jump choix2_hippie

        "Allez boire un verre au bar":
            nbRejets_hippie += 1
            jump choix2_punk


    "Il commence à se faire tard, la nuit est déjà tombée. "
    "Je travaille également demain, avec un autre groupe que je n’ai pas encore rencontré."
    "Je vais essayer de ne pas faire de folies ce soir et avoir l’air frais pour donner une bonne première impression."
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

    "Je rentre dans mon appartement, laissant la vieille femme rentrer chez elle."
    "Je ne m’attendais pas à passer une soirée si agitée. Il faudra que je fasse attention dans le voisinage désormais. "
    "Le coin n’est clairement pas aussi tranquille que le prétendais le promoteur immobilier."
    "La journée à été longue, autant aller se coucher directement."


    #METTRE FONDU NOIR

    # Journée 2 enft
    "Allez, c’est parti pour une nouvelle journée de travail. "
    "Je me demande pourquoi le groupe d’aujourd’hui ne voulait pas faire la présentation en même temps que les autres."
    #scene studio
    "Enfin, ils ne devraient pas tarder."

    skh "Oy, c’est toi le nouveau ?"

    "Oh bon sang."

    skh "Mais quelle bonne surprise ! Si c’est pas le gringalet d' hier soir ! "
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
    "Je rentre chez moi sans incidents. "
    "Demain, il faudra que je choisisse quel groupe appeler pour une session d’enregistrement. "


    # --------------------------------------------------------------------------
    # ----- JOURNEE 2 -----3
    jour += 1

    "Le bruit de mon reveil insupportable me tire de mon sommeil."
    "Apres la journée d'hier, j'ai une petite appréhension de comment celle d'aujourd'hui va tourner."
    "Un café et une tranche de pain puis direction le studio."
    # Aller chez le marchand ou non ?
    "Est-ce que je passerais pas à la supérette du coin avant pour voir ce qu'ils proposent aujourd'hui ?"
    menu:
        "oui":
            jump marchand_oui
        "non":
            jump marchand_non


    "En arrivant je découvre cette fois le studio dans un silence assez effrayant. "
    "Aujoud'hui je vais devoir choisir un des trois groupes que j'ai rencontré hier pour commencer à enregistrer."
    "J'hésite..."
    # Decision session studio de la journée
    menu:
        "Je vais appeler le groupe Effervecence.":
            nbRejets_hippie += 1
            jump choix3_got

        "Le groupe Quatuor m'avait bien plus hier.":
            jump choix3_hippie

        "J'ai envie de voir ce que peut donner le groupe de Perruquiers Noirs aujourd'hui.":
            nbRejets_hippie += 1
            jump choix3_punk





    # --------------------------------------------------------------------------
    # ----- JOURNEE 3 -----
    jour += 1

    # Aller chez le marchand ou non ?
    menu:
        "oui":
            jump marchand_oui
        "non":
            jump marchand_non


    # Decision session studio de la journée
    menu:
        "Marie-Anne":
            amitie_got += 1
            nbRejets_hippie += 1
            jump choix4_got



        "Jeanne":
            amitie_hippie += 1
            "session enregistrement"
            if (flirt_hippie):
                "est-ce que jai envie de continuer a flirt avec elle ?"
                menu:
                    "bah oui":
                        jump date2_hippie
                    "oula non":
                        if (nbRejets_hippie >= 4):
                            hippie "jai fait une overdose bg"
                            "----- BAD ENDING 2 -----"
                            jump badEnding_2
                            #code la fin
            else:
                jump choix3_hippie

        "Patrick":
            nbRejets_hippie += 1
            amitie_punk += 1
            "session enregitrement"
            if (amitie_punk >= 4):
                jump choix4_punk
            else:
                jump choix3_punk




    # --------------------------------------------------------------------------
    # ----- JOURNEE 4 -----
    jour += 1

    # Aller chez le marchand ou non ?
    menu:
        "oui":
            jump marchand_oui
        "non":
            jump marchand_non

    # Decision studio
    menu:
        "Marie-Anne":
            amitie_got += 1
            if (flirt_got):
                jump date3_got
            else:
                jump choix4_got

        "Jeanne":
            amitie_hippie += 1
            "session enregistrement"
            hippie "tu veux venir chez moi ?"
            menu:
                "elle est bonne oui":
                    jump date3_hippie

                    "elle est chiante a forcer ptn"
                    jump neutralEnding_2

        "Patrick":
            amitie_punk += 1
            punk "je ne repond pas"
            "est-ce que je vais le chercher ?"
            menu:
                "oui":
                    jump goodEnding_3
                "non":
                    if (amitie_got <= 4 or amitie_hippie <= 4):
                        #coder choix ici

                    else:
                        "on va tous le chercher"
                        "discussion sur l'acceptation de soi et les differences"
                        if (flirt_got and flirt_hippie and flirt_punk):
                            jump goodEnding_4
                        else:
                            jump goodEnding_5










    # TOUS LES CHOIX

    # --------------------------------------------------------------------------
    # Aller chez le marchand ou non ?
    label marchand_oui:
        march "bonjour"
        # coder ici l'interface du marchand
        jump marchand_done

    label marchand_non:
        "Pas le temps je suis deja en retard..."
        jump marchand_done


    # --------------------------------------------------------------------------
    # Choix 1 : Interrompre les deux femmes ou non
    label choix1_oui:
        $menu_flag = True

        "Moi" "Bonjour, est-ce que je pourrais savoir qui vous êtes ?"
        got "Excusez-moi mais que faites vous ici ? Comment avez vous fait pour rentrer ?"
        "Moi" "Je suis [nom] . J'ai été embauché en tant qu'ingé son dans ce studio. Et pour répondre à votre question, la porte était ouverte."
        hippie "Hahahaha !"
        "Moi" "Pourriez vous me dire qui vous êtes ?"

        hippie "Excusez moi hahaha ! Je suis Jeanne, membre du groupe Quatuor, on m'a dit de venir aujourd'hui concernant un festival donc me voici !"
        hippie "C'est un plaisir de vous rencontrer"

        got "Ouais, désolée. Je m'appelle Anne-Marie et suis la guitariste de mon groupe Effervecence"

        jump choix1_done

    label choix2_non:
        $menu_flag = False

        got "continue de senerver"
        jump choix1_done


    # --------------------------------------------------------------------------
    # Choix 2 : Premiere balade du soir
    label choix2_got:
        amitie_got += 1




        jump choix2_done

    label choix2_hippie:
        amitie_hippie += 1

        "Après avoir un petit peu tourné dans les rues autour de chez moi, j’ai trouvé une supérette, mais il semble y avoir un attroupement devant."
        "Mais… C’est pas la fille de tout à l’heure avec une pancarte au milieu de la foule ?"

        hippie "Non ! Non ! Non à l’exploitation !"

        "On dirait une manifestation..."
        "Je n’ai pas vraiment envie de me mêler de tout ça, autant chercher un autre magasin."

        hippie "Oh ! Mais tu es l’ingénieur de tout à l’heure ! Tu es venu te joindre à nous ? Comme c’est gentil !"

        "Trop tard, la fille aux vêtements colorés m’a vu."
        "Elle fend la foule et m’attrape par la manche et me regarde avec un sourire béat."

        Moi "Euuuh..."

        if menu_flag:
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
        amitie_punk += 1

        "J’irais bien faire un tour au bar ce soir, ça pourrait m’aider à rencontrer du monde et à me familiariser avec la ville."
        "*J'entre dans un bar et m‘approche du comptoir pour commander une bière"

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

        if menu_flag:
            punk "Par contre, t’as merdé, fallait les laisser s’arracher les cheveux au deux autres."
            "Moi" "C’était mon premier jour, je ne voulais pas avoir d’ennuis."
            punk "Ouais bah la prochaine fois laisse les en venir au mains, j’ai un billet sur la gothique."

        else:
            punk "D’ailleurs, merci de pas les avoir interrompues au studio. "
            punk "Tu m’as fait gagner un billet. "
            "Moi" "Un billet ?"
            punk "Ouais avec les gars on parie sur laquelle aura le dessus a chaque fois qu’elles s’engueulent."

        "Moi " "C’est pas vraiment moral."
        punk "Rien à carrer. "
        punk "Écoute, c’est pas que j’apprécie pas cette discussion, mais c’est bientôt l’heure ou ces tocards de droitards sortent de la fac"
        punk "J’ai bien envie de leur mettre un coup de pression."

        "Patrick se lève et s'en va, me laissant seul face à ma bière."
        "..."
        "Bon, je vais finir ma bière et je vais rentrer."


        punk "oui oui blabla"
        jump choix2_done


    # --------------------------------------------------------------------------
    # Choix 3 : Choix session studio
    label choix3_got:
        $amitie_got += 1

        "Allez, je compose le numéro du groupe de gothique."
        "Le téléphone sonne, chaque bip fais monter en moi une pression étrange."
        "Chaque tonalité sonne en harmonie avec mon cœur."

        got "Hmmmm ! Allo ?"
        "Ca a décroché !"
        "Moi" "Bonjour c'est " nom " l'ingé son d'hier, j'ai décidé de commencer à enregistrer avec votre groupe, il m'avait bien plu."
        got "Oh merde !"
        got "En voyant ta petite gueule on pensait pas que tu nous choisirait en premier."
        got "T'es plus sympa que je pensais ! Bah attends nous, on arrive."

        "Je n'ai même pas eu le temps de répondre qu'elle a déjà raccroché."
        "Au moins ils ont l'air motivés."

        "La séance se passe sans réel problème."
        "Le temps de m'accommoder à mes nouveaux outils, on a perdu un peu de temps, ce qui n'a pa eu l'air de gener le groupe."
        "Quelques heures se sont passées et je crois qu'on arrive à la fin de notre première session d'enregistrement."

        if (amitie_got == 2):
            got "Hé le bleu bite ! Ca te dirait de venir à notre petite soirée ?"
            menu:
                "Ouais pourquoi pas.":
                    got "Allez suis nous on y va !"
                    jump date1_got

                "Je comptais rentrer, je n'ai toujours pas fini de m'installer.":
                    "Moi" "C'est gentil d'avoir proposé ceci dit"
                    got "Boh pas grave ! Une prochaine fois."

                    "fin de journee retour chez lui"
        jump choix3_done




    label choix3_hippie:


        "Je vais appeler \"Quatuor\" aujourd’hui."
        "Je prends mon téléphone et compose le numéro de leur meneuse, Jeanne."
        "Moi" "Bonjour, c’est à votre tour de passer pour la session d’enregistrement."

        if amitie_hippie >= 1:
            hippie "Super ! On arrive, merci beaucoup !"
            "Moi" "Hey, merci à toi ! A tout de suite !"
            hippie "Hihi, tu veux tant que ça me revoir ? "
            #continuer
        else:
            hippie "Oh d’accord. Merci."

        "Le groupe \"Quatuor\" passe la journée au studio et s’améliore beaucoup !"

        amitie_hippie += 1
        "Vous devenez plus ami avec Jeanne !"

        "Moi" "La séance est terminée, merci beaucoup."
        hippie "Beau travail aujourd’hui !"

        if amitie_hippie < 2:
            "Moi" "Merci pour l’occasion, on en avait vraiment besoin…"
            hippie "Merci à toi, c’était sympa !"
            "Moi" "Hey, merci ! Ça fait toujours plaisir de venir ici."
            hippie "On joue de mieux en mieux, le festival n’a qu’à bien se tenir !"

        else : # si c'est la premiere fois que l'event diabolo arrive
            "Moi" "La séance est terminée, merci à vous !"
            hippie "Hey, merci à toi, ça fait plaisir de se voir de temps en temps. "
            hippie "D’ailleurs, ce soir on organise un petit atelier de découverte des arts du cirque, ça te tente de venir ? "
            hippie "Je pourrais t’apprendre à jongler."

        menu:
            "Oui, pourquoi pas !":
                jump date1_hippie

            "Non, désolé...":
                "Moi" "J’ai déjà quelque chose de prévu ce soir… Mais ça aurait été avec plaisir !"
                hippie "Pas de soucis, ça sera pour une prochaine fois !"

        jump choix3_done



    label choix3_punk:
        amitie_punk += 1

        "J'appelle un des membres du groupe et leur demande de venir."
        "blablabla"
        #ne pas oublier d'ecrire ici"

        if (amitie_punk >= 2):
            punk "Hey [nom], tu trouvais l’autre trou pas trop mal, j’t’attends à la sortie, j’vais te montrer un vrai bar."
            "C’est presque menaçant comme invitation, je me demande si je devrais avoir peur."

            menu:
                "Je pense que je vais sortir par derrière, j’ai un peu peur de Patrick":
                    "..."
                "Je vais sortir par devant, je ne pense pas qu’il soit dangereux.":
                    "..."

            punk "C’est pas trop tôt, tu traines la patte dis donc !"
            "Moi" "Désolé, je devais fermer le studio."
            punk "Ouais ouais, dépêche toi."
            "Moi" "J’arrive."

            # emmene dans un autre bar

            punk "Voilà ça c’est un super bar tu vas voir."
            punk "Allez viens on va se prendre quelques bières."

            "Patrick m'emmène dans des petites ruelles avant de se poser à une terrasse."
            punk "Je te commande un truc ?"

            menu:
                "Je vais prendre comme toi":
                    $nbBieres += 1

                "Je vais prendre un Coca"

            punk "Voilà, on est mieux ici. Moins de monde qu’à l’intérieur."
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

                "Je vais prendre un cocktail sans alcool"

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
                    $menu_flag2 = True
                    $nbBieres += 1

                "Je vais boir de l'eau pour cette fois"

            punk "Tiens."
            "Moi" "Merci."

            "Je regarde Patrick enfiler son verre cul-sec"
            if menu_flag2:
                punk "Alors ? Je t’attends là en fait."

                "Je crois qu'il veut que je cul-sec aussi..."
                menu:
                    "Je le suis.":
                        punk "Voilà ! Ça me plaît ! "
                        punk "Allez viens avec moi on va faire un tour et j’te raccompagne chez toi."

                    "Je préfere en rester la..."

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

        jump choix3_done

    label bagarre:
        #MINI JEU BAGARRE

        #si defaite
        "Après nous avoir mis tous les deux à terre et nous avoir pris nos portefeuille les skinheads sont partis."
        punk "Putain, on s’est pris une grosse raclée."
        punk "Je pensais que tu aurait été plus utile que ça."
        "Moi" "Désolé, je ne suis pas un grand bagarreur moi."
        punk "J’ai remarqué."

        "--- Votre amitié avec Patrick diminue ---"
        $amitie_punk -= 1

        # si victoire
        "Après quelques coups reçus, les skinheads ont pris la fuite."
        punk "Bien joué ! Tu lui as bien monté au tien." #???????? c'est quoi cette phrase
        "Je pourrais en dire autant de toi."
        punk "Oh quel plaisir de les voir prendre leur jambes à leur cou."
        "Moi" "Ouais, c’est vrai que c’est grisant, je peux comprendre que tu apprécies autant."
        punk "Tu l’as dit bouffi. Allez, à la prochaine [nom]."

        "--- Votre amitié avec Patrick augmente ---"
        $amitie_punk += 1

        "Tandis que je regarde Patrick s'éloigner, je décide qu'il est temps pour moi de rentrer également."

        jump bagarre_done




    # --------------------------------------------------------------------------
    # Choix 4 : Choix session studio
    label choix4_got:
        if (amitie_got >= 5):
            got "tu veux date glauque avec moi ?"
            menu:
                "oui":
                    jump date2_got
                "non":
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
            "Je vais le suivre, j’ai peur qu'il lui arrive quelque chose de grave.":
                "Je crois qu'ils n'ont pas compris la dernière fois en effet."
                amitie_punk += 1
                "--- Votre amitié avec Patrick augmente ---"
                punk "Parfait ! Viens avec moi on va chercher des baramines et on va leur montrer à ces sales fachos!"


                # reprendre ici
                "estce ue j'essaie de le convaincre de s'ouvrir ?"
                menu:
                    "oui":
                        punk "je m'ouvre et renonce a la rix"
                        "les fa entendent la conv"
                    "non":
                        "je vais avec lui ?":
                            "oui":
                                jump badEnding_3

                            "non":
                                jump badEnding_4


            "Désolé mais ce sera sans moi... J'ai encore mal aux côtes.":
                punk "Mauviette ! "
                punk "Allez dégage, j’y vais moi !"
                jump badEnding_4






    # --------------------------------------------------------------------------
    # --------------------------------- DATES  ---------------------------------
    # Date 1 :
    label date1_got:

        amitie_got += 1
        flirt_got = True

        "Après un bon moment à les suivre, nous arrivons devant une grande grille."
        "\"Cimetière de ...\""
        scene bg cimetiere5

        "Moi" "Mais qu'est-ce qu'on fait la !?"
        got "Bah notre soirée pourquoi ?"

        "Je commence légèrement à regretter d'être venu."
        "Qui fait une soirée dans un cimetière sérieux."

        "Le groupe reprend leur marche après avoir poussé dans un long grincement le portail."
        scene bg cimetiere2
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
        amitie_got += 1

        scene bg cimetiere3
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

        jump date1_done



    label date1_hippie:
        amitie_hippie += 1
        flirt_hippie = True

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
                reussite_diabolo = true

                if reussite_diabolo:
                    hippie "Ouah, t’as pris le coup super vite, c’était incroyable !"

                    "Portée par l’ambiance chaleureuse de la foule, et par sa joie de me voir réussir, Jeanne me prend dans ses bras et me serre contre elle."

                    hippie "Tu es incroyable comme gars, c’est vraiment super de t’avoir comme ami ! D’ailleurs je..."

                    "Jeanne réalise finalement la position dans laquelle nous sommes, et se recule précipitamment, les joues rouges comme des pivoines."
                    "Elle se dandine d’un pied sur l’autre, gênée. "
                    "Plusieurs fois elle semble vouloir dire quelque chose, avant de se raviser. "

                    # CHOIX FLIRT
                    "flirt"
                    if (amitie_hippie > 4):
                        "est-ce que je flirte avec elle ?"
                        menu:
                            "oui allez":
                                amitie_hippie += 1
                                hippie "oh que tu es beau"
                            "non c'est non":
                                "fin de journee"


                else:
                    hippie "Ne t’inquiète pas, tout le monde ne réussit pas du premier coup, c’est normal. "
                    hippie "On pourra recommencer une prochaine fois si tu veux."
                    '...'
                    hippie "Mais pour l’instant il commence à se faire tard, on devrait rentrer. A une prochaine fois !"

                    "Déçu, je rentre chez moi, pour me préparer à une nouvelle journée de travail le lendemain."

                    jump date1_done

            "Les balles de jonglage me tentent un peu plus !":
                "choix jonglage"




        jump date1_done


    # DATE 2 :
    label date2_got:
        got "c'est diner chandelle ajd"
        "minijeu nourriture"
        #coder si c'est reussi ou non, et donc si il y a un flirt ou non
        flirt_got = True

        jump date2_done

    label date2_hippie:
        hippie "viens on date dans un cahmp"
        # peut etre rajouter une amitie ou un truc ici nn ?

        jump date2_done


    label date3_got:
        got "tu veux rencontrer le guitariste de the cure ????????"
        menu:
            "mais quelle question.. Evidemment !":
                jump goodEnding_1
            "c'est qui ?":
                jump neutralEnding_1

        jump date3_done

    label date3_hippie:
        "il se passe ce qu'il se passe"
        jump goodEnding_2





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



    label goodEnding_1:
        got "festival gothique wouhou"
        jump goodEnding_done

    label goodEnding_2:
        hippie "festival hippie wouhou"
        hippie "je suis enceinte bb"
        jump goodEnding_done

    label goodEnding_3:
        punk "festival punk yeeeeeaaaaahhh"
        jump goodEnding_done

    label goodEnding_4:
        "festival polyamoureux hehe"
        jump goodEnding_done

    label goodEnding_5:
        "festival avec tous les groupes trop bien !!!"



    label neutralEnding_1:
        got "festival trop bieeeennn"
        jump neutralEnding_done

    label neutralEnding_2:
        hippie "festival trop bieeeennn"
        jump neutralEnding_done




    return
