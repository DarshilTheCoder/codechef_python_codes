a = int(input())
for i in range(0, a):
    alice = int(input())
    bob = int(input())
    charlie = int(input())
    if (alice != bob != charlie):
        if (alice > bob):
            if (alice > charlie):
                print("ALICE")
            else:
                print("CHARLIE")
        else:
            if (bob > charlie):
                print("BOB")
            else:
                print("CHARLIE")
