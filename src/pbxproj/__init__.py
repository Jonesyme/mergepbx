from .pbxobjects import PBXProjFile
from . import core
from . import isa
from . import reader
from . import writer
from . import pbxobjects
from plist import NSPlistReader

def read(fname_or_f):
    #open file if fname_or_f is a string
    #else use it as f
    if isinstance(fname_or_f, str) or isinstance(fname_or_f, unicode):
        f = open(fname_or_f)
    else:
        f = fname_or_f
    #read project
    reader = NSPlistReader(f)
    return PBXProjFile(reader.read())

def write(fname_or_f, data, encoding="utf-8"):
    #open file if fname_or_f is a string
    #else use it as f
    if isinstance(fname_or_f, str) or isinstance(fname_or_f, unicode):
        f = open(fname, "w", encoding=encoding)
    else:
        f = fname_or_f
    #write project
    w = writer.PBXProjectPlistWriter(f)
    w.write_project(data)
