#!/usr/bin/env python
"""Utilitário de linha de comando do Django para tarefas administrativas."""
import os
import sys

def main():
    # Define a configuração padrão do Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Event.settings')
    try:
        # Importa o utilitário para executar comandos de linha de comando do Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Exibe um erro caso o Django não esteja instalado ou não seja encontrado
        raise ImportError(
            "Não foi possível importar o Django. Você tem certeza de que ele está instalado "
            "e disponível na variável de ambiente PYTHONPATH? Você se esqueceu de ativar "
            "um ambiente virtual?"
        ) from exc
    # Executa o comando fornecido na linha de comando
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
