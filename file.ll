declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strs = constant [3 x i8] c"%d\00"
define i32 @main() nounwind{
%a = alloca i32
store i32 2, i32* %a
%b = alloca i32
store i32 5, i32* %b
%1 = load i32, i32* %a
%2 = load i32, i32* %b
%3 = sub i32 %1, %2
%c = alloca i32
store i32 %3, i32* %c
%4 = load i32, i32* %c
%5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %4)
%6 = load i32, i32* %a
%7 = load i32, i32* %b
%8 = mul i32 %6, %7
store i32 %8, i32* %c
%9 = load i32, i32* %c
%10 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %9)
%11 = load i32, i32* %b
%12 = load i32, i32* %a
%13 = sdiv i32 %11, %12
store i32 %13, i32* %c
%14 = load i32, i32* %c
%15 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %14)
%16 = fdiv double 2.8, 0.7
%d = alloca double
store double %16, double* %d
%17 = load double, double* %d
%18 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %17)
ret i32 0 }
