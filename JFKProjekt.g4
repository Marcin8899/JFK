grammar JFKProjekt;

prog: ( stat? NEWLINE )* ;

stat: PRINT value #print
	| ID '=' expr0 #assign
	| READ ID   #read
	| ID '[' type ',' INT ']' #tab
	| ID '[' INT ']' '=' expr0 #tabassign
;

expr0:  expr1 #single0
    | expr1 ADD expr0 #add
    | expr1 MINUS expr0 #minus
;

expr1: expr2 #single1
    | expr2 MULTIPLY expr1 #multiply
    | expr2 DIVIDE expr1 #divide
;

expr2:  value #value2
    | TOINT expr2 #toint
    | TOREAL expr2 #toreal
    | '(' expr0 ')' #par
;


value: ID '[' INT ']' #tabvalue
	| INT #int
	| REAL #real
	| ID #ID
	| CHAR #char
   ;

 type: 'i32' #inttype
	| 'double' #realtype
	| 'char' #chartype
	;

PRINT:	'print' ;
READ:	'read' ;

ID:   ('a'..'z'|'A'..'Z')+ ;
CHAR :  '"' ( ~('\\'|'"') ) '"';

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