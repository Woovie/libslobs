# libslobs
Library for slobs-client, StreamLabs OBS API

# How?
Stream Labs OBS provides a websocket-based API which can be used to do just about anything in the Stream Labs client. [See their documentation here](https://stream-labs.github.io/streamlabs-obs-api-docs/docs/index.html).

# So what does this project do?
I am taking all of their websocket endpoints and turning them into a Python library, making it easier to use these tools. Instead of trying to figure out how to write to their websocket, which uses SockJS, and what format the data needs to be, just simply use this library instead which provides all of that functionality, but in a Pythonic manner.

# How do I get started?
1. Install Stream Labs OBS
2. Install Python 3.8.x from [here](https://www.python.org/downloads/).
2. Enable remote connections in Stream Labs OBS by nativgating to Settings -> Remote Control, and click on the QR code that is shown, then click Show details.
3. ???
## TODO
