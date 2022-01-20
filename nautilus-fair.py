#!/usr/bin/env python
import os

from gi.repository import Nautilus as FileManager
from gi.repository import GObject


# from https://dans.knaw.nl/en/file-formats/
PREF = [
    ".pdf",
    ".odt",
    ".txt",
    ".xml",
    ".html",
    ".css",
    ".xslt",
    ".js",
    ".es",
    ".ods",
    ".csv",
    ".dat",
    ".sps",
    ".DO",
    ".jpg",
    ".jpeg",
    ".tif",
    ".tiff",
    ".png",
    ".jp2",
    ".dcm",
    ".svg",
    ".bwf",
    ".mxf",
    ".mka",
    ".flac",
    ".mxf",
    ".mkv",
    ".dxf",
    ".gml",
    ".mif",
    ".mid",
    ".asc",
    ".obj",
    ".ply",
    ".x3d",
    ".dae",
    ".rdf",
    ".trig",
    ".ttl",
    ".nt",
]

NON_PREF = [
    ".xlsx",
    ".docx",
    ".doc",
    ".rtf",
    ".sgml",
    ".md",
    ".xls",
    ".mdb",
    ".accdb",
    ".dbf",
    ".hdf5",
    ".he5",
    ".h5",
    ".por",
    ".sav",
    ".dta",
    ".7dat",
    ".sd2",
    ".tpt",
    ".ai",
    ".eps",
    ".wmf",
    ".emf",
    ".cdr",
    ".wav",
    ".mp3",
    ".aac",
    ".m4a",
    ".m4v",
    ".mpg",
    ".mpeg",
    ".m2v",
    ".mpg2",
    ".avi",
    ".mov",
    ".qt",
    ".dxf",
    ".dwg",
    ".dgn",
    ".kml",
    ".kmz",
    ".gdb",
    ".mxd",
    ".wor",
    ".qgs",
    ".jpg",
    ".img",
    ".grd",
    ".fbx",
    ".blend",
]  # note that there is some overlap with PREF


class ColumnExtensionFAIR(
    GObject.GObject, FileManager.ColumnProvider, FileManager.InfoProvider
):
    def __init__(self):
        pass

    def get_columns(self):
        return (
            FileManager.Column(
                name="FileManagerPython::FAIRness",
                attribute="FAIRness",
                label="FAIRness",
                description="FAIRness of the file extension...",
            ),
        )

    def update_file_info(self, file):
        filename, file_extension = os.path.splitext(file.get_name())

        rating = "◯"  # default 'blank' if filetype is unknown
        if file.is_directory():
            rating = ""
        elif not file_extension:
            rating = "◯"
        elif file_extension in PREF:
            rating = "🟢"
        elif file_extension in NON_PREF:
            rating = "🟠"

        file.add_string_attribute("FAIRness", rating)
