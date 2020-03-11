# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    # загружаем список контактов
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Petr", lastname="Petrov", mobile="89162935002")
    # создаем новую группу и снова загружаем список контактов
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", lastname="", mobile="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count_contact()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)