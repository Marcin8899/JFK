declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strs = constant [3 x i8] c"%d\00"
@.str = constant [3 x i8] c"%s\00"
@.char = constant [3 x i8] c"%c\00"
define i32 @main() nounwind{
%a = alloca i32
store i32 5, i32* %a
%b = alloca i32
store i32 0, i32* %b
br label %loop1

loop1:
%1 = load i32, i32* %a
%2 = load i32, i32* %b
%3 = icmp sgt i32 %1, %2
br i1 %3, label %if1, label %if2

if1:
%4 = load i32, i32* %a
%5 = sub i32 %4, 1
store i32 %5, i32* %a
%6 = load i32, i32* %a
%7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %6)
br label %loop1

if2:
%8 = load i32, i32* %a
%9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %8)
ret i32 0 }

