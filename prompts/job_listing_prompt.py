from langchain.prompts import PromptTemplate


prompt_template = PromptTemplate.from_template(
    """Analyze the following job listing text and extract key information in a structured format. Focus on:

1. Company Overview: Extract key details about the company
2. Role Overview: The main purpose and objectives of the position
3. Key Responsibilities: Main duties and tasks
4. Required Qualifications: Must-have skills, experience, and education
5. Preferred Qualifications: Nice-to-have skills and experience

Format the output as clear sections with bullet points. Exclude benefits, salary, and application process information.

Job Listing Text:
{raw_text}"""
)
