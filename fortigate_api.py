import requests
import urllib3
from config import FORTIGATE_HOST, FORTIGATE_TOKEN

urllib3.disable_warnings()
HEADERS = {"Authorization": f"Bearer {FORTIGATE_TOKEN}"}

def fetch_firewall_policies():
    url = f"{FORTIGATE_HOST}/api/v2/cmdb/firewall/policy/"
    try:
        response = requests.get(url, headers=HEADERS, verify=False)
        response.raise_for_status()
        policies = response.json().get("results", [])

        with open("firewall_policies.txt", "w") as f:
            for rule in policies:
                line = f"ID {rule['policyid']}: {rule['srcaddr']} -> {rule['dstaddr']} | Service: {rule['service']}\n"
                f.write(line)
                print(line.strip())
        print("\nRegras salvas em 'firewall_policies.txt'")
    except Exception as e:
        print("Erro ao buscar regras:", e)
