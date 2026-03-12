#整体思路和右旋字符串很接近，
#左旋字符串的意思是把字符串前面的若干个字符转移到字符串的尾部。
#例如，输入字符串"abcdefg"和数字2，那么左旋转2位得到的结果是"cdefgab"。
#所以思路为：先反转K个字符，然后反转剩余字符，最后反转整体字符串
k=int(input())
s=input()

s=s[k:]+s[:k]#这种实现方式是直接用python的切片
print(s)

#以下使用反转函数的方式来实现
def reverse(chars,left,right):

     while left < right:
         chars[left],chars[right]=chars[right],chars[left]
         left+=1
         right-=1
     return chars
def reverseLeftWords(s: str, k: int) -> str:
    s_list=list(s)
    reverse(s_list,0,k-1)
    reverse(s_list,k,len(s)-1)
    reverse(s_list,0,len(s)-1)
    return ''.join(s_list)

print(reverseLeftWords(s,k+1))#开区间，用k+1