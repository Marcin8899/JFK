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


    # Visit a parse tree produced by JFKProjektParser#stat.
    def visitStat(self, ctx:JFKProjektParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#print.
    def visitPrint(self, ctx:JFKProjektParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#assign.
    def visitAssign(self, ctx:JFKProjektParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#globalassign.
    def visitGlobalassign(self, ctx:JFKProjektParser.GlobalassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#read.
    def visitRead(self, ctx:JFKProjektParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#tab.
    def visitTab(self, ctx:JFKProjektParser.TabContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#tabassign.
    def visitTabassign(self, ctx:JFKProjektParser.TabassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#if_declr.
    def visitIf_declr(self, ctx:JFKProjektParser.If_declrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#while_declr.
    def visitWhile_declr(self, ctx:JFKProjektParser.While_declrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#fcall1.
    def visitFcall1(self, ctx:JFKProjektParser.Fcall1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#fcall2.
    def visitFcall2(self, ctx:JFKProjektParser.Fcall2Context):
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


    # Visit a parse tree produced by JFKProjektParser#tabvalue.
    def visitTabvalue(self, ctx:JFKProjektParser.TabvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#int.
    def visitInt(self, ctx:JFKProjektParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#real.
    def visitReal(self, ctx:JFKProjektParser.RealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#ID.
    def visitID(self, ctx:JFKProjektParser.IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#char.
    def visitChar(self, ctx:JFKProjektParser.CharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#string.
    def visitString(self, ctx:JFKProjektParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#inttype.
    def visitInttype(self, ctx:JFKProjektParser.InttypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#realtype.
    def visitRealtype(self, ctx:JFKProjektParser.RealtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#chartype.
    def visitChartype(self, ctx:JFKProjektParser.ChartypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#equal.
    def visitEqual(self, ctx:JFKProjektParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#greater.
    def visitGreater(self, ctx:JFKProjektParser.GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#greater_equal.
    def visitGreater_equal(self, ctx:JFKProjektParser.Greater_equalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#less.
    def visitLess(self, ctx:JFKProjektParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#less_equal.
    def visitLess_equal(self, ctx:JFKProjektParser.Less_equalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#different.
    def visitDifferent(self, ctx:JFKProjektParser.DifferentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#function_declaration.
    def visitFunction_declaration(self, ctx:JFKProjektParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#fcall.
    def visitFcall(self, ctx:JFKProjektParser.FcallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#blockif.
    def visitBlockif(self, ctx:JFKProjektParser.BlockifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#blockwhile.
    def visitBlockwhile(self, ctx:JFKProjektParser.BlockwhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JFKProjektParser#block.
    def visitBlock(self, ctx:JFKProjektParser.BlockContext):
        return self.visitChildren(ctx)



del JFKProjektParser