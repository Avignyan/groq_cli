from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
import sys
from typing import Dict, Any

console = Console()


def print_response(response: Dict[str, Any]) -> None:
    if "error" in response and response["error"]:
        console.print(Panel(f"[bold red]Error:[/bold red] {response['error']}",
                            title="Error", border_style="red"))
        return

    md = Markdown(response["text"])
    console.print(Panel(md, title=f"Response from {response['model']}", border_style="green"))

    # Print usage information
    if "usage" in response:
        usage = response["usage"]
        console.print(
            f"[dim]Tokens used: {usage['prompt_tokens']} (prompt) + "
            f"{usage['completion_tokens']} (completion) = "
            f"{usage['total_tokens']} (total)[/dim]"
        )


def prompt_user() -> str:
    console.print("[bold blue]Enter your question:[/bold blue]")
    return input("> ")