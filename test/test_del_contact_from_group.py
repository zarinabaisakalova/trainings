from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_from_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name3", header="header3", footer="footer3"))
    if len(db.get_groups_with_contacts())==0:
        contact_id = random.choice(db.get_contact_list()).id
        group_id = random.choice(db.get_group_list()).id
        app.contact.add_contact_in_group(contact_id, group_id)

    group_id = random.choice(db.get_groups_with_contacts()).id
    contact_id = random.choice(orm.get_contacts_in_group(Group(id=group_id))).id
    app.contact.delete_contact_from_group(group_id)
    assert db.get_contact_id(contact_id) not in orm.get_contacts_in_group(Group(id=group_id))