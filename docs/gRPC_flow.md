# Flow of The Communication

1. Client creates gRPC channel & stub (Stubs = simplified **interface for clients to make remote method calls on the server**. Stubs handle the serialization of data, sending requests to the server, and deserialization of responses)
2. Client invokes `get_user` with `name` parameter, and `get_status` with `status` parameter.

`client.py`:
```py
client_service = ExampleServiceClient()
client_service.get_user('//myawesomeapiservice.com/users/1')
client_service.get_status('online')
```

3. client will prepare it into a `GetUserRequest` and `GetStatusRequests` Python class and passed to gRPC via the `ExampleServiceStub`

`client.py`:
```py
class ExampleServiceClient(object):
def __init__(self):
    
    # some code

    # ExampleServiceStub
    self.stub = example_pb2_grpc.ExampleServiceStub(self.channel)

def get_user(self, name):
   
    # some code
   
    # GetUserRequest
    request = example_pb2.GetUserRequest(
        name = name
    )


def get_status(self, status):
    
    # some code

    # GetStatusRequest
    request = example_pb2.GetStatusRequest(
        status = status
    )
```

4. **Client side**: gRPC then converts/ parses the `GetUserRequest` and `GetStatusRequest` Python class into a Protocol Buffer message and send it to the server

5. **Server** receives `GetUserRequest` and `GetStatusRequest`, process it, and creates `User` and `Status` response (defined in `User` and `Status` Protocol Buffer message)

6. **Server side**: gRPC converts/ parses `User` and `Status` message into a Python `User` and `Status` class

7. **Client** receives `User` and `Status` class and details (name and status) are printed out

8. Done


## Simplication of The Flow

- `.proto` file is a contract between `client` and `server`
- gRPC is the courier
- Protocol Buffer is the translator

Protocol Buffer enforces the contract (`.proto` file), and translates what `client` and `server` speak from/into a unviversal language, with gRPC carrying the communication around in HTTP/2.

Protocol Buffers perform all administrative tasks behind the scenes (transportation, seriliazation, etc.) so your `server` and `client` can focus on what is important - the business logic of the application.

