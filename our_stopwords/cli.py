# our_stopwords/cli.py

import argparse
import json
import our_stopwords

def list_languages():
    """
    CLI command to list all available languages.
    """
    available_languages = our_stopwords.list_available_languages()
    print("Available languages:")
    for lang in available_languages:
        print(f" - {lang}")

def get_stopwords(language_code):
    """
    CLI command to get stop words for a specific language.

    Parameters:
    - language_code (str): Language code (e.g., 'ven' for Venda).
    """
    try:
        stopwords = our_stopwords.get_stopwords(language_code)
        print(json.dumps(stopwords, indent=2, ensure_ascii=False))
    except ValueError as e:
        print(f"Error: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="CLI for accessing multilingual stop words for African languages.")

    subparsers = parser.add_subparsers(dest='command', title='Commands', description='Valid commands')

    # Subcommand: list
    list_parser = subparsers.add_parser('list', help='List all available languages')

    # Subcommand: get
    get_parser = subparsers.add_parser('get', help='Get stop words for a specific language')
    get_parser.add_argument('language_code', type=str, help='Language code (e.g., "ven" for Venda)')

    args = parser.parse_args()

    if args.command == 'list':
        list_languages()
    elif args.command == 'get':
        get_stopwords(args.language_code)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
