declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strs = constant [3 x i8] c"%d\00"
@.str = constant [3 x i8] c"%s\00"
@.char = constant [3 x i8] c"%c\00"
define i32 @main() nounwind{

%1 = call i32 @test()
%tescik = alloca i32
store i32 %1, i32* %tescik
%2 = load i32, i32* %tescik
%3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %2)
ret i32 0 }
define i32 @test() nounwind {
%a = alloca i32
store i32 2, i32* %a
%1 = load i32, i32* %a
%return = alloca i32
store i32 %1, i32* %return
ret i32 %1
}


