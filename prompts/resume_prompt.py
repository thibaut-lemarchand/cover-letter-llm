from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    """Analyze the following resume text and extract key information in a structured format. Focus on:

1. Professional Summary: Core expertise and career focus
2. Technical Skills: List of technical skills, tools, and technologies
3. Domain Experience: Industries and business domains worked in
4. Key Achievements: Notable accomplishments and impacts
5. Professional Experience: Brief overview of relevant roles and responsibilities

Format the output as clear sections with bullet points. Exclude personal information like contact details.

Resume Text:
{raw_text}"""
) 