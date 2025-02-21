# D&D Extended Character sheet

This LaTeX character sheet is designed for use in Dungeon and Dragons sessions, offering plenty of space for additional information.
An autoupdater is included (via the PDFUpdater.py file), which automatically updates older sheets to the latest version.

Features:
    - Autoupdater
    - Customizable character sheet
    - More notes space
    - White and dark mode
    - Support for multiple languages
      - English
      - Italian
      - It is possible to add more languages (by creating a new "strings-XX.tex" file)

# How to compile the LaTeX file
**Already compiled PDFs can be found on the releases page.**
To compile the LaTeX file, use LuaLaTeX.
The _eforms_ package is required and is not included in TeXLive due to licensing issues.

## How to install eforms if you are using TexLive
Download the code from https://ctan.org/pkg/eforms, compile it and then move the directory into:

```C:\texlive\texmf-local\tex\latex```

Or if you are using Linux:

```/usr/share/texlive/texmf-local/tex/latex/```

And then run the following command:

```mktexlsr```

# Missing features
Auto-calculating for skills and on check-boxes is not implemented.

# Possible errors that could be encountered
- _xref table error_ during the execution of the update script
  - This could be due to the presence of special emoji in a TextField, fix this by saving the PDF (as new) and using this file as input instead.    
