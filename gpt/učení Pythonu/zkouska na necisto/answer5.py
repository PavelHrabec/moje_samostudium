from exam_lib import User

class VIPUser(User):
    def __init__(self, name, surname, email, vip_card_number):
        super().__init__(name, surname, email)
        if self._check_card(vip_card_number):
            self._vip_card_number = vip_card_number
        else:
            self._vip_card_number = None

    @staticmethod
    def _check_card(new_number):
        return isinstance(new_number, int) and new_number > 999 and new_number % 2 == 0

    @staticmethod
    def use_vip_card():
        pass  # nebo: return None

    @property
    def vip_card_number(self):
        return self._vip_card_number

    @vip_card_number.setter
    def vip_card_number(self, new_number):
        if self._check_card(new_number):
            self._vip_card_number = new_number



if __name__ == "__main__":
    user1 = VIPUser("Pavel", "Novák", "pavel@example.com", 1234)
    print(user1.vip_card_number)

    user1.vip_card_number = 555
    print(user1.vip_card_number)

    user1.vip_card_number = 2000
    print(user1.vip_card_number)
