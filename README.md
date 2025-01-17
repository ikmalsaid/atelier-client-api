# Atelier Client API

A hostable web API for Atelier clients that provides various image manipulation and generation endpoints.

## Features

- Image generation and variation
- Face restoration and identity preservation
- Style transfer and guidance
- Real-time image processing
- Background removal and upscaling
- Image captioning and prompt generation
- And many more...

## Installation

```bash
pip install atelier-client-api
```

## Quick Start

```python
from atelier_client_api import AtelierWebAPI
from atelier_client import AtelierClient

# Initialize your client
client = AtelierClient(save_as='pil') # Save output as PIL Image

# Start the API server
AtelierWebAPI(
    client=client,
    host="0.0.0.0",  # Host to bind to
    port=5733,       # Port to listen on
    debug=False      # Enable debug mode
)
```

## API Documentation

The API documentation is available at the root endpoint (`/`) when you run the server. It provides a comprehensive list of all available endpoints, their parameters, and usage examples.

### Available Endpoints

All endpoints are prefixed with `/v1/api/`. Here are some key endpoints:

- `POST /v1/api/image/generate` - Generate images from text prompts
- `POST /v1/api/image/variation` - Create variations of existing images
- `POST /v1/api/face/gfpgan` - Restore faces using GFPGAN
- `POST /v1/api/image/enhance` - Enhance image quality
- And many more...

For a complete list of endpoints and their parameters, please refer to the API documentation page served at the root endpoint.

## Response Format

All API endpoints return responses in the following JSON format:

```json
{
    "success": true,
    "result": "data:image/png;base64,..." // Base64 encoded image or text result
}
```

## Error Handling

In case of errors, the API returns:

```json
{
    "success": false,
    "error": "Error message describing what went wrong"
}
```

## License

See [LICENSE](LICENSE) for more details.
