# Generated from JFKProjekt.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,3,0,16,8,0,1,0,5,0,19,8,0,10,0,12,0,22,9,0,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,44,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,55,8,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,66,8,3,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,3,4,77,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,86,8,5,1,
        6,1,6,3,6,90,8,6,1,6,0,0,7,0,2,4,6,8,10,12,0,0,101,0,20,1,0,0,0,
        2,43,1,0,0,0,4,54,1,0,0,0,6,65,1,0,0,0,8,76,1,0,0,0,10,85,1,0,0,
        0,12,89,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,15,16,1,0,0,0,16,17,
        1,0,0,0,17,19,5,21,0,0,18,15,1,0,0,0,19,22,1,0,0,0,20,18,1,0,0,0,
        20,21,1,0,0,0,21,1,1,0,0,0,22,20,1,0,0,0,23,24,5,9,0,0,24,44,3,10,
        5,0,25,26,5,11,0,0,26,27,5,1,0,0,27,44,3,4,2,0,28,29,5,10,0,0,29,
        44,5,11,0,0,30,31,5,11,0,0,31,32,5,2,0,0,32,33,3,12,6,0,33,34,5,
        3,0,0,34,35,5,14,0,0,35,36,5,4,0,0,36,44,1,0,0,0,37,38,5,11,0,0,
        38,39,5,2,0,0,39,40,5,14,0,0,40,41,5,4,0,0,41,42,5,1,0,0,42,44,3,
        4,2,0,43,23,1,0,0,0,43,25,1,0,0,0,43,28,1,0,0,0,43,30,1,0,0,0,43,
        37,1,0,0,0,44,3,1,0,0,0,45,55,3,6,3,0,46,47,3,6,3,0,47,48,5,15,0,
        0,48,49,3,4,2,0,49,55,1,0,0,0,50,51,3,6,3,0,51,52,5,16,0,0,52,53,
        3,4,2,0,53,55,1,0,0,0,54,45,1,0,0,0,54,46,1,0,0,0,54,50,1,0,0,0,
        55,5,1,0,0,0,56,66,3,8,4,0,57,58,3,8,4,0,58,59,5,17,0,0,59,60,3,
        6,3,0,60,66,1,0,0,0,61,62,3,8,4,0,62,63,5,18,0,0,63,64,3,6,3,0,64,
        66,1,0,0,0,65,56,1,0,0,0,65,57,1,0,0,0,65,61,1,0,0,0,66,7,1,0,0,
        0,67,77,3,10,5,0,68,69,5,19,0,0,69,77,3,10,5,0,70,71,5,20,0,0,71,
        77,3,10,5,0,72,73,5,5,0,0,73,74,3,4,2,0,74,75,5,6,0,0,75,77,1,0,
        0,0,76,67,1,0,0,0,76,68,1,0,0,0,76,70,1,0,0,0,76,72,1,0,0,0,77,9,
        1,0,0,0,78,79,5,11,0,0,79,80,5,2,0,0,80,81,5,14,0,0,81,86,5,4,0,
        0,82,86,5,14,0,0,83,86,5,13,0,0,84,86,5,11,0,0,85,78,1,0,0,0,85,
        82,1,0,0,0,85,83,1,0,0,0,85,84,1,0,0,0,86,11,1,0,0,0,87,90,5,7,0,
        0,88,90,5,8,0,0,89,87,1,0,0,0,89,88,1,0,0,0,90,13,1,0,0,0,8,15,20,
        43,54,65,76,85,89
    ]

class JFKProjektParser ( Parser ):

    grammarFileName = "JFKProjekt.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'['", "','", "']'", "'('", "')'", 
                     "'i32'", "'double'", "'print'", "'read'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'(int)'", "'(real)'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "PRINT", "READ", "ID", "STRING", "REAL", 
                      "INT", "ADD", "MINUS", "MULTIPLY", "DIVIDE", "TOINT", 
                      "TOREAL", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr0 = 2
    RULE_expr1 = 3
    RULE_expr2 = 4
    RULE_value = 5
    RULE_type = 6

    ruleNames =  [ "prog", "stat", "expr0", "expr1", "expr2", "value", "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    PRINT=9
    READ=10
    ID=11
    STRING=12
    REAL=13
    INT=14
    ADD=15
    MINUS=16
    MULTIPLY=17
    DIVIDE=18
    TOINT=19
    TOREAL=20
    NEWLINE=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(JFKProjektParser.NEWLINE)
            else:
                return self.getToken(JFKProjektParser.NEWLINE, i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JFKProjektParser.StatContext)
            else:
                return self.getTypedRuleContext(JFKProjektParser.StatContext,i)


        def getRuleIndex(self):
            return JFKProjektParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = JFKProjektParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JFKProjektParser.PRINT) | (1 << JFKProjektParser.READ) | (1 << JFKProjektParser.ID) | (1 << JFKProjektParser.NEWLINE))) != 0):
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JFKProjektParser.PRINT) | (1 << JFKProjektParser.READ) | (1 << JFKProjektParser.ID))) != 0):
                    self.state = 14
                    self.stat()


                self.state = 17
                self.match(JFKProjektParser.NEWLINE)
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JFKProjektParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(JFKProjektParser.PRINT, 0)
        def value(self):
            return self.getTypedRuleContext(JFKProjektParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class ReadContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(JFKProjektParser.READ, 0)
        def ID(self):
            return self.getToken(JFKProjektParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)


    class TabassignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(JFKProjektParser.ID, 0)
        def INT(self):
            return self.getToken(JFKProjektParser.INT, 0)
        def expr0(self):
            return self.getTypedRuleContext(JFKProjektParser.Expr0Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTabassign" ):
                listener.enterTabassign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTabassign" ):
                listener.exitTabassign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTabassign" ):
                return visitor.visitTabassign(self)
            else:
                return visitor.visitChildren(self)


    class TabContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(JFKProjektParser.ID, 0)
        def type_(self):
            return self.getTypedRuleContext(JFKProjektParser.TypeContext,0)

        def INT(self):
            return self.getToken(JFKProjektParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTab" ):
                listener.enterTab(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTab" ):
                listener.exitTab(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTab" ):
                return visitor.visitTab(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(JFKProjektParser.ID, 0)
        def expr0(self):
            return self.getTypedRuleContext(JFKProjektParser.Expr0Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = JFKProjektParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = JFKProjektParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(JFKProjektParser.PRINT)
                self.state = 24
                self.value()
                pass

            elif la_ == 2:
                localctx = JFKProjektParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.match(JFKProjektParser.ID)
                self.state = 26
                self.match(JFKProjektParser.T__0)
                self.state = 27
                self.expr0()
                pass

            elif la_ == 3:
                localctx = JFKProjektParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.match(JFKProjektParser.READ)
                self.state = 29
                self.match(JFKProjektParser.ID)
                pass

            elif la_ == 4:
                localctx = JFKProjektParser.TabContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.match(JFKProjektParser.ID)
                self.state = 31
                self.match(JFKProjektParser.T__1)
                self.state = 32
                self.type_()
                self.state = 33
                self.match(JFKProjektParser.T__2)
                self.state = 34
                self.match(JFKProjektParser.INT)
                self.state = 35
                self.match(JFKProjektParser.T__3)
                pass

            elif la_ == 5:
                localctx = JFKProjektParser.TabassignContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 37
                self.match(JFKProjektParser.ID)
                self.state = 38
                self.match(JFKProjektParser.T__1)
                self.state = 39
                self.match(JFKProjektParser.INT)
                self.state = 40
                self.match(JFKProjektParser.T__3)
                self.state = 41
                self.match(JFKProjektParser.T__0)
                self.state = 42
                self.expr0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JFKProjektParser.RULE_expr0

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Single0Context(Expr0Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.Expr0Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr1(self):
            return self.getTypedRuleContext(JFKProjektParser.Expr1Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle0" ):
                listener.enterSingle0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle0" ):
                listener.exitSingle0(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle0" ):
                return visitor.visitSingle0(self)
            else:
                return visitor.visitChildren(self)


    class AddContext(Expr0Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.Expr0Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr1(self):
            return self.getTypedRuleContext(JFKProjektParser.Expr1Context,0)

        def ADD(self):
            return self.getToken(JFKProjektParser.ADD, 0)
        def expr0(self):
            return self.getTypedRuleContext(JFKProjektParser.Expr0Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class MinusContext(Expr0Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.Expr0Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr1(self):
            return self.getTypedRuleContext(JFKProjektParser.Expr1Context,0)

        def MINUS(self):
            return self.getToken(JFKProjektParser.MINUS, 0)
        def expr0(self):
            return self.getTypedRuleContext(JFKProjektParser.Expr0Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinus" ):
                listener.enterMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinus" ):
                listener.exitMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinus" ):
                return visitor.visitMinus(self)
            else:
                return visitor.visitChildren(self)



    def expr0(self):

        localctx = JFKProjektParser.Expr0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr0)
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = JFKProjektParser.Single0Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.expr1()
                pass

            elif la_ == 2:
                localctx = JFKProjektParser.AddContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.expr1()
                self.state = 47
                self.match(JFKProjektParser.ADD)
                self.state = 48
                self.expr0()
                pass

            elif la_ == 3:
                localctx = JFKProjektParser.MinusContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.expr1()
                self.state = 51
                self.match(JFKProjektParser.MINUS)
                self.state = 52
                self.expr0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JFKProjektParser.RULE_expr1

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Single1Context(Expr1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.Expr1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr2(self):
            return self.getTypedRuleContext(JFKProjektParser.Expr2Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle1" ):
                listener.enterSingle1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle1" ):
                listener.exitSingle1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle1" ):
                return visitor.visitSingle1(self)
            else:
                return visitor.visitChildren(self)


    class DivideContext(Expr1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.Expr1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr2(self):
            return self.getTypedRuleContext(JFKProjektParser.Expr2Context,0)

        def DIVIDE(self):
            return self.getToken(JFKProjektParser.DIVIDE, 0)
        def expr1(self):
            return self.getTypedRuleContext(JFKProjektParser.Expr1Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivide" ):
                listener.enterDivide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivide" ):
                listener.exitDivide(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivide" ):
                return visitor.visitDivide(self)
            else:
                return visitor.visitChildren(self)


    class MultiplyContext(Expr1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.Expr1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr2(self):
            return self.getTypedRuleContext(JFKProjektParser.Expr2Context,0)

        def MULTIPLY(self):
            return self.getToken(JFKProjektParser.MULTIPLY, 0)
        def expr1(self):
            return self.getTypedRuleContext(JFKProjektParser.Expr1Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiply" ):
                listener.enterMultiply(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiply" ):
                listener.exitMultiply(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiply" ):
                return visitor.visitMultiply(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self):

        localctx = JFKProjektParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr1)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = JFKProjektParser.Single1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.expr2()
                pass

            elif la_ == 2:
                localctx = JFKProjektParser.MultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.expr2()
                self.state = 58
                self.match(JFKProjektParser.MULTIPLY)
                self.state = 59
                self.expr1()
                pass

            elif la_ == 3:
                localctx = JFKProjektParser.DivideContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.expr2()
                self.state = 62
                self.match(JFKProjektParser.DIVIDE)
                self.state = 63
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JFKProjektParser.RULE_expr2

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParContext(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr0(self):
            return self.getTypedRuleContext(JFKProjektParser.Expr0Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPar" ):
                listener.enterPar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPar" ):
                listener.exitPar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPar" ):
                return visitor.visitPar(self)
            else:
                return visitor.visitChildren(self)


    class TointContext(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOINT(self):
            return self.getToken(JFKProjektParser.TOINT, 0)
        def value(self):
            return self.getTypedRuleContext(JFKProjektParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToint" ):
                listener.enterToint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToint" ):
                listener.exitToint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToint" ):
                return visitor.visitToint(self)
            else:
                return visitor.visitChildren(self)


    class Value2Context(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(JFKProjektParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue2" ):
                listener.enterValue2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue2" ):
                listener.exitValue2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue2" ):
                return visitor.visitValue2(self)
            else:
                return visitor.visitChildren(self)


    class TorealContext(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOREAL(self):
            return self.getToken(JFKProjektParser.TOREAL, 0)
        def value(self):
            return self.getTypedRuleContext(JFKProjektParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToreal" ):
                listener.enterToreal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToreal" ):
                listener.exitToreal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToreal" ):
                return visitor.visitToreal(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self):

        localctx = JFKProjektParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr2)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JFKProjektParser.ID, JFKProjektParser.REAL, JFKProjektParser.INT]:
                localctx = JFKProjektParser.Value2Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.value()
                pass
            elif token in [JFKProjektParser.TOINT]:
                localctx = JFKProjektParser.TointContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.match(JFKProjektParser.TOINT)
                self.state = 69
                self.value()
                pass
            elif token in [JFKProjektParser.TOREAL]:
                localctx = JFKProjektParser.TorealContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.match(JFKProjektParser.TOREAL)
                self.state = 71
                self.value()
                pass
            elif token in [JFKProjektParser.T__4]:
                localctx = JFKProjektParser.ParContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.match(JFKProjektParser.T__4)
                self.state = 73
                self.expr0()
                self.state = 74
                self.match(JFKProjektParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JFKProjektParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TabvalueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(JFKProjektParser.ID, 0)
        def INT(self):
            return self.getToken(JFKProjektParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTabvalue" ):
                listener.enterTabvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTabvalue" ):
                listener.exitTabvalue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTabvalue" ):
                return visitor.visitTabvalue(self)
            else:
                return visitor.visitChildren(self)


    class RealContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REAL(self):
            return self.getToken(JFKProjektParser.REAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReal" ):
                listener.enterReal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReal" ):
                listener.exitReal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReal" ):
                return visitor.visitReal(self)
            else:
                return visitor.visitChildren(self)


    class IDContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(JFKProjektParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterID" ):
                listener.enterID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitID" ):
                listener.exitID(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitID" ):
                return visitor.visitID(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(JFKProjektParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = JFKProjektParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_value)
        try:
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = JFKProjektParser.TabvalueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(JFKProjektParser.ID)
                self.state = 79
                self.match(JFKProjektParser.T__1)
                self.state = 80
                self.match(JFKProjektParser.INT)
                self.state = 81
                self.match(JFKProjektParser.T__3)
                pass

            elif la_ == 2:
                localctx = JFKProjektParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.match(JFKProjektParser.INT)
                pass

            elif la_ == 3:
                localctx = JFKProjektParser.RealContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.match(JFKProjektParser.REAL)
                pass

            elif la_ == 4:
                localctx = JFKProjektParser.IDContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.match(JFKProjektParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JFKProjektParser.RULE_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RealtypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRealtype" ):
                listener.enterRealtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRealtype" ):
                listener.exitRealtype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRealtype" ):
                return visitor.visitRealtype(self)
            else:
                return visitor.visitChildren(self)


    class InttypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKProjektParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInttype" ):
                listener.enterInttype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInttype" ):
                listener.exitInttype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInttype" ):
                return visitor.visitInttype(self)
            else:
                return visitor.visitChildren(self)



    def type_(self):

        localctx = JFKProjektParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_type)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JFKProjektParser.T__6]:
                localctx = JFKProjektParser.InttypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.match(JFKProjektParser.T__6)
                pass
            elif token in [JFKProjektParser.T__7]:
                localctx = JFKProjektParser.RealtypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.match(JFKProjektParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





