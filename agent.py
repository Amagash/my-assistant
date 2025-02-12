import boto3
import os

class BedrockAgent:
    def __init__(self, region=None, agent_id=None, agent_alias_id=None):
        """
        Initialize the BedrockAgent with configuration from environment variables
        """
        self.agent_id = agent_id or os.getenv('BEDROCK_AGENT_ID')
        self.agent_alias_id = agent_alias_id or os.getenv('BEDROCK_AGENT_ALIAS_ID') 
        self.client = self._connect_to_bedrock(region or os.getenv('AWS_REGION'))
        
    def _connect_to_bedrock(self, region):
        """
        Initialize the Bedrock Agent client (private method)
        """
        return boto3.client(
            service_name='bedrock-agent-runtime',
            region_name=region,
        )
    
    def get_response(self, prompt, session_id="default-session"):
        """
        Get a response from the agent
        """
        response = self.client.invoke_agent(
            agentId=self.agent_id,
            agentAliasId=self.agent_alias_id,
            sessionId=session_id,
            inputText=prompt
        )
        
        # Extract the response from the EventStream
        for event in response['completion']:
            if event.get('chunk'):
                return event['chunk']['bytes'].decode()
        
        return None

def main():
    # Create an instance of BedrockAgent
    agent = BedrockAgent()
    
    # Get response from the agent
    response = agent.get_response("What can you help me with?")
    print(response)

if __name__ == "__main__":
    print("Starting...")
    main()