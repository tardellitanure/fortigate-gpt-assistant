# FortiGate GPT CLI

Ferramenta de linha de comando para buscar regras de firewall de um FortiGate e analisá-las com a API do ChatGPT (OpenAI).

## 🔧 Instalação

```bash
pip install -r requirements.txt
cp .env.example .env  # edite com suas credenciais
```

## 🚀 Uso

```bash
# Buscar regras do FortiGate
python main.py fetch

# Analisar regras com GPT
python main.py analyze
```

## 🔐 Variáveis .env

```
FORTIGATE_HOST=https://ip_ou_dns
FORTIGATE_TOKEN=token_do_fortigate
GPT_API_KEY=sua_api_key_openai
GPT_MODEL=gpt-4  # ou gpt-3.5-turbo
```
