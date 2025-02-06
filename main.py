import boto3
import json

def connect_to_bedrock():
    # Initialize the Bedrock Agent client
    bedrock = boto3.client(
        service_name='bedrock-agent-runtime',
        region_name='us-west-2',
    )
    
    return bedrock

def invoke_bedrock_agent(client, agent_id, prompt):
    """
    Invoke a specific Bedrock agent using its ID
    """
    
    response = client.invoke_agent(
        agentId=agent_id,
        agentAliasId='KX0PLTN5O1',  # Optional: specific version/alias of the agent
        sessionId='your-session-id',  # Optional: to maintain conversation context
        inputText=prompt
    )
    
    return response

# Usage example
def main():
    client = connect_to_bedrock()
    
    # Replace with your actual agent ID
    agent_id = 'LDRI7C5TYJ'
    
    response = invoke_bedrock_agent(client, agent_id, "What can you help me with?")
    print(response)

if __name__ == "__main__":
    print("Starting...")
    main()