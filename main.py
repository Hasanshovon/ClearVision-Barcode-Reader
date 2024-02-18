#!/usr/bin/env python

import cv2
from pyzbar import pyzbar
import typer

app = typer.Typer()

@app.command()
def read_barcode(image_path: str):
    """
    Reads barcodes from the given image file.
    """
    # Load the image
    img = cv2.imread(image_path)

    # Decode the barcodes
    barcodes = pyzbar.decode(img)

    for barcode in barcodes:
        # Retrieve barcode location
        x, y, w, h = barcode.rect
        # Draw a rectangle around the barcode
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

        # Decode the barcode data
        bdata = barcode.data.decode("utf-8")
        btype = barcode.type
        text = f"{bdata}, {btype}"

        # Add text above the barcode
        cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        print(f"Found {btype} barcode: {bdata}")

    # Display the Processed Image
    cv2.imshow("Processed Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    app()

