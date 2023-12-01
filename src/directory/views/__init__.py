from src.directory.models import Document, Transmital
from api.rest import CreateListRetrieveViewSet
from src.directory.serializers import DocumentSerializer, TransmitalSerializer
from utils.constants import DEFAULT_AUTH, DEFAULT_PERMS

class DocumentViewset(CreateListRetrieveViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    authentication_classes = DEFAULT_AUTH
    permission_classes = DEFAULT_PERMS


class TransmitalViewset(CreateListRetrieveViewSet):
    queryset = Transmital.objects.all()
    serializer_class = TransmitalSerializer
    authentication_classes = DEFAULT_AUTH
    permission_classes = DEFAULT_PERMS
