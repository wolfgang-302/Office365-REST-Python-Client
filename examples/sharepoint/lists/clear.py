"""
This example deletes a SharePoint all the list items.
"""
from office365.sharepoint.client_context import ClientContext
from tests import test_client_credentials, test_team_site_url


def print_progress(items_count):
    print("List items count: {0}".format(target_list.item_count))


ctx = ClientContext(test_team_site_url).with_credentials(test_client_credentials)
target_list = ctx.web.lists.get_by_title("Contacts_Large")
target_list.clear().get().execute_query()
print("List items count: {0}".format(target_list.item_count))
