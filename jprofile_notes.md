# instrumenting
measure time of all methods
overhead + distorts actual timings
# sampling
take snaphots of thread state ( thread dump - get stack traces  )
# article to read on profilers and their limitation
1) Why (most) sampling java profilers are fucking terrible
https://psy-lob-saw.blogspot.com/2016/02/why-most-sampling-java-profilers-are.html

# issues with profilers
- safepoint bias
- shows idle threads
- no native code 

# honest-profiler 

# use build in hardware counter in CPU
## use perf tool
problem is it will not show dynamically compiled methods by JIt
## to get the dynamic names use perf-map-agent:
https://github.com/jvm-profiling-tools/perf-map-agent
## you have to enable JVM option:
-XX:+PreserveFramePointer
## flamegraph
https://github.com/brendangregg/FlameGraph
perf record
perf script
FlameGraph/stackcollapse-perf.pl
FlameGraph/flamegraph.pl

# async-profiler  ( use this one ?)
https://github.com/async-profiler/async-profiler
