#!/usr/bin/env bash
docker rm -f cloudstate-proxy
docker rm -f cloudstate-function
docker rm -f cloudstate-function-client
#  fresh docker build
docker build -t dev-cloudstate-tck:local ./

#  primary tck tests for shopping cart
docker run -d --name cloudstate-function -p 8080:8080 dev-cloudstate-tck:local \
    server \
    shoppingcart
sleep 10
docker run -d --name cloudstate-proxy -p 9000:9000 \
    -e USER_FUNCTION_HOST=host.docker.internal \
    -e USER_FUNCTION_PORT=8090 \
    cloudstateio/cloudstate-proxy-dev-mode
sleep 10
docker run --rm --name cloudstate-tck -p 8090:8090 \
    -e TCK_HOST=0.0.0.0 \
    -e TCK_PROXY_HOST=host.docker.internal \
    -e TCK_FRONTEND_HOST=host.docker.internal cloudstateio/cloudstate-tck

status=$?
echo "Removing docker containers"
docker rm -f cloudstate-proxy
docker rm -f cloudstate-function

#  secondary integration tests for stateless function:
docker run -d --name cloudstate-proxy -p 9000:9000 \
    -e USER_FUNCTION_HOST=host.docker.internal \
    -e USER_FUNCTION_PORT=8080 \
    cloudstateio/cloudstate-proxy-dev-mode
sleep 10
docker run -d --name cloudstate-function -p 8080:8080 dev-cloudstate-tck:local \
    server \
    functiondemo \
    shoppingcart
sleep 10
docker run --name cloudstate-function-client dev-cloudstate-tck:local \
    client \
    functiondemo \
    shoppingcart

docker rm -f cloudstate-proxy
docker rm -f cloudstate-function
docker rm -f cloudstate-function-client

echo "Stopping user-functions"

exit $status
