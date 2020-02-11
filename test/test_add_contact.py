# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact(firstname="Petr", middlename="Petrov", mobile="89162935002"))

def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", mobile=""))