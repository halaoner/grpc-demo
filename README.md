# Introduction

This is a learning project focused on gRPC functionality.

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