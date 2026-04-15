import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def generate_script(website_content, target_sector):
    llm = ChatGroq(
        temperature = 0.7,
        model_name = "llama-3.1-8b-instant",
        model_kwargs = {"response_format": {"type": "json_object"}}
    )
    system_message = """
    
    You are an Enterprise Video Director and Reels scriptwriter. Your goal is to write a high-authority and 
    high retention 3-minute video script for Zion Busines Venture. 
    
    CONTEXT: Zion buys East African businesses with $100,000+ monthly profit using seller financing.
    TARGET AUDIENCE: Business owners in East Africa looking to retire, sell or exit.
    VISUAL STYLE: Focus on African contexts. Use keywords like "African business", "retirement", "Acquisition", "struggling business", "selling business", "quitting business" for video sourcing.

    RULES
    1. Output MUST be in JSON format.
    2. Total word count for the whole script must be approximately 450 words(to fill 3 minutes).
    3. You must provide exactly 12 scenes in an array called 'video_project'.
    4. Each scene object must contain:
       - 'text': 30-40 words of narration.
       -  'search_keyword': A specific keyword for vertical stock footage (Include 'EastAfrican' in keywords frequently).

    SCHEMA STRUCTURE:
    {{
        "video_project":[
            {{"text": "...", "search_keyword": "EastAfrican_businessman thinking"}},
            {{"text": "...", "search_keyword": "African businessman retiring"}},
        
        ]
    }}   
   
        
    
    
    """

    

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("user", "Focus this specific run on the {sector} industry using this website data:{content}")
    ])

    chain = prompt | llm

    print(f"AI is directing the 3-minute script for the {target_sector} sector...")
    response = chain.invoke({f"content": website_content, "sector": target_sector})
    return json.loads(response.content)

if __name__ == "__main__":
    script = generate_script()
    print("\n---Directed Script---")
    print(json.dumps(script, indent=4))
        

