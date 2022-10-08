"""Hops flask middleware example"""
from flask import Flask
import ghhops_server as hs
import rhino3dm


# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)


# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"


import math


@hops.component(
    "/binmult",
    inputs=[hs.HopsNumber("A"), hs.HopsNumber("B")],
    outputs=[hs.HopsNumber("Multiply")],
)
def BinaryMultiply(a: float, b: float):
    return a * b


@hops.component(
    "/add",
    name="Add",
    nickname="Add",
    description="Add numbers with CPython",
    inputs=[
        hs.HopsNumber("A", "A", "First number"),
        hs.HopsNumber("B", "B", "Second number"),
    ],
    outputs=[hs.HopsNumber("Sum", "S", "A + B")]
)
def add(a: float, b: float):
    return a + b


@hops.component(
    "/pointat",
    name="PointAt",
    nickname="PtAt",
    description="Get point along curve",
    icon="pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate")
    ],
    outputs=[hs.HopsPoint("P", "P", "Point on curve at t")]
)
def pointat(curve: rhino3dm.Curve, t=0.0):
    return curve.PointAt(t)


@hops.component(
    "/srf4pt",
    name="4Point Surface",
    nickname="Srf4Pt",
    description="Create ruled surface from four points",
    inputs=[
        hs.HopsPoint("Corner A", "A", "First corner"),
        hs.HopsPoint("Corner B", "B", "Second corner"),
        hs.HopsPoint("Corner C", "C", "Third corner"),
        hs.HopsPoint("Corner D", "D", "Fourth corner")
    ],
    outputs=[hs.HopsSurface("Surface", "S", "Resulting surface")]
)
def ruled_surface(a: rhino3dm.Point3d,
                  b: rhino3dm.Point3d,
                  c: rhino3dm.Point3d,
                  d: rhino3dm.Point3d):
    edge1 = rhino3dm.LineCurve(a, b)
    edge2 = rhino3dm.LineCurve(c, d)
    return rhino3dm.NurbsSurface.CreateRuledSurface(edge1, edge2)





"""
██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗      
██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝██║████╗  ██║██╔════╝      
██║ █╗ ██║██║   ██║██████╔╝█████╔╝ ██║██╔██╗ ██║██║  ███╗     
██║███╗██║██║   ██║██╔══██╗██╔═██╗ ██║██║╚██╗██║██║   ██║     
╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗██║██║ ╚████║╚██████╔╝     
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝      
                                                              
██╗    ██╗██╗████████╗██╗  ██╗                                
██║    ██║██║╚══██╔══╝██║  ██║                                
██║ █╗ ██║██║   ██║   ███████║                                
██║███╗██║██║   ██║   ██╔══██║                                
╚███╔███╔╝██║   ██║   ██║  ██║                                
 ╚══╝╚══╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝                                
                                                              
██╗     ██╗██████╗ ██████╗  █████╗ ██████╗ ██╗███████╗███████╗
██║     ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██╔════╝
██║     ██║██████╔╝██████╔╝███████║██████╔╝██║█████╗  ███████╗
██║     ██║██╔══██╗██╔══██╗██╔══██║██╔══██╗██║██╔══╝  ╚════██║
███████╗██║██████╔╝██║  ██║██║  ██║██║  ██║██║███████╗███████║
╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝

"""


# python all-in-one for dummies, second edition
# continued... Book 3 Chapter 1
# Working with External Files
# folders and directories
# creating, reading, writing, and deleting files

# Understanding Text and Binary Files
# Plain Text Files (txt) and Binary Files (bin) .csv
# source code: .py, .html, .css, .js
# Data: .json, .xml, .csv, .tsv, .txt, .bin

# Executable Files (.exe) , .dmg, .bin(
# Images: .png, .jpg, .gif, .bmp, .ico
# Audio: .mp3, .wav, .aiff, .aac, .ogg, .flac
# Video: .mp4, .avi, .mov, .wmv, .mkv, .flv, .webm
# Compressed Files: .zip, .rar, .7z, .tar, .gz, .bz2, .xz, .lzma, .zstd
# Font: .ttf, .otf, .woff, .woff2, .eot, .svg, .svgz
# Document: .pdf, .docx, .xlsx

# Use VS Code for Explorer Bar

# Opening and Closing 
# use syntax: open(filename, mode)
# use forward slash for directories rather than backslash for the more common Windows style

# r+ = read and write
# r = read only
# w = write only
# a = append only
# x = create only

# b = binary mode
# t = text mode

# var = open(filename, mode)
# f = open(filename, mode)

@hops.component(
    "/open_txt",
    name="Open",
    nickname="Open",
    description="Open a file",
    inputs=[hs.HopsString("Filename", "F", "Filename to open")],
    outputs=[hs.HopsString("Contents", "C", "Contents of the file")]
)
def open_txt(filename: str):
    with open(filename, "r") as f:
        filecontents = f.read()
        print(filecontents)   
    # The unindented line below is outside the function definition.
    print('File is closed automatically: ', f.closed)
    return filecontents

# careful with .jpg files and UTF-8 files
# check out "what is UTF-8 file encoding"
@hops.component(
    "/open_UTF-8",
    name="Open UTF-8",
    nickname="Open UTF-8",
    description="Open a UTF-8 file",
    inputs=[hs.HopsString("Filename", "F", "Filename to open")],
    outputs=[hs.HopsString("Contents", "C", "Contents of the file")]
)
def open_UTF_8(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        filecontents = f.read()
        print(filecontents)   
    # The unindented line below is outside the function definition.
    print('File is closed automatically: ', f.closed)
    return filecontents

# Reading a File's Contents
# use syntax: f.read()
# read([size]) reads at most size bytes from the file.
# readline() reads a single line from the file. Good for txt files only.
# readlines() reads the rest of the lines in the file. Good for txt files only.

@hops.component(
    "/read_txt",
    name="Read",
    nickname="Read",
    description="Read a file",
    inputs=[hs.HopsString("Filename", "F", "Filename to open")],
    outputs=[hs.HopsString("Contents", "C", "Contents of the file")]
)
def read_txt(filename: str):
    with open(filename, "r") as f:
        # read the entire file
        filecontents = f.read()
        print(filecontents)   
    # The unindented line below is outside the function definition.
    print('File is closed automatically: ', f.closed)
    return filecontents

@hops.component(
    "/readlines_txt",
    name="Read",
    nickname="Read",
    description="Read a file",
    inputs=[hs.HopsString("Filename", "F", "Filename to open")],
    outputs=[hs.HopsString("Contents", "C", "Contents of the file")]
)
def readlines_txt(filename: str):
    with open(filename, "r") as f:
        # read the entire file
        filecontents = f.readlines()
        print(filecontents)   
    # The unindented line below is outside the function definition.
    print('File is closed automatically: ', f.closed)
    return filecontents

@hops.component(
    "/readline_txt",
    name="Read",
    nickname="Read",
    description="Read a file",
    inputs=[hs.HopsString("Filename", "F", "Filename to open")],
    outputs=[hs.HopsString("Contents", "C", "Contents of the file")]
)
def readline_txt(filename: str):
    with open(filename, "r") as f:
        # read the entire file
        filecontents = f.readline()
        print(filecontents)   
    # The unindented line below is outside the function definition.
    print('File is closed automatically: ', f.closed)
    return filecontents

# Looping through a File's Contents

@hops.component(
    "/loop_txt",
    name="Loop",
    nickname="Loop",
    description="Loop through a file",
    inputs=[hs.HopsString("Filename", "F", "Filename to open")],
    outputs=[hs.HopsString("Contents", "C", "Contents of the file")]
)
def loop_txt(filename: str):
    with open(filename, "r") as f:
        # read the entire file then loop through it
        listOut = []
        for line in f:
            print(line, end='')
            listOut.append(line)
    # The unindented line below is outside the function definition.
    print('File is closed automatically: ', f.closed)
    return listOut

# Enumerate the Lines in a File
@hops.component(
    "/enumerated_txt",
    name="Loop",
    nickname="Loop",
    description="Loop through a file",
    inputs=[hs.HopsString("Filename", "F", "Filename to open")],
    outputs=[hs.HopsString("Contents", "C", "Contents of the file")]
)
def enumerated_txt(filename: str):
    with open(filename, "r") as f:
        # read the entire file then loop through it
        # count each line starting at 0
        listOut = []
        for one_line in enumerate(f.readlines()):
            # If counter is even number, print with no extra newline
            if one_line[0] % 2 == 0:
                print(one_line[1], end='')  # print the line
                listOut.append(one_line[1]) # append the line to the list
            # Otherwise, print a couple spaces and an extra newline
            else:
                print('  ' + one_line[1])  # print the line
                listOut.append('  ' + one_line[1]) # append the line to the list
    # The unindented line below is outside the function definition.
    print('File is closed automatically: ', f.closed)
    return listOut

# Looping through a File with readline()
@hops.component(
    "/loop_readline_txt",
    name="Loop",    
    nickname="Loop",
    description="Loop through a file",
    inputs=[hs.HopsString("Filename", "F", "Filename to open")],
    outputs=[hs.HopsString("Contents", "C", "Contents of the file")]
)
def loop_readline_txt(filename: str):
    with open(filename, "r") as f:
        # read the entire file then loop through it
        listOut = []
        one_line = f.readline()
        while one_line:
            print(one_line, end='')
            listOut.append(one_line)
            one_line = f.readline() 
    # The unindented line below is outside the function definition.
    print('File is closed automatically: ', f.closed)
    return listOut

# while loop with counter
@hops.component(
    "/loop_counter_readline_txt",
    name="Loop",    
    nickname="Loop",
    description="Loop through a file",
    inputs=[hs.HopsString("Filename", "F", "Filename to open")],
    outputs=[hs.HopsString("Contents", "C", "Contents of the file")]
)
def loop_counter_readline_txt(filename: str):
    # Store a number to use as a loop counter
    counter = 1
    # Open the file
    with open(filename, "r") as f:
        # read one line from the file
        listOut = []
        one_line = f.readline()
        # As long as there are lines to read
        while one_line:
            # If the counter is even, print a couple of spaces
            if counter % 2 == 0:
                print('  ' + one_line, end='')
                listOut.append('  ' + one_line)
                # Otherwise, print no new line at the end. 
            else:
                print(one_line, end='')
                listOut.append(one_line)
                # increment the counter
            counter += 1
            # Read the next line from the file
            one_line = f.readline()
    # The unindented line below is outside the function definition.
    print('File is closed automatically: ', f.closed)
    return listOut

# Appending verses overwriting files
@hops.component(
    "/append_new_txt",
    name="Append",
    nickname="Append",
    description="Append to a file",
    inputs=[
        hs.HopsString("Filename", "F", "Filename to open"),
        hs.HopsString("newline", "N", "Newline to append")
    ],

    outputs=[hs.HopsString("Contents", "C", "Contents of the file")]
)
def append_new_txt(filename: str, newline: str):
    # New name to add with \n to mark the end of the line
    new_name = newline + '\n'
    # Open the file for appending with encoding utf-8
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(new_name)
        print(new_name)
    # The unindented line below is outside the function definition.
    print('File is closed automatically: ', f.closed)
    return new_name 

# then open with /open_UTF-8 component

# Using tell() to determine the pointer location in a file
@hops.component(
    "/tell_test_txt",
    name="Tell",
    nickname="Tell",
    description="Tell the pointer location in a file",
    inputs=[hs.HopsString("Filename", "F", "Filename to open")],
    outputs=[   
        hs.HopsString("Contents", "C", "Contents of the file"),
        hs.HopsNumber("Pointer", "P", "Pointer location in the file")
        ]
)
def tell_test_txt(filename: str):
    with open(filename, encoding='utf-8') as f:
        # Read the first line to get started
        listOut = []
        tellOut = []
        print(f.tell())
        one_line = f.readline()
        # Keep reading one line at a time until the end of the file
        while one_line:
            print(one_line[:-1], f.tell())
            one_line = f.readline()
            listOut.append(one_line[:-1])
            tellOut.append(f.tell())
    # The unindented line below is outside the function definition.
    print('File is closed automatically: ', f.closed)
    return listOut, tellOut

# this works differently with readlines() function

# Moving the pointer with seek()
@hops.component(
    "/seek_10_txt",
    name="Seek",
    nickname="Seek",
    description="Seek to a location in a file",
    inputs=[
        hs.HopsString("Filename", "F", "Filename to open"),
        hs.HopsNumber("Pointer", "P", "Pointer location in the file")
    ],
    outputs=[hs.HopsString("Contents", "C", "Contents of the file")]
)   
def _seek_10_txt(filename: str, pointer: int):
    with open(filename, encoding='utf-8') as f:
        # Read the first line to get started
        listOut = []
        # Move the pointer to the location specified
        f.seek(pointer)
        # Read the first line to get started
        one_line = f.readline()
        # Keep reading one line at a time until the end of the file
        while one_line:
            print(one_line[:-1])
            one_line = f.readline()
            listOut.append(one_line[:-1])
    # The unindented line below is outside the function definition.
    print('File is closed automatically: ', f.closed)
    return listOut


# read a file and return the contents as a list of lines
@hops.component(
    "/readlines_txt",
    name="Readlines",
    nickname="Readlines",
    description="Read a file and return the contents as a list of lines",
    inputs=[hs.HopsString("Filename", "F", "Filename to open")],
    outputs=[hs.HopsString("Contents", "C", "Contents of the file")]
)
def readlines_txt(filename: str):
    with open(filename, encoding='utf-8') as f:
        # Read the first line to get started
        listOut = []
        # Read the first line to get started
        one_line = f.readline()
        # Keep reading one line at a time until the end of the file
        while one_line:
            print(one_line[:-1])
            one_line = f.readline()
            listOut.append(one_line[:-1])
    # The unindented line below is outside the function definition.
    print('File is closed automatically: ', f.closed)
    return listOut


"""
██████╗  █████╗ ████████╗ █████╗                     
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗                    
██║  ██║███████║   ██║   ███████║                    
██║  ██║██╔══██║   ██║   ██╔══██║                    
██████╔╝██║  ██║   ██║   ██║  ██║                    
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝                    
                                                     
███████╗ ██████╗██╗███████╗███╗   ██╗ ██████╗███████╗
██╔════╝██╔════╝██║██╔════╝████╗  ██║██╔════╝██╔════╝
███████╗██║     ██║█████╗  ██╔██╗ ██║██║     █████╗  
╚════██║██║     ██║██╔══╝  ██║╚██╗██║██║     ██╔══╝  
███████║╚██████╗██║███████╗██║ ╚████║╚██████╗███████╗
╚══════╝ ╚═════╝╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝

"""
# Google, Facebook, Apple, and Amazon are all companies that are
# essentially huge data processing entities.
# NumpPy is a library that is used to do data processing.
# Data science and machine learning are two fields that are
# used to do data processing.
# Pandas, scikit-learn, sklearn, and tensorflow are libraries that are used to do data processing.

# Basic Two-Dimensional Array Arithmetic
# Create a two-dimensional array
import numpy as np
# The Basics
# Create a two-dimensional array
@hops.component(
    "/array_A1D",
    name="Array 1D",
    nickname="Array 1D",
    description="Create a two-dimensional array",
    inputs=[
        hs.HopsNumber("Value1", "V1", "Value 1"), 
        hs.HopsNumber("Value2", "V2", "Value 2"),
        hs.HopsNumber("Value3", "V3", "Value 3")
        ],
    outputs=[hs.HopsNumber("Array", "A", "Array of values")]
)
def array_A1D(value1: int, value2: int, value3: int):
    # Create a two-dimensional array
    listOut = []
    arr = np.array([[value1, value2, value3]])
    # Print the array
    print(arr)
    arr = arr.tolist()
    print(arr)
    for i in arr:
        for j in i:
            listOut.append(j)
    return listOut

# create a two-dimensional array from two lists
@hops.component(
    "/array_A2D",
    name="Array 2D",
    nickname="Array 2D",
    description="Create a two-dimensional array from two lists",
    inputs=[
        hs.HopsString("List1", "L1", "List 1"),
        hs.HopsString("List2", "L2", "List 2")
        ],
    outputs=[hs.HopsString("Array", "A", "Array of values")]
)
def array_A2D(list1: list, list2: list):
    # Create a two-dimensional array
    listOut = []
    arr = np.array([list1, list2])
    # Print the array
    print(arr)
    arr = arr.tolist()
    print(arr)
    for i in arr:
        for j in i:
            listOut.append(j)
    return listOut

# create a three-dimensional array from three lists
@hops.component(
    "/array_A3D",
    name="Array 3D",
    nickname="Array 3D",
    description="Create a three-dimensional array from three lists",
    inputs=[
        hs.HopsString("List1", "L1", "List 1"),
        hs.HopsString("List2", "L2", "List 2"),
        hs.HopsString("List3", "L3", "List 3")
        ],
    outputs=[hs.HopsString("Array", "A", "Array of values")]
)
def array_A3D(list1: list, list2: list, list3: list):
    # Create a three-dimensional array
    listOut = []
    arr = np.array([list1, list2, list3])
    # Print the array
    print(arr)
    arr = arr.tolist()
    print(arr)
    for i in arr:
        for j in i:
            listOut.append(j)
    return listOut

# Numpy arithmetic
# add two arrays
@hops.component(
    "/array_Add",
    name="Array Add",
    nickname="Array Add",
    description="Add two arrays",
    inputs=[
        hs.HopsNumber("List1", "A1", "List 1"),
        hs.HopsNumber("List2", "A2", "List 2"),
        hs.HopsNumber("List3", "A3", "List 3"),
        hs.HopsNumber("List4", "B1", "List 4"),
        hs.HopsNumber("List5", "B2", "List 5"),
        hs.HopsNumber("List6", "B3", "List 6")
        ],
    outputs=[hs.HopsNumber("ArrayList", "A", "Array of values")]
)
def array_Add(list1: list, list2: list, list3: list, list4: list, list5: list, list6: list):
    # Create a three-dimensional array
    listOut = []
    arr_A = np.array([list1, list2, list3])
    # Print the array
    #print(arr_A)
    arr_B = np.array([list4, list5, list6])
    # Print the array
    #print(arr_B)
    arr_C = arr_A + arr_B
    # Print the array
    print(arr_C)
    arr_C = arr_C.tolist()
    print(arr_C)
    for i in arr_C:
        listOut.append(i)
    return listOut

# subtract two arrays
@hops.component(
    "/array_Sub",
    name="Array Sub",
    nickname="Array Sub",
    description="Subtract two arrays",
    inputs=[
        hs.HopsNumber("List1", "A1", "List 1"),
        hs.HopsNumber("List2", "A2", "List 2"),
        hs.HopsNumber("List3", "A3", "List 3"),
        hs.HopsNumber("List4", "B1", "List 4"),
        hs.HopsNumber("List5", "B2", "List 5"),
        hs.HopsNumber("List6", "B3", "List 6")
        ],
    outputs=[hs.HopsNumber("ArrayList", "A", "Array of values")]
)
def array_Sub(list1: list, list2: list, list3: list, list4: list, list5: list, list6: list):
    # Create a three-dimensional array
    listOut = []
    arr_A = np.array([list1, list2, list3])
    # Print the array
    #print(arr_A)
    arr_B = np.array([list4, list5, list6])
    # Print the array
    #print(arr_B)
    arr_C = arr_A - arr_B
    # Print the array
    print(arr_C)
    arr_C = arr_C.tolist()
    print(arr_C)
    for i in arr_C:
        listOut.append(i)
    return listOut

# multiply two arrays
@hops.component(
    "/array_Mul",
    name="Array Mul",
    nickname="Array Mul",
    description="Multiply two arrays",
    inputs=[
        hs.HopsNumber("List1", "A1", "List 1"),
        hs.HopsNumber("List2", "A2", "List 2"),
        hs.HopsNumber("List3", "A3", "List 3"),
        hs.HopsNumber("List4", "B1", "List 4"),
        hs.HopsNumber("List5", "B2", "List 5"),
        hs.HopsNumber("List6", "B3", "List 6")
        ],
    outputs=[hs.HopsNumber("ArrayList", "A", "Array of values")]
)
def array_Mul(list1: list, list2: list, list3: list, list4: list, list5: list, list6: list):
    # Create a three-dimensional array
    listOut = []
    arr_A = np.array([list1, list2, list3])
    # Print the array
    #print(arr_A)
    arr_B = np.array([list4, list5, list6])
    # Print the array
    #print(arr_B)
    arr_C = arr_A * arr_B
    # Print the array
    print(arr_C)
    arr_C = arr_C.tolist()
    print(arr_C)
    for i in arr_C:
        listOut.append(i)
    return listOut

# divide two arrays
@hops.component(
    "/array_Div",
    name="Array Div",
    nickname="Array Div",
    description="Divide two arrays",
    inputs=[
        hs.HopsNumber("List1", "A1", "List 1"),
        hs.HopsNumber("List2", "A2", "List 2"),
        hs.HopsNumber("List3", "A3", "List 3"),
        hs.HopsNumber("List4", "B1", "List 4"),
        hs.HopsNumber("List5", "B2", "List 5"),
        hs.HopsNumber("List6", "B3", "List 6")
        ],
    outputs=[hs.HopsNumber("ArrayList", "A", "Array of values")]
)
def array_Div(list1: list, list2: list, list3: list, list4: list, list5: list, list6: list):
    # Create a three-dimensional array
    listOut = []
    arr_A = np.array([list1, list2, list3])
    # Print the array
    #print(arr_A)
    arr_B = np.array([list4, list5, list6])
    # Print the array
    #print(arr_B)
    arr_C = arr_A / arr_B
    # Print the array
    print(arr_C)
    arr_C = arr_C.tolist()
    print(arr_C)
    for i in arr_C:
        listOut.append(i)
    return listOut

# np.min
# np.max
# np.average

@hops.component(
    "/array_minmaxavg",
    name="Array Average",
    nickname="Array Average",
    description="Find the average value of an array",
    inputs=[
        hs.HopsInteger("List1", "A1", "List 1", access= hs.HopsParamAccess.LIST),
        hs.HopsInteger("List2", "A2", "List 2", access=hs.HopsParamAccess.LIST),
        hs.HopsInteger("List3", "A3", "List 3", access=hs.HopsParamAccess.LIST)
        ],
    outputs=[
        hs.HopsInteger("min", "min", "Minimum value"),
        hs.HopsInteger("max", "max", "Maximum value"),
        hs.HopsNumber("average", "A", "Average value of the array")]   
)
def array_minmaxavg(list1: list, list2: list, list3: list):
    # Create a three-dimensional array
    a = np.array([list1, list2, list3])
    print(np.min(a))
    print(type(np.min(a)))
    print(np.max(a))
    print(type(np.max(a)))
    print(np.average(a))
    print(type(np.average(a)))
    return int(np.min(a)), int(np.max(a)), float(np.average(a))

# Data: yearly salary in ($1000) [2017, 2018, 2019]
@hops.component(
    "/top_income2",
    name="Max Income",
    nickname="Max Income",
    description="Find the maximum income",
    inputs=[
        hs.HopsInteger("Mike", "A1", "Mike", access= hs.HopsParamAccess.LIST),
        hs.HopsInteger("Beth", "A2", "Beth", access=hs.HopsParamAccess.LIST),
        hs.HopsInteger("Oscar", "A3", "Oscar", access=hs.HopsParamAccess.LIST),
        hs.HopsNumber("Mike_tax", "B1", "Mike tax", access=hs.HopsParamAccess.LIST),
        hs.HopsNumber("Beth_tax", "B2", "Beth tax", access=hs.HopsParamAccess.LIST),
        hs.HopsNumber("Oscar_tax", "B3", "Oscar tax", access=hs.HopsParamAccess.LIST)
        ],
    outputs=[hs.HopsNumber("max_income", "A", "Maximum income")]
)
def top_income2(mike: list, beth: list, oscar: list, mike_tax: list, beth_tax: list, oscar_tax: list):
    # Create a three-dimensional array
    salaries = np.array([mike, beth, oscar])
    taxation = np.array([mike_tax, beth_tax, oscar_tax])
    #One-liner
    print(salaries - salaries * taxation)
    max_income = np.max(salaries - salaries * taxation)
    print(max_income)
    print(type(max_income))
    return max_income

@hops.component(
    "/array_sum",
    name="Array Sum",
    nickname="Array Sum",
    description="Sum of all the values in an array",
    inputs=[
        hs.HopsInteger("List1", "A1", "List 1", access= hs.HopsParamAccess.LIST),
        hs.HopsInteger("List2", "A2", "List 2", access=hs.HopsParamAccess.LIST),
        hs.HopsInteger("List3", "A3", "List 3", access=hs.HopsParamAccess.LIST)
        ],
    outputs=[hs.HopsInteger("sum", "A", "Sum of all the values in an array")]
)
def array_sum(list1: list, list2: list, list3: list):
    # Create a three-dimensional array
    a = np.array([list1, list2, list3])
    print(np.sum(a))
    print(type(np.sum(a)))
    return int(np.sum(a))

    





if __name__ == "__main__":
    app.run(debug=True)