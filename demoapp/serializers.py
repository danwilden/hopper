from rest_framework import serializers
from .models import Business, User, Financial, DataType, Listing, Viewer, Contact, Valuation

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('id', 'name', 'description', 'address','val_comp', 'valuation', 'owner', 'broker')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'phone', 'email','function')

class ViewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewer
        fields = ('id', 'business', 'viewer', 'datetime')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'business', 'contact', 'contacted','message', 'datetime', 'listing')

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('id', 'business', 'contacts', 'views','type', 'expiration', 'intiation', 'image')

class FinancialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financial
        fields = ('id', 'business', 'year', 'type','amount')

class DataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataType
        fields = ('id', 'type')

class ValuationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valuation
        fields = ('id', 'business', 'high', 'middle','low', 'start', 'sigma', 'mu', 'equity', 'debt', 'eroi', 'cod')
