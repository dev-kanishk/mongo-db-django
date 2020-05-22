from rest_framework_mongoengine import serializers

from . import models 

class ChatBoxDisplaySerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.Chatbox
        fields = '__all__'

class ChatBoxAddSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.Chatbox
        fields = '__all__'

class ChatBoxComponentAddSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        model = models.ChatboxComponent
        fields = '__all__'

class ChatBoxAddSerializerDisplay(serializers.DocumentSerializer):
    class Meta:
        model = models.ChatboxComponent
        fields = '__all__'
