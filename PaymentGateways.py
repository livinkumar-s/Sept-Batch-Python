from abc import abstractmethod,ABC


#abstract class
class PaymentGateway(ABC):
    @abstractmethod
    def pay():
        pass


class Paypal(PaymentGateway):
    @staticmethod
    def pay1():
        print("Payment Successful")   
class RazorPay(PaymentGateway):
    @staticmethod
    def pay():
        print("Payment Successful")
class CashFree(PaymentGateway):
    @staticmethod
    def pay():
        print("Payment Successful")


# p1=PaymentGateway()