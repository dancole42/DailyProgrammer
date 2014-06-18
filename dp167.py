import webbrowser

def setTabSpace(spaces):
    """Sets the spacing for line indents."""
    tab = " " * spaces
    return tab

def linePrint(line_num, indent_block, text):
    """Returns a single line of code for output."""
    if line_numbers == True:
        intro = '<!--' + str(line_num) + '-->'
    else:
        intro = ''
    return intro + indent_block * tab + text + '\n'

def convertSpacetoIndent(line_text, line_indent_block=0):
    """Turns any indents equal to tab into integers to track indentation
    level."""
    tabchars = tab
    if tabchars in line_text:
        line_text = line_text.rstrip(tabchars)
        return line_text, line_indent_block + 1
    else:
        return line_text, line_indent_block

def lineGen(raw, line_num=1, indent_block=0):
    """Turns text into a series of lists (i.e. a page) that indicate row number
    and indentation level."""
    page = []
    line_text = ''
    line_indent_block = indent_block
    for char in raw:
        line_text += char        
        line_text, line_indent_block = convertSpacetoIndent(line_text, \
            line_indent_block)
        if '\n' in line_text:
            line_text = line_text.rstrip('\n')
            page.append([line_num, line_indent_block, line_text])
            line_indent_block = indent_block
            line_text = ''
            line_num += 1
    return page

def insertLine(page, newline, line_num='default', indent_block=0):
    """Add a line to a page. Defaults to end of page."""
    if line_num == 'default':
        line_num = len(page) + 1
    newline = lineGen(newline + '\n', line_num, indent_block)[0]
    page.insert(line_num - 1, newline)
    return refreshLineNumbers(page)

def removeLine(page, line_num='default'):
    """Remove a line from a page. Defaults to end of page."""
    if line_num == 'default':
        line_num = len(page)
    del page[line_num - 1]
    return refreshLineNumbers(page)

def replaceLine(page, newline, line_num='default', indent_block=0):
    """Replaces a line with a new line. Defaults to end of page."""
    page = removeLine(page, line_num)
    page = insertLine(page, newline, line_num, indent_block)
    return page

def refreshLineNumbers(page):
    """Updates line numbers after insertions/removals."""
    new_line_number = 1
    for line in page:
        line[0] = new_line_number
        new_line_number += 1
    return page

def titleLine():
    """Prompts user for and returns a title line."""
    title = raw_input("Enter your page title: ")
    title = "<title>" + title + "</title>"
    return title

def pLine():
    """Prompts user for and returns a paragraph line."""
    title = raw_input("Enter your paragraph: ")
    title = "<p>" + title + "</p>"
    return title

def textPrint(text):
    """Prints out a page."""
    pageout = ''
    for line in text:
        pageout += linePrint(line[0], line[1], line[2])
    return pageout

def htmlOut(page, url):
    """Writes a page to a given file."""
    f = open(url, 'w')
    f.write(textPrint(page))
    f.close()

line_numbers = False # For debugging. Adds commented line numbers to output.
tab = setTabSpace(4) # Set desired indentation size.

reddit_text = """<!DOCTYPE html>
<html>
    <head>
        <title></title>
    </head>

    <body>
        <p>This is my paragraph entry</p>
    </body>
</html>
"""
page = lineGen(reddit_text) # Parse the input text.
page = replaceLine(page, titleLine(), 4, 2) # Replace boilerplate title.
page = replaceLine(page, pLine(), 8, 2) # Replace template paragraph.
url = 'index.html' # Name of output file.
htmlOut(page, url) # Write page to HTML.

webbrowser.open_new(url) # Opens URL in browser.