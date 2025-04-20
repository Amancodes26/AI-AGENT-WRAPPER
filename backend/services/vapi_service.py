from vapi import Vapi
import os
from fastapi import HTTPException
from dotenv import load_dotenv
load_dotenv()  

async def create_vapi_agent(agent_name: str, voice_id: dict, model: dict):
    try:
        api_key = os.getenv("VAPI_API_KEY")  # or from env

        if not api_key:
            raise HTTPException(status_code=500, detail="VAPI_API_KEY not found")

        client = Vapi(token=api_key)

        response = client.assistants.create(
            voice=voice_id,
            model=model,
            name=agent_name
        )

        print(f"Debug - Vapi Response: {response}")

        return {
            "success": True,
            "data": response
        }

    except Exception as e:
        print(f"Debug - Vapi Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error creating Vapi agent: {str(e)}")
