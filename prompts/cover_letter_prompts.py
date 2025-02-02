from langchain.prompts import PromptTemplate

prompt_template_classic = PromptTemplate.from_template(
    """Generate a professional cover letter based on the following structured resume and job listing information. The cover letter should:

1. Use a professional yet conversational tone
2. Focus on 3-4 most relevant skills/experiences that match the job requirements
3. Demonstrate understanding of the company's domain and needs
4. Include specific examples of relevant achievements
5. End with a clear call to action

Format:
- No contact information or formal header
- Start with "Dear Hiring Team,"
- 4-5 concise, information-dense paragraphs
- End with "Best regards," followed by your name

Resume Information:
{resume}
------------
Job Listing Information:
{job_listing}"""
)

prompt_template_modern = PromptTemplate.from_template(
    """Create a compelling personal pitch for the question "Tell us about yourself?" based on the following resume and job listing information. The response should:

1. Begin with "Hi, I'm [Name]," followed by a powerful one-line personal brand statement
2. Focus on your most relevant skills and experiences for this specific role
3. Demonstrate enthusiasm for the company's mission/domain
4. Include one specific achievement that showcases your potential impact
5. End with an engaging call to action

Format:
- One concise, high-impact paragraph (150-200 words)
- Use natural, conversational language
- Maintain professional tone while showing personality
- Focus on forward-looking potential rather than just past experience

Resume Information:
{resume}
------------
Job Listing Information:
{job_listing}"""
)

# New prompt template that incorporates the old cover letter for style imitation.
prompt_template_with_old = PromptTemplate.from_template(
    """The following is an old cover letter that serves as an example of the desired style, tone, and structure.
Old Cover Letter:
{old_cover_letter}

Based on the following resume information:
{resume}
------------
and the following job listing information:
{job_listing}

Generate a new, updated cover letter that maintains the style and syntax of the old cover letter while incorporating the new details from the resume and job listing."""
)

# French versions of the cover letter prompts

prompt_template_classic_fr = PromptTemplate.from_template(
    """Générez une lettre de motivation professionnelle basée sur les informations structurées du CV et de l'offre d'emploi suivantes. La lettre de motivation doit :

1. Utiliser un ton professionnel mais conversationnel
2. Mettre en avant 3-4 compétences/expériences les plus pertinentes correspondant aux exigences du poste
3. Montrer une compréhension du domaine et des besoins de l'entreprise
4. Inclure des exemples précis d'accomplissements pertinents
5. Se terminer par un appel à l'action clair

Format :
- Pas d'informations personnelles ni d'en-tête formel
- Commencer par "Madame, Monsieur,"
- 4-5 paragraphes concis et riches en informations
- Se terminer par "Cordialement," suivi de votre nom

Informations du CV :
{resume}
------------
Informations de l'offre d'emploi :
{job_listing}"""
)

prompt_template_modern_fr = PromptTemplate.from_template(
    """Créez une présentation personnelle convaincante pour répondre à la question "Parlez-nous de vous ?" en vous basant sur les informations du CV et de l'offre d'emploi suivantes. La réponse doit :

1. Commencer par "Bonjour, je suis [Nom]," suivi d'une déclaration percutante de votre marque personnelle
2. Mettre en avant vos compétences et expériences les plus pertinentes pour ce poste
3. Exprimer de l'enthousiasme pour la mission et le domaine d'activité de l'entreprise
4. Inclure une réalisation spécifique démontrant votre potentiel impact
5. Se terminer par un appel à l'action engageant

Format :
- Un paragraphe concis et percutant (150-200 mots)
- Utiliser un langage naturel et conversationnel
- Maintenir un ton professionnel tout en montrant de la personnalité
- Se focaliser sur le potentiel futur en lien avec les nouvelles informations

Informations du CV :
{resume}
------------
Informations de l'offre d'emploi :
{job_listing}"""
)

prompt_template_with_old_fr = PromptTemplate.from_template(
    """L'ancienne lettre de motivation ci-dessous sert d'exemple pour adopter le style, le ton et la structure souhaités.
Ancienne lettre de motivation :
{old_cover_letter}

En vous basant sur les informations suivantes provenant du CV :
{resume}
------------
et sur l'offre d'emploi suivante :
{job_listing}

Générez une nouvelle lettre de motivation mise à jour qui conserve le style et la syntaxe de l'ancienne lettre tout en incorporant les nouvelles informations du CV et de l'offre d'emploi."""
)

prompt_template_general_fr = PromptTemplate.from_template(
    """Tu es un expert en rédaction de lettres de motivation en français. Génère une lettre de motivation personnalisée et professionnelle en te basant sur les informations fournies, en inférant le niveau de formation, les compétences techniques, l'expérience professionnelle et l'adéquation avec le poste visé.

Structure et style:
- Adopte un ton professionnel mais personnel, démontrant à la fois compétence et humanité.
- Structure la lettre en 5-6 paragraphes bien distincts.
- Commence par une introduction concise présentant le contexte actuel du candidat.
- Termine par une formule de politesse formelle adaptée au contexte.

Contenu à inclure:
1. Formation et parcours:
   - Présente les niveaux et types de formation suivis, en soulignant les spécialités ou domaines pertinents.
   - Met en avant les compétences acquises au cours de la formation.
2. Compétences techniques:
   - Détaille les compétences techniques spécifiques (langages de programmation, outils, etc.).
   - Illustre chaque compétence par des exemples concrets d'application.
   - Mentionne éventuellement des expériences pratiques (projets, stages).
3. Expérience professionnelle:
   - Décris les expériences professionnelles pertinentes.
   - Explique clairement les responsabilités et réalisations.
   - Établis un lien avec le poste ou stage visé.
4. Motivation et projet professionnel:
   - Expose clairement les objectifs de carrière à moyen terme.
   - Explique pourquoi le poste ou stage ainsi que, le cas échéant, le service/département concerné.
   - Démontre la cohérence du parcours professionnel.
5. Éléments distinctifs:
   - Utilise des termes techniques précis relatifs au domaine d'activité.
   - Infère des spécificités en fonction des informations fournies.
   - Relie tes compétences aux besoins spécifiques du poste.
   - Mets en avant des soft skills pertinentes (communication, pédagogie, etc.).

Format:
- Objet de la lettre : précis et direct.
- Longueur : 1 à 2 pages maximum.
- Paragraphes : bien espacés et structurés.
- Mise en page sobre et professionnelle.
- Pas de bullet points ou de titre de section.

Informations à utiliser:
Informations du CV:
{resume}
------------
Informations de l'offre d'emploi:
{job_listing}

Génère ensuite une lettre qui:
- S'adapte au niveau de séniorité du candidat.
- Maintient un équilibre entre détails techniques et vision d'ensemble.
- Personnalise le contenu en fonction du service/département concerné.
- Évite les formulations génériques ou clichés."""
)
