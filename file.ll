declare i32 @printf(i8*, ...)
declare void @llvm.memcpy.p0i8.p0i8.i64(i8* noalias nocapture writeonly, i8* noalias nocapture readonly, i64, i1)
declare i32 @__isoc99_scanf(i8*, ...)
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strs = constant [3 x i8] c"%d\00"
@.str = constant [3 x i8] c"%s\00"
@.char = constant [3 x i8] c"%c\00"
define i32 @main() nounwind{
%a = alloca i32
store i32 5, i32* %a
store i32 10, i32* %a
%1 = load i32, i32* %a
%2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %1)
ret i32 0 }

