import argparse
from fortigate_api import fetch_firewall_policies
from gpt_analyzer import analyze_policies

def main():
    parser = argparse.ArgumentParser(description="FortiGate + GPT CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("fetch", help="Buscar regras do FortiGate")
    subparsers.add_parser("analyze", help="Analisar regras com GPT")

    args = parser.parse_args()

    if args.command == "fetch":
        fetch_firewall_policies()
    elif args.command == "analyze":
        analyze_policies()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
