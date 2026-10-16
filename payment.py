from PaymentGateways import CashFree,Paypal,RazorPay

cash=CashFree()
ray=RazorPay()
paypal=Paypal()

def makePayments(obj):
    obj.pay()


makePayments(paypal)

#call pay method from any payment gateway