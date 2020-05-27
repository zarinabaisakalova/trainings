from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture


db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')


def test_add_contact_in_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name3", header="header3", footer="footer3"))
    contact_list = db.get_contact_list()
    group_list = db.get_group_list()
    contact_id = random.choice(contact_list).id
    group_id = random.choice(group_list).id
    app.contact.add_contact_in_group(contact_id, group_id)
    assert db.get_contact_id(contact_id) in orm.get_contacts_in_group(Group(id=group_id))
