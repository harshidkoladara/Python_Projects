import unittest
from moneymanager import MoneyManager

moneyManager = MoneyManager('123456', '7890', '1000.0', [])


class TestMoneyManagerMethods(unittest.TestCase):

    def test_add_entry(self):
        moneyManager.deposite_funds(100.0)
        self.assertEqual(moneyManager.balance, str(1100.0))

    def test_add_entry(self):
        moneyManager.add_entry(100.0, 'Rent')
        self.assertEqual(moneyManager.balance, str(900.0))


if __name__ == '__main__':
    unittest.main()


# IS this ok??
#
