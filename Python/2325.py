class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        my_dict = {}
        y = 0 
        for i in range(len(key)):
            if(key[i] != " ") and key[i] not in my_dict:
           
                my_dict[key[i]] = chr(y+97)
                print(y,chr(y+97), key[i])
                y += 1

        output = ""
        for i in range(len(message)):
            if message[i] == " ":
                output += " "
            else: 
                output += my_dict[message[i]]
        return output