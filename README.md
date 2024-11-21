# Introduction

This is a learning project focused on gRPC functionality.

More information about gRPC and the code can be found in `docs/` directory.

> Inspired by: [Building APIs with gRPC](https://medium.com/google-cloud/building-apis-with-grpc-50842234aec8)

# Prerequisites

1. Install gRPC and Protocol Bufferrs:

```bash
pip3 install grpcio grpcio-tools
```

2. Protocol Buffers compiler prepares the server-end and the client-end artifacts:

```bash
python3 -m grpc_tools.protoc -I. --python_out=codegen/ --grpc_python_out=codegen/ example.proto
```
                                                                 |
# Getting Started

1. Start the server:

```bash
python3 server.py 
```

Output:

```bash
API server started. Listening at 0.0.0.0:8080.
```

2. Start the client:

The client fetches the service endpoint specified in `example.proto` file, and outputs `User` and `Status` objects.

```bash
python3 client.py  
```

Output:

```bash
User fetched.
name: "//myawesomeapiservice.com/users/1"
display_name: "Example User"
email: "user@example.com"

Status fetched.
status: "online"
validity: "OK"
```