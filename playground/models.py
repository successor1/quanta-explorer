from django.test import tag
from djongo import models

class Addresses(models.Model):
    _id = models.ObjectIdField()
    address = models.TextField()
    balance = models.IntegerField()
    firstSeen = models.JSONField()
    lastSeen = models.JSONField()
    tag = models.JSONField()
    objects = models.DjongoManager()

class BlockMetadata(models.Model):
    _id = models.ObjectIdField()
    blockNum = models.TextField()
    hashHeader = models.IntegerField()
    nbTransactions = models.JSONField()
    rewardBlock = models.JSONField()
    timestampSeconds = models.JSONField()
    objects = models.DjongoManager()

class Messages(models.Model):
    _id = models.ObjectIdField()
    blockNum = models.TextField()
    messageHash = models.IntegerField()
    transactionHash = models.JSONField()
    objects = models.DjongoManager()


class OtherTransactions(models.Model):
    _id = models.ObjectIdField()
    blockNum = models.TextField()
    data = models.IntegerField()
    transactionHash = models.JSONField()
    txType = models.JSONField()
    objects = models.DjongoManager()


class OtherTransactions(models.Model):
    _id = models.ObjectIdField()
    tokenName = models.TextField()
    tokenOwner = models.IntegerField()
    tokenOwner = models.JSONField()
    tokenSymbol = models.JSONField()
    transactionHash = models.JSONField()
    objects = models.DjongoManager()
