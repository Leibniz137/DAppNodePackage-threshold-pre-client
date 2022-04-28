import json
import logging
import os
from pathlib import Path
import subprocess
import time

logging.basicConfig(level=logging.INFO)

REQUIRED_ENV_VARS = [
    'ETH_PROVIDER_URL',
    'IP_ADDRESS',
    'MAX_GAS_PRICE',
    'NETWORK',
    'NUCYPHER_KEY_MATERIAL',
    'NUCYPHER_KEYSTORE_PASSWORD',
    'OPERATOR_KEYSTORE_PASSWORD',
    'OPERATOR_KEYSTORE_JSON',
    'PAYMENT_NETWORK',
    'PAYMENT_PROVIDER_URL',
]

# NOTE: this script assumes the directories have already been created
#       in the wrapper shell script
URSULA_CONFIG_PATH = Path('/root/.local/share/nucypher/ursula.json')
OPERATOR_KEYSTORE_PATH = Path('/root/.ethereum/keystore')
OPERATOR_KEYSTORE_JSON_PATH = OPERATOR_KEYSTORE_PATH / 'operator.json'

class EnvironmentError(Exception):
    pass


def check_env_vars(env):
    missing = []
    for var in REQUIRED_ENV_VARS:
        if var not in env:
            missing.append(var)
    return missing


def main():
    missing_env_vars = check_env_vars(os.environ)
    if missing_env_vars:
        logging.error(f"Missing the following environment variables: {missing_env_vars}")
        logging.debug("waiting 5s before exiting")
        time.sleep(5)
        raise EnvironmentError(
            f"Missing the following environment variables: {missing_env_vars}")

    logging.info("writing operator keystore json")
    operator_keystore_json = json.loads(os.environ['OPERATOR_KEYSTORE_JSON'])
    if not OPERATOR_KEYSTORE_JSON_PATH.exists():
        with OPERATOR_KEYSTORE_JSON_PATH.open('w') as fp:
            json.dump(operator_keystore_json, fp)

    operator_addr = '0x' + operator_keystore_json['address']

    signer = f'keystore://{str(OPERATOR_KEYSTORE_PATH)}'
    eth_provider = os.environ['ETH_PROVIDER_URL']
    max_gas_price = os.environ['MAX_GAS_PRICE']
    # TODO should network and payment_network still be configurable?
    network = os.environ['NETWORK']
    rest_host = os.environ['IP_ADDRESS']
    payment_network = os.environ['PAYMENT_NETWORK']
    payment_provider = os.environ['PAYMENT_PROVIDER_URL']

    if not URSULA_CONFIG_PATH.exists():
        logging.info("pre-existing ursula config not found, initializing node")
        cmd = [
            '/usr/local/bin/nucypher',
            'ursula',
            'init',
            '--signer', signer,
            '--eth-provider', eth_provider,
            '--network', network,
            '--payment-provider', payment_provider,
            '--payment-network', payment_network,
            '--operator-address', operator_addr,
            '--max-gas-price', max_gas_price,
            '--rest-host', rest_host,
            '--key-material', os.environ['NUCYPHER_KEY_MATERIAL']
        ]
        subprocess.run(cmd, check=True)

    logging.info("updating ursula config with latest config values")
    with URSULA_CONFIG_PATH.open() as fp:
        ursula_config = json.load(fp)

    ursula_config.update({
        'domain': network,
        'eth_provider_uri': eth_provider,
        'max_gas_price': max_gas_price,
        'operator_address': operator_addr,
        'payment_network': payment_network,
        'payment_provider': payment_provider,
        'rest_host': rest_host,
        'signer_uri': signer,
    })
    with URSULA_CONFIG_PATH.open('w') as fp:
        json.dump(ursula_config, fp)


if __name__ == '__main__':
    main()
