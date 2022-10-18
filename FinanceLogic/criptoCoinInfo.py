from FinanceLogic import gto

# Выбор сетей в usdt
# https://coinmarketcap.com/currencies/tether/
# https://isitcrypto.com/add-usdt-to-metamask-wallet/

# coin, network, network_fee, my_wallet_address, txid=None):
usdt = gto.CryptCoinInfo("USDT", "TRC20", 1, 0x30EC9597123a16241c6037fEa0f61DF6F9F94221)

usdc = gto.CryptCoinInfo("USDC", "ERC20", 1, 0x30EC9597123a16241c6037fEa0f61DF6F9F94221)

busd = gto.CryptCoinInfo("BUSD", "BSC", 1, 0x30EC9597123a16241c6037fEa0f61DF6F9F94221)

coin_list = [usdt, usdc, busd]
