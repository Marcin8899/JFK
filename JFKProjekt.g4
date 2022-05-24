grammar JFKProjekt;

prog: ( stat? NEWLINE )* ;

stat: stat2
    | function_declaration
;

stat2: PRINT value #print
	| ID '=' expr0 #assign
	| READ ID   #read
	| ID '[' type ',' INT ']' #tab
	| ID '[' INT ']' '=' expr0 #tabassign
    | IF condition THEN NEWLINE blockif END #if_declr
    | WHILE condition THEN NEWLINE blockwhile END #while_declr
    | ID '(' ')' #fcall
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
	| STRING #string
   ;

type: 'i32' #inttype
	| 'double' #realtype
	| 'char' #chartype
	;

condition:   value EQUAL value #equal
           | value GREATER value #greater
           | value GREATER_EQUAL value #greater_equal
           | value LESS value #less
           | value LESS_EQUAL value #less_equal
           | value DIFFERENT value #different
           ;

function_declaration: FUNCTION ID '(' ')' NEWLINE block END;

blockif: ( stat2? NEWLINE )*;
blockwhile: ( stat2? NEWLINE )*;
block: ( stat2? NEWLINE )*;

EQUAL: '==';
GREATER: '>';
GREATER_EQUAL: '>=';
LESS: '<';
LESS_EQUAL: '<=';
DIFFERENT: '!=';

PRINT:	'print' ;
READ:	'read' ;

IF: 'if';
THEN: 'then';
END: 'end';
WHILE: 'while';
FUNCTION: 'function';

ID:   ('a'..'z'|'A'..'Z')+ ;

STRING :  '"' ( ~('\\'|'"') )* '"';
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