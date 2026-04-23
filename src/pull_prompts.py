"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull dos prompts do Hub
3. Salva localmente em prompts/bug_to_user_story_v1.yml

SIMPLIFICADO: Usa serialização nativa do LangChain para extrair prompts.
"""

from http import client
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langchain import hub
from utils import save_yaml, check_env_vars, print_section_header
from langsmith import Client

load_dotenv()


def pull_prompts_from_langsmith():
    client = Client()
    prompt = client.pull_prompt("leonanluppi/bug_to_user_story_v1")    
    save_yaml(prompt, Path("prompts/raw_prompts.yml"))


def main():
    """Função principal"""
    used_vars = ["LANGSMITH_API_KEY", "LANGSMITH_ENDPOINT", "LANGSMITH_PROJECT", "USERNAME_LANGSMITH_HUB"]
    check_env_vars(used_vars)
    print_section_header("Pulling Prompts")
    pull_prompts_from_langsmith()
    print("Prompts pulled and saved to prompts/raw_prompts.yml")    


if __name__ == "__main__":
    sys.exit(main())
