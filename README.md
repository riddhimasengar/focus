# focus

a minimalist, zero-telemetry window manager sniffer that runs locally in your terminal to map your real-time cognitive velocity.

## about the developer
heyyy! i'm a high school senior using this project to learn python, figure out how operating systems track active windows, and finally learn how to use github properly.

## why it exists
most productivity tools are web apps that hog memory, or background telemetry logging your data to an external server. 

`focus` runs entirely offline. it queries your host operating system's window manager once a second to see what you're looking at. if you're in an ide or terminal, your momentum builds. if you pull up a distraction, it recoils your score instantly.

## installation

copy and paste the command for your operating system into your terminal to download, setup, and run the app:

### windows
```cmd
git clone [https://github.com/riddhimasengar/focus.git](https://github.com/riddhimasengar/focus.git) && cd focus && py -m pip install -r requirements.txt && py run.py
```
### for mac / linux:
```cmd
git clone [https://github.com/riddhimasengar/focus.git](https://github.com/riddhimasengar/focus.git) && cd focus && pip install -r requirements.txt && python3 run.py
