#!/usr/bin/env python3
import argparse
import sys
from config import Config
from api import GroqAPI
from utlis import print_response, prompt_user, console


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Interact with Groq's compound-beta-mini model from the command line."
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Specify the model to use (default: from config or compound-beta-mini)"
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=None,
        help="Maximum number of tokens to generate (default: from config or 1024)"
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=None,
        help="Temperature for response generation (0.0-1.0) (default: from config or 0.7)"
    )
    parser.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="Run in interactive mode (keep session open for multiple questions)"
    )
    parser.add_argument(
        "prompt",
        nargs="?",
        help="The prompt to send to the model. If not provided, will prompt for input."
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    try:
        # Load configuration
        config = Config()
        config.validate()

        # Override config with command line arguments if provided
        model = args.model or config.model
        max_tokens = args.max_tokens or config.max_tokens
        temperature = args.temperature or config.temperature

        # Initialize API client
        api = GroqAPI(api_key=config.api_key, model=model)

        console.print(f"[bold green]Groq CLI[/bold green] - Using model: {model}")

        # Interactive mode or single query
        if args.interactive:
            console.print("[bold]Interactive Mode[/bold] (Ctrl+C to exit)")

            try:
                while True:
                    # Get prompt from user
                    prompt = prompt_user()
                    if not prompt.strip():
                        continue

                    # Get and print response
                    response = api.ask(prompt, max_tokens=max_tokens, temperature=temperature)
                    print_response(response)
                    console.print("\n" + "-" * 50 + "\n")
            except KeyboardInterrupt:
                console.print("\n[bold]Exiting interactive mode.[/bold]")
        else:
            # Single query mode
            prompt = args.prompt
            if not prompt:
                prompt = prompt_user()

            response = api.ask(prompt, max_tokens=max_tokens, temperature=temperature)
            print_response(response)

    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        return 1
    except KeyboardInterrupt:
        console.print("\n[bold]Operation cancelled by user.[/bold]")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())