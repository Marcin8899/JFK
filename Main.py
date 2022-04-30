import sys
from antlr4 import *
from JFKProjektLexer import JFKProjektLexer
from JFKProjektParser import JFKProjektParser
from LLVMActions import LLVMActions

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = JFKProjektLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JFKProjektParser(stream)
    tree = parser.prog()

    walker = ParseTreeWalker()
    walker.walk(LLVMActions(), tree)


if __name__ == '__main__':
    main(sys.argv)
