class systems:
    """
        Представляет собой класс с функциями
            - <b>convert_from</b>
            - <b>convert_to</b>
            - <b>multi</b>
        И обязательными аргументами
            - <b>num  ->  <u>int</u></b>
            - <b>system ->  <u>int</u></b>

        <u><b>convert_from</b></u>
            Переводит число <i>num</i> из 10-ой системы счисления в <i>system</i>


        <u><b>convert_to</b></u>
            Переводит число <i>num</i> из системы со основанием <i>system</i>
            в 10-ую

        <u><b>multi</b></u>
            <i>Дополнительные аргументы:</i>
                - system_from -> <u>int</u>

            Переводит число num из системы <i>system_from</i> в систему <i>system</i>
    """

    def __init__(self, num=str, system=int, system_from=int or 0):
        self.num         = num
        self.system      = system
        self.system_from = system_from
    

    def __cc__(self, a, b):
        digits = '0123456789abcdefghijklmnopqrstuvwxyz'
        if a == 0:
            result = "0"
        
        else:
            result = ""
            is_neg = a < 0
            a = abs(a)

            while a > 0:
                result = digits[a % b] + result
                a //= b
            print(result)
            return "-" + result.upper() if is_neg else result.upper()

    
    def convert_from(self) -> int:
        a = int(self.num)
        b = int(self.system)
        return self.__cc__(a, b)

    def convert_to(self) -> int | Exception:
        return int(self.num, self.system_from)

    def multi(self):
        self.num = self.convert_to()
        return self.convert_from()


if __name__ == "__main__":
    print("Данные для примера:\n")
    
    primer = systems(20, 2, 4)
    print("Число 20 из 10й в 2ю: ")
    print("= ", primer.convert_from())
    # print("Число 20 из 2й в 10ю: ")
    # print("= ", primer.convert_to())
    print("Число 20 из 4ой в 2ю: ")
    print("= ", primer.multi())
