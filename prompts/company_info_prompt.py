from langchain.prompts import PromptTemplate


prompt_template = PromptTemplate.from_template(
    """Extract only the most relevant details from the company description

1. Company Basics
    Name: [Company name]
    Industry: [e.g., cybersecurity, SaaS, fintech]
    Core Focus: [e.g., “AI-driven threat detection,” “data analytics platforms”]

2. Tech Stack & Tools
    Technologies Mentioned: [e.g., Python, cloud platforms (AWS/Azure), AI/ML frameworks]
    Key Projects/Products: [e.g., “real-time data pipelines,” “cyber threat intelligence platform”]

3. Mission & Culture
    Values: [e.g., innovation, collaboration, simplicity]
    Development Priorities: [e.g., “scalable solutions,” “data-driven decision-making”]

4. Optional Extras (if relevant)
    CSR/Initiatives: [e.g., sustainability tech, open-source contributions]

Format the output as clear sections with bullet points.

Job Listing Text:
{raw_text}"""
)


