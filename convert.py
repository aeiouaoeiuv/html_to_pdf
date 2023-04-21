#!/usr/bin/python3

import argparse
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration


def convert_html_to_pdf(input_file, output_file):
    # Convert HTML to PDF
    font_config = FontConfiguration()
    css = CSS(
        string="""
        @font-face {
            font-family: 'Noto Sans CJK SC';
            src: url(file:///workspace/NotoSansCJKsc-Regular.otf) format('opentype');
        }
        body {
            font-family: 'Noto Sans CJK SC';
        }""",
        font_config=font_config,
    )

    HTML(input_file).write_pdf(output_file, stylesheets=[css], font_config=font_config)


def main():
    # Define the command-line arguments
    parser = argparse.ArgumentParser(description="Convert HTML to PDF")
    parser.add_argument("input", help="The input HTML file")
    parser.add_argument("output", help="The output PDF file")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Convert HTML to PDF
    convert_html_to_pdf(args.input, args.output)


if __name__ == "__main__":
    main()
