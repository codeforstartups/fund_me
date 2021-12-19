from brownie import FundMe, network, config
from scripts.helpful_scripts import get_account


def deploy_fund_me():
    account = get_account()
    # if we are on persistent network like rinkby, use the assosiated address
    # otherwise deploy mocks
    if network.show_active() == "developement":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"]
    fund_me = FundMe.deploy("0x8A753747A1Fa494EC906cE90E9f37563A8AF630e", {
                            "from": account}, publish_source=True)
    print(f"Contract Deployed to {fund_me.address}")


def main():
    deploy_fund_me()
