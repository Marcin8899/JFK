declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strs = constant [3 x i8] c"%d\00"
define i32 @main() nounwind{
%a = alloca double
store double 2.4, double* %a
%1 = fptosi double 3.5 to i32
%2 = add i32 2, %1
%x = alloca i32
store i32 %2, i32* %x
%3 = load i32, i32* %x
%4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %3)
ret i32 0 }

