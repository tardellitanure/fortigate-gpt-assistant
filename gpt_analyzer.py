import openai
from config import GPT_API_KEY, GPT_MODEL

def analyze_policies():
    try:
        with open("firewall_policies.txt", "r") as f:
            regras = f.read()

        prompt = f"""
Você é um analista de segurança especializado em FortiGate.
Analise as seguintes regras de firewall:

{regras}

1. Existem regras amplas ou sobrepostas?
2. Há riscos de segurança?
3. Sugira boas práticas para melhora.
"""

        openai.api_key = GPT_API_KEY

        response = openai.ChatCompletion.create(
            model=GPT_MODEL,
            messages=[
                {"role": "system", "content": "Você é um analista de segurança especializado em FortiGate."},
                {"role": "user", "content": prompt}
            ]
        )

        result = response["choices"][0]["message"]["content"]
        print("\n===== Análise GPT =====\n")
        print(result)

        with open("gpt_analysis.txt", "w") as out:
            out.write(result)
        print("\nAnálise salva em 'gpt_analysis.txt'")

    except Exception as e:
        print("Erro ao analisar políticas com GPT:", e)
