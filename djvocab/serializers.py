'''
Vocabulary serializers
'''

from rest_framework import serializers, viewsets
from djvocab import models


class VocabularySerializer(serializers.ModelSerializer):
    '''
    Serializer for vocabulary
    '''

    class Meta:
        model = models.Vocabulary
        fields = (
            'key',
            'value',
            'description',
            'order'
        )


class VocabularyViewSet(viewsets.ModelViewSet):
    '''
    ViewSet for Vocabulary models, allows filtering on list
    '''
    serializer_class = VocabularySerializer

    def get_queryset(self):
        queryset = models.Vocabulary.objects.all()
        field = self.request.query_params.get('field', None)
        if field:
            queryset = queryset.filter(key=field)
        return queryset
