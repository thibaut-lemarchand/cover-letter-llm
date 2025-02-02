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
