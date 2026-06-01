import sys
import psutil
def get_active_window_title() -> str:
    """
    grabs the active window title natively depending on your OS.
    """
    try:
        if sys.platform == "win32":
            import pygetwindow as gw
            window = gw.getActiveWindow()
            return window.title if window else "Unknown"
        elif sys.platform == "darwin":
            from subprocess import Popen, PIPE
            script = 'tell application "System Events" to get name of first process whose frontmost is true'
            p = Popen(['osascript', '-e', script], stdout=PIPE, stderr=PIPE)
            stdout, _ = p.communicate()
            return stdout.decode('utf-8').strip()
        elif sys.platform.startswith("linux"):
            from ewmh import EWMH
            ewmh = EWMH()
            window = ewmh.getActiveWindow()
            if window:
                return window.get_wm_name()
            return "Unknown"
    except Exception:
        return "Away from Keyboard"
    return "Unknown"
def analyze_focus_state(title: str) -> float:
    """
    maps workspace targets to focus coefficients.
    """
    title_lower = title.lower()
    # actual dev keywords vs distractions
    focus_keywords = ['vscode', 'visual studio', 'neovim', 'tmux', 'terminal', 'github', 'stackoverflow', 'docs', 'localhost']
    distraction_keywords = ['youtube', 'twitter', 'x.com', 'reddit', 'netflix', 'facebook', 'instagram', 'discord']
    for kw in distraction_keywords:
        if kw in title_lower:
            return -1.0
    for kw in focus_keywords:
        if kw in title_lower:
            return 1.0
    return 0.1
