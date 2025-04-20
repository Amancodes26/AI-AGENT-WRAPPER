# Agent Wrapper API

A FastAPI-based service that provides a unified interface for creating voice agents using Retell and VAPI platforms.

## 🚀 Features

- Create voice agents on Retell platform
- Create voice agents on VAPI platform
- Unified API interface for both platforms
- Environment-based configuration
- Error handling and validation

## 📋 Prerequisites

- Python 3.8+
- pip package manager
- Retell API key
- VAPI API key

## 🛠️ Setup

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your API keys:
```env
RETELL_API_KEY=your_retell_api_key
VAPI_API_KEY=your_vapi_api_key
```

5. Start the server:
```bash
uvicorn main:app --reload
```

## 🔍 API Documentation

### Create Agent Endpoint

**Endpoint:** `POST /create-agent`
**Description:** Creates a voice agent on either Retell or VAPI platform.

#### Request Schema
```json
{
    "platform": "string (retell or vapi)",
    "name": "string",
    "tts_provider": "string",
    "tts_voice": "string",
    "llm_provider": "string",
    "llm_id": "string"
}
```

## 🧪 Testing with Postman

### 1. Create Retell Agent

```http
POST http://localhost:8000/create-agent
Content-Type: application/json

{
    "platform": "retell",
    "name": "Test Agent Retell",
    "tts_provider": "11labs",
    "tts_voice": "11labs-Adrian",
    "llm_provider": "retell-llm",
    "llm_id": "llm_4c3c1b48869d99679c19866e9aa2"
}
```

### 2. Create VAPI Agent

```http
POST http://localhost:8000/create-agent
Content-Type: application/json

{
    "platform": "vapi",
    "name": "Test Agent VAPI",
    "tts_provider": "vapi",
    "tts_voice": "Elliot",
    "llm_provider": "openai",
    "llm_id": "gpt-4"
}
```

## 📝 Response Examples

### Successful Retell Response
```json
{
    "success": true,
    "data": {
        "agent_id": "generated_agent_id",
        "agent_name": "Test Agent Retell",
        "voice_id": "11labs-Adrian"
    }
}
```

### Successful VAPI Response
```json
{
    "success": true,
    "data": {
        "id": "generated_assistant_id",
        "name": "Test Agent VAPI",
        "voice": {
            "provider": "vapi",
            "voice_id": "Elliot"
        }
    }
}
```

## ⚠️ Error Handling

The API returns appropriate HTTP status codes and error messages:
- 400: Bad Request (invalid input)
- 500: Internal Server Error (API key missing, service unavailable)

## 🔒 Environment Variables

- `RETELL_API_KEY`: Your Retell API key
- `VAPI_API_KEY`: Your VAPI API key

## 📚 Dependencies

- FastAPI
- uvicorn
- python-dotenv
- pydantic
- retell-sdk
- vapi_server_sdk
- requests
- httpx
