from rich.console import Console

console = Console()

from rich.console import Console

console = Console()

def generate_ui(window_title: str, score: float, uptime: str) -> str:
    """
    renders the borderless terminal matrix overlay with absolute line breaks.
    """
    if score > 70:
        color = "bright_green"
        status = "STABLE FOCUS (LOCK_ENGAGED)"
    elif score > 40:
        color = "yellow"
        status = "DRIFTING (COGNITIVE_WARMUP)"
    else:
        color = "bright_red"
        status = "BREACH DETECTED (ATTENTION_DECAY)"

    # render the geometric block bar
    bar_width = int(score / 2)
    matrix_bar = f"[{color}]" + "█" * bar_width + "░" * (50 - bar_width) + "[/]"
    
    truncated_title = window_title[:50] + "..." if len(window_title) > 50 else window_title

    # We join a list of strings with a real newline to force Windows to format it right
    hud_lines = [
        "",
        f" [bold white]── F O C U S ────────────────────────────────────────────────── v1.0.0 ──[/bold white]",
        "",
        f"  [bold white][TARGET][/bold white]  {truncated_title}",
        f"  [bold white][STATUS][/bold white]  [{color}]{status}[/]",
        "",
        f"  [bold white][MATRIX][/bold white]  [{matrix_bar}]  [bold {color}]{score}%[/bold {color}]",
        "",
        f" [bold white]─────────────────────────────────────────── RUN_TIME: {uptime} // LOCAL ──[/bold white]"
    ]
    
    return "\n".join(hud_lines)
