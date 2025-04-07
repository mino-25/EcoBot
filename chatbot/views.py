from django.shortcuts import render

def home(request):
    response = "👋 Bienvenue sur EcoBot !<br>Voici les commandes disponibles :<br>" \
               "- <strong>problématique</strong><br>" \
               "- <strong>solutions</strong><br>" \
               "- <strong>sommaire</strong><br>" \
               "- <strong>crédits</strong>"

    if request.method == "POST":
        commande = request.POST.get("commande", "").strip().lower()

        if commande == "problématique":
            response = "🌍 La problématique de notre projet est : Comment réduire notre impact écologique au quotidien ?"
        elif commande == "solutions":
            response = "💡 Les solutions proposées incluent : le tri des déchets, l'économie d'énergie, et l'utilisation de transports verts."
        elif commande == "sommaire":
            response = "📄 Sommaire :<br>1. Introduction<br>2. Problématique<br>3. Solutions<br>4. Conclusion"
        elif commande == "crédits":
            response = "👥 Projet réalisé par Mino et son équipe de passionnés pour la planète."
        else:
            response = "❌ Commande inconnue. Tape : problématique, solutions, sommaire ou crédits."

    # Si on vient de cliquer sur "Revenir à l'accueil", on affiche les commandes
    elif request.method == "GET":
        response = "👋 Bienvenue sur EcoBot !<br>Voici les commandes disponibles :<br>" \
                   "- <strong>problématique</strong><br>" \
                   "- <strong>solutions</strong><br>" \
                   "- <strong>sommaire</strong><br>" \
                   "- <strong>crédits</strong>"

    return render(request, 'home.html', {'response': response})
