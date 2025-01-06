# oxnetwork

A Python client for interacting with [0x-network.com](https://api.0x-network.com).

## Installation


## Usage

```python
from oxnetwork import Agent

# 1) Create a new agent
agent = Agent.create(api_key="test", name="DemoAgent")

# 2) Query the agent
response = agent.query("What's my SOL balance?")
print("Response:", response)

# 3) Use an existing agent if you already know agent_id and thread_id
existing = Agent.get(api_key="test", agent_id=123, thread_id="abcd1234")
resp2 = existing.query("Please buy 0.01 of token abc...")
print("Response:", resp2)
