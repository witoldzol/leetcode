import os, stat, sys


def dump_fds():
    print("-" * 20)
    for name in sorted(os.listdir("/proc/self/fd"), key=int):
        fd = int(name)
        try:
            target = os.readlink(f"/proc/self/fd/{fd}")
            st = os.fstat(fd)
            kind = (
                "FIFO/pipe"
                if stat.S_ISFIFO(st.st_mode)
                else "regular"
                if stat.S_ISREG(st.st_mode)
                else "char/other"
            )
            print(
                f"fd {fd}: {kind:10} mode={oct(st.st_mode)} -> {target}",
                # file=sys.stderr,
            )
        except OSError as e:
            print(f"fd {fd}: <gone: {e}>")
    print("-" * 20)


# 0 is stdin ( terminal )
# 1 is stdout ( terminal )
# 2 is stderr
# (writer eg. ls ) -> WRITE ---> PIPE ----> READ ( reader eg. grep )
read_fd, write_fd = os.pipe()

# print("PARENT FDS")
# dump_fds()
# fds = os.listdir("/proc/self/fd")
# print(fds)

pid1 = os.fork()
if pid1 == 0:
    print("child 1 execution ")
    print("BEFORE")

    dump_fds()
    # os.dup2('from','to')
    os.dup2(write_fd, 1)
    print("AFTER dup2")
    dump_fds()
    # close
    os.close(read_fd)
    os.close(write_fd)

    # os.execvp("ls", ["ls"])
    os._exit(0)  # in case exec fails

pid2 = os.fork()
if pid2 == 0:
    print("child 2 execution ")
    # os.dup2('old','new')
    os.dup2(read_fd, 0)
    # close
    os.close(read_fd)
    os.close(write_fd)
    # os.execvp("grep", ["grep", "how_to"])
    os.execvp("cat", ["cat"])
    os._exit(0)  # in case exec fails

print("parent is done")
# cleanup
os.close(read_fd)
os.close(write_fd)
