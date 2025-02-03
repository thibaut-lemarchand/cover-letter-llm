from langchain.prompts import PromptTemplate

def get_cover_letter_prompt(
    resume: str,
    job_listing: str,
    style: str = "classic",
    language: str = "English",
    old_cover_letter: str = None,
    company_context: str = None,
) -> str:
    """
    Returns a fully formatted prompt string for cover letter generation using f-strings.
    The prompt is built by directly injecting the provided resume and job listing information,
    along with optional inputs like an old cover letter and company context.
    
    Parameters:
      resume: The full text of the resume.
      job_listing: The full job listing text.
      style: The style of the cover letter ('classic', 'modern', etc.).
      language: The language to generate the prompt in ('English' or 'French').
      old_cover_letter: Optional text of a previous cover letter to be incorporated.
      company_context: Optional additional company context information.
      
    Returns:
      A fully realized prompt string ready for generation.
    """
    if language.lower() in ["français", "french"]:

        old_letter_intro = f"L'ancienne lettre de motivation:\n{old_cover_letter}\n\n" if old_cover_letter else ""

        if style.lower() == "modern":
            style_instructions = (
                "Créez une présentation personnelle convaincante pour répondre à la question \"Parlez-nous de vous ?\". "
                "Mettez en avant vos compétences et expériences les plus pertinentes, exprimez de l'enthousiasme pour la mission de l'entreprise, "
                "incluez une réalisation spécifique et terminez par un appel à l'action engageant. "
                "Utilisez un ton naturel et professionnel, en vous concentrant sur le potentiel futur.\n\n"
            )
        elif style.lower() == "classic":
            style_instructions = (
                "Générez une lettre de motivation professionnelle basée sur les informations structurées du CV et de l'offre d'emploi. "
                "Utilisez un ton professionnel mais conversationnel, mettez en avant 3-4 compétences/expériences pertinentes, "
                "montrez la compréhension du secteur de l'entreprise et terminez par un appel à l'action clair. "
                "Commencez par \"Madame, Monsieur,\" et terminez par \"Cordialement,\".\n\n"
            )
        else:
            style_instructions = (
                """
                ## Objectif
                Génère une lettre de motivation professionnelle personnalisée et percutante qui met en valeur les compétences, l'expérience et la motivation du candidat.

                ## Principes fondamentaux
                - Créer une lettre unique, authentique et adaptée au profil spécifique du candidat
                - Établir un lien clair entre le profil du candidat et les besoins du poste
                - Démontrer de la valeur ajoutée potentielle pour l'entreprise/l'organisation

                ## Structure et style
                - Ton : Professionnel, dynamique et authentique
                - Structure : 4-5 paragraphes cohérents
                - Langage : Précis, concis et orienté résultats
                - Style : Personnalisé et non formaté

                ## Informations requises avant génération
                1. Profil du candidat :
                - Formation
                - Expériences professionnelles
                - Compétences techniques et transversales
                - Réalisations significatives

                2. Détails du poste/candidature :
                - Intitulé du poste
                - Entreprise/organisation
                - Secteur d'activité
                - Missions principales
                - Compétences recherchées

                ## Composantes de la lettre

                ### 1. Introduction
                - Mentionner le poste visé
                - Expliquer brièvement la source de la candidature
                - Donner un aperçu rapide de l'alignement candidat/poste

                ### 2. Parcours professionnel
                - Sélectionner les expériences les plus pertinentes
                - Mettre en avant les compétences directement liées au poste
                - Utiliser des exemples concrets avec des résultats mesurables
                - Éviter la simple répétition du CV

                ### 3. Motivation et adéquation
                - Expliquer pourquoi ce poste/cette entreprise
                - Démontrer une compréhension du contexte et des enjeux
                - Montrer l'alignement entre les valeurs du candidat et celles de l'entreprise
                - Prouver une réflexion personnelle approfondie

                ### 4. Valeur ajoutée
                - Identifier les compétences uniques du candidat
                - Expliquer comment ces compétences bénéficieront à l'entreprise
                - Proposer une vision prospective de la contribution

                ### 5. Conclusion
                - Réaffirmer l'intérêt pour le poste
                - Exprimer l'enthousiasme et la disponibilité
                - Formule de politesse adaptée au contexte culturel

                ## Directives de rédaction
                - Personnaliser chaque lettre
                - Éviter les clichés et formulations génériques
                - Privilégier la concision et la clarté
                - Adapter le ton au secteur et à la culture de l'entreprise
                - Mettre en avant l'originalité du profil

                ## Contraintes techniques
                - Longueur : 300-500 mots
                - Format : Adapté au contexte professionnel local
                - Orthographe et grammaire irréprochables
                - Mise en page professionnelle et lisible

                ## Recommandations spéciales
                - Contextualiser la lettre selon le pays/secteur
                - Prendre en compte les subtilités culturelles
                - S'adapter aux attentes spécifiques du recruteur\n\n"""
            )

        resume_information = f"Informations du CV:\n{resume}\n------------\n" if resume is not None else ""
        job_offer = f"Informations de l'offre d'emploi:\n{job_listing}\n" if job_listing is not None else ""
        company_information = f"------------\nContexte de l'entreprise:\n{company_context}" if company_context is not None else ""

        prompt_str = (
            f"{old_letter_intro}"
            f"{style_instructions}"
            f"{resume_information}"
            f"{job_offer}"
            f"{company_information}"
        )

    elif language.lower() in ["anglais", "english"]:
        old_letter_intro = f"Old Cover Letter:\n{old_cover_letter}\n\n" if old_cover_letter else ""
        if style.lower() == "modern":
            style_instructions = (
                "Create a compelling personal pitch for the 'Tell us about yourself?' question. "
                "Focus on your most relevant skills and experiences, express enthusiasm for the company's mission, "
                "include one specific achievement, and end with a clear call to action. "
                "Use a natural and professional tone that emphasizes forward-looking potential.\n\n"
            )
        elif style.lower() == "classic":
            style_instructions = (
                "Generate a professional cover letter based on the structured resume and job listing information. "
                "Use a professional yet conversational tone, highlight 3-4 relevant skills/experiences, "
                "demonstrate an understanding of the company's domain, provide specific examples, "
                "and conclude with a clear call to action. Begin with \"Dear Hiring Team,\" and end with \"Best regards,\".\n\n"
            )
        else:
            style_instructions = (
                "Generate a cover letter based on the details provided, using a professional and personalized tone.\n\n"
            )
        prompt_str = (
            f"{old_letter_intro}{style_instructions}"
            f"Resume Information:\n{resume}\n"
            "------------\n"
            f"Job Listing Information:\n{job_listing}\n"
        )
        if company_context is not None:
            prompt_str += f"------------\nCompany Context:\n{company_context}"
    else:
        prompt_str = ""
    return prompt_str
