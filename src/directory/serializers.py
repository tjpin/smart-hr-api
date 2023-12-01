from rest_framework import serializers

from src.directory.models import Transmital, Document


class TransmitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmital
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(source="staff", read_only=True)

    class Meta:
        model = Document
        fields = [
            "owner",
            "document_id",
            "document_type",
            "date_uploaded",
            "status",
            "is_public",
        ]
