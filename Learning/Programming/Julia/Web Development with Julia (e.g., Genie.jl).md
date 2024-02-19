Yes, Julia supports creating API web servers. One of the popular frameworks for building web applications and APIs in Julia is `Genie.jl`. Genie is a full-stack web framework that provides tools for building web applications, including APIs.

Here's a basic example of how you can create a simple API using Genie:

1. Install Genie:

```julia
import Pkg
Pkg.add("Genie")
```

2. Create a simple API using Genie:

```julia
using Genie

# Create a Genie app
app = Genie()

# Define an API route
route(app, "GET", "/api/hello") do
    return JSON["message" => "Hello, API!"]
end

# Start the Genie app
up(app)
```

In this example, we create a Genie app, define a route for a GET request at the endpoint "/api/hello," and respond with a JSON message.

You can run this script, and your API will be accessible at `http://localhost:8000/api/hello`. You can customize the routes and responses based on your API's requirements.

Note: For more complex APIs and larger web applications, you might want to explore Genie's documentation and consider additional features like database integration, middleware, etc.