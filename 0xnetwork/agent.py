# agent.py

import requests
import base64


class Agent:
    """
    Represents a Solana-based agent on https://api.0x-network.com/index.php
    
    This class provides:
      1) create()  - create a new agent
      2) get()     - use an existing agent
      3) query()   - send a message to the agent
    """

    def __init__(self, agent_id: int, thread_id: str, api_key: str, base_url: str = None):
        """
        :param agent_id: The numeric agent ID returned by create-agent
        :param thread_id: The unique thread ID (for conversation context)
        :param api_key: The user's API key
        :param base_url: Optional override of the API base URL
        """
        self.agent_id = agent_id
        self.thread_id = thread_id
        self.api_key = api_key
        self.base_url = base_url or "https://api.0x-network.com/index.php"

    @classmethod
    def create(cls, api_key: str, name: str, base_url: str = None):
        """
        Creates a new agent by calling the 'create-agent' action.

        :param api_key: The user's API key
        :param name: The desired name for the new agent
        :param base_url: Optional API base URL if different from default
        :return: An Agent instance
        """
        final_url = base_url or "https://api.0x-network.com/index.php"
        params = {
            'action': 'create-agent',
            'name': name,
            'api_key': api_key
        }
        resp = requests.get(final_url, params=params)
        data = resp.json()

        if data.get('status') != 'success':
            raise RuntimeError(f"Failed to create agent: {data.get('message')}")

        agent_id = data['data']['agent_id']
        thread_id = data['data']['thread_id']
        return cls(agent_id, thread_id, api_key, base_url=final_url)

    @classmethod
    def get(cls, api_key: str, agent_id: int, thread_id: str, base_url: str = None):
        """
        Use an existing agent if you already know agent_id and thread_id.

        :param api_key: The user's API key
        :param agent_id: Numeric agent ID
        :param thread_id: The thread ID from a previous creation
        :param base_url: Optional base URL
        :return: An Agent instance
        """
        final_url = base_url or "https://api.0x-network.com/index.php"
        return cls(agent_id, thread_id, api_key, base_url=final_url)

    def query(self, message: str) -> str:
        """
        Queries the agent by calling the 'query-agent' action with a base64-encoded message.

        :param message: The user question or command (plain text)
        :return: The agent's final response (string)
        """
        encoded_msg = base64.b64encode(message.encode('utf-8')).decode('utf-8')
        params = {
            'action': 'query-agent',
            'agent_id': self.agent_id,
            'message': encoded_msg,
            'api_key': self.api_key
        }
        resp = requests.get(self.base_url, params=params)
        data = resp.json()

        if data.get('status') != 'success':
            raise RuntimeError(f"Query failed: {data.get('message')}")
        return data['data'].get('response', '')
