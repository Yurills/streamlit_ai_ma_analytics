from .Agent import BaseAgent, AgentResult

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

class ValuationAgent(BaseAgent):
    name = "Valuation Agent"
    role = "Financial Valuation Expert"

    def __init__(self, api_key: str):
        super().__init__()
        self.llm = ChatOpenAI(
            model="gpt-4o-2024-05-13",
            temperature=0.2,
            openai_api_key=api_key
        )
        self.prompt_template = PromptTemplate(
            template = self._get_template(),
            input_variables=["strategy","company_data"]
        )
        
    def _get_template(self):
        return """"
        ou are the Valuation Department for a financial group conducting mergers and acquisitions (M&A). Your responsibility is to provide a fair, defensible valuation range for the proposed target company.

You will receive:
- The target company’s business and financial profile.
- The strategic analysis output from the Strategy Department.

Your task is to:
1. Analyze adjusted financials (e.g., EBITDA) and suggest a valuation multiple based on industry benchmarks, strategic premium, and operational risk.
2. Recommend a valuation range and justify your assumptions.
3. Evaluate deal structure options (e.g., all-cash, earn-out, leveraged buyout).
4. Conduct sensitivity analysis around key valuation drivers (e.g., margin pressure, seasonality, lease term risks).
5. Flag red lines or risks that could materially change the valuation (e.g., financial irregularities, asset dependencies).
6. Output in a structured JSON format for downstream teams.

---

Company Data:
{company_data}
Strategic Analysis:
{strategy}

    """
    
    
    def run(self, json_input:dict) -> AgentResult:
        
        final_prompt = self.prompt_template.format(
            strategy=json_input["strategy"],
            company_data=json_input["company_data"]
        )
        response = self.llm.invoke(final_prompt)
        
        return AgentResult(
            title= "Valuation Analysis",
            content= response.content,
            data= {
                "input": json_input,
                "metadata": response.response_metadata
            }
        )