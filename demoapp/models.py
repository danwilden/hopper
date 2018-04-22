# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Business(models.Model):
    id              = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=200, help_text="Enter Business Name")
    description     = models.CharField(max_length=200, help_text="Enter Business Description")
    address         = models.CharField(max_length=200, help_text="Enter Business Address")
    val_comp        = models.BooleanField()
    valuation       = models.IntegerField(help_text="Valuation", null=True)

    owner           = models.ForeignKey('User', related_name='Owner', on_delete=models.DO_NOTHING)
    broker          = models.ForeignKey('User', related_name='Broker', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):

        return self.name

class User(models.Model):
    function_choices = (('br', "Broker"), ('buy', 'Buyer'), ('own', 'Owner'))
    id              = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=200, help_text="Enter Owner Name")
    phone           = models.CharField(max_length=200, help_text="Enter Owner Phone")
    email           = models.CharField(max_length=200, help_text="Enter Owner Email")
    function        = models.CharField(max_length=3, choices=function_choices)

    def __str__(self):

        return self.name

class Viewer(models.Model):
    id              = models.AutoField(primary_key=True)
    business        = models.ForeignKey('Business', on_delete=models.DO_NOTHING)
    viewer          = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    datetime        = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.viewer

class Contact(models.Model):
    id              = models.AutoField(primary_key=True)
    business        = models.ForeignKey('Business', on_delete=models.DO_NOTHING)
    contact         = models.ForeignKey('User', related_name='Interested', on_delete=models.DO_NOTHING)
    contacted       = models.ForeignKey('User', related_name='Contacted',on_delete=models.DO_NOTHING)
    message         = models.TextField()
    datetime        = models.DateTimeField(auto_now=True)
    listing         = models.ForeignKey('Listing', on_delete=models.DO_NOTHING)

    def __str__(self):

        return self.title


class Listing(models.Model):
    listing_options = (('mon', 'Monthly'), ('year', 'Yearly'))
    id              = models.AutoField(primary_key=True)
    business        = models.ForeignKey('Business', on_delete=models.DO_NOTHING)
    contacts        = models.IntegerField(help_text="Number of Contact")
    views           = models.IntegerField(help_text="Number of Views")
    type            = models.CharField(max_length=4, choices=listing_options)
    expiration      = models.DateTimeField()
    intiation       = models.DateTimeField()
    image           = models.ImageField()

class Financial(models.Model):
    id              = models.AutoField(primary_key=True)
    business        = models.ForeignKey('Business', on_delete=models.DO_NOTHING)
    year            = models.IntegerField(help_text="Enter this year minus the entry year")
    type            = models.ForeignKey('DataType', on_delete=models.DO_NOTHING)
    amount          = models.IntegerField(help_text="Enter amount")

    def __str__(self):

        return self.title


class DataType(models.Model):
    id              = models.AutoField(primary_key=True)
    type            = models.CharField(max_length=200, help_text="Enter Input Type")

    def __str__(self):

        return self.title

class Valuation(models.Model):
    id              = models.AutoField(primary_key=True)
    business        = models.ForeignKey('Business', related_name='BisVal', on_delete=models.DO_NOTHING)
    high            = models.FloatField(help_text="Enter amount")
    middle          = models.FloatField(help_text="Enter amount")
    low             = models.FloatField(help_text="Enter amount")
    start           = models.FloatField(help_text="Enter amount")
    sigma           = models.FloatField(help_text="Enter amount")
    mu              = models.FloatField(help_text="Enter amount")
    equity          = models.FloatField(help_text="Enter amount")
    debt            = models.FloatField(help_text="Enter amount")
    eroi            = models.FloatField(help_text="Enter amount")
    cod             = models.FloatField(help_text="Enter amount")

    def __str__(self):

        return self.title



'''
class Product(models.Model):

    sku = models.CharField(max_length=13,help_text="Enter Product Stock Keeping Unit")
    barcode = models.CharField(max_length=13,help_text="Enter Product Barcode (ISBN, UPC ...)")

    title = models.CharField(max_length=200, help_text="Enter Product Title")
    description = models.TextField(help_text="Enter Product Description")

    unitCost = models.FloatField(help_text="Enter Product Unit Cost")
    unit = models.CharField(max_length=10,help_text="Enter Product Unit ")

    quantity = models.FloatField(help_text="Enter Product Quantity")
    minQuantity = models.FloatField(help_text="Enter Product Min Quantity")

    family = models.ForeignKey('Family', on_delete=models.DO_NOTHING)
    location = models.ForeignKey('Location', on_delete=models.DO_NOTHING)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Product.
        """
        return reverse('product-detail-view', args=[str(self.id)])

    def __str__(self):

        return self.title

class Family(models.Model):

    reference = models.CharField(max_length=13, help_text="Enter Family Reference")
    title = models.CharField(max_length=200, help_text="Enter Family Title")
    description = models.TextField(help_text="Enter Family Description")

    unit = models.CharField(max_length=10,help_text="Enter Family Unit ")

    minQuantity = models.FloatField(help_text="Enter Family Min Quantity")

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Family.
        """
        return reverse('family-detail-view', args=[str(self.id)])

    def __str__(self):

        return self.title

class Location(models.Model):

    reference = models.CharField(max_length=20, help_text="Enter Location Reference")
    title = models.CharField(max_length=200, help_text="Enter Location Title")
    description = models.TextField(help_text="Enter Location Description")

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Location.
        """
        return reverse('family-detail-view', args=[str(self.id)])

    def __str__(self):

        return self.title


class Transaction(models.Model):

    sku = models.CharField(max_length=13,help_text="Enter Product Stock Keeping Unit")
    barcode = models.CharField(max_length=13,help_text="Enter Product Barcode (ISBN, UPC ...)")

    comment = models.TextField(help_text="Enter Product Stock Keeping Unit")

    unitCost = models.FloatField(help_text="Enter Product Unit Cost")

    quantity = models.FloatField(help_text="Enter Product Quantity")

    product = models.ForeignKey('Product',on_delete=models.DO_NOTHING)

    date = models.DateField(null=True, blank=True)

    REASONS = (
        ('ns', 'New Stock'),
        ('ur', 'Usable Return'),
        ('nr', 'Unusable Return'),
    )


    reason = models.CharField(max_length=2, choices=REASONS, blank=True, default='ns', help_text='Reason for transaction')

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Product.
        """
        return reverse('transaction-detail-view', args=[str(self.id)])

    def __str__(self):

        return 'Transaction :  %d' % (self.id)

'''
