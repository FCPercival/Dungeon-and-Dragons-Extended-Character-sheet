# D&D Extended Character sheet

This LaTeX character sheet is designed for use in Dungeon and Dragons sessions, offering plenty of space for additional information.
An autoupdater is included (via the PDFUpdater.py file), which automatically updates older sheets to the latest version.

Support the following languages:
 - English
 - Italian

It is possible to add further languages with ease by creating a new "strings-XX.tex" file (Pull requests are welcome).

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
