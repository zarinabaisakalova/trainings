_author_ = 'zarina'

from model.group import Group
import random

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test1"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_new = Group(name="New group")
    app.group.modify_group_by_id(group.id, group_new)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    if check_ui:
        assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_modify_group_header(app):
    #old_groups = app.group.get_group_list()
   # if app.group.count() == 0:
   #     app.group.create(Group(header="test2"))
    #app.group.modify_first_group(Group(header="New header"))
   # new_groups = app.group.get_group_list()
   # assert len(old_groups) == len(new_groups)

#def test_modify_group_footer(app):
   # old_groups = app.group.get_group_list()
   # if app.group.count() == 0:
     #   app.group.create(Group(footer="test3"))
  #  app.group.modify_first_group(Group(footer="New footer"))
  #  new_groups = app.group.get_group_list()
  #  assert len(old_groups) == len(new_groups)