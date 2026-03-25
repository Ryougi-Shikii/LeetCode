class Solution:
    def isValid(self, s: str):
        st=[]
        for i in range(len(s)):
            ch=s[i]
            if ch=='(' or ch=='{' or ch=='[':
                st.append(ch)
            else:
                if len(st)==0: return False
                t=st[-1]
                if ch==')' and t!='(' or ch=='}' and t!='{' or ch==']' and t!='[':
                    return False
                st.pop()
        return len(st)==0
                    
      


        