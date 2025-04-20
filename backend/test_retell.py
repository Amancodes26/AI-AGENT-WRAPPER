# import os
# from retell import Retell

# # Set your API key
# api_key = "key_92a890aa922f03dee3505114157a"  # Replace with your actual key

# # Initialize client
# client = Retell(api_key=api_key)

# try:
#     # List existing agents
#     agents = client.agent.list()
#     print("Successfully connected to Retell API")
#     print(f"Found {len(agents)} agents")
#     for agent in agents:
#         print(f"Agent: {agent.agent_name} (ID: {agent.agent_id})")
# except Exception as e:
#     print(f"Error connecting to Retell API: {str(e)}")
# from retell import Retell

# client = Retell(api_key="api key")  # Replace with your actual key



# # List available LLMs
# try:
#     llms = client.llm.list()
#     print("Available LLMs:")
#     for llm in llms:
#         print(f"- {llm.llm_id}")
# except Exception as e:
#     print(f"Error listing LLMs: {str(e)}")