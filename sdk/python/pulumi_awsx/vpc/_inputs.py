# coding=utf-8
# *** WARNING: this file was generated by pulumi-gen-awsx. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'NatGatewayConfigurationArgs',
    'SubnetConfigurationArgs',
]

@pulumi.input_type
class NatGatewayConfigurationArgs:
    def __init__(__self__, *,
                 strategy: 'NatGatewayStrategy',
                 elastic_ip_allocation_ids: Optional[Sequence[pulumi.Input[str]]] = None):
        """
        Configuration for NAT Gateways.
        :param 'NatGatewayStrategy' strategy: The strategy for deploying NAT Gateways.
        :param Sequence[pulumi.Input[str]] elastic_ip_allocation_ids: A list of EIP allocation IDs to assign to the NAT Gateways. Optional. If specified, the number of supplied values must match the chosen strategy (either one, or the number of availability zones).
        """
        pulumi.set(__self__, "strategy", strategy)
        if elastic_ip_allocation_ids is not None:
            pulumi.set(__self__, "elastic_ip_allocation_ids", elastic_ip_allocation_ids)

    @property
    @pulumi.getter
    def strategy(self) -> 'NatGatewayStrategy':
        """
        The strategy for deploying NAT Gateways.
        """
        return pulumi.get(self, "strategy")

    @strategy.setter
    def strategy(self, value: 'NatGatewayStrategy'):
        pulumi.set(self, "strategy", value)

    @property
    @pulumi.getter(name="elasticIpAllocationIds")
    def elastic_ip_allocation_ids(self) -> Optional[Sequence[pulumi.Input[str]]]:
        """
        A list of EIP allocation IDs to assign to the NAT Gateways. Optional. If specified, the number of supplied values must match the chosen strategy (either one, or the number of availability zones).
        """
        return pulumi.get(self, "elastic_ip_allocation_ids")

    @elastic_ip_allocation_ids.setter
    def elastic_ip_allocation_ids(self, value: Optional[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "elastic_ip_allocation_ids", value)


@pulumi.input_type
class SubnetConfigurationArgs:
    def __init__(__self__, *,
                 cidr_mask: int,
                 name: str,
                 type: 'SubnetType'):
        """
        Configuration for a VPC subnet.
        :param int cidr_mask: The bitmask for the subnet's CIDR block.
        :param str name: The subnet's name. Will be templated upon creation.
        :param 'SubnetType' type: The type of subnet.
        """
        pulumi.set(__self__, "cidr_mask", cidr_mask)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="cidrMask")
    def cidr_mask(self) -> int:
        """
        The bitmask for the subnet's CIDR block.
        """
        return pulumi.get(self, "cidr_mask")

    @cidr_mask.setter
    def cidr_mask(self, value: int):
        pulumi.set(self, "cidr_mask", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The subnet's name. Will be templated upon creation.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> 'SubnetType':
        """
        The type of subnet.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: 'SubnetType'):
        pulumi.set(self, "type", value)


