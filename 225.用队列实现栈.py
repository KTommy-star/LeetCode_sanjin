'''

225. 用队列实现栈
简单
请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。
实现 MyStack 类：
void push(int x) 将元素 x 压入栈顶。
int pop() 移除并返回栈顶元素。
int top() 返回栈顶元素。
boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。
注意：
你只能使用队列的标准操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
name:sanjin
date:2026-3-15
'''
class MyStack(object):

    def __init__(self):
        #这个题目，核心思想是用两个队列来模拟一个栈，一个队列用来入栈，另一个队列用来出栈
        self.queue_in=[]
        self.queue_out=[]
        #注意：in是存所有数据，out仅有在pop的时候才会用
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        #有新元素进来，就压入入栈队列
        self.queue_in.append(x)

    def pop(self):
        """
        :rtype: int
        """
        """
               1. 首先确认不空
               2. 因为队列的特殊性，FIFO，所以我们只有在pop()的时候才会使用queue_out
               3. 先把queue_in中的所有元素（除了最后一个），依次出列放进queue_out
               4. 交换in和out，此时out里只有一个元素
               5. 把out中的pop出来，即是原队列的最后一个

               tip：这不能像栈实现队列一样，因为另一个queue也是FIFO，如果执行pop()它不能像
               stack一样从另一个pop()，所以干脆in只用来存数据，pop()的时候两个进行交换
        """
        if self.empty():
            return None
        for i in range(len(self.queue_in)-1):
            self.queue_out.append(self.queue_in.pop(0))
        self.queue_in,self.queue_out=self.queue_out,self.queue_in
        return self.queue_out.pop(0)

    def top(self):
        """
        :rtype: int
        """
        #写法一：
        #1. 首先确认不空
        #2. 我们仅有in会存放数据，所以返回第一个即可（这里实际上用到了栈）
        if self.empty():
            return None
        return self.queue_in[-1]
    def empty(self):
        """
        :rtype: bool
        """
        #in只要有元素，栈就不空了
        return not self.queue_in 

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()