#
# parsing and processing HTML
#

from html.parser import HTMLParser

paragraphs = 0

# MyHTMLParser is a subclass of HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encounter a comment:", data)
        pos = self.getpos()
        print("At line:", pos[0], " position", pos[1])
        
    def handle_starttag(self, tag, attrs):
        print("Encounter a start tag:", tag)
        pos = self.getpos()
        print("At line:", pos[0], " position", pos[1])

        # paragraphs counter
        global paragraphs
        if tag.lower() == "p":
            paragraphs += 1

        # print attributes
        if len(attrs) > 0:
            print("Attributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1]) # lang = en
        
    def handle_data(self, data):
        # doing nothing with white space
        if data.isspace():
            return
        # print out text data
        print("Encounter text data:", data)
        pos = self.getpos()
        print("At line:", pos[0], " position", pos[1])

# Main entry point function
def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()
    
    f = open("samplehtml.html", "r")
    if f.mode == "r":
        contents = f.read() # read the entire file
        parser.feed(contents)
        
    print("Paragraph tags:", paragraphs) # Paragraph tags: 2

# Execute the main function
if __name__ == "__main__":
    main()