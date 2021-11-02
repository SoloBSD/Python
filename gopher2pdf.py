#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gopher2pdf.py
#  
#  Copyright 2021 Guillermo García Rojas C. <garciarojas@solobsd.org>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
#
# Program that takes an argument - A gopher url - and produces a
# PDF document from the gopher page.
# This is intended to produce a PDF from a text document, not from a 
# gopher menu page.
#

import pituophis
import sys
from txt2pdf.core import txt2pdf

pdf_file_path = "/home/memo/Python/Document.pdf" # Point to your preferred directory

req = pituophis.parse_url(str(sys.argv[1]))
print('Getting: ', req.url())
rsp = req.get()

# Creating the text file.

f = open("gopher_text.md", "w")
        
md_content = str(rsp.text())
f.write(md_content)

f.close()

# Creating the PDF.

txt2pdf(pdf_file_path,md_content)
