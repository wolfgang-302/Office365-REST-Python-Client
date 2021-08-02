from office365.entity_collection import EntityCollection
from office365.outlook.mail.bodyType import BodyType
from office365.outlook.mail.importance import Importance
from office365.outlook.mail.itemBody import ItemBody
from office365.outlook.mail.message import Message
from office365.outlook.mail.recipient import Recipient
from office365.runtime.client_value_collection import ClientValueCollection


class MessageCollection(EntityCollection):
    """Message's collection"""

    def __init__(self, context, resource_path=None):
        super(MessageCollection, self).__init__(context, Message, resource_path)

    def add(self, subject, body, to_recipients, importance=Importance.low):
        """
        Use this API to create a draft of a new message. Drafts can be created in any folder
        and optionally updated before sending. To save to the Drafts folder, use the /messages shortcut.
        :param int importance:
        :param str subject:
        :param str or ItemBody body:
        :param list[str] to_recipients:
        :rtype: Message
        """
        return super(MessageCollection, self).add(
            subject=subject,
            importance=importance,
            body=ItemBody(body, BodyType.html),
            toRecipients=ClientValueCollection(Recipient, [Recipient.from_email(v) for v in to_recipients])
        )