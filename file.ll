declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strs = constant [3 x i8] c"%d\00"
@.str = constant [3 x i8] c"%s\00"
@.char = constant [3 x i8] c"%c\00"
@A = global i32 6
@B = global i32 2
define i32 @main() nounwind{
%x = alloca i32
store i32 3, i32* %x
%y = alloca i32
store i32 5, i32* %y
br label %loop1

loop1:
%1 = load i32, i32* %y
%2 = load i32, i32* %x
%3 = icmp sgt i32 %1, %2
br i1 %3, label %if1, label %if2

if1:
%4 = load i32, i32* %y
%5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %4)
%6 = load i32, i32* %x
%7 = add i32 %6, 1
store i32 %7, i32* %x
br label %loop1

if2:
%8 = load i32, i32* %x
%9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %8)
%10 = call i32 @test()
%tescik = alloca i32
store i32 %10, i32* %tescik
%11 = load i32, i32* %tescik
%12 = load i32, i32* @A
%13 = add i32 %11, %12
store i32 %13, i32* %tescik
%14 = load i32, i32* %tescik
%15 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %14)
%16 = load i32, i32* %x
%17 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %16)
ret i32 0 }

define i32 @test() nounwind {
%1 = load i32, i32* @B
%2 = add i32 10, %1
%x = alloca i32
store i32 %2, i32* %x
%3 = load i32, i32* %x
%return = alloca i32
store i32 %3, i32* %return
ret i32 %3
}


