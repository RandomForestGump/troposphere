# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, double, integer


class InsightsConfiguration(AWSProperty):
    """
    `InsightsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-group-insightsconfiguration.html>`__
    """

    props: PropsDictType = {
        "InsightsEnabled": (boolean, False),
        "NotificationsEnabled": (boolean, False),
    }


class TagsItems(AWSProperty):
    """
    `TagsItems <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-tagsitems.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Value": (str, True),
    }


class Group(AWSObject):
    """
    `Group <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html>`__
    """

    resource_type = "AWS::XRay::Group"

    props: PropsDictType = {
        "FilterExpression": (str, False),
        "GroupName": (str, False),
        "InsightsConfiguration": (InsightsConfiguration, False),
        "Tags": ([TagsItems], False),
    }


class ResourcePolicy(AWSObject):
    """
    `ResourcePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-resourcepolicy.html>`__
    """

    resource_type = "AWS::XRay::ResourcePolicy"

    props: PropsDictType = {
        "BypassPolicyLockoutCheck": (boolean, False),
        "PolicyDocument": (str, True),
        "PolicyName": (str, True),
    }


class SamplingRuleProperty(AWSProperty):
    """
    `SamplingRuleProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html>`__
    """

    props: PropsDictType = {
        "Attributes": (dict, False),
        "FixedRate": (double, True),
        "HTTPMethod": (str, True),
        "Host": (str, True),
        "Priority": (integer, True),
        "ReservoirSize": (integer, True),
        "ResourceARN": (str, True),
        "RuleARN": (str, False),
        "RuleName": (str, False),
        "ServiceName": (str, True),
        "ServiceType": (str, True),
        "URLPath": (str, True),
        "Version": (integer, False),
    }


class SamplingRuleRecord(AWSProperty):
    """
    `SamplingRuleRecord <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrulerecord.html>`__
    """

    props: PropsDictType = {
        "CreatedAt": (str, False),
        "ModifiedAt": (str, False),
        "SamplingRule": (SamplingRuleProperty, False),
    }


class SamplingRuleUpdate(AWSProperty):
    """
    `SamplingRuleUpdate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html>`__
    """

    props: PropsDictType = {
        "Attributes": (dict, False),
        "FixedRate": (double, False),
        "HTTPMethod": (str, False),
        "Host": (str, False),
        "Priority": (integer, False),
        "ReservoirSize": (integer, False),
        "ResourceARN": (str, False),
        "RuleARN": (str, False),
        "RuleName": (str, False),
        "ServiceName": (str, False),
        "ServiceType": (str, False),
        "URLPath": (str, False),
    }


class SamplingRule(AWSObject):
    """
    `SamplingRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html>`__
    """

    resource_type = "AWS::XRay::SamplingRule"

    props: PropsDictType = {
        "RuleName": (str, False),
        "SamplingRule": (SamplingRuleProperty, False),
        "SamplingRuleRecord": (SamplingRuleRecord, False),
        "SamplingRuleUpdate": (SamplingRuleUpdate, False),
        "Tags": ([TagsItems], False),
    }
