
# QuantumQR

QuantumQR is a command-line tool for generating and decoding QR codes. It supports creating QR codes for URLs, vCards, Wi-Fi credentials, and batch processing from a file.

## Features
- **QR Generation:** Create QR codes for URLs, vCards, and Wi-Fi access.
- **Batch Processing:** Generate multiple QR codes from a text file.
- **Decoding:** Extract data from QR code images.
- **URL Shortening:** Optionally shorten URLs via TinyURL.


## Installation

### Via PyPI
```bash
pip install quantumqr
```

### From Source
```bash
git clone https://github.com/yourusername/quantumqr.git
cd quantumqr
pip install .
```

## Usage
Display help:
```bash
quantumqr -h
```

Example - Generate a QR code for a URL:
```bash
quantumqr --link "https://example.com" --output "example.png"
```

## License
MIT License

## Contributing & Contact
Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.  
For issues or questions, visit our [GitHub repository](https://github.com/yourusername/quantumqr).
```
