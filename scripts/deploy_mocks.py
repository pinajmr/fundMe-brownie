from brownie import (
    MockV3Aggregator,
    network,
)
from scripts.helpful_scripts import (
    DECIMALS,
    get_account,
)

DECIMALS = 8
INITIAL_VALUE = 200000000000  # 2,000


def deploy_mocks():
    print(f"the active network is {network.show_active()}")
    print("Deploying Mocks ...")
    account = get_account()
    MockV3Aggregator.deploy(DECIMALS, INITIAL_VALUE, {"from": account})
    print("Mocks Deployed!!")


def main():
    deploy_mocks()
