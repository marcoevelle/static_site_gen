from textnode import *

def main():
    test = TextNode("This is some anchor text", TextType.LINK, "This is some anchor text")
    print(test)


if __name__ == "__main__":
    main()