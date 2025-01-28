; ModuleID = 'chall.c'
source_filename = "chall.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

%struct._IO_FILE = type { i32, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, %struct._IO_marker*, %struct._IO_FILE*, i32, i32, i64, i16, i8, [1 x i8], i8*, i64, %struct._IO_codecvt*, %struct._IO_wide_data*, %struct._IO_FILE*, i8*, i64, i32, [20 x i8] }
%struct._IO_marker = type opaque
%struct._IO_codecvt = type opaque
%struct._IO_wide_data = type opaque

@.str = private unnamed_addr constant [5 x i8] c"%02x\00", align 1
@__const.checkflag.m = private unnamed_addr constant [27 x i32] [i32 301, i32 728, i32 546, i32 315, i32 756, i32 497, i32 315, i32 658, i32 301, i32 322, i32 770, i32 315, i32 623, i32 532, i32 315, i32 742, i32 756, i32 315, i32 763, i32 315, i32 728, i32 343, i32 322, i32 770, i32 301, i32 294, i32 728], align 16
@.str.1 = private unnamed_addr constant [10 x i8] c"Alphabit{\00", align 1
@.str.2 = private unnamed_addr constant [17 x i8] c"6d346368316e337d\00", align 1
@__const.checkflag.n = private unnamed_addr constant [7 x i32] [i32 123, i32 54, i32 119, i32 121, i32 122, i32 57, i32 113], align 16
@.str.3 = private unnamed_addr constant [17 x i8] c"0f_Th3_l0w_l3v3l\00", align 1
@.str.4 = private unnamed_addr constant [42 x i8] c"Now The Challenge is renamed to Crack me\0A\00", align 1
@.str.5 = private unnamed_addr constant [27 x i8] c"please give me the flag : \00", align 1
@stdin = external global %struct._IO_FILE*, align 8
@.str.6 = private unnamed_addr constant [2 x i8] c"\0A\00", align 1
@.str.7 = private unnamed_addr constant [15 x i8] c"Correct Flag!\0A\00", align 1
@.str.8 = private unnamed_addr constant [11 x i8] c"Try Again\0A\00", align 1

; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @string_to_hex(i8* noundef %0, i8* noundef %1) #0 {
  %3 = alloca i8*, align 8
  %4 = alloca i8*, align 8
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  store i8* %0, i8** %3, align 8
  store i8* %1, i8** %4, align 8
  store i32 0, i32* %6, align 4
  %8 = load i8*, i8** %3, align 8
  %9 = call i64 @strlen(i8* noundef %8) #6
  %10 = trunc i64 %9 to i32
  store i32 %10, i32* %7, align 4
  store i32 0, i32* %5, align 4
  br label %11

11:                                               ; preds = %29, %2
  %12 = load i32, i32* %5, align 4
  %13 = load i32, i32* %7, align 4
  %14 = icmp slt i32 %12, %13
  br i1 %14, label %15, label %32

15:                                               ; preds = %11
  %16 = load i8*, i8** %4, align 8
  %17 = load i32, i32* %6, align 4
  %18 = sext i32 %17 to i64
  %19 = getelementptr inbounds i8, i8* %16, i64 %18
  %20 = load i8*, i8** %3, align 8
  %21 = load i32, i32* %5, align 4
  %22 = sext i32 %21 to i64
  %23 = getelementptr inbounds i8, i8* %20, i64 %22
  %24 = load i8, i8* %23, align 1
  %25 = zext i8 %24 to i32
  %26 = call i32 (i8*, i8*, ...) @sprintf(i8* noundef %19, i8* noundef getelementptr inbounds ([5 x i8], [5 x i8]* @.str, i64 0, i64 0), i32 noundef %25) #7
  %27 = load i32, i32* %6, align 4
  %28 = add nsw i32 %27, 2
  store i32 %28, i32* %6, align 4
  br label %29

29:                                               ; preds = %15
  %30 = load i32, i32* %5, align 4
  %31 = add nsw i32 %30, 1
  store i32 %31, i32* %5, align 4
  br label %11, !llvm.loop !6

32:                                               ; preds = %11
  %33 = load i8*, i8** %4, align 8
  %34 = load i32, i32* %6, align 4
  %35 = sext i32 %34 to i64
  %36 = getelementptr inbounds i8, i8* %33, i64 %35
  store i8 0, i8* %36, align 1
  ret void
}

; Function Attrs: nounwind readonly willreturn
declare i64 @strlen(i8* noundef) #1

; Function Attrs: nounwind
declare i32 @sprintf(i8* noundef, i8* noundef, ...) #2

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @checkflag(i8* noundef %0) #0 {
  %2 = alloca i32, align 4
  %3 = alloca i8*, align 8
  %4 = alloca [27 x i32], align 16
  %5 = alloca i32, align 4
  %6 = alloca [15 x i8], align 1
  %7 = alloca [7 x i32], align 16
  %8 = alloca i32, align 4
  %9 = alloca [17 x i8], align 16
  %10 = alloca i32, align 4
  store i8* %0, i8** %3, align 8
  %11 = bitcast [27 x i32]* %4 to i8*
  call void @llvm.memcpy.p0i8.p0i8.i64(i8* align 16 %11, i8* align 16 bitcast ([27 x i32]* @__const.checkflag.m to i8*), i64 108, i1 false)
  %12 = load i8*, i8** %3, align 8
  %13 = call i32 @strncmp(i8* noundef %12, i8* noundef getelementptr inbounds ([10 x i8], [10 x i8]* @.str.1, i64 0, i64 0), i64 noundef 9) #6
  %14 = icmp ne i32 %13, 0
  br i1 %14, label %21, label %15

15:                                               ; preds = %1
  %16 = load i8*, i8** %3, align 8
  %17 = getelementptr inbounds i8, i8* %16, i64 69
  %18 = load i8, i8* %17, align 1
  %19 = sext i8 %18 to i32
  %20 = icmp ne i32 %19, 125
  br i1 %20, label %21, label %22

21:                                               ; preds = %15, %1
  store i32 0, i32* %2, align 4
  br label %139

22:                                               ; preds = %15
  store i32 9, i32* %5, align 4
  br label %23

23:                                               ; preds = %43, %22
  %24 = load i32, i32* %5, align 4
  %25 = icmp slt i32 %24, 35
  br i1 %25, label %26, label %46

26:                                               ; preds = %23
  %27 = load i8*, i8** %3, align 8
  %28 = load i32, i32* %5, align 4
  %29 = sext i32 %28 to i64
  %30 = getelementptr inbounds i8, i8* %27, i64 %29
  %31 = load i8, i8* %30, align 1
  %32 = sext i8 %31 to i32
  %33 = sub nsw i32 %32, 6
  %34 = mul nsw i32 %33, 7
  %35 = load i32, i32* %5, align 4
  %36 = sub nsw i32 %35, 9
  %37 = sext i32 %36 to i64
  %38 = getelementptr inbounds [27 x i32], [27 x i32]* %4, i64 0, i64 %37
  %39 = load i32, i32* %38, align 4
  %40 = icmp ne i32 %34, %39
  br i1 %40, label %41, label %42

41:                                               ; preds = %26
  store i32 0, i32* %2, align 4
  br label %139

42:                                               ; preds = %26
  br label %43

43:                                               ; preds = %42
  %44 = load i32, i32* %5, align 4
  %45 = add nsw i32 %44, 1
  store i32 %45, i32* %5, align 4
  br label %23, !llvm.loop !8

46:                                               ; preds = %23
  %47 = load i8*, i8** %3, align 8
  %48 = getelementptr inbounds i8, i8* %47, i64 36
  %49 = load i8, i8* %48, align 1
  %50 = sext i8 %49 to i32
  %51 = icmp ne i32 %50, 95
  br i1 %51, label %82, label %52

52:                                               ; preds = %46
  %53 = load i8*, i8** %3, align 8
  %54 = getelementptr inbounds i8, i8* %53, i64 39
  %55 = load i8, i8* %54, align 1
  %56 = sext i8 %55 to i32
  %57 = icmp ne i32 %56, 95
  br i1 %57, label %82, label %58

58:                                               ; preds = %52
  %59 = load i8*, i8** %3, align 8
  %60 = getelementptr inbounds i8, i8* %59, i64 43
  %61 = load i8, i8* %60, align 1
  %62 = sext i8 %61 to i32
  %63 = icmp ne i32 %62, 95
  br i1 %63, label %82, label %64

64:                                               ; preds = %58
  %65 = load i8*, i8** %3, align 8
  %66 = getelementptr inbounds i8, i8* %65, i64 47
  %67 = load i8, i8* %66, align 1
  %68 = sext i8 %67 to i32
  %69 = icmp ne i32 %68, 95
  br i1 %69, label %82, label %70

70:                                               ; preds = %64
  %71 = load i8*, i8** %3, align 8
  %72 = getelementptr inbounds i8, i8* %71, i64 53
  %73 = load i8, i8* %72, align 1
  %74 = sext i8 %73 to i32
  %75 = icmp ne i32 %74, 95
  br i1 %75, label %82, label %76

76:                                               ; preds = %70
  %77 = load i8*, i8** %3, align 8
  %78 = getelementptr inbounds i8, i8* %77, i64 61
  %79 = load i8, i8* %78, align 1
  %80 = sext i8 %79 to i32
  %81 = icmp ne i32 %80, 95
  br i1 %81, label %82, label %83

82:                                               ; preds = %76, %70, %64, %58, %52, %46
  store i32 0, i32* %2, align 4
  br label %139

83:                                               ; preds = %76
  %84 = load i8*, i8** %3, align 8
  %85 = getelementptr inbounds i8, i8* %84, i64 62
  %86 = getelementptr inbounds [15 x i8], [15 x i8]* %6, i64 0, i64 0
  call void @string_to_hex(i8* noundef %85, i8* noundef %86)
  %87 = getelementptr inbounds [15 x i8], [15 x i8]* %6, i64 0, i64 0
  %88 = call i32 @strcmp(i8* noundef %87, i8* noundef getelementptr inbounds ([17 x i8], [17 x i8]* @.str.2, i64 0, i64 0)) #6
  %89 = icmp ne i32 %88, 0
  br i1 %89, label %90, label %91

90:                                               ; preds = %83
  store i32 0, i32* %2, align 4
  br label %139

91:                                               ; preds = %83
  %92 = bitcast [7 x i32]* %7 to i8*
  call void @llvm.memcpy.p0i8.p0i8.i64(i8* align 16 %92, i8* align 16 bitcast ([7 x i32]* @__const.checkflag.n to i8*), i64 28, i1 false)
  store i32 54, i32* %8, align 4
  br label %93

93:                                               ; preds = %112, %91
  %94 = load i32, i32* %8, align 4
  %95 = icmp slt i32 %94, 60
  br i1 %95, label %96, label %115

96:                                               ; preds = %93
  %97 = load i8*, i8** %3, align 8
  %98 = load i32, i32* %8, align 4
  %99 = sext i32 %98 to i64
  %100 = getelementptr inbounds i8, i8* %97, i64 %99
  %101 = load i8, i8* %100, align 1
  %102 = sext i8 %101 to i32
  %103 = add nsw i32 %102, 5
  %104 = load i32, i32* %8, align 4
  %105 = sub nsw i32 %104, 54
  %106 = sext i32 %105 to i64
  %107 = getelementptr inbounds [7 x i32], [7 x i32]* %7, i64 0, i64 %106
  %108 = load i32, i32* %107, align 4
  %109 = icmp ne i32 %103, %108
  br i1 %109, label %110, label %111

110:                                              ; preds = %96
  store i32 0, i32* %2, align 4
  br label %139

111:                                              ; preds = %96
  br label %112

112:                                              ; preds = %111
  %113 = load i32, i32* %8, align 4
  %114 = add nsw i32 %113, 1
  store i32 %114, i32* %8, align 4
  br label %93, !llvm.loop !9

115:                                              ; preds = %93
  %116 = bitcast [17 x i8]* %9 to i8*
  call void @llvm.memset.p0i8.i64(i8* align 16 %116, i8 0, i64 17, i1 false)
  store i32 37, i32* %10, align 4
  br label %117

117:                                              ; preds = %130, %115
  %118 = load i32, i32* %10, align 4
  %119 = icmp slt i32 %118, 53
  br i1 %119, label %120, label %133

120:                                              ; preds = %117
  %121 = load i8*, i8** %3, align 8
  %122 = load i32, i32* %10, align 4
  %123 = sext i32 %122 to i64
  %124 = getelementptr inbounds i8, i8* %121, i64 %123
  %125 = load i8, i8* %124, align 1
  %126 = load i32, i32* %10, align 4
  %127 = sub nsw i32 %126, 37
  %128 = sext i32 %127 to i64
  %129 = getelementptr inbounds [17 x i8], [17 x i8]* %9, i64 0, i64 %128
  store i8 %125, i8* %129, align 1
  br label %130

130:                                              ; preds = %120
  %131 = load i32, i32* %10, align 4
  %132 = add nsw i32 %131, 1
  store i32 %132, i32* %10, align 4
  br label %117, !llvm.loop !10

133:                                              ; preds = %117
  %134 = getelementptr inbounds [17 x i8], [17 x i8]* %9, i64 0, i64 0
  %135 = call i32 @strcmp(i8* noundef %134, i8* noundef getelementptr inbounds ([17 x i8], [17 x i8]* @.str.3, i64 0, i64 0)) #6
  %136 = icmp ne i32 %135, 0
  br i1 %136, label %137, label %138

137:                                              ; preds = %133
  store i32 0, i32* %2, align 4
  br label %139

138:                                              ; preds = %133
  store i32 1, i32* %2, align 4
  br label %139

139:                                              ; preds = %138, %137, %110, %90, %82, %41, %21
  %140 = load i32, i32* %2, align 4
  ret i32 %140
}

; Function Attrs: argmemonly nofree nounwind willreturn
declare void @llvm.memcpy.p0i8.p0i8.i64(i8* noalias nocapture writeonly, i8* noalias nocapture readonly, i64, i1 immarg) #3

; Function Attrs: nounwind readonly willreturn
declare i32 @strncmp(i8* noundef, i8* noundef, i64 noundef) #1

; Function Attrs: nounwind readonly willreturn
declare i32 @strcmp(i8* noundef, i8* noundef) #1

; Function Attrs: argmemonly nofree nounwind willreturn writeonly
declare void @llvm.memset.p0i8.i64(i8* nocapture writeonly, i8, i64, i1 immarg) #4

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca [100 x i8], align 16
  store i32 0, i32* %1, align 4
  %3 = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([42 x i8], [42 x i8]* @.str.4, i64 0, i64 0))
  %4 = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([27 x i8], [27 x i8]* @.str.5, i64 0, i64 0))
  %5 = getelementptr inbounds [100 x i8], [100 x i8]* %2, i64 0, i64 0
  %6 = load %struct._IO_FILE*, %struct._IO_FILE** @stdin, align 8
  %7 = call i8* @fgets(i8* noundef %5, i32 noundef 100, %struct._IO_FILE* noundef %6)
  %8 = getelementptr inbounds [100 x i8], [100 x i8]* %2, i64 0, i64 0
  %9 = call i64 @strcspn(i8* noundef %8, i8* noundef getelementptr inbounds ([2 x i8], [2 x i8]* @.str.6, i64 0, i64 0)) #6
  %10 = getelementptr inbounds [100 x i8], [100 x i8]* %2, i64 0, i64 %9
  store i8 0, i8* %10, align 1
  %11 = getelementptr inbounds [100 x i8], [100 x i8]* %2, i64 0, i64 0
  %12 = call i32 @checkflag(i8* noundef %11)
  %13 = icmp ne i32 %12, 0
  br i1 %13, label %14, label %16

14:                                               ; preds = %0
  %15 = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([15 x i8], [15 x i8]* @.str.7, i64 0, i64 0))
  br label %18

16:                                               ; preds = %0
  %17 = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([11 x i8], [11 x i8]* @.str.8, i64 0, i64 0))
  br label %18

18:                                               ; preds = %16, %14
  ret i32 0
}

declare i32 @printf(i8* noundef, ...) #5

declare i8* @fgets(i8* noundef, i32 noundef, %struct._IO_FILE* noundef) #5

; Function Attrs: nounwind readonly willreturn
declare i64 @strcspn(i8* noundef, i8* noundef) #1

attributes #0 = { noinline nounwind optnone uwtable "frame-pointer"="all" "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { nounwind readonly willreturn "frame-pointer"="all" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { nounwind "frame-pointer"="all" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { argmemonly nofree nounwind willreturn }
attributes #4 = { argmemonly nofree nounwind willreturn writeonly }
attributes #5 = { "frame-pointer"="all" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #6 = { nounwind readonly willreturn }
attributes #7 = { nounwind }

!llvm.module.flags = !{!0, !1, !2, !3, !4}
!llvm.ident = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 7, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 1}
!4 = !{i32 7, !"frame-pointer", i32 2}
!5 = !{!"Ubuntu clang version 14.0.0-1ubuntu1.1"}
!6 = distinct !{!6, !7}
!7 = !{!"llvm.loop.mustprogress"}
!8 = distinct !{!8, !7}
!9 = distinct !{!9, !7}
!10 = distinct !{!10, !7}
