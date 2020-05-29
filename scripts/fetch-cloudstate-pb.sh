#!/usr/bin/env bash

set -o nounset
set -o errexit
set -o pipefail

function fetch() {
  local path=$1
  local tag=$2
  mkdir -p protobuf/$(dirname $path)
  curl -o protobuf/${path} https://raw.githubusercontent.com/cloudstateio/cloudstate/${tag}/protocols/${path}
  #sed 's/^option java_package.*/option go_package = "${go_package}";/' protobuf/${path}
}

tag=$1

# Cloudstate protocol
fetch "protocol/cloudstate/entity.proto" $tag
fetch "protocol/cloudstate/event_sourced.proto" $tag
fetch "protocol/cloudstate/function.proto" $tag
fetch "protocol/cloudstate/crdt.proto" $tag

# TCK shopping cart example
fetch "example/shoppingcart/shoppingcart.proto" $tag
fetch "example/shoppingcart/persistence/domain.proto" $tag

# Cloudstate frontend
fetch "frontend/cloudstate/entity_key.proto" $tag

# dependencies
fetch "proxy/grpc/reflection/v1alpha/reflection.proto" $tag
fetch "frontend/google/api/annotations.proto" $tag
fetch "frontend/google/api/http.proto" $tag