class Solution:
    def interpret(self, command: str) -> str:
        ans=""
        for i in range(len(command)):
            if command[i]=="(":
                if command[i+1]==")":
                    ans+="o"
                    i+=1
                elif(command[i]=="("):
                    if command[i+1]=="a":
                        ans+="al"
                        i+=3
            if command[i]=="G":
                ans+="G"
        return ans