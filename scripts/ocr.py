#!/usr/bin/env python3
import sys
from pathlib import Path
import argparse
import pytesseract
from PIL import Image
import fitz  # module 'pymupdf'

from runes import RUNE

# supported formats
EXTENSIONS = {'.png', '.jpg', '.jpeg', '.tif', '.tiff', '.bmp'}

def ocr_image(path: Path) -> str:
    '''
    Runs Tesseract OCR on an image file and saves the extracted text
    to a .txt file with the same base name as the image.

    Parameters:
    -----------
    path : Path
        Path to the image file.

    Returns:
    --------
    Path
        Path to the saved .txt output file.
    '''
    # open the image file
    with Image.open(path) as img:
        text = pytesseract.image_to_string(img)

    # build output path (same directory, same base name, .txt extension)
    output_path = path.with_suffix('.txt')

    # write extracted text to file
    output_path.write_text(text, encoding = 'utf-8')

    return output_path


def ocr_pdf(path: Path, start: int | None, end: int | None) -> str:
    '''
    Runs OCR on a PDF using PyMuPDF and saves extracted text to a .txt file.

    Parameters:
    -----------
    path : Path
        Path to the PDF file.

    start : int | None
        First page to process (1-based), or None for beginning.

    end : int | None
        Last page to process (inclusive), or None for end.

    Returns:
    --------
    Path
        Path to the saved .txt output file.
    '''
    doc = fitz.open(path)
    save_as = path.with_suffix('.txt')

    start = 0 if start is None else max(start - 1, 0)
    end = len(doc) if end is None else min(end, len(doc))

    with open(save_as, 'w', encoding='utf-8') as out:
        for i, pg in enumerate(doc[start : end], start = start + 1):
            text = pg.get_text() or ''
            out.write(f'\n--- PAGE {i}/{len(doc)} ---\n\n')
            out.write(text + '\n')

    return save_as

if __name__ == '__main__':
    # argument parser
    parser = argparse.ArgumentParser(description = 'ocr a file in ~/Desktop/ocr and output .txt to same folder')
    parser.add_argument('filename', help = 'file inside CWD to process')
    parser.add_argument('-s', type = int, help = 'start page (pdf only, 1-based)')
    parser.add_argument('-e', type = int, help = 'end page (pdf only, inclusive)')
    args = parser.parse_args()

    f = Path(args.filename).resolve()

    try:
        # choose correct OCR path depending on extension
        if f.suffix.lower() in EXTENSIONS:
            save_as = ocr_image(f)
        elif f.suffix.lower() == '.pdf':
            save_as = ocr_pdf(f, start = args.s, end = args.e)
        else:
            print(f'[{RUNE.FG_BRIGHT_RED}error{RUNE.RESET}]: unsupported file extension: {f.suffix}', file = sys.stderr)
            sys.exit(1)

        # print final path
        print(f' [{RUNE.FG_BRIGHT_GREEN}ok{RUNE.RESET}]: \n   -- extracted from {RUNE.FG_BRIGHT_CYAN}{f.name}{RUNE.RESET} --')
        print(f'   -- saved as {RUNE.FG_BRIGHT_MAGENTA}{save_as.name}{RUNE.RESET} --')

    except Exception as e:
        print(f'[{RUNE.FG_BRIGHT_RED}error{RUNE.RESET}]: {e}', file = sys.stderr)
        sys.exit(1)
