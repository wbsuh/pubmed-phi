from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

## Testing Phi Assistant 
assistant = Assistant(
    llm=OpenAIChat(model="gpt-4-turbo-preview"),
    description="You are a PubMed Assistant helping users find the right article they need.",
    debug=True
)
assistant.print_response("Provide an optimal search query for discovering articles on NSCLC in pregnancy.", markdown=True)



