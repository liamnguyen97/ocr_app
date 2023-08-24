In this tutorial, you will make a callback, which is simply an API so that the server can call after finishing the request.

First, start the callback by the following commands:

```shell
python webhook_server.py
```

, then open a new terminal and start your API server by

```shell
python main.py
```

now, open the 3rd terminal, and send a request to your API server
```shell
python client.py
```