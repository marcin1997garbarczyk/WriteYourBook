from backendApp.models import UserWallet


class WalletService:
    def __init__(self):
        pass

    def get_current_wallet_for_user_id(self, userId):
        userWallet = UserWallet.objects.get(ownerId=userId)
        if not userWallet:
            userWallet = self.create_new_wallet(userId)
        return userWallet

    def reduceCoinInCurrentWallet(self, userId):
        userWallet = self.get_current_wallet_for_user_id(userId)
        currentBalance = userWallet.balance
        userWallet.balance = currentBalance - 1
        userWallet.save()

    def checkBalanceOnCurrentWallet(self, userId):
        userWallet = self.get_current_wallet_for_user_id(userId)
        if userWallet.balance > 0:
            return True
        else:
            return False

    def create_new_wallet(self, userId):
        userWallet = UserWallet()
        userWallet.ownerId = userId
        userWallet.balance = 10
        userWallet.save()
        return userWallet