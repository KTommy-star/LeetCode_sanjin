'''

232. 用栈实现队列
简单
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
实现 MyQueue 类：
void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false
说明：
你只能使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
name:sanjin
date:2026-3-15
'''


class MyQueue(object):

    def __init__(self):
        #这个题目，核心思想是用两个栈来模拟一个队列，一个栈用来入队，另一个栈用来出队
        #当需要出队的时候，如果出队栈不为空，就直接从出队栈弹出元素，如果出队栈为空，就把入队栈的所有元素弹出并压入出队栈，这样就实现了先进先出的效果
        self.stack_in=[]
        self.stack_out=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        #有新元素进来，就压入入队栈
        self.stack_in.append(x)

    def pop(self):
        """
        :rtype: int
        """
        #要模拟队列的出队，在这里首先就需要判断出队是都为空，如果不为空，就直接弹出元素，如果为空，就把入队栈的所有元素弹出并压入出队栈，然后再弹出元素
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self):
        """
        :rtype: int
        """
        #peek的意思是查看队列头部的元素，但是不弹出它，所以在这里的逻辑和pop差不多
        #只不过最后是返回出队栈的最后一个元素，而不是弹出它
        answer=self.pop()#先弹出
        self.stack_out.append(answer)#又补充回去
        return answer

    def empty(self):
        """
        :rtype: bool
        """
        #只有两个栈都为空，队列才是空的
        return not self.stack_out and not self.stack_in
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()