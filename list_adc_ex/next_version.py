def next_version(vers):
    int_vers = int(''.join(vers))
    int_vers += 1
    nxt_vers = list(str(int_vers))
    nxt_vers = '.'.join(nxt_vers)
    return nxt_vers


current_version = input().split('.')
print(next_version(current_version))
