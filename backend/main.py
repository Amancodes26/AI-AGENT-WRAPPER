from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal
from dotenv import load_dotenv

from services.retell_service import create_retell_agent
from services.vapi_service   import create_vapi_agent

load_dotenv()
app = FastAPI()

class CreateAgentPayload(BaseModel):
    platform:     Literal["retell", "vapi"]
    name:         str
    tts_provider: str
    tts_voice:    str
    llm_provider: str
    llm_id:       str

@app.post("/create-agent")
async def create_agent(payload: CreateAgentPayload):
    if payload.platform == "retell":
        return await create_retell_agent(
            agent_name      = payload.name,
            voice_id        = payload.tts_voice,
            response_engine = {
                "type":   payload.llm_provider,
                "llm_id": payload.llm_id
            }
        )
    else:  # vapi
        return await create_vapi_agent(
            agent_name = payload.name,
            voice_id   = {
                "provider": payload.tts_provider,
                "voice_id": payload.tts_voice
            },
            model      = {
                "provider": payload.llm_provider,
                "model":    payload.llm_id
            }
        )
