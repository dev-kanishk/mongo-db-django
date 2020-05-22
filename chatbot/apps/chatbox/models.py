from mongoengine import Document, EmbeddedDocument, fields
from django.db.models import signals
import datetime, uuid

class ChatboxComponentQuestions(EmbeddedDocument):
    question = fields.StringField(required=True)

class ChatboxComponent(EmbeddedDocument):
    id = fields.UUIDField(required=True, binary=False, default=uuid.uuid4)
    name = fields.DynamicField(required=True)
    questions = fields.ListField(required=False)
    COMPONENT_RESPONSE_TYPE = {
        'TXT': 'Text Field',
        'DAT': 'Date Time',
         }
    response_type = fields.StringField(max_length=3, choices=COMPONENT_RESPONSE_TYPE.keys(), default='TXT', required=True)

 
class Chatbox(Document):
    title = fields.StringField(required=True)
    live_status = fields.BooleanField(default=False)
    owner_id = fields.IntField(required=False)
    created_on = fields.DateTimeField(default=datetime.datetime.now)
    updated_on = fields.DateTimeField(default=datetime.datetime.now)
    WIDGET_PUBLISH = {
        'UCS': 'Chatbox Under Constructions',
        'PUB': 'Chatbox Published',
         }
    publish_status = fields.StringField(max_length=3, choices=WIDGET_PUBLISH.keys(), default='UCS')
    preview_url = fields.URLField(required=False)
    components = fields.ListField(fields.EmbeddedDocumentField(ChatboxComponent), required=False)

    @property
    def chatbox_publish_status(self):
        return self.codes(self.publish_status)

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_on = datetime.datetime.now()


signals.pre_save.connect(Chatbox.pre_save, sender=Chatbox)


