import time

import grpc


import logging

from cloudstate.test.shoppingcart.shoppingcart_pb2 import GetShoppingCart, AddLineItem
from cloudstate.test.shoppingcart.shoppingcart_pb2_grpc import ShoppingCartStub

from cloudstate.test.run_test_server import run_test_server

logger = logging.getLogger()


def evaluate_shoppingcart_server(host: str, port: int):
    logger.info(f"host: {host}")
    logger.info(f"port: {port}")
    server_hostport = f"{host}:{port}"
    logger.info(f"connecting on {server_hostport}")
    channel = grpc.insecure_channel(server_hostport)

    stub = ShoppingCartStub(channel)
    request = GetShoppingCart(user_id="leeroy")
    response = stub.GetCart(request)
    logger.info(f"resp: {response}")

    stub.AddItem(
        AddLineItem(user_id="leeroy", product_id="0", name="beer", quantity=24)
    )
    response = stub.GetCart(request)
    logger.info(f"resp: {response}")


def test_shoppingcart():
    server_thread = run_test_server(port=8081)
    import docker
    client = docker.from_env()
    # client.images.pull('cloudstateio/cloudstate-proxy-dev-mode:latest')
    container = client.containers.run("cloudstateio/cloudstate-proxy-dev-mode", environment={"USER_FUNCTION_HOST":"127.0.0.1", "USER_FUNCTION_PORT":"8081"},detach=True, ports={'9000/tcp': 9000}, network="host")
    logger.info(f"status {container.status}")
    try:
        time.sleep(15)
        evaluate_shoppingcart_server("127.0.0.1", 9000)
    except Exception as e:
        raise e
    finally:
        server_thread.stop(None)
        logger.info(container.logs())
        container.stop()