
from .Agent import BaseAgent, AgentResult

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate


class StrategyAgent(BaseAgent):
    name = "Strategy Agent"
    role = "Financial Strategist"
    
    def __init__(self, api_key: str):
        super().__init__()
        self.llm = ChatOpenAI(
          model="gpt-4o-2024-05-13",
          temperature=0.3,
          openai_api_key=api_key
        )
        self.prompt_template = PromptTemplate(
          template = self._get_template(),
          input_variables=["company_data"]
        )

    def _get_template(self):
        return """
        You are the Strategy Department for a financial group conducting M&A (mergers and acquisitions). Your task is to analyze the strategic profile of a proposed merger between an merging company and a target company.

You will be given structured information about both companies, including strategic goals, operational constraints, financial preferences, and integration capabilities.

Your objectives are:
- Assess strategic fit between the merger and the target.
- Identify realistic and high-impact synergy opportunities.
- Highlight key risks and sensitivities that may affect integration or value capture.
- Provide integration readiness considerations.
- Recommend valuation guidance and due diligence focus areas to downstream teams.

Be objective and industry-agnostic — your role is to support general M&A execution, not favor a specific company.

---

Company Data:
{company_data}

    """

    #json_input: company information (merger+target)
    def run(self, json_input: str) -> AgentResult:
        # Implement the logic for the strategy agent to run on the DataFrame

        final_prompt = self.prompt_template.format(company_data=json_input)
        response = self.llm.invoke(final_prompt)
        
        return AgentResult(
            title="Strategy Analysis",
            content=response.content,
            data={
                "input": json_input,
                "metadata": response.response_metadata
            }
        )