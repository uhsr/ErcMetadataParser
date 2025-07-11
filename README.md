# ErcMetadataParser

## Description

A curated collection of Solidity smart contracts implementing ERC-721 extensions for fractionalized NFT ownership and dynamic metadata updates via on-chain SVG generation, optimized for L2 scaling solutions using calldata compression.

## Features

- Extract ERC-721 and ERC-1155 metadata fields, including name, description, and image URL, from on-chain data.
- Utilize Infura or Alchemy APIs for efficient blockchain data retrieval, handling rate limits and API key management.
- Implement a caching mechanism with configurable TTL to reduce redundant API calls and improve performance.
- Support parsing of metadata URIs that conform to IPFS, Arweave, and HTTP(S) protocols.
- Provide a fallback mechanism to retrieve metadata from centralized storage if on-chain data is unavailable.
- Integrate with OpenSea's metadata standards to ensure compatibility with their display requirements.
- Expose a GraphQL API endpoint for querying ERC-721 and ERC-1155 metadata by token ID or contract address.
- Implement robust error handling and logging to identify and address issues related to metadata parsing or API connectivity.
## Installation

```bash
pip install ercmetadataparser
```

## Usage

```python
from ercmetadataparser import ErcMetadataParser

# Initialize
app = ErcMetadataParser()

# Run
app.run()
```

## Contributing

We welcome contributions! Here's how to get started:

1. Fork this repository
2. Create a new branch for your feature (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some awesome feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.
