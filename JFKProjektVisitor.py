# Generated from JFKProjekt.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JFKProjektParser import JFKProjektParser
else:
    from JFKProjektParser import JFKProjektParser

# This class defines a complete generic visitor for a parse tree produced by JFKProjektParser.

class JFKProjektVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JFKProjektParser#prog.
    def visitProg(self, ctx:JFKProjektParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#print.
    def visitPrint(self, ctx:JFKProjektParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#assign.
    def visitAssign(self, ctx:JFKProjektParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#read.
    def visitRead(self, ctx:JFKProjektParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#single0.
    def visitSingle0(self, ctx:JFKProjektParser.Single0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#add.
    def visitAdd(self, ctx:JFKProjektParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#minus.
    def visitMinus(self, ctx:JFKProjektParser.MinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#single1.
    def visitSingle1(self, ctx:JFKProjektParser.Single1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#multiply.
    def visitMultiply(self, ctx:JFKProjektParser.MultiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#divide.
    def visitDivide(self, ctx:JFKProjektParser.DivideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#value2.
    def visitValue2(self, ctx:JFKProjektParser.Value2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#toint.
    def visitToint(self, ctx:JFKProjektParser.TointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#toreal.
    def visitToreal(self, ctx:JFKProjektParser.TorealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#par.
    def visitPar(self, ctx:JFKProjektParser.ParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#ID.
    def visitID(self, ctx:JFKProjektParser.IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#int.
    def visitInt(self, ctx:JFKProjektParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#real.
    def visitReal(self, ctx:JFKProjektParser.RealContext):
        return self.visitChildren(ctx)



del JFKProjektParser