"""
TJS 2020 apache 2.0
"""

import sys
from logging import getLogger

import grpc
import pytest

from cloudstate.cloudstate import CloudState
from functiondemo.function_definition import definition, definition2
from functiondemo.functiondemo2_pb2 import FunctionRequest2
from functiondemo.functiondemo2_pb2_grpc import FunctionDemo2Stub
from functiondemo.functiondemo_pb2 import FunctionRequest, AddToSum, FunctionResponse
from functiondemo.functiondemo_pb2_grpc import FunctionDemoStub
from shoppingcart import shopping_cart_entity
from shoppingcart.shoppingcart_pb2 import AddLineItem, GetShoppingCart
from shoppingcart.shoppingcart_pb2_grpc import ShoppingCartStub

logger = getLogger()

if __name__ == "__main__":
    if len(sys.argv) < 1 or sys.argv[1] == "server":
        logger.info("starting server")
        server_builder = CloudState().host("0.0.0.0").port("8080")
        if "shoppingcart" in sys.argv:
            logger.info("adding shoppingcart service")
            server_builder = server_builder.register_event_sourced_entity(
                shopping_cart_entity.entity
            )
        if "functiondemo" in sys.argv:
            logger.info("adding functiondemo service")
            server_builder = server_builder.register_stateless_function_entity(
                definition
            )
            server_builder = server_builder.register_stateless_function_entity(
                definition2
            )

        server_builder.start()

    elif sys.argv[1] == "client":
        channel = grpc.insecure_channel("host.docker.internal:9000")

        if "shoppingcart" in sys.argv:
            stub = ShoppingCartStub(channel)
            request = GetShoppingCart(user_id="leeroy")
            response = stub.GetCart(request)
            logger.info(f"resp: {response}")

            stub.AddItem(
                AddLineItem(user_id="leeroy", product_id="0", name="beer", quantity=24)
            )
            response = stub.GetCart(request)
            logger.info(f"resp: {response}")

        if "functiondemo" in sys.argv:
            stub = FunctionDemoStub(channel)
            request_oof = FunctionRequest(foo="oof")
            response = stub.ReverseString(request_oof)
            logger.info(f"resp: {response}")
            assert response.bar == "foo"

            stub2 = FunctionDemo2Stub(channel)
            response = stub2.ReverseString2(request_oof)
            logger.info(f"resp: {response}")
            assert response.bar == "foo!"

            request_boom2 = FunctionRequest2(foo="boom")
            with pytest.raises(Exception):
                boom_resp = stub2.ReverseString2(request_boom2)
            logger.info("passed.")

            request_boom = FunctionRequest2(foo="boom")
            requests = iter(
                [FunctionRequest(foo=str(i) + ".") for i in range(10)]
                + [request_boom]
                + [FunctionRequest(foo=str(i) + "X") for i in range(10)]
            )
            response = stub.ReverseStrings(requests)
            last_response = None
            with pytest.raises(Exception):
                for r in response:
                    last_response = r
                    logger.info(f"streamed output: {r}")
            assert last_response.bar == ".9"

            numbers_to_sum = iter(
                [AddToSum(quantity=x) for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]]
            )
            sum = stub.SumStream(numbers_to_sum)
            logger.info(sum)
            assert sum.total == 45

            numbers_to_fail_summing = iter(
                AddToSum(quantity=x) for x in [1, 2, 3, 4, -1, 6, 7, 8, 9]
            )

            with pytest.raises(Exception):
                stub.SumStream(numbers_to_fail_summing)

            resp = list(stub.SillyLetterStream(FunctionRequest(foo="wow")))
            assert resp == [
                FunctionResponse(bar="w!!"),
                FunctionResponse(bar="o!!"),
                FunctionResponse(bar="w!!"),
            ]

            with pytest.raises(Exception):
                resp = stub.SillyLetterStream(FunctionRequest(foo="nope"))
                for i in resp:
                    logger.info(i)
    else:
        raise Exception("please specify client or server.")
