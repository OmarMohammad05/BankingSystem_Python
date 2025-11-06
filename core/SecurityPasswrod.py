class Security:
    @staticmethod
    def __ConvertCharToAscii(text:str)-> int:

        return ord(text)

    @staticmethod
    def __ConvertAsciiToText(ascciiText:int) -> str:
        return chr(ascciiText)

    @staticmethod
    def Encryp(password, encryptionKey=5) -> str:
        Encryptext=str()
        for ch in password:
            if ch.isdigit():
                Encryptext+=str((int(ch)+encryptionKey)%10)
            else:
                ascciCode=Security.__ConvertCharToAscii(ch)+encryptionKey
                Encryptext+=Security.__ConvertAsciiToText(ascciCode)
        return Encryptext
    
    @staticmethod         
    def Decryp(password,encryptionKey=5)->str:
        Decryptext=str()
        for ch in password:
            if ch.isdigit():
                convetInt=int(ch)
                Decryptext+=str((int(ch)+encryptionKey)%10)
            else:
                ascciCode=Security.__ConvertCharToAscii(ch)-encryptionKey
                Decryptext+=Security.__ConvertAsciiToText(ascciCode)
        return Decryptext  