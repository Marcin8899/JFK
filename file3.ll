declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strs = constant [3 x i8] c"%d\00"
@.str = constant [3 x i8] c"%s\00"
@.char = constant [3 x i8] c"%c\00"
define i32 @main() nounwind{
%y = alloca [5 x i32]
%1 = getelementptr inbounds [5 x i32], [5 x i32]* %y, i64 0, i64 0
store i32 1, i32* %1
%2 = getelementptr inbounds [5 x i32], [5 x i32]* %y, i64 0, i64 1
store i32 2, i32* %2
%3 = getelementptr inbounds [5 x i32], [5 x i32]* %y, i64 0, i64 0
%4 = load i32, i32* %3
%5 = mul i32 %4, 5
%6 = getelementptr inbounds [5 x i32], [5 x i32]* %y, i64 0, i64 2
store i32 %5, i32* %6
%7 = getelementptr inbounds [5 x i32], [5 x i32]* %y, i64 0, i64 2
%8 = load i32, i32* %7
%9 = getelementptr inbounds [5 x i32], [5 x i32]* %y, i64 0, i64 1
%10 = load i32, i32* %9
%11 = add i32 %8, %10
%12 = getelementptr inbounds [5 x i32], [5 x i32]* %y, i64 0, i64 3
store i32 %11, i32* %12
%13 = getelementptr inbounds [5 x i32], [5 x i32]* %y, i64 0, i64 3
%14 = load i32, i32* %13
%15 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %14)
ret i32 0 }

