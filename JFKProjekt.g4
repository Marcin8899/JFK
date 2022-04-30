grammar JFKProjekt;

prog: ( stat? NEWLINE )* ;

stat:	PRINT value	#print
	| ID '=' expr0 #assign
	| READ value   #read
;

expr0:  expr1 #single0
    | expr1 ADD expr1 #add
    | expr1 MINUS expr1 #minus
;

expr1:  expr2 #single1
    | expr2 MULTIPLY expr2 #multiply
    | expr2 DIVIDE expr2 #divide
;

expr2:  value #value2
    | TOINT expr2 #toint
    | TOREAL expr2 #toreal
    | '(' expr0 ')' #par
;

value: ID #ID
	| INT #int
	| REAL #real
   ;	

PRINT:	'print' ;
READ:	'read' ;

ID:   ('a'..'z'|'A'..'Z')+ ;
STRING :  '"' ( ~('\\'|'"') )* '"';

REAL: '0'..'9'+'.''0'..'9'+ ;
INT: '0'..'9'+ ;

ADD: '+' ;
MINUS: '-' ;
MULTIPLY: '*' ;
DIVIDE: '/' ;

TOINT: '(int)' ;
TOREAL: '(real)' ;

NEWLINE:	'\r'? '\n' ;
WS : [ \t\r\n]+ -> skip ;

// doskey antlr4=java org.antlr.v4.Tool $*
// SET CLASSPATH=.;C:\Javalib\antlr-4.10.1-complete.jar;%CLASSPATH%
// antlr4 -Dlanguage=Python3 JFKProjekt.g4 -visitor
// java -cp antlr-4.10.1-complete.jar:. org.antlr.v4.gui.TestRig Hello r
// java -cp ".;C:\Javalib\antlr-4.10.1-complete.jar" org.antlr.v4.gui.TestRig Hello r