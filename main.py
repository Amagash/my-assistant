import boto3
import json

def connect_to_bedrock():
    # Initialize the Bedrock Agent client
    bedrock = boto3.client(
        service_name='bedrock-agent-runtime',  # Note the different service name
        region_name='us-west-2',
    )
    
    return bedrock

def get_agent_response(client, prompt):
    """
    Invoke a specific Bedrock agent
    """
    response = client.invoke_agent(
        agentId='LDRI7C5TYJ',  # Replace with your agent ID from Bedrock console
        inputText=prompt
    )
    return response

def main():
    client = connect_to_bedrock()
    response = get_agent_response(client, "Tell me a joke about programming.")
    print(response)

if __name__ == "__main__":
    print("Starting...")
    main()