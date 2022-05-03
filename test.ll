@.str = private unnamed_addr constant [3 x i8] c"%s\00", align 1

@__const.main.str1 = private unnamed_addr constant [12 x i8] c"Hrllo\00\00\00\00\00\00\00", align 1

declare void @llvm.memcpy.p0i8.p0i8.i64(i8* noalias nocapture writeonly, i8* noalias nocapture readonly, i64, i1)

declare dso_local i32 @printf(i8*, ...)
define dso_local i32 @main() {
  %1 = alloca [12 x i8], align 1
  %2 = getelementptr inbounds [12 x i8], [12 x i8]* %1, i64 0, i64 0
  store i8 97, i8* %2, align 1
  %3 = getelementptr inbounds [12 x i8], [12 x i8]* %1, i64 0, i64 0
  %4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i64 0, i64 0), i8* %3)
  ret i32 0
}

 