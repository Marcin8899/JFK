declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strs = constant [3 x i8] c"%d\00"
@.str = constant [3 x i8] c"%s\00"
@.char = constant [3 x i8] c"%c\00"
define i32 @main() nounwind{
%y = alloca [5 x i8]
%1 = getelementptr inbounds [5 x i8], [5 x i8]* %y, i64 0, i64 3
store i8 116, i8* %1
%2 = getelementptr inbounds [5 x i8], [5 x i8]* %y, i64 0, i64 2
store i8 115, i8* %2
%3 = getelementptr inbounds [5 x i8], [5 x i8]* %y, i64 0, i64 1
store i8 101, i8* %3
%4 = getelementptr inbounds [5 x i8], [5 x i8]* %y, i64 0, i64 0
store i8 116, i8* %4
%5 = getelementptr inbounds [5 x i8], [5 x i8]* %y, i64 0, i64 2
store i8 83, i8* %5
%6 = getelementptr inbounds [5 x i8], [5 x i8]* %y, i64 0, i64 0
%7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i8* %6)
ret i32 0 }

