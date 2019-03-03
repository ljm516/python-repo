# 调用栈
def greet2(name):
    print("how are you, {name}?".format(name=name))


def bye():
    print("ok, bye!")


def greet(name):
    print("hello, {name} !".format(name=name))
    greet2(name)
    print("greeting ready to say bye...")

    bye()


greet("ljming")

'''
    说明：
        调用 greet(), 计算机为该函数分配一块内存。
        变量 name 被设置为 ljming，存储在内存中。
        每当调用函数时，计算机都像这样将函数调用
        涉及的所有变量的值存储在内存中。
        打印出 ‘hello, ljming’ 后，在调用 greet2('ljming')。
        同样，计算机也为这个函数分配一块内存。
        计算机使用一个栈表示这些内存块，
        其中第二个内存块位于第一个内存块上面。打印 'how are you, ljming'。
        然后从函数调用返回。此时，栈顶的内存块被弹出。
        现在栈顶内存块是 greet 的，这意味着你返回到了函数 greet。
        当调用函数 greet2 时，函数 greet 只是执行了一部分。
        一个重要的概念: 调用另一个函数时，当前函数暂停并处于
        未完成状态。该函数的所有变量的值还在内存中。执行完函数 greet2 后，
        回到函数greet，并从离开的地方开始往下执行：
        首先打印 ‘greeting ready to say bye..’，在调用函数 bye。
        在栈顶添加了函数 bye 的内存块。然后，打印 ‘OK，bye’。
        并从这个函数返回，现在又回到了 greet 。由于没有其他的函数调用，
        从 greet 函数返回。这个栈用于存储多个函数的变量，被称之为调用栈。
'''
