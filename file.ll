declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strs = constant [3 x i8] c"%d\00"
define i32 @main() nounwind{
%x = alloca i32
store i32 4, i32* %x
%1 = load i32, i32* %x
%2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %1)
%a = alloca [10 x i32]
%3 = getelementptr inbounds [10 x i32], [10 x i32]* %a, i64 0, i64 0
store i32 10, i32* %3
%4 = getelementptr inbounds [10 x i32], [10 x i32]* %a, i64 0, i64 0
%5 = load i32, i32* %4
%6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %5)
%7 = getelementptr inbounds [10 x i32], [10 x i32]* %a, i64 0, i64 1
store i32 3, i32* %7
%8 = getelementptr inbounds [10 x i32], [10 x i32]* %a, i64 0, i64 1
%9 = load i32, i32* %8
%10 = getelementptr inbounds [10 x i32], [10 x i32]* %a, i64 0, i64 0
%11 = load i32, i32* %10
%12 = mul i32 %9, %11
%13 = getelementptr inbounds [10 x i32], [10 x i32]* %a, i64 0, i64 0
%14 = load i32, i32* %13
%15 = add i32 %12, %14
%b = alloca i32
store i32 %15, i32* %b
%16 = load i32, i32* %b
%17 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %16)
%18 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 5)
ret i32 0 }

