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
        table = self.request.query_params.get('table', None)
        if table:
            queryset = queryset.filter(key=table)
        return queryset
