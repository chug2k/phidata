from phi.agent import Agent, RunResponse
from phi.model.xai import xAI

agent = Agent(
    model=xAI(id="grok-beta", client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))),
)

# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story.")
# print(run.content)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")
