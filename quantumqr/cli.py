#!/usr/bin/env python3

import qrcode
import argparse
import qrcode_terminal
import requests
import os
import cv2
import numpy as np
from PIL import Image

def shorten_url(url):
    """Shorten a URL using the TinyURL API."""
    response = requests.get(f"https://tinyurl.com/api-create.php?url={url}")
    return response.text if response.status_code == 200 else url


def generate_qr_code(link, output, directory=".", color="black", bgcolor="white"):
    """Generate a QR code, display it in the terminal, and save it."""
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(link)
    qr.make(fit=True)

    # Generate the image file
    img = qr.make_image(fill=color, back_color=bgcolor).convert("RGB")
    save_path = os.path.join(directory, output)
    img.save(save_path)

    # Display the QR code in the terminal
    qrcode_terminal.draw(link)
    return save_path


def batch_generate_qr(file, directory):
    """Generate multiple QR codes from a file containing links (one per line)."""
    if not os.path.exists(file):
        return

    os.makedirs(directory, exist_ok=True)
    with open(file, "r") as f:
        links = f.readlines()

    for i, link in enumerate(links):
        link = link.strip()
        if link:
            generate_qr_code(link, f"qr_code_{i+1}.png", directory)


def decode_qr_code(image_path):
    """Decode a QR code from an image file and return the extracted data."""
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)
    return data if data else None


def generate_vcard(name, phone, email, output, directory="."):
    """Generate a vCard QR code containing contact information."""
    vcard_data = f"""
BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD
"""
    return generate_qr_code(vcard_data, output, directory)


def generate_wifi_qr(ssid, password, security, output, directory="."):
    """Generate a QR code for Wi-Fi access."""
    wifi_data = f"WIFI:T:{security};S:{ssid};P:{password};;"
    return generate_qr_code(wifi_data, output, directory)


def cli():
    parser = argparse.ArgumentParser(description="QuantumQR - The Ultimate QR Code Generator")

    parser.add_argument("-l", "--link", type=str, metavar="URL", help="Generate a QR code from a URL and display it in the terminal.")
    parser.add_argument("-o", "--output", type=str, default="qrcode.png", metavar="FILENAME", help="Output file name.")
    parser.add_argument("-b", "--batch", type=str, metavar="FILENAME", help="Generate multiple QR codes from a text file.")
    parser.add_argument("-r", "--read", type=str, metavar="IMAGE", help="Decode a QR code from an image file.")
    parser.add_argument("-vc", "--vcard", nargs=3, metavar=("NAME", "PHONE", "EMAIL"), help="Generate a vCard QR code.")
    parser.add_argument("-wf", "--wifi", nargs=3, metavar=("SSID", "PASSWORD", "SECURITY"), help="Generate a Wi-Fi QR code.")

    args = parser.parse_args()

    if args.batch:
        batch_generate_qr(args.batch, os.getcwd())
    elif args.read:
        decoded_data = decode_qr_code(args.read)
        if decoded_data:
            print(decoded_data)
    elif args.vcard:
        generate_vcard(*args.vcard, args.output)
    elif args.wifi:
        generate_wifi_qr(*args.wifi, args.output)
    elif args.link:
        generate_qr_code(args.link, args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    cli()
