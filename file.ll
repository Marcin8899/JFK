rzutowanie
declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strs = constant [3 x i8] c"%d\00"
define i32 @main() nounwind{
%a = alloca double
store double 2.4, double* %a
%1 = fadd double 2.5, 2.5
%2 = fptosi double %1 to i32
%3 = sub i32 4, 2
%4 = sdiv i32 8, %3
%5 = mul i32 %2, %4
%x = alloca i32
store i32 %5, i32* %x
%6 = load i32, i32* %x
%7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %6)
ret i32 0 }

