import time
from engine.tracking import get_active_window_title, analyze_focus_state
class FocusEngine:
    def __init__(self):
        self.focus_score = 50.0
        self.history = []
        self.start_time = time.time()
    def update(self):
        """
        polls the os window manager and mutates the momentum score.
        """
        current_window = get_active_window_title()
        weight = analyze_focus_state(current_window)
        # unfair math: focus builds slowly, drops instantly on distraction
        if weight < 0:
            self.focus_score += weight * 2.5
        else:
            self.focus_score += weight * 0.8
        self.focus_score = max(0.0, min(100.0, self.focus_score))
        self.history.append({
            "timestamp": time.time(),
            "window": current_window,
            "score": self.focus_score
        })
        return current_window, round(self.focus_score, 1)
    def get_uptime(self) -> str:
        seconds = int(time.time() - self.start_time)
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        return f"{hours:02d}:{mins:02d}:{secs:02d}"
