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
        4,1,17,69,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,3,
        0,14,8,0,1,0,5,0,17,8,0,10,0,12,0,20,9,0,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,29,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,40,8,2,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,51,8,3,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,3,4,62,8,4,1,5,1,5,1,5,3,5,67,8,5,1,5,0,0,6,0,2,
        4,6,8,10,0,0,75,0,18,1,0,0,0,2,28,1,0,0,0,4,39,1,0,0,0,6,50,1,0,
        0,0,8,61,1,0,0,0,10,66,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,13,14,
        1,0,0,0,14,15,1,0,0,0,15,17,5,16,0,0,16,13,1,0,0,0,17,20,1,0,0,0,
        18,16,1,0,0,0,18,19,1,0,0,0,19,1,1,0,0,0,20,18,1,0,0,0,21,22,5,4,
        0,0,22,29,3,10,5,0,23,24,5,6,0,0,24,25,5,1,0,0,25,29,3,4,2,0,26,
        27,5,5,0,0,27,29,5,6,0,0,28,21,1,0,0,0,28,23,1,0,0,0,28,26,1,0,0,
        0,29,3,1,0,0,0,30,40,3,6,3,0,31,32,3,6,3,0,32,33,5,10,0,0,33,34,
        3,4,2,0,34,40,1,0,0,0,35,36,3,6,3,0,36,37,5,11,0,0,37,38,3,4,2,0,
        38,40,1,0,0,0,39,30,1,0,0,0,39,31,1,0,0,0,39,35,1,0,0,0,40,5,1,0,
        0,0,41,51,3,8,4,0,42,43,3,8,4,0,43,44,5,12,0,0,44,45,3,6,3,0,45,
        51,1,0,0,0,46,47,3,8,4,0,47,48,5,13,0,0,48,49,3,6,3,0,49,51,1,0,
        0,0,50,41,1,0,0,0,50,42,1,0,0,0,50,46,1,0,0,0,51,7,1,0,0,0,52,62,
        3,10,5,0,53,54,5,14,0,0,54,62,3,8,4,0,55,56,5,15,0,0,56,62,3,8,4,
        0,57,58,5,2,0,0,58,59,3,4,2,0,59,60,5,3,0,0,60,62,1,0,0,0,61,52,
        1,0,0,0,61,53,1,0,0,0,61,55,1,0,0,0,61,57,1,0,0,0,62,9,1,0,0,0,63,
        67,5,6,0,0,64,67,5,9,0,0,65,67,5,8,0,0,66,63,1,0,0,0,66,64,1,0,0,
        0,66,65,1,0,0,0,67,11,1,0,0,0,7,13,18,28,39,50,61,66
    ]

class JFKProjektParser ( Parser ):

    grammarFileName = "JFKProjekt.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'print'", "'read'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'(int)'", "'(real)'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "PRINT", "READ", "ID", "STRING", "REAL", "INT", "ADD", 
                      "MINUS", "MULTIPLY", "DIVIDE", "TOINT", "TOREAL", 
                      "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr0 = 2
    RULE_expr1 = 3
    RULE_expr2 = 4
    RULE_value = 5

    ruleNames =  [ "prog", "stat", "expr0", "expr1", "expr2", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    PRINT=4
    READ=5
    ID=6
    STRING=7
    REAL=8
    INT=9
    ADD=10
    MINUS=11
    MULTIPLY=12
    DIVIDE=13
    TOINT=14
    TOREAL=15
    NEWLINE=16
    WS=17

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
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JFKProjektParser.PRINT) | (1 << JFKProjektParser.READ) | (1 << JFKProjektParser.ID) | (1 << JFKProjektParser.NEWLINE))) != 0):
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JFKProjektParser.PRINT) | (1 << JFKProjektParser.READ) | (1 << JFKProjektParser.ID))) != 0):
                    self.state = 12
                    self.stat()


                self.state = 15
                self.match(JFKProjektParser.NEWLINE)
                self.state = 20
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
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JFKProjektParser.PRINT]:
                localctx = JFKProjektParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(JFKProjektParser.PRINT)
                self.state = 22
                self.value()
                pass
            elif token in [JFKProjektParser.ID]:
                localctx = JFKProjektParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(JFKProjektParser.ID)
                self.state = 24
                self.match(JFKProjektParser.T__0)
                self.state = 25
                self.expr0()
                pass
            elif token in [JFKProjektParser.READ]:
                localctx = JFKProjektParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.match(JFKProjektParser.READ)
                self.state = 27
                self.match(JFKProjektParser.ID)
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
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = JFKProjektParser.Single0Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.expr1()
                pass

            elif la_ == 2:
                localctx = JFKProjektParser.AddContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.expr1()
                self.state = 32
                self.match(JFKProjektParser.ADD)
                self.state = 33
                self.expr0()
                pass

            elif la_ == 3:
                localctx = JFKProjektParser.MinusContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.expr1()
                self.state = 36
                self.match(JFKProjektParser.MINUS)
                self.state = 37
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
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = JFKProjektParser.Single1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.expr2()
                pass

            elif la_ == 2:
                localctx = JFKProjektParser.MultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.expr2()
                self.state = 43
                self.match(JFKProjektParser.MULTIPLY)
                self.state = 44
                self.expr1()
                pass

            elif la_ == 3:
                localctx = JFKProjektParser.DivideContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.expr2()
                self.state = 47
                self.match(JFKProjektParser.DIVIDE)
                self.state = 48
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
        def expr2(self):
            return self.getTypedRuleContext(JFKProjektParser.Expr2Context,0)


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
        def expr2(self):
            return self.getTypedRuleContext(JFKProjektParser.Expr2Context,0)


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
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JFKProjektParser.ID, JFKProjektParser.REAL, JFKProjektParser.INT]:
                localctx = JFKProjektParser.Value2Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.value()
                pass
            elif token in [JFKProjektParser.TOINT]:
                localctx = JFKProjektParser.TointContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(JFKProjektParser.TOINT)
                self.state = 54
                self.expr2()
                pass
            elif token in [JFKProjektParser.TOREAL]:
                localctx = JFKProjektParser.TorealContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.match(JFKProjektParser.TOREAL)
                self.state = 56
                self.expr2()
                pass
            elif token in [JFKProjektParser.T__1]:
                localctx = JFKProjektParser.ParContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.match(JFKProjektParser.T__1)
                self.state = 58
                self.expr0()
                self.state = 59
                self.match(JFKProjektParser.T__2)
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
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JFKProjektParser.ID]:
                localctx = JFKProjektParser.IDContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(JFKProjektParser.ID)
                pass
            elif token in [JFKProjektParser.INT]:
                localctx = JFKProjektParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(JFKProjektParser.INT)
                pass
            elif token in [JFKProjektParser.REAL]:
                localctx = JFKProjektParser.RealContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.match(JFKProjektParser.REAL)
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





