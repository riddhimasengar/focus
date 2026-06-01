import time
import sys
from rich.live import Live
from engine.core import FocusEngine
from engine.interface import generate_ui
def main():
    engine = FocusEngine()
    # wipe terminal and hide cursor for a clean utility frame
    print("\033[H\033[J\033[?25l", end="") 
    try:
        with Live(generate_ui("INITIALIZING...", 50.0, "00:00:00"), refresh_per_second=2, screen=False) as live:
            while True:
                window, score = engine.update()
                uptime = engine.get_uptime()
                live.update(generate_ui(window, score, uptime))
                time.sleep(0.5)
    except KeyboardInterrupt:
        # restore terminal cursor when killing script
        print("\033[?25h")
        print("\n[bold red]── ENGINE HALTED ──[/bold red]\n")
        sys.exit(0)
if __name__ == "__main__":
    main()
