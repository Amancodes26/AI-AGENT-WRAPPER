import os
from retell import Retell
from dotenv import load_dotenv
load_dotenv()  

async def create_retell_agent(agent_name, voice_id, response_engine):
    client = Retell(api_key=os.getenv("RETELL_API_KEY"))  # or from env
    try:
        agent_response = client.agent.create(
            response_engine=response_engine,
            voice_id=voice_id,
            agent_name=agent_name
        )
        return {
            "success": True,
            "data": {
                "agent_id": agent_response.agent_id,
                "agent_name": agent_response.agent_name,
                "voice_id": agent_response.voice_id
            }
        }
    except Exception as e:
        return {"success": False, "error": str(e)}