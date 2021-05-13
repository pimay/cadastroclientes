#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 23:52:20 2021

@author: hideosuzuki
"""

from tkinter import *
from tkinter import ttk
import sqlite3
#fazer relatorio
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
#chamar navegador padrao do computador
import webbrowser