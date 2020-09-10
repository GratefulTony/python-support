"""
Copyright 2020 Lightbend Inc.
Licensed under the Apache License, Version 2.0.
"""
import os

from setuptools import setup, find_packages
import pathlib

# Load version in cloudstate package.
from setuptools.command.build_py import build_py

exec(open("cloudstate/version.py").read())

PROTOBUF_VERSION = "v0.5.01"

version = __version__  # noqa
name = "cloudstate"

print(f"package name: {name}, version: {version}", flush=True)

proto_lib_roots = ["protobuf/lib"]
proto_roots = ["protobuf/proto"]


class FetchBuildProtosCommand(build_py):
    """fetch libs and install the protocol buffer generated sources."""

    def run(self):
        os.system(f"scripts/fetch-cloudstate-pb.sh {PROTOBUF_VERSION}")

        for proto_root in proto_roots + proto_lib_roots:
            for root, subdirs, files in os.walk(proto_root):
                for file in [f for f in files if f.endswith(".proto")]:
                    file_path = pathlib.Path(root) / file
                    destination = "."#str(pathlib.Path(self.build_lib) / root).replace(
                        # proto_root, ""
                    # )
                    print(f"compiling {file_path} to {destination}")
                    command = f"python -m grpc_tools.protoc {' '.join([' -I ' + i for i in proto_roots + proto_lib_roots])} --python_out={destination} --grpc_python_out={destination} {file_path}"
                    os.system(command)

        return super().run()

packages = find_packages(exclude=[])
print(f"packages: {packages}")
setup(
    name=name,
    version=version,
    url="https://github.com/cloudstateio/python-support",
    license="Apache 2.0",
    description="Cloudstate Python Support Library",
    packages=packages,
    long_description=open("Description.md", "r").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    # include_package_data = True,
    scripts=["scripts/compile-protobuf.sh", "scripts/fetch-cloudstate-pb.sh"],
    cmdclass={
        "build_py": FetchBuildProtosCommand,
    },
)
